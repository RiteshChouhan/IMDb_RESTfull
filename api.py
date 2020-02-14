#!/usr/bin/python
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import create_engine
from config import DB_CONN_STR, ADMIN_USERNAME, ADMIN_PASSWORD

db_connect = create_engine(DB_CONN_STR)
app = Flask(__name__)
api = Api(app)
auth = HTTPBasicAuth()

@auth.verify_password
def verify(username, password):
    if not (username and password):
        return False
    hashed_pass = generate_password_hash(password)
    if check_password_hash(hashed_pass, ADMIN_PASSWORD) and username == ADMIN_USERNAME:
        return True

class Movies(Resource):
    @auth.login_required
    def get(self):
        """
        Return JSON object of movie details based on args.

        Arguments:
            sort_by: sort data based on given element.
                     e.g. title, released, runtime, imdbRating

            sort_seq: it is associated with sort_by and will return result in ascending or descending order.
                     e.g. ASC(default), DESC

            search_name: will return list of movies having given name.

            search_desc: will return list of movies having given description.
        
        """
        col_names = ["title", "released", "runtime", "imdbRating"]
        sort_by = request.args.get('sort_by', None)
        sort_seq = request.args.get('sort_seq', "ASC")
        search_name = request.args.get('search_name', '')
        search_desc = request.args.get('search_desc', '')

        conn = db_connect.connect() # connect to database
        query_str = "select * from imdb_movies as a"
        
        if search_name:
            query_str = query_str + "where title like '%{}%' ".format(search_name)
        elif search_desc:
            query_str = query_str + "where plot like '%{}%' ".format(search_desc)
        if sort_by in col_names:
            query_str = query_str + " order by {} {}".format(sort_by, sort_seq)                    

        query = conn.execute(query_str)
        result = {'movie_data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

api.add_resource(Movies, '/movie_list', methods=['GET']) # Route


if __name__ == '__main__':
     app.run()
