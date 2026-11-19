"""Generated from Smithy shape ``com.amazonaws.kinesis#UpdateDeadLetterQueueRecordsVisibilityRequestEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kinesis.types.receipt_handle
    import capo_kinesis.types.visibility_timeout_seconds


class UpdateDeadLetterQueueRecordsVisibilityRequestEntry(TypedDict, closed=True):
    receipt_handle: "capo_kinesis.types.receipt_handle.ReceiptHandle"
    """<p>The receipt handle of the record, as returned by <a>ReceiveDeadLetterQueueRecords</a>.</p>"""
    visibility_timeout_seconds: (
        "capo_kinesis.types.visibility_timeout_seconds.VisibilityTimeoutSeconds"
    )
    """<p>The new duration, in seconds, that the record is in flight and not visible to any consumer instance, measured from when this request is processed. Specify <code>0</code> to make the record visible immediately.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: UpdateDeadLetterQueueRecordsVisibilityRequestEntry,
) -> dict:
    out: dict = {}
    out["ReceiptHandle"] = value["receipt_handle"]
    out["VisibilityTimeoutSeconds"] = value["visibility_timeout_seconds"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> UpdateDeadLetterQueueRecordsVisibilityRequestEntry:
    out: UpdateDeadLetterQueueRecordsVisibilityRequestEntry = {}  # type: ignore[typeddict-item]
    if data.get("ReceiptHandle") is not None:
        out["receipt_handle"] = data["ReceiptHandle"]
    else:
        out["receipt_handle"] = ""
    if data.get("VisibilityTimeoutSeconds") is not None:
        out["visibility_timeout_seconds"] = data["VisibilityTimeoutSeconds"]
    else:
        out["visibility_timeout_seconds"] = 0
    return out
