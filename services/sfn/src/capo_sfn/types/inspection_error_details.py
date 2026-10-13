"""Generated from Smithy shape ``com.amazonaws.sfn#InspectionErrorDetails``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sfn.types.exception_handler_index
    import capo_sfn.types.retry_backoff_interval_seconds


class InspectionErrorDetails(TypedDict, closed=True):
    catch_index: NotRequired[
        "capo_sfn.types.exception_handler_index.ExceptionHandlerIndex"
    ]
    """<p>The array index of the Catch which handled the exception.</p>"""
    retry_index: NotRequired[
        "capo_sfn.types.exception_handler_index.ExceptionHandlerIndex"
    ]
    """<p>The array index of the Retry which handled the exception.</p>"""
    retry_backoff_interval_seconds: NotRequired[
        "capo_sfn.types.retry_backoff_interval_seconds.RetryBackoffIntervalSeconds"
    ]
    """<p>The duration in seconds of the backoff for a retry on a failed state invocation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InspectionErrorDetails) -> dict:
    out: dict = {}
    if "catch_index" in value:
        out["catchIndex"] = value["catch_index"]
    if "retry_index" in value:
        out["retryIndex"] = value["retry_index"]
    if "retry_backoff_interval_seconds" in value:
        out["retryBackoffIntervalSeconds"] = value["retry_backoff_interval_seconds"]
    return out


def deserialize_aws_json_1_0(data: dict) -> InspectionErrorDetails:
    out: InspectionErrorDetails = {}  # type: ignore[typeddict-item]
    if data.get("catchIndex") is not None:
        out["catch_index"] = data["catchIndex"]
    if data.get("retryIndex") is not None:
        out["retry_index"] = data["retryIndex"]
    if data.get("retryBackoffIntervalSeconds") is not None:
        out["retry_backoff_interval_seconds"] = data["retryBackoffIntervalSeconds"]
    return out


def redact_sensitive(value: InspectionErrorDetails) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "catch_index" in value:
        out["catch_index"] = "*** Sensitive Data Redacted ***"
    if "retry_index" in value:
        out["retry_index"] = "*** Sensitive Data Redacted ***"
    if "retry_backoff_interval_seconds" in value:
        out["retry_backoff_interval_seconds"] = "*** Sensitive Data Redacted ***"
    return out
