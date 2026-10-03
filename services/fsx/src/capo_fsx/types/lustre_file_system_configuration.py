"""Generated from Smithy shape ``com.amazonaws.fsx#LustreFileSystemConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.automatic_backup_retention_days
    import capo_fsx.types.daily_time
    import capo_fsx.types.data_compression_type
    import capo_fsx.types.data_repository_configuration
    import capo_fsx.types.drive_cache_type
    import capo_fsx.types.file_system_lustre_metadata_configuration
    import capo_fsx.types.flag
    import capo_fsx.types.lustre_deployment_type
    import capo_fsx.types.lustre_file_system_mount_name
    import capo_fsx.types.lustre_log_configuration
    import capo_fsx.types.lustre_read_cache_configuration
    import capo_fsx.types.lustre_root_squash_configuration
    import capo_fsx.types.per_unit_storage_throughput
    import capo_fsx.types.throughput_capacity_mbps
    import capo_fsx.types.weekly_time


class LustreFileSystemConfiguration(TypedDict, closed=True):
    weekly_maintenance_start_time: NotRequired["capo_fsx.types.weekly_time.WeeklyTime"]
    """<p>The preferred start time to perform weekly maintenance, formatted d:HH:MM in the UTC time zone. Here, <code>d</code> is the weekday number, from 1 through 7, beginning with Monday and ending with Sunday.</p>"""
    data_repository_configuration: NotRequired[
        "capo_fsx.types.data_repository_configuration.DataRepositoryConfiguration"
    ]
    deployment_type: NotRequired[
        "capo_fsx.types.lustre_deployment_type.LustreDeploymentType"
    ]
    """<p>The deployment type of the FSx for Lustre file system. <i>Scratch deployment type</i> is designed for temporary storage and shorter-term processing of data.</p> <p> <code>SCRATCH_1</code> and <code>SCRATCH_2</code> deployment types are best suited for when you need temporary storage and shorter-term processing of data. The <code>SCRATCH_2</code> deployment type provides in-transit encryption of data and higher burst throughput capacity than <code>SCRATCH_1</code>.</p> <p>The <code>PERSISTENT_1</code> and <code>PERSISTENT_2</code> deployment type is used for longer-term storage and workloads and encryption of data in transit. <code>PERSISTENT_2</code> offers higher <code>PerUnitStorageThroughput</code> (up to 1000 MB/s/TiB) along with a lower minimum storage capacity requirement (600 GiB). To learn more about FSx for Lustre deployment types, see <a href="https://docs.aws.amazon.com/fsx/latest/LustreGuide/using-fsx-lustre.html">Deployment and storage class options for FSx for Lustre file systems</a>.</p> <p>The default is <code>SCRATCH_1</code>.</p>"""
    per_unit_storage_throughput: NotRequired[
        "capo_fsx.types.per_unit_storage_throughput.PerUnitStorageThroughput"
    ]
    """<p>Per unit storage throughput represents the megabytes per second of read or write throughput per 1 tebibyte of storage provisioned. File system throughput capacity is equal to Storage capacity (TiB) * PerUnitStorageThroughput (MB/s/TiB). This option is only valid for <code>PERSISTENT_1</code> and <code>PERSISTENT_2</code> deployment types. </p> <p>Valid values:</p> <ul> <li> <p>For <code>PERSISTENT_1</code> SSD storage: 50, 100, 200.</p> </li> <li> <p>For <code>PERSISTENT_1</code> HDD storage: 12, 40.</p> </li> <li> <p>For <code>PERSISTENT_2</code> SSD storage: 125, 250, 500, 1000.</p> </li> </ul>"""
    mount_name: NotRequired[
        "capo_fsx.types.lustre_file_system_mount_name.LustreFileSystemMountName"
    ]
    """<p>You use the <code>MountName</code> value when mounting the file system.</p> <p>For the <code>SCRATCH_1</code> deployment type, this value is always "<code>fsx</code>". For <code>SCRATCH_2</code>, <code>PERSISTENT_1</code>, and <code>PERSISTENT_2</code> deployment types, this value is a string that is unique within an Amazon Web Services Region. </p>"""
    daily_automatic_backup_start_time: NotRequired[
        "capo_fsx.types.daily_time.DailyTime"
    ]
    automatic_backup_retention_days: NotRequired[
        "capo_fsx.types.automatic_backup_retention_days.AutomaticBackupRetentionDays"
    ]
    copy_tags_to_backups: NotRequired["capo_fsx.types.flag.Flag"]
    """<p>A boolean flag indicating whether tags on the file system are copied to backups. If it's set to true, all tags on the file system are copied to all automatic backups and any user-initiated backups where the user doesn't specify any tags. If this value is true, and you specify one or more tags, only the specified tags are copied to backups. If you specify one or more tags when creating a user-initiated backup, no tags are copied from the file system, regardless of this value. (Default = false)</p>"""
    drive_cache_type: NotRequired["capo_fsx.types.drive_cache_type.DriveCacheType"]
    """<p>The type of drive cache used by <code>PERSISTENT_1</code> file systems that are provisioned with HDD storage devices. This parameter is required when <code>StorageType</code> is HDD. When set to <code>READ</code> the file system has an SSD storage cache that is sized to 20% of the file system's storage capacity. This improves the performance for frequently accessed files by caching up to 20% of the total storage capacity.</p> <p>This parameter is required when <code>StorageType</code> is set to HDD.</p>"""
    data_compression_type: NotRequired[
        "capo_fsx.types.data_compression_type.DataCompressionType"
    ]
    """<p>The data compression configuration for the file system. <code>DataCompressionType</code> can have the following values:</p> <ul> <li> <p> <code>NONE</code> - Data compression is turned off for the file system.</p> </li> <li> <p> <code>LZ4</code> - Data compression is turned on with the LZ4 algorithm.</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/fsx/latest/LustreGuide/data-compression.html">Lustre data compression</a>.</p>"""
    log_configuration: NotRequired[
        "capo_fsx.types.lustre_log_configuration.LustreLogConfiguration"
    ]
    """<p>The Lustre logging configuration. Lustre logging writes the enabled log events for your file system to Amazon CloudWatch Logs.</p>"""
    root_squash_configuration: NotRequired[
        "capo_fsx.types.lustre_root_squash_configuration.LustreRootSquashConfiguration"
    ]
    """<p>The Lustre root squash configuration for an Amazon FSx for Lustre file system. When enabled, root squash restricts root-level access from clients that try to access your file system as a root user.</p>"""
    metadata_configuration: NotRequired[
        "capo_fsx.types.file_system_lustre_metadata_configuration.FileSystemLustreMetadataConfiguration"
    ]
    """<p>The Lustre metadata performance configuration for an Amazon FSx for Lustre file system using a <code>PERSISTENT_2</code> deployment type.</p>"""
    efa_enabled: NotRequired["capo_fsx.types.flag.Flag"]
    """<p>Specifies whether Elastic Fabric Adapter (EFA) and GPUDirect Storage (GDS) support is enabled for the Amazon FSx for Lustre file system.</p>"""
    throughput_capacity: NotRequired[
        "capo_fsx.types.throughput_capacity_mbps.ThroughputCapacityMbps"
    ]
    """<p>The throughput of an Amazon FSx for Lustre file system using the Intelligent-Tiering storage class, measured in megabytes per second (MBps).</p>"""
    data_read_cache_configuration: NotRequired[
        "capo_fsx.types.lustre_read_cache_configuration.LustreReadCacheConfiguration"
    ]
    """<p>Required when <code>StorageType</code> is set to <code>INTELLIGENT_TIERING</code>. Specifies the optional provisioned SSD read cache.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LustreFileSystemConfiguration) -> dict:
    out: dict = {}
    if "weekly_maintenance_start_time" in value:
        out["WeeklyMaintenanceStartTime"] = value["weekly_maintenance_start_time"]
    if "data_repository_configuration" in value:
        import capo_fsx.types.data_repository_configuration

        out["DataRepositoryConfiguration"] = (
            capo_fsx.types.data_repository_configuration.serialize_aws_json_1_1(
                value["data_repository_configuration"]
            )
        )
    if "deployment_type" in value:
        import capo_fsx.types.lustre_deployment_type

        out["DeploymentType"] = (
            capo_fsx.types.lustre_deployment_type.serialize_aws_json_1_1(
                value["deployment_type"]
            )
        )
    if "per_unit_storage_throughput" in value:
        out["PerUnitStorageThroughput"] = value["per_unit_storage_throughput"]
    if "mount_name" in value:
        out["MountName"] = value["mount_name"]
    if "daily_automatic_backup_start_time" in value:
        out["DailyAutomaticBackupStartTime"] = value[
            "daily_automatic_backup_start_time"
        ]
    if "automatic_backup_retention_days" in value:
        out["AutomaticBackupRetentionDays"] = value["automatic_backup_retention_days"]
    if "copy_tags_to_backups" in value:
        out["CopyTagsToBackups"] = value["copy_tags_to_backups"]
    if "drive_cache_type" in value:
        import capo_fsx.types.drive_cache_type

        out["DriveCacheType"] = capo_fsx.types.drive_cache_type.serialize_aws_json_1_1(
            value["drive_cache_type"]
        )
    if "data_compression_type" in value:
        import capo_fsx.types.data_compression_type

        out["DataCompressionType"] = (
            capo_fsx.types.data_compression_type.serialize_aws_json_1_1(
                value["data_compression_type"]
            )
        )
    if "log_configuration" in value:
        import capo_fsx.types.lustre_log_configuration

        out["LogConfiguration"] = (
            capo_fsx.types.lustre_log_configuration.serialize_aws_json_1_1(
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
    if "metadata_configuration" in value:
        import capo_fsx.types.file_system_lustre_metadata_configuration

        out["MetadataConfiguration"] = (
            capo_fsx.types.file_system_lustre_metadata_configuration.serialize_aws_json_1_1(
                value["metadata_configuration"]
            )
        )
    if "efa_enabled" in value:
        out["EfaEnabled"] = value["efa_enabled"]
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


def deserialize_aws_json_1_1(data: dict) -> LustreFileSystemConfiguration:
    out: LustreFileSystemConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("WeeklyMaintenanceStartTime") is not None:
        out["weekly_maintenance_start_time"] = data["WeeklyMaintenanceStartTime"]
    if data.get("DataRepositoryConfiguration") is not None:
        import capo_fsx.types.data_repository_configuration

        out["data_repository_configuration"] = (
            capo_fsx.types.data_repository_configuration.deserialize_aws_json_1_1(
                data["DataRepositoryConfiguration"]
            )
        )
    if data.get("DeploymentType") is not None:
        import capo_fsx.types.lustre_deployment_type

        out["deployment_type"] = (
            capo_fsx.types.lustre_deployment_type.deserialize_aws_json_1_1(
                data["DeploymentType"]
            )
        )
    if data.get("PerUnitStorageThroughput") is not None:
        out["per_unit_storage_throughput"] = data["PerUnitStorageThroughput"]
    if data.get("MountName") is not None:
        out["mount_name"] = data["MountName"]
    if data.get("DailyAutomaticBackupStartTime") is not None:
        out["daily_automatic_backup_start_time"] = data["DailyAutomaticBackupStartTime"]
    if data.get("AutomaticBackupRetentionDays") is not None:
        out["automatic_backup_retention_days"] = data["AutomaticBackupRetentionDays"]
    if data.get("CopyTagsToBackups") is not None:
        out["copy_tags_to_backups"] = data["CopyTagsToBackups"]
    if data.get("DriveCacheType") is not None:
        import capo_fsx.types.drive_cache_type

        out["drive_cache_type"] = (
            capo_fsx.types.drive_cache_type.deserialize_aws_json_1_1(
                data["DriveCacheType"]
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
        import capo_fsx.types.lustre_log_configuration

        out["log_configuration"] = (
            capo_fsx.types.lustre_log_configuration.deserialize_aws_json_1_1(
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
    if data.get("MetadataConfiguration") is not None:
        import capo_fsx.types.file_system_lustre_metadata_configuration

        out["metadata_configuration"] = (
            capo_fsx.types.file_system_lustre_metadata_configuration.deserialize_aws_json_1_1(
                data["MetadataConfiguration"]
            )
        )
    if data.get("EfaEnabled") is not None:
        out["efa_enabled"] = data["EfaEnabled"]
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
