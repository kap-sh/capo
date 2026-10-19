"""Generated from Smithy shape ``com.amazonaws.braket#QuantumTaskSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_braket.types.device_arn
    import capo_braket.types.quantum_task_arn
    import capo_braket.types.quantum_task_status
    import capo_braket.types.tags_map


class QuantumTaskSummary(TypedDict, closed=True):
    quantum_task_arn: "capo_braket.types.quantum_task_arn.QuantumTaskArn"
    """<p>The ARN of the quantum task.</p>"""
    status: "capo_braket.types.quantum_task_status.QuantumTaskStatus"
    """<p>The status of the quantum task.</p>"""
    device_arn: "capo_braket.types.device_arn.DeviceArn"
    """<p>The ARN of the device the quantum task ran on.</p>"""
    shots: "int"
    """<p>The shots used for the quantum task.</p>"""
    output_s3_bucket: "str"
    """<p>The S3 bucket where the quantum task result file is stored.</p>"""
    output_s3_directory: "str"
    """<p>The folder in the S3 bucket where the quantum task result file is stored.</p>"""
    created_at: "datetime.datetime"
    """<p>The time at which the quantum task was created.</p>"""
    ended_at: NotRequired["datetime.datetime"]
    """<p>The time at which the quantum task finished.</p>"""
    tags: NotRequired["capo_braket.types.tags_map.TagsMap"]
    """<p>Displays the key, value pairs of tags associated with this quantum task.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QuantumTaskSummary) -> dict:
    out: dict = {}
    out["quantumTaskArn"] = value["quantum_task_arn"]
    out["status"] = value["status"]
    out["deviceArn"] = value["device_arn"]
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
    return out


def deserialize_json(data: dict) -> QuantumTaskSummary:
    out: QuantumTaskSummary = {}  # type: ignore[typeddict-item]
    if data.get("quantumTaskArn") is not None:
        out["quantum_task_arn"] = data["quantumTaskArn"]
    else:
        out["quantum_task_arn"] = ""
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        out["status"] = ""
    if data.get("deviceArn") is not None:
        out["device_arn"] = data["deviceArn"]
    else:
        out["device_arn"] = ""
    if data.get("shots") is not None:
        out["shots"] = data["shots"]
    else:
        out["shots"] = 0
    if data.get("outputS3Bucket") is not None:
        out["output_s3_bucket"] = data["outputS3Bucket"]
    else:
        out["output_s3_bucket"] = ""
    if data.get("outputS3Directory") is not None:
        out["output_s3_directory"] = data["outputS3Directory"]
    else:
        out["output_s3_directory"] = ""
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("endedAt") is not None:
        import datetime

        out["ended_at"] = datetime.datetime.fromisoformat(
            data["endedAt"].replace("Z", "+00:00")
        )
    if data.get("tags") is not None:
        import capo_braket.types.tags_map

        out["tags"] = capo_braket.types.tags_map.deserialize_json(data["tags"])
    return out
