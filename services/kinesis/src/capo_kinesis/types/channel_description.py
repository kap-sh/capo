"""Generated from Smithy shape ``com.amazonaws.kinesis#ChannelDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kinesis.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis.types.channel_arn
    import capo_kinesis.types.channel_encryption_configuration
    import capo_kinesis.types.channel_id
    import capo_kinesis.types.channel_logging_configuration
    import capo_kinesis.types.channel_name
    import capo_kinesis.types.channel_status
    import capo_kinesis.types.channel_status_reason
    import capo_kinesis.types.channel_stream_description_list
    import capo_kinesis.types.role_arn
    import capo_kinesis.types.s3_destination_description
    import capo_kinesis.types.s3_tables_destination_description
    import capo_kinesis.types.timestamp


class ChannelDescription(TypedDict, closed=True):
    channel_name: "capo_kinesis.types.channel_name.ChannelName"
    """<p>The name of the channel.</p>"""
    channel_arn: "capo_kinesis.types.channel_arn.ChannelARN"
    """<p>The Amazon Resource Name (ARN) of the channel.</p>"""
    channel_id: "capo_kinesis.types.channel_id.ChannelId"
    """<p>The unique identifier of the channel.</p>"""
    channel_status: "capo_kinesis.types.channel_status.ChannelStatus"
    """<p>The current status of the channel. Valid values:</p> <ul> <li> <p> <code>CREATING</code> - The channel is being created.</p> </li> <li> <p> <code>ACTIVE</code> - The channel is ready to deliver records.</p> </li> <li> <p> <code>UPDATING</code> - The channel configuration is being updated.</p> </li> <li> <p> <code>DELETING</code> - The channel is being deleted.</p> </li> <li> <p> <code>FAILED</code> - See <code>ChannelStatusReason</code> for the failure cause.</p> </li> </ul>"""
    channel_status_reason: NotRequired[
        "capo_kinesis.types.channel_status_reason.ChannelStatusReason"
    ]
    """<p>A message describing the reason for a <code>FAILED</code> status.</p>"""
    channel_creation_timestamp: "capo_kinesis.types.timestamp.Timestamp"
    """<p>The time at which the channel was created.</p>"""
    service_execution_role_arn: "capo_kinesis.types.role_arn.RoleARN"
    """<p>The Amazon Resource Name (ARN) of the IAM role that Amazon Kinesis Data Streams assumes to write records to the destination.</p>"""
    stream_configuration_list: "capo_kinesis.types.channel_stream_description_list.ChannelStreamDescriptionList"
    """<p>The source stream configuration for the channel.</p>"""
    s3_destination_configuration: NotRequired[
        "capo_kinesis.types.s3_destination_description.S3DestinationDescription"
    ]
    """<p>The configuration for delivery to a general purpose Amazon S3 bucket. Present only when the channel destination is a general purpose Amazon S3 bucket.</p>"""
    s3_tables_destination_configuration: NotRequired[
        "capo_kinesis.types.s3_tables_destination_description.S3TablesDestinationDescription"
    ]
    """<p>The configuration for delivery to streaming tables on Apache Iceberg in Amazon S3 Tables. Present only when the channel destination is a streaming table.</p>"""
    encryption_configuration: NotRequired[
        "capo_kinesis.types.channel_encryption_configuration.ChannelEncryptionConfiguration"
    ]
    """<p>The Amazon Web Services KMS key configuration that Amazon Kinesis Data Streams uses to encrypt data delivered to the channel's destination.</p>"""
    logging_configuration: (
        "capo_kinesis.types.channel_logging_configuration.ChannelLoggingConfiguration"
    )
    """<p>The Amazon CloudWatch Logs configuration for the channel.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ChannelDescription) -> dict:
    out: dict = {}
    out["ChannelName"] = value["channel_name"]
    out["ChannelARN"] = value["channel_arn"]
    out["ChannelId"] = value["channel_id"]
    import capo_kinesis.types.channel_status

    out["ChannelStatus"] = capo_kinesis.types.channel_status.serialize_aws_json_1_1(
        value["channel_status"]
    )
    if "channel_status_reason" in value:
        out["ChannelStatusReason"] = value["channel_status_reason"]
    import capo_kinesis.types.timestamp

    out["ChannelCreationTimestamp"] = (
        capo_kinesis.types.timestamp.serialize_aws_json_1_1(
            value["channel_creation_timestamp"]
        )
    )
    out["ServiceExecutionRoleARN"] = value["service_execution_role_arn"]
    import capo_kinesis.types.channel_stream_description_list

    out["StreamConfigurationList"] = (
        capo_kinesis.types.channel_stream_description_list.serialize_aws_json_1_1(
            value["stream_configuration_list"]
        )
    )
    if "s3_destination_configuration" in value:
        import capo_kinesis.types.s3_destination_description

        out["S3DestinationConfiguration"] = (
            capo_kinesis.types.s3_destination_description.serialize_aws_json_1_1(
                value["s3_destination_configuration"]
            )
        )
    if "s3_tables_destination_configuration" in value:
        import capo_kinesis.types.s3_tables_destination_description

        out["S3TablesDestinationConfiguration"] = (
            capo_kinesis.types.s3_tables_destination_description.serialize_aws_json_1_1(
                value["s3_tables_destination_configuration"]
            )
        )
    if "encryption_configuration" in value:
        import capo_kinesis.types.channel_encryption_configuration

        out["EncryptionConfiguration"] = (
            capo_kinesis.types.channel_encryption_configuration.serialize_aws_json_1_1(
                value["encryption_configuration"]
            )
        )
    import capo_kinesis.types.channel_logging_configuration

    out["LoggingConfiguration"] = (
        capo_kinesis.types.channel_logging_configuration.serialize_aws_json_1_1(
            value["logging_configuration"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ChannelDescription:
    out: ChannelDescription = {}  # type: ignore[typeddict-item]
    if data.get("ChannelName") is not None:
        out["channel_name"] = data["ChannelName"]
    else:
        out["channel_name"] = ""
    if data.get("ChannelARN") is not None:
        out["channel_arn"] = data["ChannelARN"]
    else:
        out["channel_arn"] = ""
    if data.get("ChannelId") is not None:
        out["channel_id"] = data["ChannelId"]
    else:
        out["channel_id"] = ""
    if data.get("ChannelStatus") is not None:
        import capo_kinesis.types.channel_status

        out["channel_status"] = (
            capo_kinesis.types.channel_status.deserialize_aws_json_1_1(
                data["ChannelStatus"]
            )
        )
    else:
        import typing

        out["channel_status"] = typing.cast(
            "capo_kinesis.types.channel_status.ChannelStatus", ""
        )
    if data.get("ChannelStatusReason") is not None:
        out["channel_status_reason"] = data["ChannelStatusReason"]
    if data.get("ChannelCreationTimestamp") is not None:
        import capo_kinesis.types.timestamp

        out["channel_creation_timestamp"] = (
            capo_kinesis.types.timestamp.deserialize_aws_json_1_1(
                data["ChannelCreationTimestamp"]
            )
        )
    else:
        import datetime

        out["channel_creation_timestamp"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("ServiceExecutionRoleARN") is not None:
        out["service_execution_role_arn"] = data["ServiceExecutionRoleARN"]
    else:
        out["service_execution_role_arn"] = ""
    if data.get("StreamConfigurationList") is not None:
        import capo_kinesis.types.channel_stream_description_list

        out["stream_configuration_list"] = (
            capo_kinesis.types.channel_stream_description_list.deserialize_aws_json_1_1(
                data["StreamConfigurationList"]
            )
        )
    else:
        out["stream_configuration_list"] = []
    if data.get("S3DestinationConfiguration") is not None:
        import capo_kinesis.types.s3_destination_description

        out["s3_destination_configuration"] = (
            capo_kinesis.types.s3_destination_description.deserialize_aws_json_1_1(
                data["S3DestinationConfiguration"]
            )
        )
    if data.get("S3TablesDestinationConfiguration") is not None:
        import capo_kinesis.types.s3_tables_destination_description

        out["s3_tables_destination_configuration"] = (
            capo_kinesis.types.s3_tables_destination_description.deserialize_aws_json_1_1(
                data["S3TablesDestinationConfiguration"]
            )
        )
    if data.get("EncryptionConfiguration") is not None:
        import capo_kinesis.types.channel_encryption_configuration

        out["encryption_configuration"] = (
            capo_kinesis.types.channel_encryption_configuration.deserialize_aws_json_1_1(
                data["EncryptionConfiguration"]
            )
        )
    if data.get("LoggingConfiguration") is not None:
        import capo_kinesis.types.channel_logging_configuration

        out["logging_configuration"] = (
            capo_kinesis.types.channel_logging_configuration.deserialize_aws_json_1_1(
                data["LoggingConfiguration"]
            )
        )
    else:
        raise DeserializationError("ChannelDescription.logging_configuration required")
    return out
