"""Generated from Smithy shape ``com.amazonaws.kinesis#AcknowledgeDeadLetterQueueRecordsErrorEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis.types.error_code
    import capo_kinesis.types.error_message
    import capo_kinesis.types.receipt_handle


class AcknowledgeDeadLetterQueueRecordsErrorEntry(TypedDict, closed=True):
    receipt_handle: "capo_kinesis.types.receipt_handle.ReceiptHandle"
    """<p>The receipt handle of the record that was not acknowledged.</p>"""
    error_code: "capo_kinesis.types.error_code.ErrorCode"
    """<p>A code identifying the type of failure. One of <code>ResourceNotFoundException</code>, <code>InvalidArgumentException</code>, <code>ThrottlingException</code>, or <code>InternalFailureException</code>.</p>"""
    error_message: NotRequired["capo_kinesis.types.error_message.ErrorMessage"]
    """<p>A description of the cause of the failure.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AcknowledgeDeadLetterQueueRecordsErrorEntry) -> dict:
    out: dict = {}
    out["ReceiptHandle"] = value["receipt_handle"]
    out["ErrorCode"] = value["error_code"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AcknowledgeDeadLetterQueueRecordsErrorEntry:
    out: AcknowledgeDeadLetterQueueRecordsErrorEntry = {}  # type: ignore[typeddict-item]
    if data.get("ReceiptHandle") is not None:
        out["receipt_handle"] = data["ReceiptHandle"]
    else:
        out["receipt_handle"] = ""
    if data.get("ErrorCode") is not None:
        out["error_code"] = data["ErrorCode"]
    else:
        out["error_code"] = ""
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    return out
