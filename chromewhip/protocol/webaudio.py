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

# GraphObjectId: An unique ID for a graph object (AudioContext, AudioNode, AudioParam) in Web Audio API
GraphObjectId = str

# ContextType: Enum of BaseAudioContext types
ContextType = str

# ContextState: Enum of AudioContextState from the spec
ContextState = str

# NodeType: Enum of AudioNode types
NodeType = str

# ChannelCountMode: Enum of AudioNode::ChannelCountMode from the spec
ChannelCountMode = str

# ChannelInterpretation: Enum of AudioNode::ChannelInterpretation from the spec
ChannelInterpretation = str

# ParamType: Enum of AudioParam types
ParamType = str

# AutomationRate: Enum of AudioParam::AutomationRate from the spec
AutomationRate = str

# ContextRealtimeData: Fields in AudioContext that change in real-time.
class ContextRealtimeData(ChromeTypeBase):
    def __init__(self,
                 currentTime: Union['float'],
                 renderCapacity: Union['float'],
                 callbackIntervalMean: Union['float'],
                 callbackIntervalVariance: Union['float'],
                 ):

        self.currentTime = currentTime
        self.renderCapacity = renderCapacity
        self.callbackIntervalMean = callbackIntervalMean
        self.callbackIntervalVariance = callbackIntervalVariance


# BaseAudioContext: Protocol object for BaseAudioContext
class BaseAudioContext(ChromeTypeBase):
    def __init__(self,
                 contextId: Union['GraphObjectId'],
                 contextType: Union['ContextType'],
                 contextState: Union['ContextState'],
                 callbackBufferSize: Union['float'],
                 maxOutputChannelCount: Union['float'],
                 sampleRate: Union['float'],
                 realtimeData: Optional['ContextRealtimeData'] = None,
                 ):

        self.contextId = contextId
        self.contextType = contextType
        self.contextState = contextState
        self.realtimeData = realtimeData
        self.callbackBufferSize = callbackBufferSize
        self.maxOutputChannelCount = maxOutputChannelCount
        self.sampleRate = sampleRate


# AudioListener: Protocol object for AudioListner
class AudioListener(ChromeTypeBase):
    def __init__(self,
                 listenerId: Union['GraphObjectId'],
                 contextId: Union['GraphObjectId'],
                 ):

        self.listenerId = listenerId
        self.contextId = contextId


# AudioNode: Protocol object for AudioNode
class AudioNode(ChromeTypeBase):
    def __init__(self,
                 nodeId: Union['GraphObjectId'],
                 contextId: Union['GraphObjectId'],
                 nodeType: Union['NodeType'],
                 numberOfInputs: Union['float'],
                 numberOfOutputs: Union['float'],
                 channelCount: Union['float'],
                 channelCountMode: Union['ChannelCountMode'],
                 channelInterpretation: Union['ChannelInterpretation'],
                 ):

        self.nodeId = nodeId
        self.contextId = contextId
        self.nodeType = nodeType
        self.numberOfInputs = numberOfInputs
        self.numberOfOutputs = numberOfOutputs
        self.channelCount = channelCount
        self.channelCountMode = channelCountMode
        self.channelInterpretation = channelInterpretation


# AudioParam: Protocol object for AudioParam
class AudioParam(ChromeTypeBase):
    def __init__(self,
                 paramId: Union['GraphObjectId'],
                 nodeId: Union['GraphObjectId'],
                 contextId: Union['GraphObjectId'],
                 paramType: Union['ParamType'],
                 rate: Union['AutomationRate'],
                 defaultValue: Union['float'],
                 minValue: Union['float'],
                 maxValue: Union['float'],
                 ):

        self.paramId = paramId
        self.nodeId = nodeId
        self.contextId = contextId
        self.paramType = paramType
        self.rate = rate
        self.defaultValue = defaultValue
        self.minValue = minValue
        self.maxValue = maxValue


