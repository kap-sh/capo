"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DataMigration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.data_migration_cidr_block
    import capo_database_migration_service.types.data_migration_settings
    import capo_database_migration_service.types.data_migration_statistics
    import capo_database_migration_service.types.iso8601_date_time
    import capo_database_migration_service.types.migration_type_value
    import capo_database_migration_service.types.public_ip_address_list
    import capo_database_migration_service.types.source_data_settings
    import capo_database_migration_service.types.string
    import capo_database_migration_service.types.target_data_settings


class DataMigration(TypedDict, closed=True):
    data_migration_name: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The user-friendly name for the data migration.</p>"""
    data_migration_arn: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The Amazon Resource Name (ARN) that identifies this replication.</p>"""
    data_migration_create_time: NotRequired[
        "capo_database_migration_service.types.iso8601_date_time.Iso8601DateTime"
    ]
    """<p>The UTC time when DMS created the data migration.</p>"""
    data_migration_start_time: NotRequired[
        "capo_database_migration_service.types.iso8601_date_time.Iso8601DateTime"
    ]
    """<p>The UTC time when DMS started the data migration.</p>"""
    data_migration_end_time: NotRequired[
        "capo_database_migration_service.types.iso8601_date_time.Iso8601DateTime"
    ]
    """<p>The UTC time when data migration ended.</p>"""
    service_access_role_arn: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The IAM role that the data migration uses to access Amazon Web Services resources.</p>"""
    migration_project_arn: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The Amazon Resource Name (ARN) of the data migration's associated migration project.</p>"""
    data_migration_type: NotRequired[
        "capo_database_migration_service.types.migration_type_value.MigrationTypeValue"
    ]
    """<p>Specifies whether the data migration is full-load only, change data capture (CDC) only, or full-load and CDC.</p>"""
    data_migration_settings: NotRequired[
        "capo_database_migration_service.types.data_migration_settings.DataMigrationSettings"
    ]
    """<p>Specifies CloudWatch settings and selection rules for the data migration.</p>"""
    source_data_settings: NotRequired[
        "capo_database_migration_service.types.source_data_settings.SourceDataSettings"
    ]
    """<p>Specifies information about the data migration's source data provider.</p>"""
    target_data_settings: NotRequired[
        "capo_database_migration_service.types.target_data_settings.TargetDataSettings"
    ]
    """<p>Specifies information about the data migration's target data provider.</p>"""
    data_migration_statistics: NotRequired[
        "capo_database_migration_service.types.data_migration_statistics.DataMigrationStatistics"
    ]
    """<p>Provides information about the data migration's run, including start and stop time, latency, and data migration progress.</p>"""
    data_migration_status: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The current status of the data migration. </p>"""
    public_ip_addresses: NotRequired[
        "capo_database_migration_service.types.public_ip_address_list.PublicIpAddressList"
    ]
    """<p>The IP addresses of the endpoints for the data migration.</p>"""
    data_migration_cidr_blocks: NotRequired[
        "capo_database_migration_service.types.data_migration_cidr_block.DataMigrationCidrBlock"
    ]
    """<p>The CIDR blocks of the endpoints for the data migration.</p>"""
    last_failure_message: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>Information about the data migration's most recent error or failure.</p>"""
    stop_reason: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The reason the data migration last stopped.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataMigration) -> dict:
    out: dict = {}
    if "data_migration_name" in value:
        out["DataMigrationName"] = value["data_migration_name"]
    if "data_migration_arn" in value:
        out["DataMigrationArn"] = value["data_migration_arn"]
    if "data_migration_create_time" in value:
        import capo_database_migration_service.types.iso8601_date_time

        out["DataMigrationCreateTime"] = (
            capo_database_migration_service.types.iso8601_date_time.serialize_aws_json_1_1(
                value["data_migration_create_time"]
            )
        )
    if "data_migration_start_time" in value:
        import capo_database_migration_service.types.iso8601_date_time

        out["DataMigrationStartTime"] = (
            capo_database_migration_service.types.iso8601_date_time.serialize_aws_json_1_1(
                value["data_migration_start_time"]
            )
        )
    if "data_migration_end_time" in value:
        import capo_database_migration_service.types.iso8601_date_time

        out["DataMigrationEndTime"] = (
            capo_database_migration_service.types.iso8601_date_time.serialize_aws_json_1_1(
                value["data_migration_end_time"]
            )
        )
    if "service_access_role_arn" in value:
        out["ServiceAccessRoleArn"] = value["service_access_role_arn"]
    if "migration_project_arn" in value:
        out["MigrationProjectArn"] = value["migration_project_arn"]
    if "data_migration_type" in value:
        import capo_database_migration_service.types.migration_type_value

        out["DataMigrationType"] = (
            capo_database_migration_service.types.migration_type_value.serialize_aws_json_1_1(
                value["data_migration_type"]
            )
        )
    if "data_migration_settings" in value:
        import capo_database_migration_service.types.data_migration_settings

        out["DataMigrationSettings"] = (
            capo_database_migration_service.types.data_migration_settings.serialize_aws_json_1_1(
                value["data_migration_settings"]
            )
        )
    if "source_data_settings" in value:
        import capo_database_migration_service.types.source_data_settings

        out["SourceDataSettings"] = (
            capo_database_migration_service.types.source_data_settings.serialize_aws_json_1_1(
                value["source_data_settings"]
            )
        )
    if "target_data_settings" in value:
        import capo_database_migration_service.types.target_data_settings

        out["TargetDataSettings"] = (
            capo_database_migration_service.types.target_data_settings.serialize_aws_json_1_1(
                value["target_data_settings"]
            )
        )
    if "data_migration_statistics" in value:
        import capo_database_migration_service.types.data_migration_statistics

        out["DataMigrationStatistics"] = (
            capo_database_migration_service.types.data_migration_statistics.serialize_aws_json_1_1(
                value["data_migration_statistics"]
            )
        )
    if "data_migration_status" in value:
        out["DataMigrationStatus"] = value["data_migration_status"]
    if "public_ip_addresses" in value:
        import capo_database_migration_service.types.public_ip_address_list

        out["PublicIpAddresses"] = (
            capo_database_migration_service.types.public_ip_address_list.serialize_aws_json_1_1(
                value["public_ip_addresses"]
            )
        )
    if "data_migration_cidr_blocks" in value:
        import capo_database_migration_service.types.data_migration_cidr_block

        out["DataMigrationCidrBlocks"] = (
            capo_database_migration_service.types.data_migration_cidr_block.serialize_aws_json_1_1(
                value["data_migration_cidr_blocks"]
            )
        )
    if "last_failure_message" in value:
        out["LastFailureMessage"] = value["last_failure_message"]
    if "stop_reason" in value:
        out["StopReason"] = value["stop_reason"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DataMigration:
    out: DataMigration = {}  # type: ignore[typeddict-item]
    if data.get("DataMigrationName") is not None:
        out["data_migration_name"] = data["DataMigrationName"]
    if data.get("DataMigrationArn") is not None:
        out["data_migration_arn"] = data["DataMigrationArn"]
    if data.get("DataMigrationCreateTime") is not None:
        import capo_database_migration_service.types.iso8601_date_time

        out["data_migration_create_time"] = (
            capo_database_migration_service.types.iso8601_date_time.deserialize_aws_json_1_1(
                data["DataMigrationCreateTime"]
            )
        )
    if data.get("DataMigrationStartTime") is not None:
        import capo_database_migration_service.types.iso8601_date_time

        out["data_migration_start_time"] = (
            capo_database_migration_service.types.iso8601_date_time.deserialize_aws_json_1_1(
                data["DataMigrationStartTime"]
            )
        )
    if data.get("DataMigrationEndTime") is not None:
        import capo_database_migration_service.types.iso8601_date_time

        out["data_migration_end_time"] = (
            capo_database_migration_service.types.iso8601_date_time.deserialize_aws_json_1_1(
                data["DataMigrationEndTime"]
            )
        )
    if data.get("ServiceAccessRoleArn") is not None:
        out["service_access_role_arn"] = data["ServiceAccessRoleArn"]
    if data.get("MigrationProjectArn") is not None:
        out["migration_project_arn"] = data["MigrationProjectArn"]
    if data.get("DataMigrationType") is not None:
        import capo_database_migration_service.types.migration_type_value

        out["data_migration_type"] = (
            capo_database_migration_service.types.migration_type_value.deserialize_aws_json_1_1(
                data["DataMigrationType"]
            )
        )
    if data.get("DataMigrationSettings") is not None:
        import capo_database_migration_service.types.data_migration_settings

        out["data_migration_settings"] = (
            capo_database_migration_service.types.data_migration_settings.deserialize_aws_json_1_1(
                data["DataMigrationSettings"]
            )
        )
    if data.get("SourceDataSettings") is not None:
        import capo_database_migration_service.types.source_data_settings

        out["source_data_settings"] = (
            capo_database_migration_service.types.source_data_settings.deserialize_aws_json_1_1(
                data["SourceDataSettings"]
            )
        )
    if data.get("TargetDataSettings") is not None:
        import capo_database_migration_service.types.target_data_settings

        out["target_data_settings"] = (
            capo_database_migration_service.types.target_data_settings.deserialize_aws_json_1_1(
                data["TargetDataSettings"]
            )
        )
    if data.get("DataMigrationStatistics") is not None:
        import capo_database_migration_service.types.data_migration_statistics

        out["data_migration_statistics"] = (
            capo_database_migration_service.types.data_migration_statistics.deserialize_aws_json_1_1(
                data["DataMigrationStatistics"]
            )
        )
    if data.get("DataMigrationStatus") is not None:
        out["data_migration_status"] = data["DataMigrationStatus"]
    if data.get("PublicIpAddresses") is not None:
        import capo_database_migration_service.types.public_ip_address_list

        out["public_ip_addresses"] = (
            capo_database_migration_service.types.public_ip_address_list.deserialize_aws_json_1_1(
                data["PublicIpAddresses"]
            )
        )
    if data.get("DataMigrationCidrBlocks") is not None:
        import capo_database_migration_service.types.data_migration_cidr_block

        out["data_migration_cidr_blocks"] = (
            capo_database_migration_service.types.data_migration_cidr_block.deserialize_aws_json_1_1(
                data["DataMigrationCidrBlocks"]
            )
        )
    if data.get("LastFailureMessage") is not None:
        out["last_failure_message"] = data["LastFailureMessage"]
    if data.get("StopReason") is not None:
        out["stop_reason"] = data["StopReason"]
    return out


def redact_sensitive(value: DataMigration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "data_migration_settings" in value:
        import capo_database_migration_service.types.data_migration_settings

        out["data_migration_settings"] = (
            capo_database_migration_service.types.data_migration_settings.redact_sensitive(
                value["data_migration_settings"]
            )
        )
    if "public_ip_addresses" in value:
        out["public_ip_addresses"] = "*** Sensitive Data Redacted ***"
    return out
