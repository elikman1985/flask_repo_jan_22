from flask import Flask

from db import execute_query
from formater import list_rec2html_br
from utils import calculations

app = Flask(__name__)


@app.route("/unique_name")
def get_unique_name():
    sql = 'select FirstName from customers group by FirstName'

    records = execute_query(sql)

    return list_rec2html_br(records)


@app.route("/tracks_count")
def get_tracks_count():
    sql = 'select count(*) from tracks'

    records = execute_query(sql)

    return list_rec2html_br(records)


@app.route("/genres_duration")
def get_genres_duration():
    sql = 'select g.Name, t.Milliseconds from genres g, tracks t where g.GenreId = t.GenreId'

    records = execute_query(sql)

    return calculations(records)


app.run(debug=True, port=8000)
