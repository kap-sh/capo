"""Generated from Smithy shape ``com.amazonaws.kinesis#CreateStreamInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis.types.max_record_size_in_ki_b
    import capo_kinesis.types.natural_integer_object
    import capo_kinesis.types.positive_integer_object
    import capo_kinesis.types.record_distribution_strategy
    import capo_kinesis.types.stream_mode_details
    import capo_kinesis.types.stream_name
    import capo_kinesis.types.tag_map


class CreateStreamInput(TypedDict, closed=True):
    stream_name: "capo_kinesis.types.stream_name.StreamName"
    """<p>A name to identify the stream. The stream name is scoped to the Amazon Web Services account used by the application that creates the stream. It is also scoped by Amazon Web Services Region. That is, two streams in two different Amazon Web Services accounts can have the same name. Two streams in the same Amazon Web Services account but in two different Regions can also have the same name.</p>"""
    shard_count: NotRequired[
        "capo_kinesis.types.positive_integer_object.PositiveIntegerObject"
    ]
    """<p>The number of shards that the stream will use. The throughput of the stream is a function of the number of shards; more shards are required for greater provisioned throughput.</p>"""
    stream_mode_details: NotRequired[
        "capo_kinesis.types.stream_mode_details.StreamModeDetails"
    ]
    """<p> Indicates the capacity mode of the data stream. Currently, in Kinesis Data Streams, you can choose between an <b>on-demand</b> capacity mode and a <b>provisioned</b> capacity mode for your data streams.</p>"""
    tags: NotRequired["capo_kinesis.types.tag_map.TagMap"]
    """<p>A set of up to 50 key-value pairs to use to create the tags. A tag consists of a required key and an optional value.</p>"""
    warm_throughput_mi_bps: NotRequired[
        "capo_kinesis.types.natural_integer_object.NaturalIntegerObject"
    ]
    """<p>The target warm throughput in MB/s that the stream should be scaled to handle. This represents the throughput capacity that will be immediately available for write operations.</p>"""
    max_record_size_in_ki_b: NotRequired[
        "capo_kinesis.types.max_record_size_in_ki_b.MaxRecordSizeInKiB"
    ]
    """<p>The maximum record size of a single record in kibibyte (KiB) that you can write to, and read from a stream.</p>"""
    record_distribution_strategy: NotRequired[
        "capo_kinesis.types.record_distribution_strategy.RecordDistributionStrategy"
    ]
    """<p>The record distribution strategy for the stream, which determines how Amazon Kinesis Data Streams distributes records across shards. Specify one of the following values:</p> <ul> <li> <p> <code>AUTO</code> – Amazon Kinesis Data Streams distributes records evenly across shards and ignores any partition key and <code>ExplicitHashKey</code> that producers supply. Use this value for stateless workloads that do not require partition-key ordering.</p> </li> <li> <p> <code>USER_PARTITION_KEY</code> – Producers must supply a partition key, which Amazon Kinesis Data Streams uses to determine shard placement. This is the default.</p> </li> </ul> <p>The record distribution strategy is only supported for streams that use the on-demand capacity mode. If you do not specify this parameter, the stream uses <code>USER_PARTITION_KEY</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateStreamInput) -> dict:
    out: dict = {}
    out["StreamName"] = value["stream_name"]
    if "shard_count" in value:
        out["ShardCount"] = value["shard_count"]
    if "stream_mode_details" in value:
        import capo_kinesis.types.stream_mode_details

        out["StreamModeDetails"] = (
            capo_kinesis.types.stream_mode_details.serialize_aws_json_1_1(
                value["stream_mode_details"]
            )
        )
    if "tags" in value:
        import capo_kinesis.types.tag_map

        out["Tags"] = capo_kinesis.types.tag_map.serialize_aws_json_1_1(value["tags"])
    if "warm_throughput_mi_bps" in value:
        out["WarmThroughputMiBps"] = value["warm_throughput_mi_bps"]
    if "max_record_size_in_ki_b" in value:
        out["MaxRecordSizeInKiB"] = value["max_record_size_in_ki_b"]
    if "record_distribution_strategy" in value:
        import capo_kinesis.types.record_distribution_strategy

        out["RecordDistributionStrategy"] = (
            capo_kinesis.types.record_distribution_strategy.serialize_aws_json_1_1(
                value["record_distribution_strategy"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateStreamInput:
    out: CreateStreamInput = {}  # type: ignore[typeddict-item]
    if data.get("StreamName") is not None:
        out["stream_name"] = data["StreamName"]
    else:
        out["stream_name"] = ""
    if data.get("ShardCount") is not None:
        out["shard_count"] = data["ShardCount"]
    if data.get("StreamModeDetails") is not None:
        import capo_kinesis.types.stream_mode_details

        out["stream_mode_details"] = (
            capo_kinesis.types.stream_mode_details.deserialize_aws_json_1_1(
                data["StreamModeDetails"]
            )
        )
    if data.get("Tags") is not None:
        import capo_kinesis.types.tag_map

        out["tags"] = capo_kinesis.types.tag_map.deserialize_aws_json_1_1(data["Tags"])
    if data.get("WarmThroughputMiBps") is not None:
        out["warm_throughput_mi_bps"] = data["WarmThroughputMiBps"]
    if data.get("MaxRecordSizeInKiB") is not None:
        out["max_record_size_in_ki_b"] = data["MaxRecordSizeInKiB"]
    if data.get("RecordDistributionStrategy") is not None:
        import capo_kinesis.types.record_distribution_strategy

        out["record_distribution_strategy"] = (
            capo_kinesis.types.record_distribution_strategy.deserialize_aws_json_1_1(
                data["RecordDistributionStrategy"]
            )
        )
    return out
