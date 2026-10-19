"""Generated from Smithy shape ``com.amazonaws.iot#KinesisAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.aws_arn
    import capo_iot.types.partition_key
    import capo_iot.types.stream_name


class KinesisAction(TypedDict, closed=True):
    role_arn: "capo_iot.types.aws_arn.AwsArn"
    """<p>The ARN of the IAM role that grants access to the Amazon Kinesis stream.</p>"""
    stream_name: "capo_iot.types.stream_name.StreamName"
    """<p>The name of the Amazon Kinesis stream.</p>"""
    partition_key: NotRequired["capo_iot.types.partition_key.PartitionKey"]
    """<p>The partition key.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KinesisAction) -> dict:
    out: dict = {}
    out["roleArn"] = value["role_arn"]
    out["streamName"] = value["stream_name"]
    if "partition_key" in value:
        out["partitionKey"] = value["partition_key"]
    return out


def deserialize_json(data: dict) -> KinesisAction:
    out: KinesisAction = {}  # type: ignore[typeddict-item]
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        out["role_arn"] = ""
    if data.get("streamName") is not None:
        out["stream_name"] = data["streamName"]
    else:
        out["stream_name"] = ""
    if data.get("partitionKey") is not None:
        out["partition_key"] = data["partitionKey"]
    return out
