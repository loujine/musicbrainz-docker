#!/usr/bin/env python

# your postgres server IP
PGHOST = IP = 'localhost'
PGDATABASE = 'musicbrainz'
PGUSER = os.environ.get('POSTGRES_USER', 'musicbrainz')
PGPASSWORD = os.environ.get('POSTGRES_PASSWORD', 'musicbrainz')
