"""Generated from Smithy shape ``com.amazonaws.firehose#SnowflakeDestinationDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_firehose.types.cloud_watch_logging_options
    import capo_firehose.types.processing_configuration
    import capo_firehose.types.role_arn
    import capo_firehose.types.s3_destination_description
    import capo_firehose.types.secrets_manager_configuration
    import capo_firehose.types.snowflake_account_url
    import capo_firehose.types.snowflake_buffering_hints
    import capo_firehose.types.snowflake_content_column_name
    import capo_firehose.types.snowflake_data_loading_option
    import capo_firehose.types.snowflake_database
    import capo_firehose.types.snowflake_meta_data_column_name
    import capo_firehose.types.snowflake_retry_options
    import capo_firehose.types.snowflake_role_configuration
    import capo_firehose.types.snowflake_s3_backup_mode
    import capo_firehose.types.snowflake_schema
    import capo_firehose.types.snowflake_table
    import capo_firehose.types.snowflake_user
    import capo_firehose.types.snowflake_vpc_configuration


class SnowflakeDestinationDescription(TypedDict, closed=True):
    account_url: NotRequired[
        "capo_firehose.types.snowflake_account_url.SnowflakeAccountUrl"
    ]
    """<p>URL for accessing your Snowflake account. This URL must include your <a href="https://docs.snowflake.com/en/user-guide/admin-account-identifier">account identifier</a>. Note that the protocol (https://) and port number are optional.</p>"""
    user: NotRequired["capo_firehose.types.snowflake_user.SnowflakeUser"]
    """<p>User login name for the Snowflake account.</p>"""
    database: NotRequired["capo_firehose.types.snowflake_database.SnowflakeDatabase"]
    """<p>All data in Snowflake is maintained in databases.</p>"""
    schema: NotRequired["capo_firehose.types.snowflake_schema.SnowflakeSchema"]
    """<p>Each database consists of one or more schemas, which are logical groupings of database objects, such as tables and views</p>"""
    table: NotRequired["capo_firehose.types.snowflake_table.SnowflakeTable"]
    """<p>All data in Snowflake is stored in database tables, logically structured as collections of columns and rows.</p>"""
    snowflake_role_configuration: NotRequired[
        "capo_firehose.types.snowflake_role_configuration.SnowflakeRoleConfiguration"
    ]
    """<p>Optionally configure a Snowflake role. Otherwise the default user role will be used.</p>"""
    data_loading_option: NotRequired[
        "capo_firehose.types.snowflake_data_loading_option.SnowflakeDataLoadingOption"
    ]
    """<p>Choose to load JSON keys mapped to table column names or choose to split the JSON payload where content is mapped to a record content column and source metadata is mapped to a record metadata column.</p>"""
    meta_data_column_name: NotRequired[
        "capo_firehose.types.snowflake_meta_data_column_name.SnowflakeMetaDataColumnName"
    ]
    """<p>The name of the record metadata column</p>"""
    content_column_name: NotRequired[
        "capo_firehose.types.snowflake_content_column_name.SnowflakeContentColumnName"
    ]
    """<p>The name of the record content column</p>"""
    snowflake_vpc_configuration: NotRequired[
        "capo_firehose.types.snowflake_vpc_configuration.SnowflakeVpcConfiguration"
    ]
    """<p>The VPCE ID for Firehose to privately connect with Snowflake. The ID format is com.amazonaws.vpce.[region].vpce-svc-<[id]>. For more information, see <a href="https://docs.snowflake.com/en/user-guide/admin-security-privatelink">Amazon PrivateLink & Snowflake</a> </p>"""
    cloud_watch_logging_options: NotRequired[
        "capo_firehose.types.cloud_watch_logging_options.CloudWatchLoggingOptions"
    ]
    processing_configuration: NotRequired[
        "capo_firehose.types.processing_configuration.ProcessingConfiguration"
    ]
    role_arn: NotRequired["capo_firehose.types.role_arn.RoleARN"]
    """<p>The Amazon Resource Name (ARN) of the Snowflake role</p>"""
    retry_options: NotRequired[
        "capo_firehose.types.snowflake_retry_options.SnowflakeRetryOptions"
    ]
    """<p>The time period where Firehose will retry sending data to the chosen HTTP endpoint.</p>"""
    s3_backup_mode: NotRequired[
        "capo_firehose.types.snowflake_s3_backup_mode.SnowflakeS3BackupMode"
    ]
    """<p>Choose an S3 backup mode</p>"""
    s3_destination_description: NotRequired[
        "capo_firehose.types.s3_destination_description.S3DestinationDescription"
    ]
    secrets_manager_configuration: NotRequired[
        "capo_firehose.types.secrets_manager_configuration.SecretsManagerConfiguration"
    ]
    """<p> The configuration that defines how you access secrets for Snowflake. </p>"""
    buffering_hints: NotRequired[
        "capo_firehose.types.snowflake_buffering_hints.SnowflakeBufferingHints"
    ]
    """<p> Describes the buffering to perform before delivering data to the Snowflake destination. If you do not specify any value, Firehose uses the default values. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SnowflakeDestinationDescription) -> dict:
    out: dict = {}
    if "account_url" in value:
        out["AccountUrl"] = value["account_url"]
    if "user" in value:
        out["User"] = value["user"]
    if "database" in value:
        out["Database"] = value["database"]
    if "schema" in value:
        out["Schema"] = value["schema"]
    if "table" in value:
        out["Table"] = value["table"]
    if "snowflake_role_configuration" in value:
        import capo_firehose.types.snowflake_role_configuration

        out["SnowflakeRoleConfiguration"] = (
            capo_firehose.types.snowflake_role_configuration.serialize_aws_json_1_1(
                value["snowflake_role_configuration"]
            )
        )
    if "data_loading_option" in value:
        import capo_firehose.types.snowflake_data_loading_option

        out["DataLoadingOption"] = (
            capo_firehose.types.snowflake_data_loading_option.serialize_aws_json_1_1(
                value["data_loading_option"]
            )
        )
    if "meta_data_column_name" in value:
        out["MetaDataColumnName"] = value["meta_data_column_name"]
    if "content_column_name" in value:
        out["ContentColumnName"] = value["content_column_name"]
    if "snowflake_vpc_configuration" in value:
        import capo_firehose.types.snowflake_vpc_configuration

        out["SnowflakeVpcConfiguration"] = (
            capo_firehose.types.snowflake_vpc_configuration.serialize_aws_json_1_1(
                value["snowflake_vpc_configuration"]
            )
        )
    if "cloud_watch_logging_options" in value:
        import capo_firehose.types.cloud_watch_logging_options

        out["CloudWatchLoggingOptions"] = (
            capo_firehose.types.cloud_watch_logging_options.serialize_aws_json_1_1(
                value["cloud_watch_logging_options"]
            )
        )
    if "processing_configuration" in value:
        import capo_firehose.types.processing_configuration

        out["ProcessingConfiguration"] = (
            capo_firehose.types.processing_configuration.serialize_aws_json_1_1(
                value["processing_configuration"]
            )
        )
    if "role_arn" in value:
        out["RoleARN"] = value["role_arn"]
    if "retry_options" in value:
        import capo_firehose.types.snowflake_retry_options

        out["RetryOptions"] = (
            capo_firehose.types.snowflake_retry_options.serialize_aws_json_1_1(
                value["retry_options"]
            )
        )
    if "s3_backup_mode" in value:
        import capo_firehose.types.snowflake_s3_backup_mode

        out["S3BackupMode"] = (
            capo_firehose.types.snowflake_s3_backup_mode.serialize_aws_json_1_1(
                value["s3_backup_mode"]
            )
        )
    if "s3_destination_description" in value:
        import capo_firehose.types.s3_destination_description

        out["S3DestinationDescription"] = (
            capo_firehose.types.s3_destination_description.serialize_aws_json_1_1(
                value["s3_destination_description"]
            )
        )
    if "secrets_manager_configuration" in value:
        import capo_firehose.types.secrets_manager_configuration

        out["SecretsManagerConfiguration"] = (
            capo_firehose.types.secrets_manager_configuration.serialize_aws_json_1_1(
                value["secrets_manager_configuration"]
            )
        )
    if "buffering_hints" in value:
        import capo_firehose.types.snowflake_buffering_hints

        out["BufferingHints"] = (
            capo_firehose.types.snowflake_buffering_hints.serialize_aws_json_1_1(
                value["buffering_hints"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SnowflakeDestinationDescription:
    out: SnowflakeDestinationDescription = {}  # type: ignore[typeddict-item]
    if data.get("AccountUrl") is not None:
        out["account_url"] = data["AccountUrl"]
    if data.get("User") is not None:
        out["user"] = data["User"]
    if data.get("Database") is not None:
        out["database"] = data["Database"]
    if data.get("Schema") is not None:
        out["schema"] = data["Schema"]
    if data.get("Table") is not None:
        out["table"] = data["Table"]
    if data.get("SnowflakeRoleConfiguration") is not None:
        import capo_firehose.types.snowflake_role_configuration

        out["snowflake_role_configuration"] = (
            capo_firehose.types.snowflake_role_configuration.deserialize_aws_json_1_1(
                data["SnowflakeRoleConfiguration"]
            )
        )
    if data.get("DataLoadingOption") is not None:
        import capo_firehose.types.snowflake_data_loading_option

        out["data_loading_option"] = (
            capo_firehose.types.snowflake_data_loading_option.deserialize_aws_json_1_1(
                data["DataLoadingOption"]
            )
        )
    if data.get("MetaDataColumnName") is not None:
        out["meta_data_column_name"] = data["MetaDataColumnName"]
    if data.get("ContentColumnName") is not None:
        out["content_column_name"] = data["ContentColumnName"]
    if data.get("SnowflakeVpcConfiguration") is not None:
        import capo_firehose.types.snowflake_vpc_configuration

        out["snowflake_vpc_configuration"] = (
            capo_firehose.types.snowflake_vpc_configuration.deserialize_aws_json_1_1(
                data["SnowflakeVpcConfiguration"]
            )
        )
    if data.get("CloudWatchLoggingOptions") is not None:
        import capo_firehose.types.cloud_watch_logging_options

        out["cloud_watch_logging_options"] = (
            capo_firehose.types.cloud_watch_logging_options.deserialize_aws_json_1_1(
                data["CloudWatchLoggingOptions"]
            )
        )
    if data.get("ProcessingConfiguration") is not None:
        import capo_firehose.types.processing_configuration

        out["processing_configuration"] = (
            capo_firehose.types.processing_configuration.deserialize_aws_json_1_1(
                data["ProcessingConfiguration"]
            )
        )
    if data.get("RoleARN") is not None:
        out["role_arn"] = data["RoleARN"]
    if data.get("RetryOptions") is not None:
        import capo_firehose.types.snowflake_retry_options

        out["retry_options"] = (
            capo_firehose.types.snowflake_retry_options.deserialize_aws_json_1_1(
                data["RetryOptions"]
            )
        )
    if data.get("S3BackupMode") is not None:
        import capo_firehose.types.snowflake_s3_backup_mode

        out["s3_backup_mode"] = (
            capo_firehose.types.snowflake_s3_backup_mode.deserialize_aws_json_1_1(
                data["S3BackupMode"]
            )
        )
    if data.get("S3DestinationDescription") is not None:
        import capo_firehose.types.s3_destination_description

        out["s3_destination_description"] = (
            capo_firehose.types.s3_destination_description.deserialize_aws_json_1_1(
                data["S3DestinationDescription"]
            )
        )
    if data.get("SecretsManagerConfiguration") is not None:
        import capo_firehose.types.secrets_manager_configuration

        out["secrets_manager_configuration"] = (
            capo_firehose.types.secrets_manager_configuration.deserialize_aws_json_1_1(
                data["SecretsManagerConfiguration"]
            )
        )
    if data.get("BufferingHints") is not None:
        import capo_firehose.types.snowflake_buffering_hints

        out["buffering_hints"] = (
            capo_firehose.types.snowflake_buffering_hints.deserialize_aws_json_1_1(
                data["BufferingHints"]
            )
        )
    return out
