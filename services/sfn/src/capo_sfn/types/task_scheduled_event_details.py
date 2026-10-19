"""Generated from Smithy shape ``com.amazonaws.sfn#TaskScheduledEventDetails``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sfn.types.connector_parameters
    import capo_sfn.types.name
    import capo_sfn.types.task_credentials
    import capo_sfn.types.timeout_in_seconds


class TaskScheduledEventDetails(TypedDict, closed=True):
    resource_type: "capo_sfn.types.name.Name"
    """<p>The service name of the resource in a task state.</p>"""
    resource: "capo_sfn.types.name.Name"
    """<p>The action of the resource called by a task state.</p>"""
    region: "capo_sfn.types.name.Name"
    """<p>The region of the scheduled task</p>"""
    parameters: "capo_sfn.types.connector_parameters.ConnectorParameters"
    """<p>The JSON data passed to the resource referenced in a task state. Length constraints apply to the payload size, and are expressed as bytes in UTF-8 encoding.</p>"""
    timeout_in_seconds: NotRequired[
        "capo_sfn.types.timeout_in_seconds.TimeoutInSeconds"
    ]
    """<p>The maximum allowed duration of the task.</p>"""
    heartbeat_in_seconds: NotRequired[
        "capo_sfn.types.timeout_in_seconds.TimeoutInSeconds"
    ]
    """<p>The maximum allowed duration between two heartbeats for the task.</p>"""
    task_credentials: NotRequired["capo_sfn.types.task_credentials.TaskCredentials"]
    """<p>The credentials that Step Functions uses for the task.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TaskScheduledEventDetails) -> dict:
    out: dict = {}
    out["resourceType"] = value["resource_type"]
    out["resource"] = value["resource"]
    out["region"] = value["region"]
    out["parameters"] = value["parameters"]
    if "timeout_in_seconds" in value:
        out["timeoutInSeconds"] = value["timeout_in_seconds"]
    if "heartbeat_in_seconds" in value:
        out["heartbeatInSeconds"] = value["heartbeat_in_seconds"]
    if "task_credentials" in value:
        import capo_sfn.types.task_credentials

        out["taskCredentials"] = capo_sfn.types.task_credentials.serialize_aws_json_1_0(
            value["task_credentials"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> TaskScheduledEventDetails:
    out: TaskScheduledEventDetails = {}  # type: ignore[typeddict-item]
    if data.get("resourceType") is not None:
        out["resource_type"] = data["resourceType"]
    else:
        out["resource_type"] = ""
    if data.get("resource") is not None:
        out["resource"] = data["resource"]
    else:
        out["resource"] = ""
    if data.get("region") is not None:
        out["region"] = data["region"]
    else:
        out["region"] = ""
    if data.get("parameters") is not None:
        out["parameters"] = data["parameters"]
    else:
        out["parameters"] = ""
    if data.get("timeoutInSeconds") is not None:
        out["timeout_in_seconds"] = data["timeoutInSeconds"]
    if data.get("heartbeatInSeconds") is not None:
        out["heartbeat_in_seconds"] = data["heartbeatInSeconds"]
    if data.get("taskCredentials") is not None:
        import capo_sfn.types.task_credentials

        out["task_credentials"] = (
            capo_sfn.types.task_credentials.deserialize_aws_json_1_0(
                data["taskCredentials"]
            )
        )
    return out


def redact_sensitive(value: TaskScheduledEventDetails) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "parameters" in value:
        out["parameters"] = "*** Sensitive Data Redacted ***"
    return out
