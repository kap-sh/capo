"""Generated from Smithy shape ``com.amazonaws.kinesis#GetRecordsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis.types.boolean_object
    import capo_kinesis.types.get_records_input_limit
    import capo_kinesis.types.shard_iterator
    import capo_kinesis.types.stream_arn
    import capo_kinesis.types.stream_id


class GetRecordsInput(TypedDict, closed=True):
    shard_iterator: "capo_kinesis.types.shard_iterator.ShardIterator"
    """<p>The position in the shard from which you want to start sequentially reading data records. A shard iterator specifies this position using the sequence number of a data record in the shard.</p>"""
    limit: NotRequired[
        "capo_kinesis.types.get_records_input_limit.GetRecordsInputLimit"
    ]
    """<p>The maximum number of records to return. Specify a value of up to 10,000. If you specify a value that is greater than 10,000, <a>GetRecords</a> throws <code>InvalidArgumentException</code>. The default value is 10,000.</p>"""
    stream_arn: NotRequired["capo_kinesis.types.stream_arn.StreamARN"]
    """<p>The ARN of the stream.</p>"""
    stream_id: NotRequired["capo_kinesis.types.stream_id.StreamId"]
    """<p>Not Implemented. Reserved for future use.</p>"""
    dry_run: NotRequired["capo_kinesis.types.boolean_object.BooleanObject"]
    """<p>Checks if your request will succeed. <code>DryRun</code> is an optional parameter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetRecordsInput) -> dict:
    out: dict = {}
    out["ShardIterator"] = value["shard_iterator"]
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "stream_arn" in value:
        out["StreamARN"] = value["stream_arn"]
    if "stream_id" in value:
        out["StreamId"] = value["stream_id"]
    if "dry_run" in value:
        out["DryRun"] = value["dry_run"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetRecordsInput:
    out: GetRecordsInput = {}  # type: ignore[typeddict-item]
    if data.get("ShardIterator") is not None:
        out["shard_iterator"] = data["ShardIterator"]
    else:
        out["shard_iterator"] = ""
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    if data.get("StreamARN") is not None:
        out["stream_arn"] = data["StreamARN"]
    if data.get("StreamId") is not None:
        out["stream_id"] = data["StreamId"]
    if data.get("DryRun") is not None:
        out["dry_run"] = data["DryRun"]
    return out
