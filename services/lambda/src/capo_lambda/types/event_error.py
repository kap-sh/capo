"""Generated from Smithy shape ``com.amazonaws.lambda#EventError``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.error_object
    import capo_lambda.types.truncated


class EventError(TypedDict, closed=True):
    payload: NotRequired["capo_lambda.types.error_object.ErrorObject"]
    """<p>The error payload.</p>"""
    truncated: NotRequired["capo_lambda.types.truncated.Truncated"]
    """<p>Indicates if the error payload was truncated due to size limits.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EventError) -> dict:
    out: dict = {}
    if "payload" in value:
        import capo_lambda.types.error_object

        out["Payload"] = capo_lambda.types.error_object.serialize_json(value["payload"])
    if "truncated" in value:
        out["Truncated"] = value["truncated"]
    return out


def deserialize_json(data: dict) -> EventError:
    out: EventError = {}  # type: ignore[typeddict-item]
    if data.get("Payload") is not None:
        import capo_lambda.types.error_object

        out["payload"] = capo_lambda.types.error_object.deserialize_json(
            data["Payload"]
        )
    if data.get("Truncated") is not None:
        out["truncated"] = data["Truncated"]
    return out


def redact_sensitive(value: EventError) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "payload" in value:
        import capo_lambda.types.error_object

        out["payload"] = capo_lambda.types.error_object.redact_sensitive(
            value["payload"]
        )
    return out
