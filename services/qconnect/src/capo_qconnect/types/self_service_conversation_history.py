"""Generated from Smithy shape ``com.amazonaws.qconnect#SelfServiceConversationHistory``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_qconnect.types.sensitive_string


class SelfServiceConversationHistory(TypedDict, closed=True):
    turn_number: "int"
    """<p>The number of turn of the conversation history data.</p>"""
    input_transcript: NotRequired[
        "capo_qconnect.types.sensitive_string.SensitiveString"
    ]
    """<p>The input transcript of the conversation history data.</p>"""
    bot_response: NotRequired["capo_qconnect.types.sensitive_string.SensitiveString"]
    """<p>The bot response of the conversation history data.</p>"""
    timestamp: NotRequired["datetime.datetime"]
    """<p>The timestamp of the conversation history entry.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SelfServiceConversationHistory) -> dict:
    out: dict = {}
    out["turnNumber"] = value.get("turn_number", 0)
    if "input_transcript" in value:
        out["inputTranscript"] = value["input_transcript"]
    if "bot_response" in value:
        out["botResponse"] = value["bot_response"]
    if "timestamp" in value:
        import capo_qconnect.types._prelude.timestamp

        out["timestamp"] = capo_qconnect.types._prelude.timestamp.serialize_json(
            value["timestamp"]
        )
    return out


def deserialize_json(data: dict) -> SelfServiceConversationHistory:
    out: SelfServiceConversationHistory = {}  # type: ignore[typeddict-item]
    if data.get("turnNumber") is not None:
        out["turn_number"] = data["turnNumber"]
    else:
        out["turn_number"] = 0
    if data.get("inputTranscript") is not None:
        out["input_transcript"] = data["inputTranscript"]
    if data.get("botResponse") is not None:
        out["bot_response"] = data["botResponse"]
    if data.get("timestamp") is not None:
        import capo_qconnect.types._prelude.timestamp

        out["timestamp"] = capo_qconnect.types._prelude.timestamp.deserialize_json(
            data["timestamp"]
        )
    return out


def redact_sensitive(value: SelfServiceConversationHistory) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "input_transcript" in value:
        out["input_transcript"] = "*** Sensitive Data Redacted ***"
    if "bot_response" in value:
        out["bot_response"] = "*** Sensitive Data Redacted ***"
    return out
