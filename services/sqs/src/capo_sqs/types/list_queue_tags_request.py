"""Generated from Smithy shape ``com.amazonaws.sqs#ListQueueTagsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sqs.types.string


class ListQueueTagsRequest(TypedDict, closed=True):
    queue_url: "capo_sqs.types.string.String"
    """<p>The URL of the queue.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListQueueTagsRequest) -> dict:
    out: dict = {}
    out["QueueUrl"] = value["queue_url"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListQueueTagsRequest:
    out: ListQueueTagsRequest = {}  # type: ignore[typeddict-item]
    if data.get("QueueUrl") is not None:
        out["queue_url"] = data["QueueUrl"]
    else:
        out["queue_url"] = ""
    return out
