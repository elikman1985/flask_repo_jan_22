from flask import Flask

from db import execute_query
from formater import list_rec2html_br

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


app.run(debug=True, port=8000)
