"""Generated from Smithy shape ``com.amazonaws.sqs#DeleteQueueRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sqs.types.string


class DeleteQueueRequest(TypedDict, closed=True):
    queue_url: "capo_sqs.types.string.String"
    """<p>The URL of the Amazon SQS queue to delete.</p> <p>Queue URLs and names are case-sensitive.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteQueueRequest) -> dict:
    out: dict = {}
    out["QueueUrl"] = value["queue_url"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteQueueRequest:
    out: DeleteQueueRequest = {}  # type: ignore[typeddict-item]
    if data.get("QueueUrl") is not None:
        out["queue_url"] = data["QueueUrl"]
    else:
        out["queue_url"] = ""
    return out
