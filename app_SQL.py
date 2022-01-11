from flask import Flask

from db import execute_query
from formater_SQL import list_rec2html_br

from webargs import fields
from webargs.flaskparser import use_kwargs


app = Flask(__name__)


@app.route("/genres_duration_sql")
def get_genres_duration_sql():

    sql = 'select g.Name, sum(t.Milliseconds) from genres g, tracks t where g.GenreId = t.GenreId group by g.Name'
    records = execute_query(sql)

    return list_rec2html_br(records)


@app.route("/popular_tracks_sql")
@use_kwargs(
    {
        'count': fields.Str(
            required=False,
            missing=None,
        )
    },
    location='query'
)
def get_popular_tracks_sql(count):

    if count:
        sql = """
            select t.Name, round(t.UnitPrice*count(t.Name), 2)
            from invoices inv, invoice_items itm, tracks t
            where inv.InvoiceId = itm.InvoiceId and t.TrackId = itm.TrackId
            group by t.Name having count(t.Name) > 1
        """

        records = execute_query(sql)

        return list_rec2html_br(records)

    else:
        sql = 'select * from invoices order by Total desc'

    records = execute_query(sql)

    return list_rec2html_br(records)


app.run(debug=True, port=8000)
