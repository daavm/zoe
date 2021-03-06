# -*- coding: utf-8 -*-
#
# This file is part of Zoe Assistant
# Licensed under MIT license - see LICENSE file
#

from zoe import *

@Agent('Mail')
class MailAgent:

    @Intent('mail.send')
    def receive(self, intent):
        dest = intent['recipient']['email']
        # send email...
        return {
            'data': 'notification',
            'from': 'email',
            'text': 'message sent'
        }
