"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#IntentResultEvent``."""

import json
from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lex_runtime_v2._protocol.eventstream import HeaderValue, Message

if TYPE_CHECKING:
    import capo_lex_runtime_v2.types.event_id
    import capo_lex_runtime_v2.types.input_mode
    import capo_lex_runtime_v2.types.interpretations
    import capo_lex_runtime_v2.types.recognized_bot_member
    import capo_lex_runtime_v2.types.session_id
    import capo_lex_runtime_v2.types.session_state
    import capo_lex_runtime_v2.types.string_map


class IntentResultEvent(TypedDict, closed=True):
    input_mode: NotRequired["capo_lex_runtime_v2.types.input_mode.InputMode"]
    """<p>Indicates whether the input to the operation was text, speech, or from a touch-tone keypad.</p>"""
    interpretations: NotRequired[
        "capo_lex_runtime_v2.types.interpretations.Interpretations"
    ]
    """<p>A list of intents that Amazon Lex V2 determined might satisfy the user's utterance.</p> <p>Each interpretation includes the intent, a score that indicates how confident Amazon Lex V2 is that the interpretation is the correct one, and an optional sentiment response that indicates the sentiment expressed in the utterance.</p>"""
    session_state: NotRequired["capo_lex_runtime_v2.types.session_state.SessionState"]
    request_attributes: NotRequired["capo_lex_runtime_v2.types.string_map.StringMap"]
    """<p>The attributes sent in the request.</p>"""
    session_id: NotRequired["capo_lex_runtime_v2.types.session_id.SessionId"]
    """<p>The identifier of the session in use.</p>"""
    event_id: NotRequired["capo_lex_runtime_v2.types.event_id.EventId"]
    """<p>A unique identifier of the event sent by Amazon Lex V2. The identifier is in the form <code>RESPONSE-N</code>, where N is a number starting with one and incremented for each event sent by Amazon Lex V2 in the current session.</p>"""
    recognized_bot_member: NotRequired[
        "capo_lex_runtime_v2.types.recognized_bot_member.RecognizedBotMember"
    ]
    """<p>The bot member that is processing the intent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IntentResultEvent) -> dict:
    out: dict = {}
    if "input_mode" in value:
        import capo_lex_runtime_v2.types.input_mode

        out["inputMode"] = capo_lex_runtime_v2.types.input_mode.serialize_json(
            value["input_mode"]
        )
    if "interpretations" in value:
        import capo_lex_runtime_v2.types.interpretations

        out["interpretations"] = (
            capo_lex_runtime_v2.types.interpretations.serialize_json(
                value["interpretations"]
            )
        )
    if "session_state" in value:
        import capo_lex_runtime_v2.types.session_state

        out["sessionState"] = capo_lex_runtime_v2.types.session_state.serialize_json(
            value["session_state"]
        )
    if "request_attributes" in value:
        import capo_lex_runtime_v2.types.string_map

        out["requestAttributes"] = capo_lex_runtime_v2.types.string_map.serialize_json(
            value["request_attributes"]
        )
    if "session_id" in value:
        out["sessionId"] = value["session_id"]
    if "event_id" in value:
        out["eventId"] = value["event_id"]
    if "recognized_bot_member" in value:
        import capo_lex_runtime_v2.types.recognized_bot_member

        out["recognizedBotMember"] = (
            capo_lex_runtime_v2.types.recognized_bot_member.serialize_json(
                value["recognized_bot_member"]
            )
        )
    return out


def deserialize_json(data: dict) -> IntentResultEvent:
    out: IntentResultEvent = {}  # type: ignore[typeddict-item]
    if data.get("inputMode") is not None:
        import capo_lex_runtime_v2.types.input_mode

        out["input_mode"] = capo_lex_runtime_v2.types.input_mode.deserialize_json(
            data["inputMode"]
        )
    if data.get("interpretations") is not None:
        import capo_lex_runtime_v2.types.interpretations

        out["interpretations"] = (
            capo_lex_runtime_v2.types.interpretations.deserialize_json(
                data["interpretations"]
            )
        )
    if data.get("sessionState") is not None:
        import capo_lex_runtime_v2.types.session_state

        out["session_state"] = capo_lex_runtime_v2.types.session_state.deserialize_json(
            data["sessionState"]
        )
    if data.get("requestAttributes") is not None:
        import capo_lex_runtime_v2.types.string_map

        out["request_attributes"] = (
            capo_lex_runtime_v2.types.string_map.deserialize_json(
                data["requestAttributes"]
            )
        )
    if data.get("sessionId") is not None:
        out["session_id"] = data["sessionId"]
    if data.get("eventId") is not None:
        out["event_id"] = data["eventId"]
    if data.get("recognizedBotMember") is not None:
        import capo_lex_runtime_v2.types.recognized_bot_member

        out["recognized_bot_member"] = (
            capo_lex_runtime_v2.types.recognized_bot_member.deserialize_json(
                data["recognizedBotMember"]
            )
        )
    return out


def serialize_event_json(value: IntentResultEvent) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "IntentResultEvent",
        ":content-type": "application/json",
    }
    payload = b""
    payload = json.dumps(serialize_json(value)).encode("utf-8")
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> IntentResultEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: IntentResultEvent = {}  # type: ignore[typeddict-item]
    if payload:
        out = deserialize_json(json.loads(payload))
    return out
