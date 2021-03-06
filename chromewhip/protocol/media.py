# noinspection PyPep8
# noinspection PyArgumentList

"""
AUTO-GENERATED BY `scripts/generate_protocol.py` using `data/browser_protocol.json`
and `data/js_protocol.json` as inputs! Please do not modify this file.
"""

import logging
from typing import Any, Optional, Union

from chromewhip.helpers import PayloadMixin, BaseEvent, ChromeTypeBase

log = logging.getLogger(__name__)

# PlayerId: Players will get an ID that is unique within the agent context.
PlayerId = str

# Timestamp: 
Timestamp = float

# PlayerMessage: Have one type per entry in MediaLogRecord::TypeCorresponds to kMessage
class PlayerMessage(ChromeTypeBase):
    def __init__(self,
                 level: Union['str'],
                 message: Union['str'],
                 ):

        self.level = level
        self.message = message


# PlayerProperty: Corresponds to kMediaPropertyChange
class PlayerProperty(ChromeTypeBase):
    def __init__(self,
                 name: Union['str'],
                 value: Union['str'],
                 ):

        self.name = name
        self.value = value


# PlayerEvent: Corresponds to kMediaEventTriggered
class PlayerEvent(ChromeTypeBase):
    def __init__(self,
                 timestamp: Union['Timestamp'],
                 value: Union['str'],
                 ):

        self.timestamp = timestamp
        self.value = value


# PlayerError: Corresponds to kMediaError
class PlayerError(ChromeTypeBase):
    def __init__(self,
                 type: Union['str'],
                 errorCode: Union['str'],
                 ):

        self.type = type
        self.errorCode = errorCode


class Media(PayloadMixin):
    """ This domain allows detailed inspection of media elements
    """
    @classmethod
    def enable(cls):
        """Enables the Media domain
        """
        return (
            cls.build_send_payload("enable", {
            }),
            None
        )

    @classmethod
    def disable(cls):
        """Disables the Media domain.
        """
        return (
            cls.build_send_payload("disable", {
            }),
            None
        )



class PlayerPropertiesChangedEvent(BaseEvent):

    js_name = 'Media.playerPropertiesChanged'
    hashable = ['playerId']
    is_hashable = True

    def __init__(self,
                 playerId: Union['PlayerId', dict],
                 properties: Union['[PlayerProperty]', dict],
                 ):
        if isinstance(playerId, dict):
            playerId = PlayerId(**playerId)
        self.playerId = playerId
        if isinstance(properties, dict):
            properties = [PlayerProperty](**properties)
        self.properties = properties

    @classmethod
    def build_hash(cls, playerId):
        kwargs = locals()
        kwargs.pop('cls')
        serialized_id_params = ','.join(['='.join([p, str(v)]) for p, v in kwargs.items()])
        h = '{}:{}'.format(cls.js_name, serialized_id_params)
        log.debug('generated hash = %s' % h)
        return h


class PlayerEventsAddedEvent(BaseEvent):

    js_name = 'Media.playerEventsAdded'
    hashable = ['playerId']
    is_hashable = True

    def __init__(self,
                 playerId: Union['PlayerId', dict],
                 events: Union['[PlayerEvent]', dict],
                 ):
        if isinstance(playerId, dict):
            playerId = PlayerId(**playerId)
        self.playerId = playerId
        if isinstance(events, dict):
            events = [PlayerEvent](**events)
        self.events = events

    @classmethod
    def build_hash(cls, playerId):
        kwargs = locals()
        kwargs.pop('cls')
        serialized_id_params = ','.join(['='.join([p, str(v)]) for p, v in kwargs.items()])
        h = '{}:{}'.format(cls.js_name, serialized_id_params)
        log.debug('generated hash = %s' % h)
        return h


class PlayerMessagesLoggedEvent(BaseEvent):

    js_name = 'Media.playerMessagesLogged'
    hashable = ['playerId']
    is_hashable = True

    def __init__(self,
                 playerId: Union['PlayerId', dict],
                 messages: Union['[PlayerMessage]', dict],
                 ):
        if isinstance(playerId, dict):
            playerId = PlayerId(**playerId)
        self.playerId = playerId
        if isinstance(messages, dict):
            messages = [PlayerMessage](**messages)
        self.messages = messages

    @classmethod
    def build_hash(cls, playerId):
        kwargs = locals()
        kwargs.pop('cls')
        serialized_id_params = ','.join(['='.join([p, str(v)]) for p, v in kwargs.items()])
        h = '{}:{}'.format(cls.js_name, serialized_id_params)
        log.debug('generated hash = %s' % h)
        return h


class PlayerErrorsRaisedEvent(BaseEvent):

    js_name = 'Media.playerErrorsRaised'
    hashable = ['playerId']
    is_hashable = True

    def __init__(self,
                 playerId: Union['PlayerId', dict],
                 errors: Union['[PlayerError]', dict],
                 ):
        if isinstance(playerId, dict):
            playerId = PlayerId(**playerId)
        self.playerId = playerId
        if isinstance(errors, dict):
            errors = [PlayerError](**errors)
        self.errors = errors

    @classmethod
    def build_hash(cls, playerId):
        kwargs = locals()
        kwargs.pop('cls')
        serialized_id_params = ','.join(['='.join([p, str(v)]) for p, v in kwargs.items()])
        h = '{}:{}'.format(cls.js_name, serialized_id_params)
        log.debug('generated hash = %s' % h)
        return h


class PlayersCreatedEvent(BaseEvent):

    js_name = 'Media.playersCreated'
    hashable = []
    is_hashable = False

    def __init__(self,
                 players: Union['[PlayerId]', dict],
                 ):
        if isinstance(players, dict):
            players = [PlayerId](**players)
        self.players = players

    @classmethod
    def build_hash(cls):
        raise ValueError('Unable to build hash for non-hashable type')
