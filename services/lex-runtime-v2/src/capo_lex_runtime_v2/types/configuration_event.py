"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#ConfigurationEvent``."""

import json
from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lex_runtime_v2._protocol.eventstream import HeaderValue, Message
from capo_lex_runtime_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lex_runtime_v2.types.boolean
    import capo_lex_runtime_v2.types.epoch_millis
    import capo_lex_runtime_v2.types.event_id
    import capo_lex_runtime_v2.types.messages
    import capo_lex_runtime_v2.types.non_empty_string
    import capo_lex_runtime_v2.types.session_state
    import capo_lex_runtime_v2.types.string_map


class ConfigurationEvent(TypedDict, closed=True):
    request_attributes: NotRequired["capo_lex_runtime_v2.types.string_map.StringMap"]
    """<p>Request-specific information passed between the client application and Amazon Lex V2.</p> <p>The namespace <code>x-amz-lex:</code> is reserved for special attributes. Don't create any request attributes for prefix <code>x-amz-lex:</code>.</p>"""
    response_content_type: "capo_lex_runtime_v2.types.non_empty_string.NonEmptyString"
    """<p>The message that Amazon Lex V2 returns in the response can be either text or speech based on the <code>responseContentType</code> value.</p> <ul> <li> <p>If the value is <code>text/plain;charset=utf-8</code>, Amazon Lex V2 returns text in the response.</p> </li> <li> <p>If the value begins with <code>audio/</code>, Amazon Lex V2 returns speech in the response. Amazon Lex V2 uses Amazon Polly to generate the speech using the configuration that you specified in the <code>requestContentType</code> parameter. For example, if you specify <code>audio/mpeg</code> as the value, Amazon Lex V2 returns speech in the MPEG format.</p> </li> <li> <p>If the value is <code>audio/pcm</code>, the speech returned is audio/pcm in 16-bit, little-endian format.</p> </li> <li> <p>The following are the accepted values:</p> <ul> <li> <p>audio/mpeg</p> </li> <li> <p>audio/ogg</p> </li> <li> <p>audio/pcm</p> </li> <li> <p>audio/* (defaults to mpeg)</p> </li> <li> <p>text/plain; charset=utf-8</p> </li> </ul> </li> </ul>"""
    session_state: NotRequired["capo_lex_runtime_v2.types.session_state.SessionState"]
    welcome_messages: NotRequired["capo_lex_runtime_v2.types.messages.Messages"]
    r"""<p>A list of messages to send to the user.</p> <p>If you set the <code>welcomeMessage</code> field, you must also set the <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/API_runtime_DialogAction.html\"> <code>DialogAction</code> </a> structure's <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/API_runtime_DialogAction.html#lexv2-Type-runtime_DialogAction-type\"> <code>type</code> </a> field.</p>"""
    disable_playback: "capo_lex_runtime_v2.types.boolean.Boolean"
    """<p>Determines whether Amazon Lex V2 should send audio responses to the client application. </p> <p>Set this field to false when the client is operating in a playback mode where audio responses are played to the user. If the client isn't operating in playback mode, such as a text chat application, set this to true so that Amazon Lex V2 doesn't wait for the prompt to finish playing on the client.</p>"""
    event_id: NotRequired["capo_lex_runtime_v2.types.event_id.EventId"]
    """<p>A unique identifier that your application assigns to the event. You can use this to identify events in logs.</p>"""
    client_timestamp_millis: "capo_lex_runtime_v2.types.epoch_millis.EpochMillis"
    """<p>A timestamp set by the client of the date and time that the event was sent to Amazon Lex V2.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationEvent) -> dict:
    out: dict = {}
    if "request_attributes" in value:
        import capo_lex_runtime_v2.types.string_map

        out["requestAttributes"] = capo_lex_runtime_v2.types.string_map.serialize_json(
            value["request_attributes"]
        )
    out["responseContentType"] = value["response_content_type"]
    if "session_state" in value:
        import capo_lex_runtime_v2.types.session_state

        out["sessionState"] = capo_lex_runtime_v2.types.session_state.serialize_json(
            value["session_state"]
        )
    if "welcome_messages" in value:
        import capo_lex_runtime_v2.types.messages

        out["welcomeMessages"] = capo_lex_runtime_v2.types.messages.serialize_json(
            value["welcome_messages"]
        )
    out["disablePlayback"] = value.get("disable_playback", False)
    if "event_id" in value:
        out["eventId"] = value["event_id"]
    out["clientTimestampMillis"] = value.get("client_timestamp_millis", 0)
    return out


def deserialize_json(data: dict) -> ConfigurationEvent:
    out: ConfigurationEvent = {}  # type: ignore[typeddict-item]
    if data.get("requestAttributes") is not None:
        import capo_lex_runtime_v2.types.string_map

        out["request_attributes"] = (
            capo_lex_runtime_v2.types.string_map.deserialize_json(
                data["requestAttributes"]
            )
        )
    if data.get("responseContentType") is not None:
        out["response_content_type"] = data["responseContentType"]
    else:
        raise DeserializationError("ConfigurationEvent.response_content_type required")
    if data.get("sessionState") is not None:
        import capo_lex_runtime_v2.types.session_state

        out["session_state"] = capo_lex_runtime_v2.types.session_state.deserialize_json(
            data["sessionState"]
        )
    if data.get("welcomeMessages") is not None:
        import capo_lex_runtime_v2.types.messages

        out["welcome_messages"] = capo_lex_runtime_v2.types.messages.deserialize_json(
            data["welcomeMessages"]
        )
    if data.get("disablePlayback") is not None:
        out["disable_playback"] = data["disablePlayback"]
    else:
        out["disable_playback"] = False
    if data.get("eventId") is not None:
        out["event_id"] = data["eventId"]
    if data.get("clientTimestampMillis") is not None:
        out["client_timestamp_millis"] = data["clientTimestampMillis"]
    else:
        out["client_timestamp_millis"] = 0
    return out


def serialize_event_json(value: ConfigurationEvent) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "ConfigurationEvent",
        ":content-type": "application/json",
    }
    payload = b""
    payload = json.dumps(serialize_json(value)).encode("utf-8")
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> ConfigurationEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: ConfigurationEvent = {}  # type: ignore[typeddict-item]
    if payload:
        out = deserialize_json(json.loads(payload))
    return out