class WebAudio(PayloadMixin):
    """ This domain allows inspection of Web Audio API.
https://webaudio.github.io/web-audio-api/
    """
    @classmethod
    def enable(cls):
        """Enables the WebAudio domain and starts sending context lifetime events.
        """
        return (
            cls.build_send_payload("enable", {
            }),
            None
        )

    @classmethod
    def disable(cls):
        """Disables the WebAudio domain.
        """
        return (
            cls.build_send_payload("disable", {
            }),
            None
        )

    @classmethod
    def getRealtimeData(cls,
                        contextId: Union['GraphObjectId'],
                        ):
        """Fetch the realtime data from the registered contexts.
        :param contextId: 
        :type contextId: GraphObjectId
        """
        return (
            cls.build_send_payload("getRealtimeData", {
                "contextId": contextId,
            }),
            cls.convert_payload({
                "realtimeData": {
                    "class": ContextRealtimeData,
                    "optional": False
                },
            })
        )



class ContextCreatedEvent(BaseEvent):

    js_name = 'Webaudio.contextCreated'
    hashable = []
    is_hashable = False

    def __init__(self,
                 context: Union['BaseAudioContext', dict],
                 ):
        if isinstance(context, dict):
            context = BaseAudioContext(**context)
        self.context = context

    @classmethod
    def build_hash(cls):
        raise ValueError('Unable to build hash for non-hashable type')


class ContextWillBeDestroyedEvent(BaseEvent):

    js_name = 'Webaudio.contextWillBeDestroyed'
    hashable = ['contextId']
    is_hashable = True

    def __init__(self,
                 contextId: Union['GraphObjectId', dict],
                 ):
        if isinstance(contextId, dict):
            contextId = GraphObjectId(**contextId)
        self.contextId = contextId

    @classmethod
    def build_hash(cls, contextId):
        kwargs = locals()
        kwargs.pop('cls')
        serialized_id_params = ','.join(['='.join([p, str(v)]) for p, v in kwargs.items()])
        h = '{}:{}'.format(cls.js_name, serialized_id_params)
        log.debug('generated hash = %s' % h)
        return h


class ContextChangedEvent(BaseEvent):

    js_name = 'Webaudio.contextChanged'
    hashable = []
    is_hashable = False

    def __init__(self,
                 context: Union['BaseAudioContext', dict],
                 ):
        if isinstance(context, dict):
            context = BaseAudioContext(**context)
        self.context = context

    @classmethod
    def build_hash(cls):
        raise ValueError('Unable to build hash for non-hashable type')


class AudioListenerCreatedEvent(BaseEvent):

    js_name = 'Webaudio.audioListenerCreated'
    hashable = []
    is_hashable = False

    def __init__(self,
                 listener: Union['AudioListener', dict],
                 ):
        if isinstance(listener, dict):
            listener = AudioListener(**listener)
        self.listener = listener

    @classmethod
    def build_hash(cls):
        raise ValueError('Unable to build hash for non-hashable type')


class AudioListenerWillBeDestroyedEvent(BaseEvent):

    js_name = 'Webaudio.audioListenerWillBeDestroyed'
    hashable = ['contextId', 'listenerId']
    is_hashable = True

    def __init__(self,
                 contextId: Union['GraphObjectId', dict],
                 listenerId: Union['GraphObjectId', dict],
                 ):
        if isinstance(contextId, dict):
            contextId = GraphObjectId(**contextId)
        self.contextId = contextId
        if isinstance(listenerId, dict):
            listenerId = GraphObjectId(**listenerId)
        self.listenerId = listenerId

    @classmethod
    def build_hash(cls, contextId, listenerId):
        kwargs = locals()
        kwargs.pop('cls')
        serialized_id_params = ','.join(['='.join([p, str(v)]) for p, v in kwargs.items()])
        h = '{}:{}'.format(cls.js_name, serialized_id_params)
        log.debug('generated hash = %s' % h)
        return h


class AudioNodeCreatedEvent(BaseEvent):

    js_name = 'Webaudio.audioNodeCreated'
    hashable = []
    is_hashable = False

    def __init__(self,
                 node: Union['AudioNode', dict],
                 ):
        if isinstance(node, dict):
            node = AudioNode(**node)
        self.node = node

    @classmethod
    def build_hash(cls):
        raise ValueError('Unable to build hash for non-hashable type')


