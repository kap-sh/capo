"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#KinesisParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudwatch_events.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudwatch_events.types.target_partition_key_path


class KinesisParameters(TypedDict, closed=True):
    partition_key_path: (
        "capo_cloudwatch_events.types.target_partition_key_path.TargetPartitionKeyPath"
    )
    """<p>The JSON path to be extracted from the event and used as the partition key. For more information, see <a href="https://docs.aws.amazon.com/streams/latest/dev/key-concepts.html#partition-key">Amazon Kinesis Streams Key Concepts</a> in the <i>Amazon Kinesis Streams Developer Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KinesisParameters) -> dict:
    out: dict = {}
    out["PartitionKeyPath"] = value["partition_key_path"]
    return out


def deserialize_aws_json_1_1(data: dict) -> KinesisParameters:
    out: KinesisParameters = {}  # type: ignore[typeddict-item]
    if data.get("PartitionKeyPath") is not None:
        out["partition_key_path"] = data["PartitionKeyPath"]
    else:
        raise DeserializationError("KinesisParameters.partition_key_path required")
    return out
