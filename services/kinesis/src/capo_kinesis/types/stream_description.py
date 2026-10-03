"""Generated from Smithy shape ``com.amazonaws.kinesis#StreamDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kinesis.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis.types.boolean_object
    import capo_kinesis.types.encryption_type
    import capo_kinesis.types.enhanced_monitoring_list
    import capo_kinesis.types.key_id
    import capo_kinesis.types.retention_period_hours
    import capo_kinesis.types.shard_list
    import capo_kinesis.types.stream_arn
    import capo_kinesis.types.stream_mode_details
    import capo_kinesis.types.stream_name
    import capo_kinesis.types.stream_status
    import capo_kinesis.types.timestamp


class StreamDescription(TypedDict, closed=True):
    stream_name: "capo_kinesis.types.stream_name.StreamName"
    """<p>The name of the stream being described.</p>"""
    stream_arn: "capo_kinesis.types.stream_arn.StreamARN"
    """<p>The Amazon Resource Name (ARN) for the stream being described.</p>"""
    stream_status: "capo_kinesis.types.stream_status.StreamStatus"
    """<p>The current status of the stream being described. The stream status is one of the following states:</p> <ul> <li> <p> <code>CREATING</code> - The stream is being created. Kinesis Data Streams immediately returns and sets <code>StreamStatus</code> to <code>CREATING</code>.</p> </li> <li> <p> <code>DELETING</code> - The stream is being deleted. The specified stream is in the <code>DELETING</code> state until Kinesis Data Streams completes the deletion.</p> </li> <li> <p> <code>ACTIVE</code> - The stream exists and is ready for read and write operations or deletion. You should perform read and write operations only on an <code>ACTIVE</code> stream.</p> </li> <li> <p> <code>UPDATING</code> - Shards in the stream are being merged or split. Read and write operations continue to work while the stream is in the <code>UPDATING</code> state.</p> </li> </ul>"""
    stream_mode_details: NotRequired[
        "capo_kinesis.types.stream_mode_details.StreamModeDetails"
    ]
    """<p> Specifies the capacity mode to which you want to set your data stream. Currently, in Kinesis Data Streams, you can choose between an <b>on-demand</b> capacity mode and a <b>provisioned</b> capacity mode for your data streams. </p>"""
    shards: "capo_kinesis.types.shard_list.ShardList"
    """<p>The shards that comprise the stream.</p>"""
    has_more_shards: "capo_kinesis.types.boolean_object.BooleanObject"
    """<p>If set to <code>true</code>, more shards in the stream are available to describe.</p>"""
    retention_period_hours: (
        "capo_kinesis.types.retention_period_hours.RetentionPeriodHours"
    )
    """<p>The current retention period, in hours. Minimum value of 24. Maximum value of 168.</p>"""
    stream_creation_timestamp: "capo_kinesis.types.timestamp.Timestamp"
    """<p>The approximate time that the stream was created.</p>"""
    enhanced_monitoring: (
        "capo_kinesis.types.enhanced_monitoring_list.EnhancedMonitoringList"
    )
    """<p>Represents the current enhanced monitoring settings of the stream.</p>"""
    encryption_type: NotRequired["capo_kinesis.types.encryption_type.EncryptionType"]
    """<p>The server-side encryption type used on the stream. This parameter can be one of the following values:</p> <ul> <li> <p> <code>NONE</code>: Do not encrypt the records in the stream.</p> </li> <li> <p> <code>KMS</code>: Use server-side encryption on the records in the stream using a customer-managed Amazon Web Services KMS key.</p> </li> </ul>"""
    key_id: NotRequired["capo_kinesis.types.key_id.KeyId"]
    """<p>The GUID for the customer-managed Amazon Web Services KMS key to use for encryption. This value can be a globally unique identifier, a fully specified ARN to either an alias or a key, or an alias name prefixed by "alias/".You can also use a master key owned by Kinesis Data Streams by specifying the alias <code>aws/kinesis</code>.</p> <ul> <li> <p>Key ARN example: <code>arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012</code> </p> </li> <li> <p>Alias ARN example: <code>arn:aws:kms:us-east-1:123456789012:alias/MyAliasName</code> </p> </li> <li> <p>Globally unique key ID example: <code>12345678-1234-1234-1234-123456789012</code> </p> </li> <li> <p>Alias name example: <code>alias/MyAliasName</code> </p> </li> <li> <p>Master key owned by Kinesis Data Streams: <code>alias/aws/kinesis</code> </p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StreamDescription) -> dict:
    out: dict = {}
    out["StreamName"] = value["stream_name"]
    out["StreamARN"] = value["stream_arn"]
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
    import capo_kinesis.types.shard_list

    out["Shards"] = capo_kinesis.types.shard_list.serialize_aws_json_1_1(
        value["shards"]
    )
    out["HasMoreShards"] = value["has_more_shards"]
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
    return out


def deserialize_aws_json_1_1(data: dict) -> StreamDescription:
    out: StreamDescription = {}  # type: ignore[typeddict-item]
    if data.get("StreamName") is not None:
        out["stream_name"] = data["StreamName"]
    else:
        raise DeserializationError("StreamDescription.stream_name required")
    if data.get("StreamARN") is not None:
        out["stream_arn"] = data["StreamARN"]
    else:
        raise DeserializationError("StreamDescription.stream_arn required")
    if data.get("StreamStatus") is not None:
        import capo_kinesis.types.stream_status

        out["stream_status"] = (
            capo_kinesis.types.stream_status.deserialize_aws_json_1_1(
                data["StreamStatus"]
            )
        )
    else:
        raise DeserializationError("StreamDescription.stream_status required")
    if data.get("StreamModeDetails") is not None:
        import capo_kinesis.types.stream_mode_details

        out["stream_mode_details"] = (
            capo_kinesis.types.stream_mode_details.deserialize_aws_json_1_1(
                data["StreamModeDetails"]
            )
        )
    if data.get("Shards") is not None:
        import capo_kinesis.types.shard_list

        out["shards"] = capo_kinesis.types.shard_list.deserialize_aws_json_1_1(
            data["Shards"]
        )
    else:
        raise DeserializationError("StreamDescription.shards required")
    if data.get("HasMoreShards") is not None:
        out["has_more_shards"] = data["HasMoreShards"]
    else:
        raise DeserializationError("StreamDescription.has_more_shards required")
    if data.get("RetentionPeriodHours") is not None:
        out["retention_period_hours"] = data["RetentionPeriodHours"]
    else:
        raise DeserializationError("StreamDescription.retention_period_hours required")
    if data.get("StreamCreationTimestamp") is not None:
        import capo_kinesis.types.timestamp

        out["stream_creation_timestamp"] = (
            capo_kinesis.types.timestamp.deserialize_aws_json_1_1(
                data["StreamCreationTimestamp"]
            )
        )
    else:
        raise DeserializationError(
            "StreamDescription.stream_creation_timestamp required"
        )
    if data.get("EnhancedMonitoring") is not None:
        import capo_kinesis.types.enhanced_monitoring_list

        out["enhanced_monitoring"] = (
            capo_kinesis.types.enhanced_monitoring_list.deserialize_aws_json_1_1(
                data["EnhancedMonitoring"]
            )
        )
    else:
        raise DeserializationError("StreamDescription.enhanced_monitoring required")
    if data.get("EncryptionType") is not None:
        import capo_kinesis.types.encryption_type

        out["encryption_type"] = (
            capo_kinesis.types.encryption_type.deserialize_aws_json_1_1(
                data["EncryptionType"]
            )
        )
    if data.get("KeyId") is not None:
        out["key_id"] = data["KeyId"]
    return out