class AudioNodeWillBeDestroyedEvent(BaseEvent):

    js_name = 'Webaudio.audioNodeWillBeDestroyed'
    hashable = ['contextId', 'nodeId']
    is_hashable = True

    def __init__(self,
                 contextId: Union['GraphObjectId', dict],
                 nodeId: Union['GraphObjectId', dict],
                 ):
        if isinstance(contextId, dict):
            contextId = GraphObjectId(**contextId)
        self.contextId = contextId
        if isinstance(nodeId, dict):
            nodeId = GraphObjectId(**nodeId)
        self.nodeId = nodeId

    @classmethod
    def build_hash(cls, contextId, nodeId):
        kwargs = locals()
        kwargs.pop('cls')
        serialized_id_params = ','.join(['='.join([p, str(v)]) for p, v in kwargs.items()])
        h = '{}:{}'.format(cls.js_name, serialized_id_params)
        log.debug('generated hash = %s' % h)
        return h


class AudioParamCreatedEvent(BaseEvent):

    js_name = 'Webaudio.audioParamCreated'
    hashable = []
    is_hashable = False

    def __init__(self,
                 param: Union['AudioParam', dict],
                 ):
        if isinstance(param, dict):
            param = AudioParam(**param)
        self.param = param

    @classmethod
    def build_hash(cls):
        raise ValueError('Unable to build hash for non-hashable type')


class AudioParamWillBeDestroyedEvent(BaseEvent):

    js_name = 'Webaudio.audioParamWillBeDestroyed'
    hashable = ['contextId', 'nodeId', 'paramId']
    is_hashable = True

    def __init__(self,
                 contextId: Union['GraphObjectId', dict],
                 nodeId: Union['GraphObjectId', dict],
                 paramId: Union['GraphObjectId', dict],
                 ):
        if isinstance(contextId, dict):
            contextId = GraphObjectId(**contextId)
        self.contextId = contextId
        if isinstance(nodeId, dict):
            nodeId = GraphObjectId(**nodeId)
        self.nodeId = nodeId
        if isinstance(paramId, dict):
            paramId = GraphObjectId(**paramId)
        self.paramId = paramId

    @classmethod
    def build_hash(cls, contextId, nodeId, paramId):
        kwargs = locals()
        kwargs.pop('cls')
        serialized_id_params = ','.join(['='.join([p, str(v)]) for p, v in kwargs.items()])
        h = '{}:{}'.format(cls.js_name, serialized_id_params)
        log.debug('generated hash = %s' % h)
        return h


class NodesConnectedEvent(BaseEvent):

    js_name = 'Webaudio.nodesConnected'
    hashable = ['contextId', 'sourceId', 'destinationId']
    is_hashable = True

    def __init__(self,
                 contextId: Union['GraphObjectId', dict],
                 sourceId: Union['GraphObjectId', dict],
                 destinationId: Union['GraphObjectId', dict],
                 sourceOutputIndex: Union['float', dict, None] = None,
                 destinationInputIndex: Union['float', dict, None] = None,
                 ):
        if isinstance(contextId, dict):
            contextId = GraphObjectId(**contextId)
        self.contextId = contextId
        if isinstance(sourceId, dict):
            sourceId = GraphObjectId(**sourceId)
        self.sourceId = sourceId
        if isinstance(destinationId, dict):
            destinationId = GraphObjectId(**destinationId)
        self.destinationId = destinationId
        if isinstance(sourceOutputIndex, dict):
            sourceOutputIndex = float(**sourceOutputIndex)
        self.sourceOutputIndex = sourceOutputIndex
        if isinstance(destinationInputIndex, dict):
            destinationInputIndex = float(**destinationInputIndex)
        self.destinationInputIndex = destinationInputIndex

    @classmethod
    def build_hash(cls, contextId, sourceId, destinationId):
        kwargs = locals()
        kwargs.pop('cls')
        serialized_id_params = ','.join(['='.join([p, str(v)]) for p, v in kwargs.items()])
        h = '{}:{}'.format(cls.js_name, serialized_id_params)
        log.debug('generated hash = %s' % h)
        return h


