"""Generated from Smithy shape ``com.amazonaws.kinesis#RestoreDeadLetterQueueRecordsRequestEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kinesis.types.receipt_handle


class RestoreDeadLetterQueueRecordsRequestEntry(TypedDict, closed=True):
    receipt_handle: "capo_kinesis.types.receipt_handle.ReceiptHandle"
    """<p>The receipt handle of the record to restore, as returned by <a>ReceiveDeadLetterQueueRecords</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RestoreDeadLetterQueueRecordsRequestEntry) -> dict:
    out: dict = {}
    out["ReceiptHandle"] = value["receipt_handle"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RestoreDeadLetterQueueRecordsRequestEntry:
    out: RestoreDeadLetterQueueRecordsRequestEntry = {}  # type: ignore[typeddict-item]
    if data.get("ReceiptHandle") is not None:
        out["receipt_handle"] = data["ReceiptHandle"]
    else:
        out["receipt_handle"] = ""
    return out
