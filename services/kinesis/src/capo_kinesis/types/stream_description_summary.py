"""Generated from Smithy shape ``com.amazonaws.kinesis#StreamDescriptionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kinesis.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis.types.channel_count_object
    import capo_kinesis.types.consumer_count_object
    import capo_kinesis.types.encryption_type
    import capo_kinesis.types.enhanced_monitoring_list
    import capo_kinesis.types.key_id
    import capo_kinesis.types.max_record_size_in_ki_b
    import capo_kinesis.types.record_distribution_strategy
    import capo_kinesis.types.retention_period_hours
    import capo_kinesis.types.shard_count_object
    import capo_kinesis.types.stream_arn
    import capo_kinesis.types.stream_id
    import capo_kinesis.types.stream_mode_details
    import capo_kinesis.types.stream_name
    import capo_kinesis.types.stream_status
    import capo_kinesis.types.timestamp
    import capo_kinesis.types.warm_throughput_object


class StreamDescriptionSummary(TypedDict, closed=True):
    stream_name: "capo_kinesis.types.stream_name.StreamName"
    """<p>The name of the stream being described.</p>"""
    stream_arn: "capo_kinesis.types.stream_arn.StreamARN"
    """<p>The Amazon Resource Name (ARN) for the stream being described.</p>"""
    stream_id: NotRequired["capo_kinesis.types.stream_id.StreamId"]
    """<p>Not Implemented. Reserved for future use.</p>"""
    stream_status: "capo_kinesis.types.stream_status.StreamStatus"
    """<p>The current status of the stream being described. The stream status is one of the following states:</p> <ul> <li> <p> <code>CREATING</code> - The stream is being created. Kinesis Data Streams immediately returns and sets <code>StreamStatus</code> to <code>CREATING</code>.</p> </li> <li> <p> <code>DELETING</code> - The stream is being deleted. The specified stream is in the <code>DELETING</code> state until Kinesis Data Streams completes the deletion.</p> </li> <li> <p> <code>ACTIVE</code> - The stream exists and is ready for read and write operations or deletion. You should perform read and write operations only on an <code>ACTIVE</code> stream.</p> </li> <li> <p> <code>UPDATING</code> - Shards in the stream are being merged or split. Read and write operations continue to work while the stream is in the <code>UPDATING</code> state.</p> </li> </ul>"""
    stream_mode_details: NotRequired[
        "capo_kinesis.types.stream_mode_details.StreamModeDetails"
    ]
    """<p> Specifies the capacity mode to which you want to set your data stream. Currently, in Kinesis Data Streams, you can choose between an <b>on-demand</b> ycapacity mode and a <b>provisioned</b> capacity mode for your data streams. </p>"""
    retention_period_hours: (
        "capo_kinesis.types.retention_period_hours.RetentionPeriodHours"
    )
    """<p>The current retention period, in hours.</p>"""
    stream_creation_timestamp: "capo_kinesis.types.timestamp.Timestamp"
    """<p>The approximate time that the stream was created.</p>"""
    enhanced_monitoring: (
        "capo_kinesis.types.enhanced_monitoring_list.EnhancedMonitoringList"
    )
    """<p>Represents the current enhanced monitoring settings of the stream.</p>"""
    encryption_type: NotRequired["capo_kinesis.types.encryption_type.EncryptionType"]
    """<p>The encryption type used. This value is one of the following:</p> <ul> <li> <p> <code>KMS</code> </p> </li> <li> <p> <code>NONE</code> </p> </li> </ul>"""
    key_id: NotRequired["capo_kinesis.types.key_id.KeyId"]
    """<p>The GUID for the customer-managed Amazon Web Services KMS key to use for encryption. This value can be a globally unique identifier, a fully specified ARN to either an alias or a key, or an alias name prefixed by "alias/".You can also use a master key owned by Kinesis Data Streams by specifying the alias <code>aws/kinesis</code>.</p> <ul> <li> <p>Key ARN example: <code>arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012</code> </p> </li> <li> <p>Alias ARN example: <code> arn:aws:kms:us-east-1:123456789012:alias/MyAliasName</code> </p> </li> <li> <p>Globally unique key ID example: <code>12345678-1234-1234-1234-123456789012</code> </p> </li> <li> <p>Alias name example: <code>alias/MyAliasName</code> </p> </li> <li> <p>Master key owned by Kinesis Data Streams: <code>alias/aws/kinesis</code> </p> </li> </ul>"""
    open_shard_count: "capo_kinesis.types.shard_count_object.ShardCountObject"
    """<p>The number of open shards in the stream.</p>"""
    consumer_count: NotRequired[
        "capo_kinesis.types.consumer_count_object.ConsumerCountObject"
    ]
    """<p>The number of enhanced fan-out consumers registered with the stream.</p>"""
    warm_throughput: NotRequired[
        "capo_kinesis.types.warm_throughput_object.WarmThroughputObject"
    ]
    """<p>The warm throughput in MB/s for the stream. This represents the throughput capacity that will be immediately available for write operations.</p>"""
    max_record_size_in_ki_b: NotRequired[
        "capo_kinesis.types.max_record_size_in_ki_b.MaxRecordSizeInKiB"
    ]
    """<p>The maximum record size of a single record in kibibyte (KiB) that you can write to, and read from a stream.</p>"""
    channel_count: NotRequired[
        "capo_kinesis.types.channel_count_object.ChannelCountObject"
    ]
    """<p>The number of channels associated with the stream.</p>"""
    record_distribution_strategy: NotRequired[
        "capo_kinesis.types.record_distribution_strategy.RecordDistributionStrategy"
    ]
    """<p>The record distribution strategy that the stream currently uses. A value of <code>AUTO</code> indicates that Amazon Kinesis Data Streams distributes records across shards using service-managed algorithms. A value of <code>USER_PARTITION_KEY</code> indicates that shard placement is determined by the partition key that producers supply. This field is only present for streams that use the on-demand capacity mode.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StreamDescriptionSummary) -> dict:
    out: dict = {}
    out["StreamName"] = value["stream_name"]
    out["StreamARN"] = value["stream_arn"]
    if "stream_id" in value:
        out["StreamId"] = value["stream_id"]
    import capo_kinesis.types.stream_status

    out["StreamStatus"] = capo_kinesis.types.stream_status.serialize_aws_json_1_1(
        value["stream_status"]
    )
    if "stream_mode_details" in value:
        import capo_kinesis.types.stream_mode_details

        out["StreamModeDetails"] = (
            capo_kinesis.types.stream_mode_details.serialize_aws_json_1_1(
                value["stream_mode_details"]
            )
        )
    out["RetentionPeriodHours"] = value["retention_period_hours"]
    import capo_kinesis.types.timestamp

    out["StreamCreationTimestamp"] = (
        capo_kinesis.types.timestamp.serialize_aws_json_1_1(
            value["stream_creation_timestamp"]
        )
    )
    import capo_kinesis.types.enhanced_monitoring_list

    out["EnhancedMonitoring"] = (
        capo_kinesis.types.enhanced_monitoring_list.serialize_aws_json_1_1(
            value["enhanced_monitoring"]
        )
    )
    if "encryption_type" in value:
        import capo_kinesis.types.encryption_type

        out["EncryptionType"] = (
            capo_kinesis.types.encryption_type.serialize_aws_json_1_1(
                value["encryption_type"]
            )
        )
    if "key_id" in value:
        out["KeyId"] = value["key_id"]
    out["OpenShardCount"] = value["open_shard_count"]
    if "consumer_count" in value:
        out["ConsumerCount"] = value["consumer_count"]
    if "warm_throughput" in value:
        import capo_kinesis.types.warm_throughput_object

        out["WarmThroughput"] = (
            capo_kinesis.types.warm_throughput_object.serialize_aws_json_1_1(
                value["warm_throughput"]
            )
        )
    if "max_record_size_in_ki_b" in value:
        out["MaxRecordSizeInKiB"] = value["max_record_size_in_ki_b"]
    if "channel_count" in value:
        out["ChannelCount"] = value["channel_count"]
    if "record_distribution_strategy" in value:
        import capo_kinesis.types.record_distribution_strategy

        out["RecordDistributionStrategy"] = (
            capo_kinesis.types.record_distribution_strategy.serialize_aws_json_1_1(
                value["record_distribution_strategy"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StreamDescriptionSummary:
    out: StreamDescriptionSummary = {}  # type: ignore[typeddict-item]
    if data.get("StreamName") is not None:
        out["stream_name"] = data["StreamName"]
    else:
        raise DeserializationError("StreamDescriptionSummary.stream_name required")
    if data.get("StreamARN") is not None:
        out["stream_arn"] = data["StreamARN"]
    else:
        raise DeserializationError("StreamDescriptionSummary.stream_arn required")
    if data.get("StreamId") is not None:
        out["stream_id"] = data["StreamId"]
    if data.get("StreamStatus") is not None:
        import capo_kinesis.types.stream_status

        out["stream_status"] = (
            capo_kinesis.types.stream_status.deserialize_aws_json_1_1(
                data["StreamStatus"]
            )
        )
    else:
        raise DeserializationError("StreamDescriptionSummary.stream_status required")
    if data.get("StreamModeDetails") is not None:
        import capo_kinesis.types.stream_mode_details

        out["stream_mode_details"] = (
            capo_kinesis.types.stream_mode_details.deserialize_aws_json_1_1(
                data["StreamModeDetails"]
            )
        )
    if data.get("RetentionPeriodHours") is not None:
        out["retention_period_hours"] = data["RetentionPeriodHours"]
    else:
        raise DeserializationError(
            "StreamDescriptionSummary.retention_period_hours required"
        )
    if data.get("StreamCreationTimestamp") is not None:
        import capo_kinesis.types.timestamp

        out["stream_creation_timestamp"] = (
            capo_kinesis.types.timestamp.deserialize_aws_json_1_1(
                data["StreamCreationTimestamp"]
            )
        )
    else:
        raise DeserializationError(
            "StreamDescriptionSummary.stream_creation_timestamp required"
        )
    if data.get("EnhancedMonitoring") is not None:
        import capo_kinesis.types.enhanced_monitoring_list

        out["enhanced_monitoring"] = (
            capo_kinesis.types.enhanced_monitoring_list.deserialize_aws_json_1_1(
                data["EnhancedMonitoring"]
            )
        )
    else:
        raise DeserializationError(
            "StreamDescriptionSummary.enhanced_monitoring required"
        )
    if data.get("EncryptionType") is not None:
        import capo_kinesis.types.encryption_type

        out["encryption_type"] = (
            capo_kinesis.types.encryption_type.deserialize_aws_json_1_1(
                data["EncryptionType"]
            )
        )
    if data.get("KeyId") is not None:
        out["key_id"] = data["KeyId"]
    if data.get("OpenShardCount") is not None:
        out["open_shard_count"] = data["OpenShardCount"]
    else:
        raise DeserializationError("StreamDescriptionSummary.open_shard_count required")
    if data.get("ConsumerCount") is not None:
        out["consumer_count"] = data["ConsumerCount"]
    if data.get("WarmThroughput") is not None:
        import capo_kinesis.types.warm_throughput_object

        out["warm_throughput"] = (
            capo_kinesis.types.warm_throughput_object.deserialize_aws_json_1_1(
                data["WarmThroughput"]
            )
        )
    if data.get("MaxRecordSizeInKiB") is not None:
        out["max_record_size_in_ki_b"] = data["MaxRecordSizeInKiB"]
    if data.get("ChannelCount") is not None:
        out["channel_count"] = data["ChannelCount"]
    if data.get("RecordDistributionStrategy") is not None:
        import capo_kinesis.types.record_distribution_strategy

        out["record_distribution_strategy"] = (
            capo_kinesis.types.record_distribution_strategy.deserialize_aws_json_1_1(
                data["RecordDistributionStrategy"]
            )
        )
    return out
