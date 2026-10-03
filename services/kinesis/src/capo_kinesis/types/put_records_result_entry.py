"""Generated from Smithy shape ``com.amazonaws.kinesis#PutRecordsResultEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis.types.error_code
    import capo_kinesis.types.error_message
    import capo_kinesis.types.sequence_number
    import capo_kinesis.types.shard_id


class PutRecordsResultEntry(TypedDict, closed=True):
    sequence_number: NotRequired["capo_kinesis.types.sequence_number.SequenceNumber"]
    """<p>The sequence number for an individual record result.</p>"""
    shard_id: NotRequired["capo_kinesis.types.shard_id.ShardId"]
    """<p>The shard ID for an individual record result.</p>"""
    error_code: NotRequired["capo_kinesis.types.error_code.ErrorCode"]
    """<p>The error code for an individual record result. <code>ErrorCodes</code> can be either <code>ProvisionedThroughputExceededException</code> or <code>InternalFailure</code>.</p>"""
    error_message: NotRequired["capo_kinesis.types.error_message.ErrorMessage"]
    """<p>The error message for an individual record result. An <code>ErrorCode</code> value of <code>ProvisionedThroughputExceededException</code> has an error message that includes the account ID, stream name, and shard ID. An <code>ErrorCode</code> value of <code>InternalFailure</code> has the error message <code>"Internal Service Failure"</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutRecordsResultEntry) -> dict:
    out: dict = {}
    if "sequence_number" in value:
        out["SequenceNumber"] = value["sequence_number"]
    if "shard_id" in value:
        out["ShardId"] = value["shard_id"]
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutRecordsResultEntry:
    out: PutRecordsResultEntry = {}  # type: ignore[typeddict-item]
    if data.get("SequenceNumber") is not None:
        out["sequence_number"] = data["SequenceNumber"]
    if data.get("ShardId") is not None:
        out["shard_id"] = data["ShardId"]
    if data.get("ErrorCode") is not None:
        out["error_code"] = data["ErrorCode"]
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    return out
