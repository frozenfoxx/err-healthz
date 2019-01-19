# -*- coding: utf8 -*-

from errbot import BotPlugin, botcmd, webhook
import argparse
import requests

class Healthz(BotPlugin):

    def get_configuration_template(self):
        """ configuration entries """
        config = {
        }
        return config

    def _check_config(self, option):

        # if no config, return nothing
        if self.config is None:
            return None
        else:
            # now, let's validate the key
            if option in self.config:
                return self.config[option]
            else:
                return None

    @webhook('/healthz')
    def _healthz(self, args):
        """ Return 200 OK """

        return
