Jupyter notebook for MusicBrainz
================================

Repository mirrors are available on [bitbucket](https://bitbucket.org/loujine/musicbrainz-docker) and [github](https://github.com/loujine/musicbrainz-docker).

This Docker configuration installs a [Jupyter notebook server](https://jupyter.org/) connected to the MusicBrainz database for people who want to analyze and visualize MusicBrainz data (for example with Python or JavaScript) with a minimal setup. Global variables (PGHOST, PGDATABASE, PGUSER, PGPASSWORD) are predefined in Python notebooks to access the database.

Examples of data visualization — not using this Docker setup for the moment — can be found on [my dataviz repo](https://github.com/loujine/musicbrainz-dataviz).

The server is:

 * listening on port 8888 (http://127.0.0.1:8888)
 * single-user (login *jovyan* on the VM)
 * offering **NO SECURITY**, available by any user from the host computer (no authentication)

Notebooks are stored in a volume on the host, by default *this directory*/notebooks.


