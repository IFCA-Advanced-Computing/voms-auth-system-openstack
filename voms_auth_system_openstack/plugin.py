# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2013 Spanish National Research Council
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.


from novaclient import auth_plugin
from novaclient import exceptions
from novaclient import utils


class VomsAuthPlugin(auth_plugin.BaseAuthPlugin):
    def __init__(self):
        self.opts = {}

    def parse_opts(self, args):
        x509_user_proxy = args.x509_user_proxy
        if not x509_user_proxy:
            raise exceptions.CommandError("You requested to use the 'voms' "
                                          "auth system, but you did not provide "
                                          "a proxy file with --x509-user-proxy "
                                          "or env[X509_USER_PROXY].")

        self.opts = {"x509_user_proxy": x509_user_proxy}
        return self.opts

    @staticmethod
    def add_opts(parser):
        parser.add_argument('--x509-user-proxy',
                metavar='<x509-user-proxy>',
                default=utils.env('X509_USER_PROXY', default=None),
                help=("VOMS proxy to use with 'voms' auth system. "
                      "Defaults to env[X509_USER_PROXY]."))
        return parser

    def authenticate(self, cls, auth_url):
        """Authenticate against a VOMS enabled keystone."""
        body = {"auth": {"voms": True }}
        if cls.projectid:
            body['auth']['tenantName'] = cls.projectid

        x509_user_proxy = self.opts.get("x509_user_proxy", None)
        if not x509_user_proxy:
            pass # raise exception
        return cls._authenticate(auth_url, body, cert=x509_user_proxy)
