"""Generated from Smithy shape ``com.amazonaws.groundstation#KinesisDataStreamData``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_groundstation.types.kinesis_data_stream_arn
    import capo_groundstation.types.role_arn


class KinesisDataStreamData(TypedDict, closed=True):
    kinesis_role_arn: "capo_groundstation.types.role_arn.RoleArn"
    """<p>ARN of the IAM Role used by AWS Ground Station to deliver telemetry.</p>"""
    kinesis_data_stream_arn: (
        "capo_groundstation.types.kinesis_data_stream_arn.KinesisDataStreamArn"
    )
    """<p>ARN of the Kinesis Data Stream to deliver telemetry to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KinesisDataStreamData) -> dict:
    out: dict = {}
    out["kinesisRoleArn"] = value["kinesis_role_arn"]
    out["kinesisDataStreamArn"] = value["kinesis_data_stream_arn"]
    return out


def deserialize_json(data: dict) -> KinesisDataStreamData:
    out: KinesisDataStreamData = {}  # type: ignore[typeddict-item]
    if data.get("kinesisRoleArn") is not None:
        out["kinesis_role_arn"] = data["kinesisRoleArn"]
    else:
        out["kinesis_role_arn"] = ""
    if data.get("kinesisDataStreamArn") is not None:
        out["kinesis_data_stream_arn"] = data["kinesisDataStreamArn"]
    else:
        out["kinesis_data_stream_arn"] = ""
    return out
