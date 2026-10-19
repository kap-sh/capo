"""Generated from Smithy shape ``com.amazonaws.dynamodbstreams#DescribeStreamInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb_streams.types.positive_integer_object
    import capo_dynamodb_streams.types.shard_filter
    import capo_dynamodb_streams.types.shard_id
    import capo_dynamodb_streams.types.stream_arn


class DescribeStreamInput(TypedDict, closed=True):
    stream_arn: "capo_dynamodb_streams.types.stream_arn.StreamArn"
    """<p>The Amazon Resource Name (ARN) for the stream.</p>"""
    limit: NotRequired[
        "capo_dynamodb_streams.types.positive_integer_object.PositiveIntegerObject"
    ]
    """<p>The maximum number of shard objects to return. The upper limit is 100.</p>"""
    exclusive_start_shard_id: NotRequired[
        "capo_dynamodb_streams.types.shard_id.ShardId"
    ]
    """<p>The shard ID of the first item that this operation will evaluate. Use the value that was returned for <code>LastEvaluatedShardId</code> in the previous operation. </p>"""
    shard_filter: NotRequired["capo_dynamodb_streams.types.shard_filter.ShardFilter"]
    """<p>This optional field contains the filter definition for the <code>DescribeStream</code> API.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeStreamInput) -> dict:
    out: dict = {}
    out["StreamArn"] = value["stream_arn"]
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "exclusive_start_shard_id" in value:
        out["ExclusiveStartShardId"] = value["exclusive_start_shard_id"]
    if "shard_filter" in value:
        import capo_dynamodb_streams.types.shard_filter

        out["ShardFilter"] = (
            capo_dynamodb_streams.types.shard_filter.serialize_aws_json_1_0(
                value["shard_filter"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeStreamInput:
    out: DescribeStreamInput = {}  # type: ignore[typeddict-item]
    if data.get("StreamArn") is not None:
        out["stream_arn"] = data["StreamArn"]
    else:
        out["stream_arn"] = ""
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    if data.get("ExclusiveStartShardId") is not None:
        out["exclusive_start_shard_id"] = data["ExclusiveStartShardId"]
    if data.get("ShardFilter") is not None:
        import capo_dynamodb_streams.types.shard_filter

        out["shard_filter"] = (
            capo_dynamodb_streams.types.shard_filter.deserialize_aws_json_1_0(
                data["ShardFilter"]
            )
        )
    return out
