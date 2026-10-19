"""Generated from Smithy shape ``com.amazonaws.sqs#DeleteMessageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sqs.types.string


class DeleteMessageRequest(TypedDict, closed=True):
    queue_url: "capo_sqs.types.string.String"
    """<p>The URL of the Amazon SQS queue from which messages are deleted.</p> <p>Queue URLs and names are case-sensitive.</p>"""
    receipt_handle: "capo_sqs.types.string.String"
    """<p>The receipt handle associated with the message to delete.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteMessageRequest) -> dict:
    out: dict = {}
    out["QueueUrl"] = value["queue_url"]
    out["ReceiptHandle"] = value["receipt_handle"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteMessageRequest:
    out: DeleteMessageRequest = {}  # type: ignore[typeddict-item]
    if data.get("QueueUrl") is not None:
        out["queue_url"] = data["QueueUrl"]
    else:
        out["queue_url"] = ""
    if data.get("ReceiptHandle") is not None:
        out["receipt_handle"] = data["ReceiptHandle"]
    else:
        out["receipt_handle"] = ""
    return out
