"""Generated from Smithy shape ``com.amazonaws.fsx#UpdateFileSystemLustreConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.auto_import_policy_type
    import capo_fsx.types.automatic_backup_retention_days
    import capo_fsx.types.daily_time
    import capo_fsx.types.data_compression_type
    import capo_fsx.types.lustre_log_create_configuration
    import capo_fsx.types.lustre_read_cache_configuration
    import capo_fsx.types.lustre_root_squash_configuration
    import capo_fsx.types.per_unit_storage_throughput
    import capo_fsx.types.throughput_capacity_mbps
    import capo_fsx.types.update_file_system_lustre_metadata_configuration
    import capo_fsx.types.weekly_time


class UpdateFileSystemLustreConfiguration(TypedDict, closed=True):
    weekly_maintenance_start_time: NotRequired["capo_fsx.types.weekly_time.WeeklyTime"]
    """<p>(Optional) The preferred start time to perform weekly maintenance, formatted d:HH:MM in the UTC time zone. d is the weekday number, from 1 through 7, beginning with Monday and ending with Sunday.</p>"""
    daily_automatic_backup_start_time: NotRequired[
        "capo_fsx.types.daily_time.DailyTime"
    ]
    automatic_backup_retention_days: NotRequired[
        "capo_fsx.types.automatic_backup_retention_days.AutomaticBackupRetentionDays"
    ]
    """<p>The number of days to retain automatic backups. Setting this property to <code>0</code> disables automatic backups. You can retain automatic backups for a maximum of 90 days. The default is <code>0</code>.</p>"""
    auto_import_policy: NotRequired[
        "capo_fsx.types.auto_import_policy_type.AutoImportPolicyType"
    ]
    """<p> (Optional) When you create your file system, your existing S3 objects appear as file and directory listings. Use this property to choose how Amazon FSx keeps your file and directory listing up to date as you add or modify objects in your linked S3 bucket. <code>AutoImportPolicy</code> can have the following values:</p> <ul> <li> <p> <code>NONE</code> - (Default) AutoImport is off. Amazon FSx only updates file and directory listings from the linked S3 bucket when the file system is created. FSx does not update the file and directory listing for any new or changed objects after choosing this option.</p> </li> <li> <p> <code>NEW</code> - AutoImport is on. Amazon FSx automatically imports directory listings of any new objects added to the linked S3 bucket that do not currently exist in the FSx file system. </p> </li> <li> <p> <code>NEW_CHANGED</code> - AutoImport is on. Amazon FSx automatically imports file and directory listings of any new objects added to the S3 bucket and any existing objects that are changed in the S3 bucket after you choose this option.</p> </li> <li> <p> <code>NEW_CHANGED_DELETED</code> - AutoImport is on. Amazon FSx automatically imports file and directory listings of any new objects added to the S3 bucket, any existing objects that are changed in the S3 bucket, and any objects that were deleted in the S3 bucket.</p> </li> </ul> <p>This parameter is not supported for file systems with a data repository association.</p>"""
    data_compression_type: NotRequired[
        "capo_fsx.types.data_compression_type.DataCompressionType"
    ]
    """<p>Sets the data compression configuration for the file system. <code>DataCompressionType</code> can have the following values:</p> <ul> <li> <p> <code>NONE</code> - Data compression is turned off for the file system.</p> </li> <li> <p> <code>LZ4</code> - Data compression is turned on with the LZ4 algorithm.</p> </li> </ul> <p>If you don't use <code>DataCompressionType</code>, the file system retains its current data compression configuration.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/fsx/latest/LustreGuide/data-compression.html">Lustre data compression</a>.</p>"""
    log_configuration: NotRequired[
        "capo_fsx.types.lustre_log_create_configuration.LustreLogCreateConfiguration"
    ]
    """<p>The Lustre logging configuration used when updating an Amazon FSx for Lustre file system. When logging is enabled, Lustre logs error and warning events for data repositories associated with your file system to Amazon CloudWatch Logs.</p>"""
    root_squash_configuration: NotRequired[
        "capo_fsx.types.lustre_root_squash_configuration.LustreRootSquashConfiguration"
    ]
    """<p>The Lustre root squash configuration used when updating an Amazon FSx for Lustre file system. When enabled, root squash restricts root-level access from clients that try to access your file system as a root user.</p>"""
    per_unit_storage_throughput: NotRequired[
        "capo_fsx.types.per_unit_storage_throughput.PerUnitStorageThroughput"
    ]
    """<p>The throughput of an Amazon FSx for Lustre Persistent SSD-based file system, measured in megabytes per second per tebibyte (MB/s/TiB). You can increase or decrease your file system's throughput. Valid values depend on the deployment type of the file system, as follows:</p> <ul> <li> <p>For <code>PERSISTENT_1</code> SSD-based deployment types, valid values are 50, 100, and 200 MB/s/TiB.</p> </li> <li> <p>For <code>PERSISTENT_2</code> SSD-based deployment types, valid values are 125, 250, 500, and 1000 MB/s/TiB.</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/fsx/latest/LustreGuide/managing-throughput-capacity.html"> Managing throughput capacity</a>.</p>"""
    metadata_configuration: NotRequired[
        "capo_fsx.types.update_file_system_lustre_metadata_configuration.UpdateFileSystemLustreMetadataConfiguration"
    ]
    """<p>The Lustre metadata performance configuration for an Amazon FSx for Lustre file system using a <code>PERSISTENT_2</code> deployment type. When this configuration is enabled, the file system supports increasing metadata performance.</p>"""
    throughput_capacity: NotRequired[
        "capo_fsx.types.throughput_capacity_mbps.ThroughputCapacityMbps"
    ]
    """<p>The throughput of an Amazon FSx for Lustre file system using an Intelligent-Tiering storage class, measured in megabytes per second (MBps). You can only increase your file system's throughput. Valid values are 4000 MBps or multiples of 4000 MBps.</p>"""
    data_read_cache_configuration: NotRequired[
        "capo_fsx.types.lustre_read_cache_configuration.LustreReadCacheConfiguration"
    ]
    """<p>Specifies the optional provisioned SSD read cache on Amazon FSx for Lustre file systems that use the Intelligent-Tiering storage class.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateFileSystemLustreConfiguration) -> dict:
    out: dict = {}
    if "weekly_maintenance_start_time" in value:
        out["WeeklyMaintenanceStartTime"] = value["weekly_maintenance_start_time"]
    if "daily_automatic_backup_start_time" in value:
        out["DailyAutomaticBackupStartTime"] = value[
            "daily_automatic_backup_start_time"
        ]
    if "automatic_backup_retention_days" in value:
        out["AutomaticBackupRetentionDays"] = value["automatic_backup_retention_days"]
    if "auto_import_policy" in value:
        import capo_fsx.types.auto_import_policy_type

        out["AutoImportPolicy"] = (
            capo_fsx.types.auto_import_policy_type.serialize_aws_json_1_1(
                value["auto_import_policy"]
            )
        )
    if "data_compression_type" in value:
        import capo_fsx.types.data_compression_type

        out["DataCompressionType"] = (
            capo_fsx.types.data_compression_type.serialize_aws_json_1_1(
                value["data_compression_type"]
            )
        )
    if "log_configuration" in value:
        import capo_fsx.types.lustre_log_create_configuration

        out["LogConfiguration"] = (
            capo_fsx.types.lustre_log_create_configuration.serialize_aws_json_1_1(
                value["log_configuration"]
            )
        )
    if "root_squash_configuration" in value:
        import capo_fsx.types.lustre_root_squash_configuration

        out["RootSquashConfiguration"] = (
            capo_fsx.types.lustre_root_squash_configuration.serialize_aws_json_1_1(
                value["root_squash_configuration"]
            )
        )
    if "per_unit_storage_throughput" in value:
        out["PerUnitStorageThroughput"] = value["per_unit_storage_throughput"]
    if "metadata_configuration" in value:
        import capo_fsx.types.update_file_system_lustre_metadata_configuration

        out["MetadataConfiguration"] = (
            capo_fsx.types.update_file_system_lustre_metadata_configuration.serialize_aws_json_1_1(
                value["metadata_configuration"]
            )
        )
    if "throughput_capacity" in value:
        out["ThroughputCapacity"] = value["throughput_capacity"]
    if "data_read_cache_configuration" in value:
        import capo_fsx.types.lustre_read_cache_configuration

        out["DataReadCacheConfiguration"] = (
            capo_fsx.types.lustre_read_cache_configuration.serialize_aws_json_1_1(
                value["data_read_cache_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateFileSystemLustreConfiguration:
    out: UpdateFileSystemLustreConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("WeeklyMaintenanceStartTime") is not None:
        out["weekly_maintenance_start_time"] = data["WeeklyMaintenanceStartTime"]
    if data.get("DailyAutomaticBackupStartTime") is not None:
        out["daily_automatic_backup_start_time"] = data["DailyAutomaticBackupStartTime"]
    if data.get("AutomaticBackupRetentionDays") is not None:
        out["automatic_backup_retention_days"] = data["AutomaticBackupRetentionDays"]
    if data.get("AutoImportPolicy") is not None:
        import capo_fsx.types.auto_import_policy_type

        out["auto_import_policy"] = (
            capo_fsx.types.auto_import_policy_type.deserialize_aws_json_1_1(
                data["AutoImportPolicy"]
            )
        )
    if data.get("DataCompressionType") is not None:
        import capo_fsx.types.data_compression_type

        out["data_compression_type"] = (
            capo_fsx.types.data_compression_type.deserialize_aws_json_1_1(
                data["DataCompressionType"]
            )
        )
    if data.get("LogConfiguration") is not None:
        import capo_fsx.types.lustre_log_create_configuration

        out["log_configuration"] = (
            capo_fsx.types.lustre_log_create_configuration.deserialize_aws_json_1_1(
                data["LogConfiguration"]
            )
        )
    if data.get("RootSquashConfiguration") is not None:
        import capo_fsx.types.lustre_root_squash_configuration

        out["root_squash_configuration"] = (
            capo_fsx.types.lustre_root_squash_configuration.deserialize_aws_json_1_1(
                data["RootSquashConfiguration"]
            )
        )
    if data.get("PerUnitStorageThroughput") is not None:
        out["per_unit_storage_throughput"] = data["PerUnitStorageThroughput"]
    if data.get("MetadataConfiguration") is not None:
        import capo_fsx.types.update_file_system_lustre_metadata_configuration

        out["metadata_configuration"] = (
            capo_fsx.types.update_file_system_lustre_metadata_configuration.deserialize_aws_json_1_1(
                data["MetadataConfiguration"]
            )
        )
    if data.get("ThroughputCapacity") is not None:
        out["throughput_capacity"] = data["ThroughputCapacity"]
    if data.get("DataReadCacheConfiguration") is not None:
        import capo_fsx.types.lustre_read_cache_configuration

        out["data_read_cache_configuration"] = (
            capo_fsx.types.lustre_read_cache_configuration.deserialize_aws_json_1_1(
                data["DataReadCacheConfiguration"]
            )
        )
    return out
