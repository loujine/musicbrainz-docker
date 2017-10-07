#!/usr/bin/env python
import os
from pprint import pprint

import pandas
import sqlalchemy


# your postgres server IP
PGHOST = IP = 'localhost'
PGDATABASE = 'musicbrainz'
PGUSER = os.environ.get('POSTGRES_USER', 'musicbrainz')
PGPASSWORD = os.environ.get('POSTGRES_PASSWORD', 'musicbrainz')

def sql(query, **kwargs):
    """helper function for SQL queries using the %(...) syntax
    Parameters defined globally are replaced implicitely"""
    params = globals().copy()
    params.update(kwargs)

    # define DB connection parameters if needed
    PGHOST = globals().get('PGHOST', IP)
    PGDATABASE = globals().get('PGDATABASE', 'musicbrainz')
    PGUSER = globals().get('PGUSER', 'musicbrainz')
    PGPASSWORD = globals().get('PGPASSWORD', 'musicbrainz')
    engine = sqlalchemy.create_engine(
       'postgresql+psycopg2://%(PGUSER)s:%(PGPASSWORD)s@%(PGHOST)s/%(PGDATABASE)s' % locals(),
        isolation_level='READ UNCOMMITTED')
    return pandas.read_sql(query, engine, params=params)

# helper functions to generate an HTML link to an entity MusicBrainz URL
def _mb_link(type, mbid):
    return '<a href="https://musicbrainz.org/%(type)s/%(mbid)s">%(mbid)s</a>' % locals()

mb_artist_link = lambda mbid: _mb_link('artist', mbid)
mb_recording_link = lambda mbid: _mb_link('recording', mbid)
mb_work_link = lambda mbid: _mb_link('work', mbid)
mb_series_link = lambda mbid: _mb_link('series', mbid)
