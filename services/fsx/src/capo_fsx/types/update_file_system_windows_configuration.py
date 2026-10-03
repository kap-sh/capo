"""Generated from Smithy shape ``com.amazonaws.fsx#UpdateFileSystemWindowsConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.automatic_backup_retention_days
    import capo_fsx.types.daily_time
    import capo_fsx.types.disk_iops_configuration
    import capo_fsx.types.megabytes_per_second
    import capo_fsx.types.self_managed_active_directory_configuration_updates
    import capo_fsx.types.weekly_time
    import capo_fsx.types.windows_audit_log_create_configuration
    import capo_fsx.types.windows_fsrm_configuration


class UpdateFileSystemWindowsConfiguration(TypedDict, closed=True):
    weekly_maintenance_start_time: NotRequired["capo_fsx.types.weekly_time.WeeklyTime"]
    """<p>The preferred start time to perform weekly maintenance, formatted d:HH:MM in the UTC time zone. Where d is the weekday number, from 1 through 7, with 1 = Monday and 7 = Sunday.</p>"""
    daily_automatic_backup_start_time: NotRequired[
        "capo_fsx.types.daily_time.DailyTime"
    ]
    """<p>The preferred time to start the daily automatic backup, in the UTC time zone, for example, <code>02:00</code> </p>"""
    automatic_backup_retention_days: NotRequired[
        "capo_fsx.types.automatic_backup_retention_days.AutomaticBackupRetentionDays"
    ]
    """<p>The number of days to retain automatic backups. Setting this property to <code>0</code> disables automatic backups. You can retain automatic backups for a maximum of 90 days. The default is <code>30</code>. For more information, see <a href="https://docs.aws.amazon.com/fsx/latest/WindowsGuide/using-backups.html#automatic-backups">Working with Automatic Daily Backups</a>.</p>"""
    throughput_capacity: NotRequired[
        "capo_fsx.types.megabytes_per_second.MegabytesPerSecond"
    ]
    """<p>Sets the target value for a file system's throughput capacity, in MB/s, that you are updating the file system to. Valid values are 8, 16, 32, 64, 128, 256, 512, 1024, 2048. You cannot make a throughput capacity update request if there is an existing throughput capacity update request in progress. For more information, see <a href="https://docs.aws.amazon.com/fsx/latest/WindowsGuide/managing-throughput-capacity.html">Managing Throughput Capacity</a>.</p>"""
    self_managed_active_directory_configuration: NotRequired[
        "capo_fsx.types.self_managed_active_directory_configuration_updates.SelfManagedActiveDirectoryConfigurationUpdates"
    ]
    """<p>The configuration Amazon FSx uses to join the Windows File Server instance to the self-managed Microsoft AD directory. You cannot make a self-managed Microsoft AD update request if there is an existing self-managed Microsoft AD update request in progress.</p>"""
    audit_log_configuration: NotRequired[
        "capo_fsx.types.windows_audit_log_create_configuration.WindowsAuditLogCreateConfiguration"
    ]
    """<p>The configuration that Amazon FSx for Windows File Server uses to audit and log user accesses of files, folders, and file shares on the Amazon FSx for Windows File Server file system..</p>"""
    disk_iops_configuration: NotRequired[
        "capo_fsx.types.disk_iops_configuration.DiskIopsConfiguration"
    ]
    """<p>The SSD IOPS (input/output operations per second) configuration for an Amazon FSx for Windows file system. By default, Amazon FSx automatically provisions 3 IOPS per GiB of storage capacity. You can provision additional IOPS per GiB of storage, up to the maximum limit associated with your chosen throughput capacity.</p>"""
    fsrm_configuration: NotRequired[
        "capo_fsx.types.windows_fsrm_configuration.WindowsFsrmConfiguration"
    ]
    """<p>The File Server Resource Manager (FSRM) configuration that Amazon FSx for Windows File Server uses for the file system. FSRM is disabled by default.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateFileSystemWindowsConfiguration) -> dict:
    out: dict = {}
    if "weekly_maintenance_start_time" in value:
        out["WeeklyMaintenanceStartTime"] = value["weekly_maintenance_start_time"]
    if "daily_automatic_backup_start_time" in value:
        out["DailyAutomaticBackupStartTime"] = value[
            "daily_automatic_backup_start_time"
        ]
    if "automatic_backup_retention_days" in value:
        out["AutomaticBackupRetentionDays"] = value["automatic_backup_retention_days"]
    if "throughput_capacity" in value:
        out["ThroughputCapacity"] = value["throughput_capacity"]
    if "self_managed_active_directory_configuration" in value:
        import capo_fsx.types.self_managed_active_directory_configuration_updates

        out["SelfManagedActiveDirectoryConfiguration"] = (
            capo_fsx.types.self_managed_active_directory_configuration_updates.serialize_aws_json_1_1(
                value["self_managed_active_directory_configuration"]
            )
        )
    if "audit_log_configuration" in value:
        import capo_fsx.types.windows_audit_log_create_configuration

        out["AuditLogConfiguration"] = (
            capo_fsx.types.windows_audit_log_create_configuration.serialize_aws_json_1_1(
                value["audit_log_configuration"]
            )
        )
    if "disk_iops_configuration" in value:
        import capo_fsx.types.disk_iops_configuration

        out["DiskIopsConfiguration"] = (
            capo_fsx.types.disk_iops_configuration.serialize_aws_json_1_1(
                value["disk_iops_configuration"]
            )
        )
    if "fsrm_configuration" in value:
        import capo_fsx.types.windows_fsrm_configuration

        out["FsrmConfiguration"] = (
            capo_fsx.types.windows_fsrm_configuration.serialize_aws_json_1_1(
                value["fsrm_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateFileSystemWindowsConfiguration:
    out: UpdateFileSystemWindowsConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("WeeklyMaintenanceStartTime") is not None:
        out["weekly_maintenance_start_time"] = data["WeeklyMaintenanceStartTime"]
    if data.get("DailyAutomaticBackupStartTime") is not None:
        out["daily_automatic_backup_start_time"] = data["DailyAutomaticBackupStartTime"]
    if data.get("AutomaticBackupRetentionDays") is not None:
        out["automatic_backup_retention_days"] = data["AutomaticBackupRetentionDays"]
    if data.get("ThroughputCapacity") is not None:
        out["throughput_capacity"] = data["ThroughputCapacity"]
    if data.get("SelfManagedActiveDirectoryConfiguration") is not None:
        import capo_fsx.types.self_managed_active_directory_configuration_updates

        out["self_managed_active_directory_configuration"] = (
            capo_fsx.types.self_managed_active_directory_configuration_updates.deserialize_aws_json_1_1(
                data["SelfManagedActiveDirectoryConfiguration"]
            )
        )
    if data.get("AuditLogConfiguration") is not None:
        import capo_fsx.types.windows_audit_log_create_configuration

        out["audit_log_configuration"] = (
            capo_fsx.types.windows_audit_log_create_configuration.deserialize_aws_json_1_1(
                data["AuditLogConfiguration"]
            )
        )
    if data.get("DiskIopsConfiguration") is not None:
        import capo_fsx.types.disk_iops_configuration

        out["disk_iops_configuration"] = (
            capo_fsx.types.disk_iops_configuration.deserialize_aws_json_1_1(
                data["DiskIopsConfiguration"]
            )
        )
    if data.get("FsrmConfiguration") is not None:
        import capo_fsx.types.windows_fsrm_configuration

        out["fsrm_configuration"] = (
            capo_fsx.types.windows_fsrm_configuration.deserialize_aws_json_1_1(
                data["FsrmConfiguration"]
            )
        )
    return out
