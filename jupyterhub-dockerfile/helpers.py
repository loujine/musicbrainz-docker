#!/usr/bin/env python
import os
from pprint import pprint # noqa

import pandas
import sqlalchemy

SITE_URL = 'https://musicbrainz.org/'

# import postgresql environ variables
# defined in postgres-dockerfile/postgres.env
PGHOST = 'db'
PGDATABASE = 'musicbrainz'
PGUSER = os.environ.get('POSTGRES_USER', 'musicbrainz')
PGPASSWORD = os.environ.get('POSTGRES_PASSWORD', 'musicbrainz')


def sql(query, **kwargs):
    """helper function for SQL queries using the %(...) syntax
    Parameters for the query must be passed as keyword arguments
    e.g. sql('SELECT * FROM artist WHERE name=%(singer)s', singer='Bob Dylan')
    """
    engine = sqlalchemy.create_engine(
        'postgresql+psycopg2://'
        '{PGUSER}:{PGPASSWORD}@{PGHOST}/{PGDATABASE}'.format(**globals()),
        isolation_level='READ UNCOMMITTED')
    return pandas.read_sql(query, engine, params=kwargs)


# helper function to build canonical URLs
def _mb_link(entity_type, mbid):
    return '<a href="{url}/{entity_type}/{mbid}">{mbid}</a>'.format(
        url=SITE_URL, **locals())

mb_artist_link = lambda mbid: _mb_link('artist', mbid) # noqa
mb_work_link = lambda mbid: _mb_link('work', mbid) # noqa
mb_series_link = lambda mbid: _mb_link('series', mbid) # noqa
mb_release_link = lambda mbid: _mb_link('release', mbid) # noqa
