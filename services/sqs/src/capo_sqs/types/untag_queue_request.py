"""Generated from Smithy shape ``com.amazonaws.sqs#UntagQueueRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sqs.types.string
    import capo_sqs.types.tag_key_list


class UntagQueueRequest(TypedDict, closed=True):
    queue_url: "capo_sqs.types.string.String"
    """<p>The URL of the queue.</p>"""
    tag_keys: "capo_sqs.types.tag_key_list.TagKeyList"
    """<p>The list of tags to be removed from the specified queue.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UntagQueueRequest) -> dict:
    out: dict = {}
    out["QueueUrl"] = value["queue_url"]
    import capo_sqs.types.tag_key_list

    out["TagKeys"] = capo_sqs.types.tag_key_list.serialize_aws_json_1_0(
        value["tag_keys"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UntagQueueRequest:
    out: UntagQueueRequest = {}  # type: ignore[typeddict-item]
    if data.get("QueueUrl") is not None:
        out["queue_url"] = data["QueueUrl"]
    else:
        out["queue_url"] = ""
    if data.get("TagKeys") is not None:
        import capo_sqs.types.tag_key_list

        out["tag_keys"] = capo_sqs.types.tag_key_list.deserialize_aws_json_1_0(
            data["TagKeys"]
        )
    else:
        out["tag_keys"] = []
    return out
