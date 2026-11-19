"""Generated from Smithy shape ``com.amazonaws.kinesis#UpdateQueueInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_kinesis.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis.types.queue_arn
    import capo_kinesis.types.queue_attributes


class UpdateQueueInput(TypedDict, closed=True):
    queue_arn: "capo_kinesis.types.queue_arn.QueueARN"
    """<p>The ARN of the queue to update.</p>"""
    queue_attributes: "capo_kinesis.types.queue_attributes.QueueAttributes"
    """<p>The configuration attributes to apply to the queue. Attributes you do not specify are left unchanged.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateQueueInput) -> dict:
    out: dict = {}
    out["QueueARN"] = value["queue_arn"]
    import capo_kinesis.types.queue_attributes

    out["QueueAttributes"] = capo_kinesis.types.queue_attributes.serialize_aws_json_1_1(
        value["queue_attributes"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateQueueInput:
    out: UpdateQueueInput = {}  # type: ignore[typeddict-item]
    if data.get("QueueARN") is not None:
        out["queue_arn"] = data["QueueARN"]
    else:
        out["queue_arn"] = ""
    if data.get("QueueAttributes") is not None:
        import capo_kinesis.types.queue_attributes

        out["queue_attributes"] = (
            capo_kinesis.types.queue_attributes.deserialize_aws_json_1_1(
                data["QueueAttributes"]
            )
        )
    else:
        raise DeserializationError("UpdateQueueInput.queue_attributes required")
    return out
