# -*- coding: utf-8 -*-
#
# This file is part of Zoe Assistant
# Licensed under MIT license - see LICENSE file
#
import getpass

from zoe import *
import pwd

import datetime

@Agent('Conversation')
class ConversationAgent:

    @Intent('zoe.answer')
    def receive(self, intent):
        f = open("src/names.txt", "r")

        name = intent['name']
        if('HOLA' in name.upper()):
            for line in f.readlines():
                parts = line.split()
                for part in parts:
                    print(part)
                    if('{0}'.format(part) in name.upper()):
                        part = "{0}{1}".format(part[0], part[1:len(part)].lower())
                        str = ("ºhello {0}º".format(part))
                        return{
                            'answer' : '{0}'.format(str)
                        }
        else:
            if("time" in name):
                str = ('º{0}º'.format(datetime.datetime.now().strftime('%H:%M:%S')))
                return {
                    'answer' : str
                }

            return {
                'answer': 'not a valid argument'
            }


