"""Generated from Smithy shape ``com.amazonaws.sqs#TagQueueRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sqs.types.string
    import capo_sqs.types.tag_map


class TagQueueRequest(TypedDict, closed=True):
    queue_url: "capo_sqs.types.string.String"
    """<p>The URL of the queue.</p>"""
    tags: "capo_sqs.types.tag_map.TagMap"
    """<p>The list of tags to be added to the specified queue.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TagQueueRequest) -> dict:
    out: dict = {}
    out["QueueUrl"] = value["queue_url"]
    import capo_sqs.types.tag_map

    out["Tags"] = capo_sqs.types.tag_map.serialize_aws_json_1_0(value["tags"])
    return out


def deserialize_aws_json_1_0(data: dict) -> TagQueueRequest:
    out: TagQueueRequest = {}  # type: ignore[typeddict-item]
    if data.get("QueueUrl") is not None:
        out["queue_url"] = data["QueueUrl"]
    else:
        out["queue_url"] = ""
    if data.get("Tags") is not None:
        import capo_sqs.types.tag_map

        out["tags"] = capo_sqs.types.tag_map.deserialize_aws_json_1_0(data["Tags"])
    else:
        out["tags"] = {}
    return out
