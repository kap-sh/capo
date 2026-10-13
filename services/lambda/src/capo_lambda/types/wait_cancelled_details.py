"""Generated from Smithy shape ``com.amazonaws.lambda#WaitCancelledDetails``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.event_error


class WaitCancelledDetails(TypedDict, closed=True):
    error: NotRequired["capo_lambda.types.event_error.EventError"]
    """<p>Details about why the wait operation was cancelled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WaitCancelledDetails) -> dict:
    out: dict = {}
    if "error" in value:
        import capo_lambda.types.event_error

        out["Error"] = capo_lambda.types.event_error.serialize_json(value["error"])
    return out


def deserialize_json(data: dict) -> WaitCancelledDetails:
    out: WaitCancelledDetails = {}  # type: ignore[typeddict-item]
    if data.get("Error") is not None:
        import capo_lambda.types.event_error

        out["error"] = capo_lambda.types.event_error.deserialize_json(data["Error"])
    return out


def redact_sensitive(value: WaitCancelledDetails) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "error" in value:
        import capo_lambda.types.event_error

        out["error"] = capo_lambda.types.event_error.redact_sensitive(value["error"])
    return out
