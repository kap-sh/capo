"""Generated from Smithy shape ``com.amazonaws.lambda#ExecutionStoppedDetails``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_lambda.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lambda.types.event_error


class ExecutionStoppedDetails(TypedDict, closed=True):
    error: "capo_lambda.types.event_error.EventError"
    """<p>Details about why the execution stopped.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExecutionStoppedDetails) -> dict:
    out: dict = {}
    import capo_lambda.types.event_error

    out["Error"] = capo_lambda.types.event_error.serialize_json(value["error"])
    return out


def deserialize_json(data: dict) -> ExecutionStoppedDetails:
    out: ExecutionStoppedDetails = {}  # type: ignore[typeddict-item]
    if data.get("Error") is not None:
        import capo_lambda.types.event_error

        out["error"] = capo_lambda.types.event_error.deserialize_json(data["Error"])
    else:
        raise DeserializationError("ExecutionStoppedDetails.error required")
    return out


def redact_sensitive(value: ExecutionStoppedDetails) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "error" in value:
        import capo_lambda.types.event_error

        out["error"] = capo_lambda.types.event_error.redact_sensitive(value["error"])
    return out
