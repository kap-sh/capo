"""Generated from Smithy shape ``com.amazonaws.kinesis#DescribeQueueOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_kinesis.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis.types.queue_description


class DescribeQueueOutput(TypedDict, closed=True):
    queue_description: "capo_kinesis.types.queue_description.QueueDescription"
    """<p>A description of the queue.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeQueueOutput) -> dict:
    out: dict = {}
    import capo_kinesis.types.queue_description

    out["QueueDescription"] = (
        capo_kinesis.types.queue_description.serialize_aws_json_1_1(
            value["queue_description"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeQueueOutput:
    out: DescribeQueueOutput = {}  # type: ignore[typeddict-item]
    if data.get("QueueDescription") is not None:
        import capo_kinesis.types.queue_description

        out["queue_description"] = (
            capo_kinesis.types.queue_description.deserialize_aws_json_1_1(
                data["QueueDescription"]
            )
        )
    else:
        raise DeserializationError("DescribeQueueOutput.queue_description required")
    return out
