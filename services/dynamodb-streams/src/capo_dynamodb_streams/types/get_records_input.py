"""Generated from Smithy shape ``com.amazonaws.dynamodbstreams#GetRecordsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb_streams.types.positive_integer_object
    import capo_dynamodb_streams.types.shard_iterator


class GetRecordsInput(TypedDict, closed=True):
    shard_iterator: "capo_dynamodb_streams.types.shard_iterator.ShardIterator"
    """<p>A shard iterator that was retrieved from a previous GetShardIterator operation. This iterator can be used to access the stream records in this shard.</p>"""
    limit: NotRequired[
        "capo_dynamodb_streams.types.positive_integer_object.PositiveIntegerObject"
    ]
    """<p>The maximum number of records to return from the shard. The upper limit is 1000.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetRecordsInput) -> dict:
    out: dict = {}
    out["ShardIterator"] = value["shard_iterator"]
    if "limit" in value:
        out["Limit"] = value["limit"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetRecordsInput:
    out: GetRecordsInput = {}  # type: ignore[typeddict-item]
    if data.get("ShardIterator") is not None:
        out["shard_iterator"] = data["ShardIterator"]
    else:
        out["shard_iterator"] = ""
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    return out