class NodesDisconnectedEvent(BaseEvent):

    js_name = 'Webaudio.nodesDisconnected'
    hashable = ['contextId', 'sourceId', 'destinationId']
    is_hashable = True

    def __init__(self,
                 contextId: Union['GraphObjectId', dict],
                 sourceId: Union['GraphObjectId', dict],
                 destinationId: Union['GraphObjectId', dict],
                 sourceOutputIndex: Union['float', dict, None] = None,
                 destinationInputIndex: Union['float', dict, None] = None,
                 ):
        if isinstance(contextId, dict):
            contextId = GraphObjectId(**contextId)
        self.contextId = contextId
        if isinstance(sourceId, dict):
            sourceId = GraphObjectId(**sourceId)
        self.sourceId = sourceId
        if isinstance(destinationId, dict):
            destinationId = GraphObjectId(**destinationId)
        self.destinationId = destinationId
        if isinstance(sourceOutputIndex, dict):
            sourceOutputIndex = float(**sourceOutputIndex)
        self.sourceOutputIndex = sourceOutputIndex
        if isinstance(destinationInputIndex, dict):
            destinationInputIndex = float(**destinationInputIndex)
        self.destinationInputIndex = destinationInputIndex

    @classmethod
    def build_hash(cls, contextId, sourceId, destinationId):
        kwargs = locals()
        kwargs.pop('cls')
        serialized_id_params = ','.join(['='.join([p, str(v)]) for p, v in kwargs.items()])
        h = '{}:{}'.format(cls.js_name, serialized_id_params)
        log.debug('generated hash = %s' % h)
        return h


class NodeParamConnectedEvent(BaseEvent):

    js_name = 'Webaudio.nodeParamConnected'
    hashable = ['contextId', 'sourceId', 'destinationId']
    is_hashable = True

    def __init__(self,
                 contextId: Union['GraphObjectId', dict],
                 sourceId: Union['GraphObjectId', dict],
                 destinationId: Union['GraphObjectId', dict],
                 sourceOutputIndex: Union['float', dict, None] = None,
                 ):
        if isinstance(contextId, dict):
            contextId = GraphObjectId(**contextId)
        self.contextId = contextId
        if isinstance(sourceId, dict):
            sourceId = GraphObjectId(**sourceId)
        self.sourceId = sourceId
        if isinstance(destinationId, dict):
            destinationId = GraphObjectId(**destinationId)
        self.destinationId = destinationId
        if isinstance(sourceOutputIndex, dict):
            sourceOutputIndex = float(**sourceOutputIndex)
        self.sourceOutputIndex = sourceOutputIndex

    @classmethod
    def build_hash(cls, contextId, sourceId, destinationId):
        kwargs = locals()
        kwargs.pop('cls')
        serialized_id_params = ','.join(['='.join([p, str(v)]) for p, v in kwargs.items()])
        h = '{}:{}'.format(cls.js_name, serialized_id_params)
        log.debug('generated hash = %s' % h)
        return h


class NodeParamDisconnectedEvent(BaseEvent):

    js_name = 'Webaudio.nodeParamDisconnected'
    hashable = ['contextId', 'sourceId', 'destinationId']
    is_hashable = True

    def __init__(self,
                 contextId: Union['GraphObjectId', dict],
                 sourceId: Union['GraphObjectId', dict],
                 destinationId: Union['GraphObjectId', dict],
                 sourceOutputIndex: Union['float', dict, None] = None,
                 ):
        if isinstance(contextId, dict):
            contextId = GraphObjectId(**contextId)
        self.contextId = contextId
        if isinstance(sourceId, dict):
            sourceId = GraphObjectId(**sourceId)
        self.sourceId = sourceId
        if isinstance(destinationId, dict):
            destinationId = GraphObjectId(**destinationId)
        self.destinationId = destinationId
        if isinstance(sourceOutputIndex, dict):
            sourceOutputIndex = float(**sourceOutputIndex)
        self.sourceOutputIndex = sourceOutputIndex

    @classmethod
    def build_hash(cls, contextId, sourceId, destinationId):
        kwargs = locals()
        kwargs.pop('cls')
        serialized_id_params = ','.join(['='.join([p, str(v)]) for p, v in kwargs.items()])
        h = '{}:{}'.format(cls.js_name, serialized_id_params)
        log.debug('generated hash = %s' % h)
        return h
