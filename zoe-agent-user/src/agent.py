# -*- coding: utf-8 -*-
#
# This file is part of Zoe Assistant
# Licensed under MIT license - see LICENSE file
#

from zoe import *

@Agent('User')
class UserAgent:

    def fakeuser(self, name):
        # ... lookup for user in database ...
        return {
            'data': 'user',
            'name': name,
            'email': '%s@gmail.com' % (name)
        }

    @Intent('user.get')
    def receive(self, intent):
        name = intent['name']
        # fetch user from database
        return self.fakeuser(name)

    @Intent('user.add')
    def adduser(self, intent):
        name = intent['name']
        # extract user info from intent
        # store in database
        return self.fakeuser(name)
