"""Generated from Smithy shape ``com.amazonaws.keyspacesstreams#GetStreamInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_keyspacesstreams.types.shard_filter
    import capo_keyspacesstreams.types.shard_id_token
    import capo_keyspacesstreams.types.stream_arn


class GetStreamInput(TypedDict, closed=True):
    stream_arn: "capo_keyspacesstreams.types.stream_arn.StreamArn"
    """<p> The Amazon Resource Name (ARN) of the stream for which detailed information is requested. This uniquely identifies the specific stream you want to get information about. </p>"""
    max_results: NotRequired["int"]
    """<p> The maximum number of shard objects to return in a single <code>GetStream</code> request. The default value is 100. The minimum value is 1 and the maximum value is 100. </p>"""
    shard_filter: NotRequired["capo_keyspacesstreams.types.shard_filter.ShardFilter"]
    """<p> Optional filter criteria to apply when retrieving shards. You can filter shards based on their parent <code>shardID</code> to get a list of children shards to narrow down the results returned by the <code>GetStream</code> operation. </p>"""
    next_token: NotRequired["capo_keyspacesstreams.types.shard_id_token.ShardIdToken"]
    """<p> An optional pagination token provided by a previous <code>GetStream</code> operation. If this parameter is specified, the response includes only records beyond the token, up to the value specified by <code>MaxResults</code>. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetStreamInput) -> dict:
    out: dict = {}
    out["streamArn"] = value["stream_arn"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "shard_filter" in value:
        import capo_keyspacesstreams.types.shard_filter

        out["shardFilter"] = (
            capo_keyspacesstreams.types.shard_filter.serialize_aws_json_1_0(
                value["shard_filter"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetStreamInput:
    out: GetStreamInput = {}  # type: ignore[typeddict-item]
    if data.get("streamArn") is not None:
        out["stream_arn"] = data["streamArn"]
    else:
        out["stream_arn"] = ""
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("shardFilter") is not None:
        import capo_keyspacesstreams.types.shard_filter

        out["shard_filter"] = (
            capo_keyspacesstreams.types.shard_filter.deserialize_aws_json_1_0(
                data["shardFilter"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
