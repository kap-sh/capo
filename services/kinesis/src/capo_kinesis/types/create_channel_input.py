"""Generated from Smithy shape ``com.amazonaws.kinesis#CreateChannelInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis.types.channel_encryption_configuration
    import capo_kinesis.types.channel_logging_configuration
    import capo_kinesis.types.channel_name
    import capo_kinesis.types.channel_stream_configuration_list
    import capo_kinesis.types.role_arn
    import capo_kinesis.types.s3_destination_configuration
    import capo_kinesis.types.s3_tables_destination_configuration
    import capo_kinesis.types.tag_map


class CreateChannelInput(TypedDict, closed=True):
    channel_name: "capo_kinesis.types.channel_name.ChannelName"
    """<p>The name of the channel. The name is unique within your Amazon Web Services account and Amazon Web Services Region.</p>"""
    service_execution_role_arn: "capo_kinesis.types.role_arn.RoleARN"
    """<p>The Amazon Resource Name (ARN) of the IAM role that Amazon Kinesis Data Streams assumes to write records to the destination.</p>"""
    stream_configuration_list: "capo_kinesis.types.channel_stream_configuration_list.ChannelStreamConfigurationList"
    """<p>The source stream configuration for the channel. Currently, one stream is supported per channel.</p>"""
    s3_destination_configuration: NotRequired[
        "capo_kinesis.types.s3_destination_configuration.S3DestinationConfiguration"
    ]
    """<p>The configuration for delivery to a general purpose Amazon S3 bucket. Specify this parameter when <code>S3TablesDestinationConfiguration</code> is not specified.</p>"""
    s3_tables_destination_configuration: NotRequired[
        "capo_kinesis.types.s3_tables_destination_configuration.S3TablesDestinationConfiguration"
    ]
    """<p>The configuration for delivery to streaming tables on Apache Iceberg in Amazon S3 Tables. Specify this parameter when <code>S3DestinationConfiguration</code> is not specified.</p>"""
    encryption_configuration: NotRequired[
        "capo_kinesis.types.channel_encryption_configuration.ChannelEncryptionConfiguration"
    ]
    """<p>The server-side encryption configuration that uses an Amazon Web Services KMS key to encrypt data delivered to the destination.</p>"""
    tags: NotRequired["capo_kinesis.types.tag_map.TagMap"]
    """<p>A set of key-value pairs to assign to the channel. A tag consists of a required key and an optional value.</p>"""
    logging_configuration: NotRequired[
        "capo_kinesis.types.channel_logging_configuration.ChannelLoggingConfiguration"
    ]
    """<p>The Amazon CloudWatch Logs configuration for the channel.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateChannelInput) -> dict:
    out: dict = {}
    out["ChannelName"] = value["channel_name"]
    out["ServiceExecutionRoleARN"] = value["service_execution_role_arn"]
    import capo_kinesis.types.channel_stream_configuration_list

    out["StreamConfigurationList"] = (
        capo_kinesis.types.channel_stream_configuration_list.serialize_aws_json_1_1(
            value["stream_configuration_list"]
        )
    )
    if "s3_destination_configuration" in value:
        import capo_kinesis.types.s3_destination_configuration

        out["S3DestinationConfiguration"] = (
            capo_kinesis.types.s3_destination_configuration.serialize_aws_json_1_1(
                value["s3_destination_configuration"]
            )
        )
    if "s3_tables_destination_configuration" in value:
        import capo_kinesis.types.s3_tables_destination_configuration

        out["S3TablesDestinationConfiguration"] = (
            capo_kinesis.types.s3_tables_destination_configuration.serialize_aws_json_1_1(
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
    if "tags" in value:
        import capo_kinesis.types.tag_map

        out["Tags"] = capo_kinesis.types.tag_map.serialize_aws_json_1_1(value["tags"])
    if "logging_configuration" in value:
        import capo_kinesis.types.channel_logging_configuration

        out["LoggingConfiguration"] = (
            capo_kinesis.types.channel_logging_configuration.serialize_aws_json_1_1(
                value["logging_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateChannelInput:
    out: CreateChannelInput = {}  # type: ignore[typeddict-item]
    if data.get("ChannelName") is not None:
        out["channel_name"] = data["ChannelName"]
    else:
        out["channel_name"] = ""
    if data.get("ServiceExecutionRoleARN") is not None:
        out["service_execution_role_arn"] = data["ServiceExecutionRoleARN"]
    else:
        out["service_execution_role_arn"] = ""
    if data.get("StreamConfigurationList") is not None:
        import capo_kinesis.types.channel_stream_configuration_list

        out["stream_configuration_list"] = (
            capo_kinesis.types.channel_stream_configuration_list.deserialize_aws_json_1_1(
                data["StreamConfigurationList"]
            )
        )
    else:
        out["stream_configuration_list"] = []
    if data.get("S3DestinationConfiguration") is not None:
        import capo_kinesis.types.s3_destination_configuration

        out["s3_destination_configuration"] = (
            capo_kinesis.types.s3_destination_configuration.deserialize_aws_json_1_1(
                data["S3DestinationConfiguration"]
            )
        )
    if data.get("S3TablesDestinationConfiguration") is not None:
        import capo_kinesis.types.s3_tables_destination_configuration

        out["s3_tables_destination_configuration"] = (
            capo_kinesis.types.s3_tables_destination_configuration.deserialize_aws_json_1_1(
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
    if data.get("Tags") is not None:
        import capo_kinesis.types.tag_map

        out["tags"] = capo_kinesis.types.tag_map.deserialize_aws_json_1_1(data["Tags"])
    if data.get("LoggingConfiguration") is not None:
        import capo_kinesis.types.channel_logging_configuration

        out["logging_configuration"] = (
            capo_kinesis.types.channel_logging_configuration.deserialize_aws_json_1_1(
                data["LoggingConfiguration"]
            )
        )
    return out
