#!/usr/bin/env python
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# Inspired from: https://github.com/redhat-openstack/khaleesi/blob/master/plugins/callbacks/collector.py
# Further improved support Ansible 2.0

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

try:
    import simplejson as json
except ImportError:
    import json


class CallbackModule(object):

    """
    Ansible callback plugin for collect result into a common repository for the platform
    """
    CALLBACK_VERSION = 2.0
    CALLBACK_TYPE = 'notification'
    CALLBACK_NAME = 'collector'
    CALLBACK_NEEDS_WHITELIST = False


    ####### V2 METHODS ######
    def v2_runner_on_ok(self, result):
        data = result._result
        try:
            log_entry = data["custom_log"]
            print(log_entry)
            custom_log = open('./logs/log', 'a')
            custom_log.write(log_entry + "\n")
            custom_log.close()
        except:
            pass
