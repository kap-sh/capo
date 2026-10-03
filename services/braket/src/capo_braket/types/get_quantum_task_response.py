"""Generated from Smithy shape ``com.amazonaws.braket#GetQuantumTaskResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_braket.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_braket.types.action_metadata
    import capo_braket.types.associations
    import capo_braket.types.device_arn
    import capo_braket.types.experimental_capabilities
    import capo_braket.types.job_arn
    import capo_braket.types.json_value
    import capo_braket.types.quantum_task_arn
    import capo_braket.types.quantum_task_queue_info
    import capo_braket.types.quantum_task_status
    import capo_braket.types.tags_map


class GetQuantumTaskResponse(TypedDict, closed=True):
    quantum_task_arn: "capo_braket.types.quantum_task_arn.QuantumTaskArn"
    """<p>The ARN of the quantum task.</p>"""
    status: "capo_braket.types.quantum_task_status.QuantumTaskStatus"
    """<p>The status of the quantum task.</p>"""
    failure_reason: NotRequired["str"]
    """<p>The reason that a quantum task failed.</p>"""
    device_arn: "capo_braket.types.device_arn.DeviceArn"
    """<p>The ARN of the device the quantum task was run on.</p>"""
    device_parameters: "capo_braket.types.json_value.JsonValue"
    """<p>The parameters for the device on which the quantum task ran.</p>"""
    shots: "int"
    """<p>The number of shots used in the quantum task.</p>"""
    output_s3_bucket: "str"
    """<p>The S3 bucket where quantum task results are stored.</p>"""
    output_s3_directory: "str"
    """<p>The folder in the S3 bucket where quantum task results are stored.</p>"""
    created_at: "datetime.datetime"
    """<p>The time at which the quantum task was created.</p>"""
    ended_at: NotRequired["datetime.datetime"]
    """<p>The time at which the quantum task ended.</p>"""
    tags: NotRequired["capo_braket.types.tags_map.TagsMap"]
    """<p>The tags that belong to this quantum task.</p>"""
    job_arn: NotRequired["capo_braket.types.job_arn.JobArn"]
    """<p>The ARN of the Amazon Braket job associated with the quantum task.</p>"""
    queue_info: NotRequired[
        "capo_braket.types.quantum_task_queue_info.QuantumTaskQueueInfo"
    ]
    """<p>Queue information for the requested quantum task. Only returned if <code>QueueInfo</code> is specified in the <code>additionalAttributeNames"</code> field in the <code>GetQuantumTask</code> API request.</p>"""
    associations: NotRequired["capo_braket.types.associations.Associations"]
    """<p>The list of Amazon Braket resources associated with the quantum task.</p>"""
    num_successful_shots: NotRequired["int"]
    """<p>The number of successful shots for the quantum task. This is available after a successfully completed quantum task.</p>"""
    action_metadata: NotRequired["capo_braket.types.action_metadata.ActionMetadata"]
    """<p>Metadata about the action performed by the quantum task, including information about the type of action and program counts.</p>"""
    experimental_capabilities: NotRequired[
        "capo_braket.types.experimental_capabilities.ExperimentalCapabilities"
    ]
    """<p>Enabled experimental capabilities for the quantum task, if any.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetQuantumTaskResponse) -> dict:
    out: dict = {}
    out["quantumTaskArn"] = value["quantum_task_arn"]
    out["status"] = value["status"]
    if "failure_reason" in value:
        out["failureReason"] = value["failure_reason"]
    out["deviceArn"] = value["device_arn"]
    out["deviceParameters"] = value["device_parameters"]
    out["shots"] = value["shots"]
    out["outputS3Bucket"] = value["output_s3_bucket"]
    out["outputS3Directory"] = value["output_s3_directory"]
    import capo_braket._protocol.serialize

    out["createdAt"] = capo_braket._protocol.serialize.fmt_date_time(
        value["created_at"]
    )
    if "ended_at" in value:
        import capo_braket._protocol.serialize

        out["endedAt"] = capo_braket._protocol.serialize.fmt_date_time(
            value["ended_at"]
        )
    if "tags" in value:
        import capo_braket.types.tags_map

        out["tags"] = capo_braket.types.tags_map.serialize_json(value["tags"])
    if "job_arn" in value:
        out["jobArn"] = value["job_arn"]
    if "queue_info" in value:
        import capo_braket.types.quantum_task_queue_info

        out["queueInfo"] = capo_braket.types.quantum_task_queue_info.serialize_json(
            value["queue_info"]
        )
    if "associations" in value:
        import capo_braket.types.associations

        out["associations"] = capo_braket.types.associations.serialize_json(
            value["associations"]
        )
    if "num_successful_shots" in value:
        out["numSuccessfulShots"] = value["num_successful_shots"]
    if "action_metadata" in value:
        import capo_braket.types.action_metadata

        out["actionMetadata"] = capo_braket.types.action_metadata.serialize_json(
            value["action_metadata"]
        )
    if "experimental_capabilities" in value:
        import capo_braket.types.experimental_capabilities

        out["experimentalCapabilities"] = (
            capo_braket.types.experimental_capabilities.serialize_json(
                value["experimental_capabilities"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetQuantumTaskResponse:
    out: GetQuantumTaskResponse = {}  # type: ignore[typeddict-item]
    if data.get("quantumTaskArn") is not None:
        out["quantum_task_arn"] = data["quantumTaskArn"]
    else:
        raise DeserializationError("GetQuantumTaskResponse.quantum_task_arn required")
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        raise DeserializationError("GetQuantumTaskResponse.status required")
    if data.get("failureReason") is not None:
        out["failure_reason"] = data["failureReason"]
    if data.get("deviceArn") is not None:
        out["device_arn"] = data["deviceArn"]
    else:
        raise DeserializationError("GetQuantumTaskResponse.device_arn required")
    if data.get("deviceParameters") is not None:
        out["device_parameters"] = data["deviceParameters"]
    else:
        raise DeserializationError("GetQuantumTaskResponse.device_parameters required")
    if data.get("shots") is not None:
        out["shots"] = data["shots"]
    else:
        raise DeserializationError("GetQuantumTaskResponse.shots required")
    if data.get("outputS3Bucket") is not None:
        out["output_s3_bucket"] = data["outputS3Bucket"]
    else:
        raise DeserializationError("GetQuantumTaskResponse.output_s3_bucket required")
    if data.get("outputS3Directory") is not None:
        out["output_s3_directory"] = data["outputS3Directory"]
    else:
        raise DeserializationError(
            "GetQuantumTaskResponse.output_s3_directory required"
        )
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    else:
        raise DeserializationError("GetQuantumTaskResponse.created_at required")
    if data.get("endedAt") is not None:
        import datetime

        out["ended_at"] = datetime.datetime.fromisoformat(
            data["endedAt"].replace("Z", "+00:00")
        )
    if data.get("tags") is not None:
        import capo_braket.types.tags_map

        out["tags"] = capo_braket.types.tags_map.deserialize_json(data["tags"])
    if data.get("jobArn") is not None:
        out["job_arn"] = data["jobArn"]
    if data.get("queueInfo") is not None:
        import capo_braket.types.quantum_task_queue_info

        out["queue_info"] = capo_braket.types.quantum_task_queue_info.deserialize_json(
            data["queueInfo"]
        )
    if data.get("associations") is not None:
        import capo_braket.types.associations

        out["associations"] = capo_braket.types.associations.deserialize_json(
            data["associations"]
        )
    if data.get("numSuccessfulShots") is not None:
        out["num_successful_shots"] = data["numSuccessfulShots"]
    if data.get("actionMetadata") is not None:
        import capo_braket.types.action_metadata

        out["action_metadata"] = capo_braket.types.action_metadata.deserialize_json(
            data["actionMetadata"]
        )
    if data.get("experimentalCapabilities") is not None:
        import capo_braket.types.experimental_capabilities

        out["experimental_capabilities"] = (
            capo_braket.types.experimental_capabilities.deserialize_json(
                data["experimentalCapabilities"]
            )
        )
    return out
