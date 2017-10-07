#  See `hub_connect_ip` for cases where the bind and connect address should
#  differ.
c.JupyterHub.hub_ip = '127.0.0.1'

## The public facing port of the proxy
c.JupyterHub.port = 8000

## Select the Proxy API implementation.
c.JupyterHub.proxy_class = 'jupyterhub.proxy.ConfigurableHTTPProxy'

## The class to use for spawning single-user servers.
c.JupyterHub.spawner_class = 'jupyterhub.spawner.LocalProcessSpawner'

## The IP address (or hostname) the single-user server should listen on.
c.Spawner.ip = '127.0.0.1'

#  Defaults to an empty set, in which case no user has admin access.
c.Authenticator.admin_users = set(['musicbrainz'])
