"""Generated from Smithy shape ``com.amazonaws.lambda#StepFailedDetails``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_lambda.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lambda.types.event_error
    import capo_lambda.types.retry_details


class StepFailedDetails(TypedDict, closed=True):
    error: "capo_lambda.types.event_error.EventError"
    """<p>Details about the step failure.</p>"""
    retry_details: "capo_lambda.types.retry_details.RetryDetails"
    """<p>Information about retry attempts for this step operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StepFailedDetails) -> dict:
    out: dict = {}
    import capo_lambda.types.event_error

    out["Error"] = capo_lambda.types.event_error.serialize_json(value["error"])
    import capo_lambda.types.retry_details

    out["RetryDetails"] = capo_lambda.types.retry_details.serialize_json(
        value["retry_details"]
    )
    return out


def deserialize_json(data: dict) -> StepFailedDetails:
    out: StepFailedDetails = {}  # type: ignore[typeddict-item]
    if data.get("Error") is not None:
        import capo_lambda.types.event_error

        out["error"] = capo_lambda.types.event_error.deserialize_json(data["Error"])
    else:
        raise DeserializationError("StepFailedDetails.error required")
    if data.get("RetryDetails") is not None:
        import capo_lambda.types.retry_details

        out["retry_details"] = capo_lambda.types.retry_details.deserialize_json(
            data["RetryDetails"]
        )
    else:
        raise DeserializationError("StepFailedDetails.retry_details required")
    return out


def redact_sensitive(value: StepFailedDetails) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "error" in value:
        import capo_lambda.types.event_error

        out["error"] = capo_lambda.types.event_error.redact_sensitive(value["error"])
    return out
