VOMS authentication plugin for Openstack clients
================================================

This is a plugin for OpenStack Clients which provides client support for
VOMS authentication extensions to OpenStack.

Installation
~~~~~~~~~~~~

In your Openstack client machine just run::

    git clone https://github.com/IFCA/voms-auth-system-openstack
    cd voms-auth-system-openstack
    python setup.py install

Usage
~~~~~

You have to specify the `voms` in the `--os_auth-system` option and provide a
valid proxy with `--x509-user-proxy`::

    nova --os-auth-system voms --x509-user-proxy /tmp/x509up_u1000 credentials

