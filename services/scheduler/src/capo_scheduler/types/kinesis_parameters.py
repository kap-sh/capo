"""Generated from Smithy shape ``com.amazonaws.scheduler#KinesisParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_scheduler.errors import DeserializationError

if TYPE_CHECKING:
    import capo_scheduler.types.target_partition_key


class KinesisParameters(TypedDict, closed=True):
    partition_key: "capo_scheduler.types.target_partition_key.TargetPartitionKey"
    """<p>Specifies the shard to which EventBridge Scheduler sends the event. For more information, see <a href="https://docs.aws.amazon.com/streams/latest/dev/key-concepts.html">Amazon Kinesis Data Streams terminology and concepts</a> in the <i>Amazon Kinesis Streams Developer Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KinesisParameters) -> dict:
    out: dict = {}
    out["PartitionKey"] = value["partition_key"]
    return out


def deserialize_json(data: dict) -> KinesisParameters:
    out: KinesisParameters = {}  # type: ignore[typeddict-item]
    if data.get("PartitionKey") is not None:
        out["partition_key"] = data["PartitionKey"]
    else:
        raise DeserializationError("KinesisParameters.partition_key required")
    return out
