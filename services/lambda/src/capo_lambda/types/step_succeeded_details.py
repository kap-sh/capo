"""Generated from Smithy shape ``com.amazonaws.lambda#StepSucceededDetails``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_lambda.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lambda.types.event_result
    import capo_lambda.types.retry_details


class StepSucceededDetails(TypedDict, closed=True):
    result: "capo_lambda.types.event_result.EventResult"
    """<p>The response payload from the successful operation.</p>"""
    retry_details: "capo_lambda.types.retry_details.RetryDetails"
    """<p>Information about retry attempts for this step operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StepSucceededDetails) -> dict:
    out: dict = {}
    import capo_lambda.types.event_result

    out["Result"] = capo_lambda.types.event_result.serialize_json(value["result"])
    import capo_lambda.types.retry_details

    out["RetryDetails"] = capo_lambda.types.retry_details.serialize_json(
        value["retry_details"]
    )
    return out


def deserialize_json(data: dict) -> StepSucceededDetails:
    out: StepSucceededDetails = {}  # type: ignore[typeddict-item]
    if data.get("Result") is not None:
        import capo_lambda.types.event_result

        out["result"] = capo_lambda.types.event_result.deserialize_json(data["Result"])
    else:
        raise DeserializationError("StepSucceededDetails.result required")
    if data.get("RetryDetails") is not None:
        import capo_lambda.types.retry_details

        out["retry_details"] = capo_lambda.types.retry_details.deserialize_json(
            data["RetryDetails"]
        )
    else:
        raise DeserializationError("StepSucceededDetails.retry_details required")
    return out


def redact_sensitive(value: StepSucceededDetails) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "result" in value:
        import capo_lambda.types.event_result

        out["result"] = capo_lambda.types.event_result.redact_sensitive(value["result"])
    return out
