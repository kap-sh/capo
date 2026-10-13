"""Generated from Smithy shape ``com.amazonaws.sfn#TestStateConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sfn.types.map_iteration_failure_count
    import capo_sfn.types.retrier_retry_count
    import capo_sfn.types.sensitive_data
    import capo_sfn.types.test_state_state_name


class TestStateConfiguration(TypedDict, closed=True):
    retrier_retry_count: NotRequired[
        "capo_sfn.types.retrier_retry_count.RetrierRetryCount"
    ]
    """<p>The number of retry attempts that have occurred for the state's Retry that applies to the mocked error.</p>"""
    error_caused_by_state: NotRequired[
        "capo_sfn.types.test_state_state_name.TestStateStateName"
    ]
    """<p>The name of the state from which an error originates when an error is mocked for a Map or Parallel state.</p>"""
    map_iteration_failure_count: NotRequired[
        "capo_sfn.types.map_iteration_failure_count.MapIterationFailureCount"
    ]
    """<p>The number of Map state iterations that failed during the Map state invocation.</p>"""
    map_item_reader_data: NotRequired["capo_sfn.types.sensitive_data.SensitiveData"]
    """<p>The data read by ItemReader in Distributed Map states as found in its original source.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TestStateConfiguration) -> dict:
    out: dict = {}
    if "retrier_retry_count" in value:
        out["retrierRetryCount"] = value["retrier_retry_count"]
    if "error_caused_by_state" in value:
        out["errorCausedByState"] = value["error_caused_by_state"]
    if "map_iteration_failure_count" in value:
        out["mapIterationFailureCount"] = value["map_iteration_failure_count"]
    if "map_item_reader_data" in value:
        out["mapItemReaderData"] = value["map_item_reader_data"]
    return out


def deserialize_aws_json_1_0(data: dict) -> TestStateConfiguration:
    out: TestStateConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("retrierRetryCount") is not None:
        out["retrier_retry_count"] = data["retrierRetryCount"]
    if data.get("errorCausedByState") is not None:
        out["error_caused_by_state"] = data["errorCausedByState"]
    if data.get("mapIterationFailureCount") is not None:
        out["map_iteration_failure_count"] = data["mapIterationFailureCount"]
    if data.get("mapItemReaderData") is not None:
        out["map_item_reader_data"] = data["mapItemReaderData"]
    return out


def redact_sensitive(value: TestStateConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "error_caused_by_state" in value:
        out["error_caused_by_state"] = "*** Sensitive Data Redacted ***"
    if "map_item_reader_data" in value:
        out["map_item_reader_data"] = "*** Sensitive Data Redacted ***"
    return out
