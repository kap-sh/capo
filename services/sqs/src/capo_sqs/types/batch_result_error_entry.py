"""Generated from Smithy shape ``com.amazonaws.sqs#BatchResultErrorEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sqs.types.boolean
    import capo_sqs.types.string


class BatchResultErrorEntry(TypedDict, closed=True):
    id: "capo_sqs.types.string.String"
    """<p>The <code>Id</code> of an entry in a batch request.</p>"""
    sender_fault: "capo_sqs.types.boolean.Boolean"
    """<p>Specifies whether the error happened due to the caller of the batch API action.</p>"""
    code: "capo_sqs.types.string.String"
    """<p>An error code representing why the action failed on this entry.</p>"""
    message: NotRequired["capo_sqs.types.string.String"]
    """<p>A message explaining why the action failed on this entry.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchResultErrorEntry) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    out["SenderFault"] = value.get("sender_fault", False)
    out["Code"] = value["code"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchResultErrorEntry:
    out: BatchResultErrorEntry = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    if data.get("SenderFault") is not None:
        out["sender_fault"] = data["SenderFault"]
    else:
        out["sender_fault"] = False
    if data.get("Code") is not None:
        out["code"] = data["Code"]
    else:
        out["code"] = ""
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out
