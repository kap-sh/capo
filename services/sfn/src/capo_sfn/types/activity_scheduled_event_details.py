"""Generated from Smithy shape ``com.amazonaws.sfn#ActivityScheduledEventDetails``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_sfn.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sfn.types.arn
    import capo_sfn.types.history_event_execution_data_details
    import capo_sfn.types.sensitive_data
    import capo_sfn.types.timeout_in_seconds


class ActivityScheduledEventDetails(TypedDict, closed=True):
    resource: "capo_sfn.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the scheduled activity.</p>"""
    input: NotRequired["capo_sfn.types.sensitive_data.SensitiveData"]
    """<p>The JSON data input to the activity task. Length constraints apply to the payload size, and are expressed as bytes in UTF-8 encoding.</p>"""
    input_details: NotRequired[
        "capo_sfn.types.history_event_execution_data_details.HistoryEventExecutionDataDetails"
    ]
    """<p>Contains details about the input for an execution history event.</p>"""
    timeout_in_seconds: NotRequired[
        "capo_sfn.types.timeout_in_seconds.TimeoutInSeconds"
    ]
    """<p>The maximum allowed duration of the activity task.</p>"""
    heartbeat_in_seconds: NotRequired[
        "capo_sfn.types.timeout_in_seconds.TimeoutInSeconds"
    ]
    """<p>The maximum allowed duration between two heartbeats for the activity task.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ActivityScheduledEventDetails) -> dict:
    out: dict = {}
    out["resource"] = value["resource"]
    if "input" in value:
        out["input"] = value["input"]
    if "input_details" in value:
        import capo_sfn.types.history_event_execution_data_details

        out["inputDetails"] = (
            capo_sfn.types.history_event_execution_data_details.serialize_aws_json_1_0(
                value["input_details"]
            )
        )
    if "timeout_in_seconds" in value:
        out["timeoutInSeconds"] = value["timeout_in_seconds"]
    if "heartbeat_in_seconds" in value:
        out["heartbeatInSeconds"] = value["heartbeat_in_seconds"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ActivityScheduledEventDetails:
    out: ActivityScheduledEventDetails = {}  # type: ignore[typeddict-item]
    if data.get("resource") is not None:
        out["resource"] = data["resource"]
    else:
        raise DeserializationError("ActivityScheduledEventDetails.resource required")
    if data.get("input") is not None:
        out["input"] = data["input"]
    if data.get("inputDetails") is not None:
        import capo_sfn.types.history_event_execution_data_details

        out["input_details"] = (
            capo_sfn.types.history_event_execution_data_details.deserialize_aws_json_1_0(
                data["inputDetails"]
            )
        )
    if data.get("timeoutInSeconds") is not None:
        out["timeout_in_seconds"] = data["timeoutInSeconds"]
    if data.get("heartbeatInSeconds") is not None:
        out["heartbeat_in_seconds"] = data["heartbeatInSeconds"]
    return out


def redact_sensitive(value: ActivityScheduledEventDetails) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "input" in value:
        out["input"] = "*** Sensitive Data Redacted ***"
    return out
