"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#GetSessionResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_runtime_v2.types.interpretations
    import capo_lex_runtime_v2.types.messages
    import capo_lex_runtime_v2.types.non_empty_string
    import capo_lex_runtime_v2.types.session_state


class GetSessionResponse(TypedDict, closed=True):
    session_id: NotRequired["capo_lex_runtime_v2.types.non_empty_string.NonEmptyString"]
    """<p>The identifier of the returned session.</p>"""
    messages: NotRequired["capo_lex_runtime_v2.types.messages.Messages"]
    """<p>A list of messages that were last sent to the user. The messages are ordered based on the order that your returned the messages from your Lambda function or the order that messages are defined in the bot. </p>"""
    interpretations: NotRequired[
        "capo_lex_runtime_v2.types.interpretations.Interpretations"
    ]
    """<p>A list of intents that Amazon Lex V2 determined might satisfy the user's utterance. </p> <p>Each interpretation includes the intent, a score that indicates how confident Amazon Lex V2 is that the interpretation is the correct one, and an optional sentiment response that indicates the sentiment expressed in the utterance.</p>"""
    session_state: NotRequired["capo_lex_runtime_v2.types.session_state.SessionState"]
    """<p>Represents the current state of the dialog between the user and the bot.</p> <p>You can use this to determine the progress of the conversation and what the next action might be.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSessionResponse) -> dict:
    out: dict = {}
    if "session_id" in value:
        out["sessionId"] = value["session_id"]
    if "messages" in value:
        import capo_lex_runtime_v2.types.messages

        out["messages"] = capo_lex_runtime_v2.types.messages.serialize_json(
            value["messages"]
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
    return out


def deserialize_json(data: dict) -> GetSessionResponse:
    out: GetSessionResponse = {}  # type: ignore[typeddict-item]
    if data.get("sessionId") is not None:
        out["session_id"] = data["sessionId"]
    if data.get("messages") is not None:
        import capo_lex_runtime_v2.types.messages

        out["messages"] = capo_lex_runtime_v2.types.messages.deserialize_json(
            data["messages"]
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
    return out


def redact_sensitive(value: GetSessionResponse) -> dict[str, Any]:
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
