"""Generated from Smithy shape ``com.amazonaws.sqs#DeleteMessageBatchRequestEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sqs.types.string


class DeleteMessageBatchRequestEntry(TypedDict, closed=True):
    id: "capo_sqs.types.string.String"
    """<p>The identifier for this particular receipt handle. This is used to communicate the result.</p> <note> <p>The <code>Id</code>s of a batch request need to be unique within a request.</p> <p>This identifier can have up to 80 characters. The following characters are accepted: alphanumeric characters, hyphens(-), and underscores (_).</p> </note>"""
    receipt_handle: "capo_sqs.types.string.String"
    """<p>A receipt handle.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteMessageBatchRequestEntry) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    out["ReceiptHandle"] = value["receipt_handle"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteMessageBatchRequestEntry:
    out: DeleteMessageBatchRequestEntry = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    if data.get("ReceiptHandle") is not None:
        out["receipt_handle"] = data["ReceiptHandle"]
    else:
        out["receipt_handle"] = ""
    return out
