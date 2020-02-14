# IMDb RESTfull

It is a REST api built using Flask having top 250 movie details from IMDb.

## Installation
Use Python 2.7 to create a virtualenv...

```bash
virtualenv restenv
source restenv/bin/activate

git clone https://github.com/RiteshChouhan/IMDb_RESTfull.git
cd IMDb_RESTfull

pip install -r requirements.txt

export FLASK_ENV=development
export FLASK_APP=api

flask run
```

Open below link in browser

```python
http://localhost:5000/movie_list
```

### Authentication
       Username: ritesh
       Password: test@digiqt
## Arguments

            sort_by: sort data based on given element.
                     e.g. title, released, runtime, imdbRating

            sort_seq: it is associated with sort_by and will return result in 
                      ascending or descending order.
                      e.g. ASC(default), DESC

            search_name: will return list of movies having given name.

            search_desc: will return list of movies having given description.

## Usage
```python
http://localhost:5000/movie_list?sort_by=title

http://localhost:5000/movie_list?search_desc=cricket

http://localhost:5000/movie_list?sort_by=runtime&sort_seq=DESC&search_name=the lord of the ring
```
