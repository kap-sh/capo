"""Generated from Smithy shape ``com.amazonaws.kinesis#DescribeLimitsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis.types.channel_count_object
    import capo_kinesis.types.on_demand_stream_count_limit_object
    import capo_kinesis.types.on_demand_stream_count_object
    import capo_kinesis.types.shard_count_object


class DescribeLimitsOutput(TypedDict, closed=True):
    shard_limit: "capo_kinesis.types.shard_count_object.ShardCountObject"
    """<p>The maximum number of shards.</p>"""
    open_shard_count: "capo_kinesis.types.shard_count_object.ShardCountObject"
    """<p>The number of open shards.</p>"""
    on_demand_stream_count: (
        "capo_kinesis.types.on_demand_stream_count_object.OnDemandStreamCountObject"
    )
    """<p> Indicates the number of data streams with the on-demand capacity mode.</p>"""
    on_demand_stream_count_limit: "capo_kinesis.types.on_demand_stream_count_limit_object.OnDemandStreamCountLimitObject"
    """<p> The maximum number of data streams with the on-demand capacity mode. </p>"""
    channel_count: NotRequired[
        "capo_kinesis.types.channel_count_object.ChannelCountObject"
    ]
    """<p>The number of channels in the account.</p>"""
    channel_count_limit: NotRequired[
        "capo_kinesis.types.channel_count_object.ChannelCountObject"
    ]
    """<p>The maximum number of channels allowed in the account.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeLimitsOutput) -> dict:
    out: dict = {}
    out["ShardLimit"] = value["shard_limit"]
    out["OpenShardCount"] = value["open_shard_count"]
    out["OnDemandStreamCount"] = value["on_demand_stream_count"]
    out["OnDemandStreamCountLimit"] = value["on_demand_stream_count_limit"]
    if "channel_count" in value:
        out["ChannelCount"] = value["channel_count"]
    if "channel_count_limit" in value:
        out["ChannelCountLimit"] = value["channel_count_limit"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeLimitsOutput:
    out: DescribeLimitsOutput = {}  # type: ignore[typeddict-item]
    if data.get("ShardLimit") is not None:
        out["shard_limit"] = data["ShardLimit"]
    else:
        out["shard_limit"] = 0
    if data.get("OpenShardCount") is not None:
        out["open_shard_count"] = data["OpenShardCount"]
    else:
        out["open_shard_count"] = 0
    if data.get("OnDemandStreamCount") is not None:
        out["on_demand_stream_count"] = data["OnDemandStreamCount"]
    else:
        out["on_demand_stream_count"] = 0
    if data.get("OnDemandStreamCountLimit") is not None:
        out["on_demand_stream_count_limit"] = data["OnDemandStreamCountLimit"]
    else:
        out["on_demand_stream_count_limit"] = 0
    if data.get("ChannelCount") is not None:
        out["channel_count"] = data["ChannelCount"]
    if data.get("ChannelCountLimit") is not None:
        out["channel_count_limit"] = data["ChannelCountLimit"]
    return out
