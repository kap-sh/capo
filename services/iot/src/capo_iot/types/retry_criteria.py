"""Generated from Smithy shape ``com.amazonaws.iot#RetryCriteria``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot.types.number_of_retries
    import capo_iot.types.retryable_failure_type


class RetryCriteria(TypedDict, closed=True):
    failure_type: "capo_iot.types.retryable_failure_type.RetryableFailureType"
    """<p>The type of job execution failures that can initiate a job retry.</p>"""
    number_of_retries: "capo_iot.types.number_of_retries.NumberOfRetries"
    """<p>The number of retries allowed for a failure type for the job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RetryCriteria) -> dict:
    out: dict = {}
    import capo_iot.types.retryable_failure_type

    out["failureType"] = capo_iot.types.retryable_failure_type.serialize_json(
        value["failure_type"]
    )
    out["numberOfRetries"] = value["number_of_retries"]
    return out


def deserialize_json(data: dict) -> RetryCriteria:
    out: RetryCriteria = {}  # type: ignore[typeddict-item]
    if data.get("failureType") is not None:
        import capo_iot.types.retryable_failure_type

        out["failure_type"] = capo_iot.types.retryable_failure_type.deserialize_json(
            data["failureType"]
        )
    else:
        import typing

        out["failure_type"] = typing.cast(
            "capo_iot.types.retryable_failure_type.RetryableFailureType", ""
        )
    if data.get("numberOfRetries") is not None:
        out["number_of_retries"] = data["numberOfRetries"]
    else:
        out["number_of_retries"] = 0
    return out
