from flask import Flask
from webargs import fields
from webargs.flaskparser import use_kwargs
from db import execute_query
from utils import calculations_2
from operator import itemgetter


app = Flask(__name__)


@app.route("/popular_tracks")
@use_kwargs(
    {
        'count': fields.Str(
            required=False,
            missing=None,
        )
    },
    location='query'
)
def get_popular_tracks(count):

    if count:
        sql = 'select t.Name, t.UnitPrice from invoices inv, invoice_items itm, tracks t ' \
              'where inv.InvoiceId = itm.InvoiceId and t.TrackId = itm.TrackId'
        records = execute_query(sql)
        return calculations_2(records)
    else:
        sql = 'select * from invoices'

    records = execute_query(sql)

    return '<p>'.join(str(value) for value in sorted(records, key=itemgetter(8), reverse=True)) + '</p>'


app.run(debug=True, port=8000)
