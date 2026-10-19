"""Generated from Smithy shape ``com.amazonaws.sqs#ChangeMessageVisibilityRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sqs.types.nullable_integer
    import capo_sqs.types.string


class ChangeMessageVisibilityRequest(TypedDict, closed=True):
    queue_url: "capo_sqs.types.string.String"
    """<p>The URL of the Amazon SQS queue whose message's visibility is changed.</p> <p>Queue URLs and names are case-sensitive.</p>"""
    receipt_handle: "capo_sqs.types.string.String"
    """<p>The receipt handle associated with the message, whose visibility timeout is changed. This parameter is returned by the <code> <a>ReceiveMessage</a> </code> action.</p>"""
    visibility_timeout: "capo_sqs.types.nullable_integer.NullableInteger"
    """<p>The new value for the message's visibility timeout (in seconds). Values range: <code>0</code> to <code>43200</code>. Maximum: 12 hours.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ChangeMessageVisibilityRequest) -> dict:
    out: dict = {}
    out["QueueUrl"] = value["queue_url"]
    out["ReceiptHandle"] = value["receipt_handle"]
    out["VisibilityTimeout"] = value["visibility_timeout"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ChangeMessageVisibilityRequest:
    out: ChangeMessageVisibilityRequest = {}  # type: ignore[typeddict-item]
    if data.get("QueueUrl") is not None:
        out["queue_url"] = data["QueueUrl"]
    else:
        out["queue_url"] = ""
    if data.get("ReceiptHandle") is not None:
        out["receipt_handle"] = data["ReceiptHandle"]
    else:
        out["receipt_handle"] = ""
    if data.get("VisibilityTimeout") is not None:
        out["visibility_timeout"] = data["VisibilityTimeout"]
    else:
        out["visibility_timeout"] = 0
    return out
