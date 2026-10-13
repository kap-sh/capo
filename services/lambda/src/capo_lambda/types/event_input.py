"""Generated from Smithy shape ``com.amazonaws.lambda#EventInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.input_payload
    import capo_lambda.types.truncated


class EventInput(TypedDict, closed=True):
    payload: NotRequired["capo_lambda.types.input_payload.InputPayload"]
    """<p>The input payload.</p>"""
    truncated: NotRequired["capo_lambda.types.truncated.Truncated"]
    """<p>Indicates if the error payload was truncated due to size limits.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EventInput) -> dict:
    out: dict = {}
    if "payload" in value:
        out["Payload"] = value["payload"]
    if "truncated" in value:
        out["Truncated"] = value["truncated"]
    return out


def deserialize_json(data: dict) -> EventInput:
    out: EventInput = {}  # type: ignore[typeddict-item]
    if data.get("Payload") is not None:
        out["payload"] = data["Payload"]
    if data.get("Truncated") is not None:
        out["truncated"] = data["Truncated"]
    return out


def redact_sensitive(value: EventInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "payload" in value:
        out["payload"] = "*** Sensitive Data Redacted ***"
    return out
