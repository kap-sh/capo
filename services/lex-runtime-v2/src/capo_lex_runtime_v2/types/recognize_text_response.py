"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#RecognizeTextResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_runtime_v2.types.interpretations
    import capo_lex_runtime_v2.types.messages
    import capo_lex_runtime_v2.types.recognized_bot_member
    import capo_lex_runtime_v2.types.session_id
    import capo_lex_runtime_v2.types.session_state
    import capo_lex_runtime_v2.types.string_map


class RecognizeTextResponse(TypedDict, closed=True):
    messages: NotRequired["capo_lex_runtime_v2.types.messages.Messages"]
    """<p>A list of messages last sent to the user. The messages are ordered based on the order that you returned the messages from your Lambda function or the order that the messages are defined in the bot.</p>"""
    session_state: NotRequired["capo_lex_runtime_v2.types.session_state.SessionState"]
    """<p>Represents the current state of the dialog between the user and the bot. </p> <p>Use this to determine the progress of the conversation and what the next action may be.</p>"""
    interpretations: NotRequired[
        "capo_lex_runtime_v2.types.interpretations.Interpretations"
    ]
    """<p>A list of intents that Amazon Lex V2 determined might satisfy the user's utterance. </p> <p>Each interpretation includes the intent, a score that indicates now confident Amazon Lex V2 is that the interpretation is the correct one, and an optional sentiment response that indicates the sentiment expressed in the utterance.</p>"""
    request_attributes: NotRequired["capo_lex_runtime_v2.types.string_map.StringMap"]
    """<p>The attributes sent in the request.</p>"""
    session_id: NotRequired["capo_lex_runtime_v2.types.session_id.SessionId"]
    """<p>The identifier of the session in use.</p>"""
    recognized_bot_member: NotRequired[
        "capo_lex_runtime_v2.types.recognized_bot_member.RecognizedBotMember"
    ]
    """<p>The bot member that recognized the text.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecognizeTextResponse) -> dict:
    out: dict = {}
    if "messages" in value:
        import capo_lex_runtime_v2.types.messages

        out["messages"] = capo_lex_runtime_v2.types.messages.serialize_json(
            value["messages"]
        )
    if "session_state" in value:
        import capo_lex_runtime_v2.types.session_state

        out["sessionState"] = capo_lex_runtime_v2.types.session_state.serialize_json(
            value["session_state"]
        )
    if "interpretations" in value:
        import capo_lex_runtime_v2.types.interpretations

        out["interpretations"] = (
            capo_lex_runtime_v2.types.interpretations.serialize_json(
                value["interpretations"]
            )
        )
    if "request_attributes" in value:
        import capo_lex_runtime_v2.types.string_map

        out["requestAttributes"] = capo_lex_runtime_v2.types.string_map.serialize_json(
            value["request_attributes"]
        )
    if "session_id" in value:
        out["sessionId"] = value["session_id"]
    if "recognized_bot_member" in value:
        import capo_lex_runtime_v2.types.recognized_bot_member

        out["recognizedBotMember"] = (
            capo_lex_runtime_v2.types.recognized_bot_member.serialize_json(
                value["recognized_bot_member"]
            )
        )
    return out


def deserialize_json(data: dict) -> RecognizeTextResponse:
    out: RecognizeTextResponse = {}  # type: ignore[typeddict-item]
    if data.get("messages") is not None:
        import capo_lex_runtime_v2.types.messages

        out["messages"] = capo_lex_runtime_v2.types.messages.deserialize_json(
            data["messages"]
        )
    if data.get("sessionState") is not None:
        import capo_lex_runtime_v2.types.session_state

        out["session_state"] = capo_lex_runtime_v2.types.session_state.deserialize_json(
            data["sessionState"]
        )
    if data.get("interpretations") is not None:
        import capo_lex_runtime_v2.types.interpretations

        out["interpretations"] = (
            capo_lex_runtime_v2.types.interpretations.deserialize_json(
                data["interpretations"]
            )
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
    if data.get("recognizedBotMember") is not None:
        import capo_lex_runtime_v2.types.recognized_bot_member

        out["recognized_bot_member"] = (
            capo_lex_runtime_v2.types.recognized_bot_member.deserialize_json(
                data["recognizedBotMember"]
            )
        )
    return out


def redact_sensitive(value: RecognizeTextResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "messages" in value:
        import capo_lex_runtime_v2.types.messages

        out["messages"] = capo_lex_runtime_v2.types.messages.redact_sensitive(
            value["messages"]
        )
    if "session_state" in value:
        import capo_lex_runtime_v2.types.session_state

        out["session_state"] = capo_lex_runtime_v2.types.session_state.redact_sensitive(
            value["session_state"]
        )
    return out
