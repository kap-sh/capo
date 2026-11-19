"""Generated from Smithy shape ``com.amazonaws.kinesis#DeleteQueueInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kinesis.types.queue_arn


class DeleteQueueInput(TypedDict, closed=True):
    queue_arn: "capo_kinesis.types.queue_arn.QueueARN"
    """<p>The ARN of the queue to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteQueueInput) -> dict:
    out: dict = {}
    out["QueueARN"] = value["queue_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteQueueInput:
    out: DeleteQueueInput = {}  # type: ignore[typeddict-item]
    if data.get("QueueARN") is not None:
        out["queue_arn"] = data["QueueARN"]
    else:
        out["queue_arn"] = ""
    return out
