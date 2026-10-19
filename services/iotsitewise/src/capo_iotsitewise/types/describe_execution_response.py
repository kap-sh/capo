"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DescribeExecutionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.execution_details
    import capo_iotsitewise.types.execution_result
    import capo_iotsitewise.types.execution_status
    import capo_iotsitewise.types.id
    import capo_iotsitewise.types.name
    import capo_iotsitewise.types.resolve_to
    import capo_iotsitewise.types.target_resource
    import capo_iotsitewise.types.timestamp
    import capo_iotsitewise.types.version


class DescribeExecutionResponse(TypedDict, closed=True):
    execution_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the execution.</p>"""
    action_type: NotRequired["capo_iotsitewise.types.name.Name"]
    """<p>The type of action exectued.</p>"""
    target_resource: "capo_iotsitewise.types.target_resource.TargetResource"
    target_resource_version: "capo_iotsitewise.types.version.Version"
    """<p>The version of the target resource.</p>"""
    resolve_to: NotRequired["capo_iotsitewise.types.resolve_to.ResolveTo"]
    """<p>The detailed resource this execution resolves to.</p>"""
    execution_start_time: "capo_iotsitewise.types.timestamp.Timestamp"
    """<p>The time the process started.</p>"""
    execution_end_time: NotRequired["capo_iotsitewise.types.timestamp.Timestamp"]
    """<p>The time the process ended.</p>"""
    execution_status: "capo_iotsitewise.types.execution_status.ExecutionStatus"
    """<p>The status of the execution process.</p>"""
    execution_result: NotRequired[
        "capo_iotsitewise.types.execution_result.ExecutionResult"
    ]
    """<p>The result of the execution.</p>"""
    execution_details: NotRequired[
        "capo_iotsitewise.types.execution_details.ExecutionDetails"
    ]
    """<p>Provides detailed information about the execution of your anomaly detection models. This includes model metrics and training timestamps for both training and inference actions.</p> <ul> <li> <p> The training action (Amazon Web Services/ANOMALY_DETECTION_TRAINING), includes performance metrics that help you compare different versions of your anomaly detection models. These metrics provide insights into the model's performance during the training process. </p> </li> <li> <p> The inference action (Amazon Web Services/ANOMALY_DETECTION_INFERENCE), includes information about the results of executing your anomaly detection models. This helps you understand the output of your models and assess their performance. </p> </li> </ul>"""
    execution_entity_version: NotRequired["capo_iotsitewise.types.version.Version"]
    """<p>Entity version used for the execution.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeExecutionResponse) -> dict:
    out: dict = {}
    out["executionId"] = value["execution_id"]
    if "action_type" in value:
        out["actionType"] = value["action_type"]
    import capo_iotsitewise.types.target_resource

    out["targetResource"] = capo_iotsitewise.types.target_resource.serialize_json(
        value["target_resource"]
    )
    out["targetResourceVersion"] = value["target_resource_version"]
    if "resolve_to" in value:
        import capo_iotsitewise.types.resolve_to

        out["resolveTo"] = capo_iotsitewise.types.resolve_to.serialize_json(
            value["resolve_to"]
        )
    import capo_iotsitewise.types.timestamp

    out["executionStartTime"] = capo_iotsitewise.types.timestamp.serialize_json(
        value["execution_start_time"]
    )
    if "execution_end_time" in value:
        import capo_iotsitewise.types.timestamp

        out["executionEndTime"] = capo_iotsitewise.types.timestamp.serialize_json(
            value["execution_end_time"]
        )
    import capo_iotsitewise.types.execution_status

    out["executionStatus"] = capo_iotsitewise.types.execution_status.serialize_json(
        value["execution_status"]
    )
    if "execution_result" in value:
        import capo_iotsitewise.types.execution_result

        out["executionResult"] = capo_iotsitewise.types.execution_result.serialize_json(
            value["execution_result"]
        )
    if "execution_details" in value:
        import capo_iotsitewise.types.execution_details

        out["executionDetails"] = (
            capo_iotsitewise.types.execution_details.serialize_json(
                value["execution_details"]
            )
        )
    if "execution_entity_version" in value:
        out["executionEntityVersion"] = value["execution_entity_version"]
    return out


def deserialize_json(data: dict) -> DescribeExecutionResponse:
    out: DescribeExecutionResponse = {}  # type: ignore[typeddict-item]
    if data.get("executionId") is not None:
        out["execution_id"] = data["executionId"]
    else:
        out["execution_id"] = ""
    if data.get("actionType") is not None:
        out["action_type"] = data["actionType"]
    if data.get("targetResource") is not None:
        import capo_iotsitewise.types.target_resource

        out["target_resource"] = (
            capo_iotsitewise.types.target_resource.deserialize_json(
                data["targetResource"]
            )
        )
    else:
        raise DeserializationError("DescribeExecutionResponse.target_resource required")
    if data.get("targetResourceVersion") is not None:
        out["target_resource_version"] = data["targetResourceVersion"]
    else:
        out["target_resource_version"] = ""
    if data.get("resolveTo") is not None:
        import capo_iotsitewise.types.resolve_to

        out["resolve_to"] = capo_iotsitewise.types.resolve_to.deserialize_json(
            data["resolveTo"]
        )
    if data.get("executionStartTime") is not None:
        import capo_iotsitewise.types.timestamp

        out["execution_start_time"] = capo_iotsitewise.types.timestamp.deserialize_json(
            data["executionStartTime"]
        )
    else:
        import datetime

        out["execution_start_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("executionEndTime") is not None:
        import capo_iotsitewise.types.timestamp

        out["execution_end_time"] = capo_iotsitewise.types.timestamp.deserialize_json(
            data["executionEndTime"]
        )
    if data.get("executionStatus") is not None:
        import capo_iotsitewise.types.execution_status

        out["execution_status"] = (
            capo_iotsitewise.types.execution_status.deserialize_json(
                data["executionStatus"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeExecutionResponse.execution_status required"
        )
    if data.get("executionResult") is not None:
        import capo_iotsitewise.types.execution_result

        out["execution_result"] = (
            capo_iotsitewise.types.execution_result.deserialize_json(
                data["executionResult"]
            )
        )
    if data.get("executionDetails") is not None:
        import capo_iotsitewise.types.execution_details

        out["execution_details"] = (
            capo_iotsitewise.types.execution_details.deserialize_json(
                data["executionDetails"]
            )
        )
    if data.get("executionEntityVersion") is not None:
        out["execution_entity_version"] = data["executionEntityVersion"]
    return out
