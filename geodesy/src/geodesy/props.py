# Software License Agreement (BSD License)
#
# Copyright (C) 2012, Jack O'Quin
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of the author nor of other contributors may be
#    used to endorse or promote products derived from this software
#    without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Revision $Id$

"""
:module:`props` KeyValue property interface for Geographic Information
        Systems.

:todo: rename tags to props in all these messages

:author: Jack O'Quin
"""

PKG='geodesy'
import roslib; roslib.load_manifest(PKG)

from geographic_msgs.msg import KeyValue

def get(msg, key):
    """ Get property value.

    :param msg: Message containing properties.
    :param key: Property key to match.
    :returns:   Corresponding value, if defined; None otherwise.
    """
    for prop in msg.tags:
        if prop.key == key:
            return prop.value
    return None

def put(msg, key, val=''):
    """ Add KeyValue to message properties.

    :param msg:   Message to update.
    :param key:   Property key name.
    :param value: Corresponding value string (default '').
    """
    for prop in msg.tags:
        if prop.key == key:
            # key already present, update value
            prop.value = str(val)
            return
    # key missing, append a new KeyValue pair
    msg.tags.append(KeyValue(key=key, value=str(val)))

def match(msg, key_set):
    """ Match message properties.

    :param msg:     Message containing properties.
    :param key_set: Set of property keys to match.
    :returns: (key, value) of first property matched; None otherwise.
    :raises: :exc:`ValueError` if key_set is not a set
    """
    if type(key_set) is not set:
        raise ValueError('property matching requires a set of keys')
    for prop in msg.tags:
        if prop.key in key_set:
            return (prop.key, prop.value)
    return None
