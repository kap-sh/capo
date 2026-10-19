"""Generated from Smithy shape ``com.amazonaws.keyspacesstreams#GetRecordsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_keyspacesstreams.types.shard_iterator


class GetRecordsInput(TypedDict, closed=True):
    shard_iterator: "capo_keyspacesstreams.types.shard_iterator.ShardIterator"
    """<p> The unique identifier of the shard iterator. A shard iterator specifies the position in the shard from which you want to start reading data records sequentially. You obtain this value by calling the <code>GetShardIterator </code> operation. Each shard iterator is valid for 15 minutes after creation. </p>"""
    max_results: NotRequired["int"]
    """<p> The maximum number of records to return in a single <code>GetRecords</code> request. The default value is 100. You can specify a limit between 1 and 1000, but the actual number returned might be less than the specified maximum if the size of the data for the returned records exceeds the internal size limit. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetRecordsInput) -> dict:
    out: dict = {}
    out["shardIterator"] = value["shard_iterator"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetRecordsInput:
    out: GetRecordsInput = {}  # type: ignore[typeddict-item]
    if data.get("shardIterator") is not None:
        out["shard_iterator"] = data["shardIterator"]
    else:
        out["shard_iterator"] = ""
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out
