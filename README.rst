VOMS authentication plugin for Openstack clients
================================================

This is a plugin for OpenStack Clients which provides client support for
VOMS authentication extensions to OpenStack.

Installation
~~~~~~~~~~~~

Install it via pip::

    pip install voms-auth-system-openstack

Or clone the repo and install it::

    git clone https://github.com/IFCA/voms-auth-system-openstack
    cd voms-auth-system-openstack
    python setup.py install

Usage
~~~~~

CLI
---

You have to specify the `voms` in the `--os_auth-system` option and provide a
valid proxy with `--x509-user-proxy`::

    nova --os-auth-system voms --x509-user-proxy /tmp/x509up_u1000 credentials

API
---

::

    import novaclient
    import novaclient.auth_plugin
    import novaclient.client

    username = password = None
    tenant = "foo"
    url = "https://example.org:5000/v2.0/"
    version = 2

    auth_system = "voms"
    novaclient.auth_plugin.discover_auth_systems()
    auth_plugin = novaclient.auth_plugin.load_plugin(auth_system)
    auth_plugin.opts["x509_user_proxy"] = "/path/to/your/proxy"

    client =  novaclient.client.Client(version, username, password,
                                        tenant, url,
                                        auth_plugin=auth_plugin,
                                        auth_system=auth_system)
