"""Generated from Smithy shape ``com.amazonaws.kinesis#ShardFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis.types.shard_filter_type
    import capo_kinesis.types.shard_id
    import capo_kinesis.types.timestamp


class ShardFilter(TypedDict, closed=True):
    type: "capo_kinesis.types.shard_filter_type.ShardFilterType"
    """<p>The shard type specified in the <code>ShardFilter</code> parameter. This is a required property of the <code>ShardFilter</code> parameter.</p> <p>You can specify the following valid values: </p> <ul> <li> <p> <code>AFTER_SHARD_ID</code> - the response includes all the shards, starting with the shard whose ID immediately follows the <code>ShardId</code> that you provided. </p> </li> <li> <p> <code>AT_TRIM_HORIZON</code> - the response includes all the shards that were open at <code>TRIM_HORIZON</code>.</p> </li> <li> <p> <code>FROM_TRIM_HORIZON</code> - (default), the response includes all the shards within the retention period of the data stream (trim to tip).</p> </li> <li> <p> <code>AT_LATEST</code> - the response includes only the currently open shards of the data stream.</p> </li> <li> <p> <code>AT_TIMESTAMP</code> - the response includes all shards whose start timestamp is less than or equal to the given timestamp and end timestamp is greater than or equal to the given timestamp or still open. </p> </li> <li> <p> <code>FROM_TIMESTAMP</code> - the response incldues all closed shards whose end timestamp is greater than or equal to the given timestamp and also all open shards. Corrected to <code>TRIM_HORIZON</code> of the data stream if <code>FROM_TIMESTAMP</code> is less than the <code>TRIM_HORIZON</code> value.</p> </li> </ul>"""
    shard_id: NotRequired["capo_kinesis.types.shard_id.ShardId"]
    """<p>The exclusive start <code>shardID</code> speified in the <code>ShardFilter</code> parameter. This property can only be used if the <code>AFTER_SHARD_ID</code> shard type is specified.</p>"""
    timestamp: NotRequired["capo_kinesis.types.timestamp.Timestamp"]
    """<p>The timestamps specified in the <code>ShardFilter</code> parameter. A timestamp is a Unix epoch date with precision in milliseconds. For example, 2016-04-04T19:58:46.480-00:00 or 1459799926.480. This property can only be used if <code>FROM_TIMESTAMP</code> or <code>AT_TIMESTAMP</code> shard types are specified.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ShardFilter) -> dict:
    out: dict = {}
    import capo_kinesis.types.shard_filter_type

    out["Type"] = capo_kinesis.types.shard_filter_type.serialize_aws_json_1_1(
        value["type"]
    )
    if "shard_id" in value:
        out["ShardId"] = value["shard_id"]
    if "timestamp" in value:
        import capo_kinesis.types.timestamp

        out["Timestamp"] = capo_kinesis.types.timestamp.serialize_aws_json_1_1(
            value["timestamp"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ShardFilter:
    out: ShardFilter = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_kinesis.types.shard_filter_type

        out["type"] = capo_kinesis.types.shard_filter_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_kinesis.types.shard_filter_type.ShardFilterType", ""
        )
    if data.get("ShardId") is not None:
        out["shard_id"] = data["ShardId"]
    if data.get("Timestamp") is not None:
        import capo_kinesis.types.timestamp

        out["timestamp"] = capo_kinesis.types.timestamp.deserialize_aws_json_1_1(
            data["Timestamp"]
        )
    return out
