"""Generated from Smithy shape ``com.amazonaws.sqs#RemovePermissionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sqs.types.string


class RemovePermissionRequest(TypedDict, closed=True):
    queue_url: "capo_sqs.types.string.String"
    """<p>The URL of the Amazon SQS queue from which permissions are removed.</p> <p>Queue URLs and names are case-sensitive.</p>"""
    label: "capo_sqs.types.string.String"
    """<p>The identification of the permission to remove. This is the label added using the <code> <a>AddPermission</a> </code> action.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RemovePermissionRequest) -> dict:
    out: dict = {}
    out["QueueUrl"] = value["queue_url"]
    out["Label"] = value["label"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RemovePermissionRequest:
    out: RemovePermissionRequest = {}  # type: ignore[typeddict-item]
    if data.get("QueueUrl") is not None:
        out["queue_url"] = data["QueueUrl"]
    else:
        out["queue_url"] = ""
    if data.get("Label") is not None:
        out["label"] = data["Label"]
    else:
        out["label"] = ""
    return out
