"""Generated from Smithy shape ``com.amazonaws.fsx#WindowsFileSystemConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.aliases
    import capo_fsx.types.automatic_backup_retention_days
    import capo_fsx.types.daily_time
    import capo_fsx.types.directory_id
    import capo_fsx.types.disk_iops_configuration
    import capo_fsx.types.dns_name
    import capo_fsx.types.file_system_maintenance_operations
    import capo_fsx.types.flag
    import capo_fsx.types.ip_address
    import capo_fsx.types.megabytes_per_second
    import capo_fsx.types.self_managed_active_directory_attributes
    import capo_fsx.types.subnet_id
    import capo_fsx.types.weekly_time
    import capo_fsx.types.windows_audit_log_configuration
    import capo_fsx.types.windows_deployment_type
    import capo_fsx.types.windows_fsrm_configuration


class WindowsFileSystemConfiguration(TypedDict, closed=True):
    active_directory_id: NotRequired["capo_fsx.types.directory_id.DirectoryId"]
    """<p>The ID for an existing Amazon Web Services Managed Microsoft Active Directory instance that the file system is joined to.</p>"""
    self_managed_active_directory_configuration: NotRequired[
        "capo_fsx.types.self_managed_active_directory_attributes.SelfManagedActiveDirectoryAttributes"
    ]
    deployment_type: NotRequired[
        "capo_fsx.types.windows_deployment_type.WindowsDeploymentType"
    ]
    """<p>Specifies the file system deployment type, valid values are the following:</p> <ul> <li> <p> <code>MULTI_AZ_1</code> - Specifies a high availability file system that is configured for Multi-AZ redundancy to tolerate temporary Availability Zone (AZ) unavailability, and supports SSD and HDD storage.</p> </li> <li> <p> <code>SINGLE_AZ_1</code> - (Default) Specifies a file system that is configured for single AZ redundancy, only supports SSD storage.</p> </li> <li> <p> <code>SINGLE_AZ_2</code> - Latest generation Single AZ file system. Specifies a file system that is configured for single AZ redundancy and supports SSD and HDD storage.</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/fsx/latest/WindowsGuide/high-availability-multiAZ.html">Single-AZ and Multi-AZ File Systems</a>.</p>"""
    remote_administration_endpoint: NotRequired["capo_fsx.types.dns_name.DNSName"]
    """<p>For <code>MULTI_AZ_1</code> deployment types, use this endpoint when performing administrative tasks on the file system using Amazon FSx Remote PowerShell.</p> <p>For <code>SINGLE_AZ_1</code> and <code>SINGLE_AZ_2</code> deployment types, this is the DNS name of the file system.</p> <p>This endpoint is temporarily unavailable when the file system is undergoing maintenance.</p>"""
    preferred_subnet_id: NotRequired["capo_fsx.types.subnet_id.SubnetId"]
    """<p>For <code>MULTI_AZ_1</code> deployment types, it specifies the ID of the subnet where the preferred file server is located. Must be one of the two subnet IDs specified in <code>SubnetIds</code> property. Amazon FSx serves traffic from this subnet except in the event of a failover to the secondary file server.</p> <p>For <code>SINGLE_AZ_1</code> and <code>SINGLE_AZ_2</code> deployment types, this value is the same as that for <code>SubnetIDs</code>. For more information, see <a href="https://docs.aws.amazon.com/fsx/latest/WindowsGuide/high-availability-multiAZ.html#single-multi-az-resources">Availability and durability: Single-AZ and Multi-AZ file systems</a>.</p>"""
    preferred_file_server_ip: NotRequired["capo_fsx.types.ip_address.IpAddress"]
    """<p>For <code>MULTI_AZ_1</code> deployment types, the IPv4 address of the primary, or preferred, file server.</p> <p>Use this IP address when mounting the file system on Linux SMB clients or Windows SMB clients that are not joined to a Microsoft Active Directory. Applicable for all Windows file system deployment types. This IPv4 address is temporarily unavailable when the file system is undergoing maintenance. For Linux and Windows SMB clients that are joined to an Active Directory, use the file system's DNSName instead. For more information on mapping and mounting file shares, see <a href="https://docs.aws.amazon.com/fsx/latest/WindowsGuide/using-file-shares.html">Accessing data using file shares</a>.</p>"""
    throughput_capacity: NotRequired[
        "capo_fsx.types.megabytes_per_second.MegabytesPerSecond"
    ]
    """<p>The throughput of the Amazon FSx file system, measured in megabytes per second.</p>"""
    maintenance_operations_in_progress: NotRequired[
        "capo_fsx.types.file_system_maintenance_operations.FileSystemMaintenanceOperations"
    ]
    """<p>The list of maintenance operations in progress for this file system.</p>"""
    weekly_maintenance_start_time: NotRequired["capo_fsx.types.weekly_time.WeeklyTime"]
    """<p>The preferred start time to perform weekly maintenance, formatted d:HH:MM in the UTC time zone. d is the weekday number, from 1 through 7, beginning with Monday and ending with Sunday.</p>"""
    daily_automatic_backup_start_time: NotRequired[
        "capo_fsx.types.daily_time.DailyTime"
    ]
    """<p>The preferred time to take daily automatic backups, in the UTC time zone.</p>"""
    automatic_backup_retention_days: NotRequired[
        "capo_fsx.types.automatic_backup_retention_days.AutomaticBackupRetentionDays"
    ]
    """<p>The number of days to retain automatic backups. Setting this to 0 disables automatic backups. You can retain automatic backups for a maximum of 90 days.</p>"""
    copy_tags_to_backups: NotRequired["capo_fsx.types.flag.Flag"]
    """<p>A boolean flag indicating whether tags on the file system should be copied to backups. This value defaults to false. If it's set to true, all tags on the file system are copied to all automatic backups and any user-initiated backups where the user doesn't specify any tags. If this value is true, and you specify one or more tags, only the specified tags are copied to backups. If you specify one or more tags when creating a user-initiated backup, no tags are copied from the file system, regardless of this value.</p>"""
    aliases: NotRequired["capo_fsx.types.aliases.Aliases"]
    audit_log_configuration: NotRequired[
        "capo_fsx.types.windows_audit_log_configuration.WindowsAuditLogConfiguration"
    ]
    """<p>The configuration that Amazon FSx for Windows File Server uses to audit and log user accesses of files, folders, and file shares on the Amazon FSx for Windows File Server file system.</p>"""
    disk_iops_configuration: NotRequired[
        "capo_fsx.types.disk_iops_configuration.DiskIopsConfiguration"
    ]
    """<p>The SSD IOPS (input/output operations per second) configuration for an Amazon FSx for Windows file system. By default, Amazon FSx automatically provisions 3 IOPS per GiB of storage capacity. You can provision additional IOPS per GiB of storage, up to the maximum limit associated with your chosen throughput capacity.</p>"""
    preferred_file_server_ipv6: NotRequired["capo_fsx.types.ip_address.IpAddress"]
    """<p>For MULTI_AZ_1 deployment types, the IPv6 address of the primary, or preferred, file server. Use this IP address when mounting the file system on Linux SMB clients or Windows SMB clients that are not joined to a Microsoft Active Directory. Applicable for all Windows file system deployment types. This IPv6 address is temporarily unavailable when the file system is undergoing maintenance. For Linux and Windows SMB clients that are joined to an Active Directory, use the file system's DNSName instead.</p>"""
    fsrm_configuration: NotRequired[
        "capo_fsx.types.windows_fsrm_configuration.WindowsFsrmConfiguration"
    ]
    """<p>The File Server Resource Manager (FSRM) configuration that Amazon FSx for Windows File Server uses for the file system. FSRM is disabled by default.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WindowsFileSystemConfiguration) -> dict:
    out: dict = {}
    if "active_directory_id" in value:
        out["ActiveDirectoryId"] = value["active_directory_id"]
    if "self_managed_active_directory_configuration" in value:
        import capo_fsx.types.self_managed_active_directory_attributes

        out["SelfManagedActiveDirectoryConfiguration"] = (
            capo_fsx.types.self_managed_active_directory_attributes.serialize_aws_json_1_1(
                value["self_managed_active_directory_configuration"]
            )
        )
    if "deployment_type" in value:
        import capo_fsx.types.windows_deployment_type

        out["DeploymentType"] = (
            capo_fsx.types.windows_deployment_type.serialize_aws_json_1_1(
                value["deployment_type"]
            )
        )
    if "remote_administration_endpoint" in value:
        out["RemoteAdministrationEndpoint"] = value["remote_administration_endpoint"]
    if "preferred_subnet_id" in value:
        out["PreferredSubnetId"] = value["preferred_subnet_id"]
    if "preferred_file_server_ip" in value:
        out["PreferredFileServerIp"] = value["preferred_file_server_ip"]
    if "throughput_capacity" in value:
        out["ThroughputCapacity"] = value["throughput_capacity"]
    if "maintenance_operations_in_progress" in value:
        import capo_fsx.types.file_system_maintenance_operations

        out["MaintenanceOperationsInProgress"] = (
            capo_fsx.types.file_system_maintenance_operations.serialize_aws_json_1_1(
                value["maintenance_operations_in_progress"]
            )
        )
    if "weekly_maintenance_start_time" in value:
        out["WeeklyMaintenanceStartTime"] = value["weekly_maintenance_start_time"]
    if "daily_automatic_backup_start_time" in value:
        out["DailyAutomaticBackupStartTime"] = value[
            "daily_automatic_backup_start_time"
        ]
    if "automatic_backup_retention_days" in value:
        out["AutomaticBackupRetentionDays"] = value["automatic_backup_retention_days"]
    if "copy_tags_to_backups" in value:
        out["CopyTagsToBackups"] = value["copy_tags_to_backups"]
    if "aliases" in value:
        import capo_fsx.types.aliases

        out["Aliases"] = capo_fsx.types.aliases.serialize_aws_json_1_1(value["aliases"])
    if "audit_log_configuration" in value:
        import capo_fsx.types.windows_audit_log_configuration

        out["AuditLogConfiguration"] = (
            capo_fsx.types.windows_audit_log_configuration.serialize_aws_json_1_1(
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
    if "preferred_file_server_ipv6" in value:
        out["PreferredFileServerIpv6"] = value["preferred_file_server_ipv6"]
    if "fsrm_configuration" in value:
        import capo_fsx.types.windows_fsrm_configuration

        out["FsrmConfiguration"] = (
            capo_fsx.types.windows_fsrm_configuration.serialize_aws_json_1_1(
                value["fsrm_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> WindowsFileSystemConfiguration:
    out: WindowsFileSystemConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("ActiveDirectoryId") is not None:
        out["active_directory_id"] = data["ActiveDirectoryId"]
    if data.get("SelfManagedActiveDirectoryConfiguration") is not None:
        import capo_fsx.types.self_managed_active_directory_attributes

        out["self_managed_active_directory_configuration"] = (
            capo_fsx.types.self_managed_active_directory_attributes.deserialize_aws_json_1_1(
                data["SelfManagedActiveDirectoryConfiguration"]
            )
        )
    if data.get("DeploymentType") is not None:
        import capo_fsx.types.windows_deployment_type

        out["deployment_type"] = (
            capo_fsx.types.windows_deployment_type.deserialize_aws_json_1_1(
                data["DeploymentType"]
            )
        )
    if data.get("RemoteAdministrationEndpoint") is not None:
        out["remote_administration_endpoint"] = data["RemoteAdministrationEndpoint"]
    if data.get("PreferredSubnetId") is not None:
        out["preferred_subnet_id"] = data["PreferredSubnetId"]
    if data.get("PreferredFileServerIp") is not None:
        out["preferred_file_server_ip"] = data["PreferredFileServerIp"]
    if data.get("ThroughputCapacity") is not None:
        out["throughput_capacity"] = data["ThroughputCapacity"]
    if data.get("MaintenanceOperationsInProgress") is not None:
        import capo_fsx.types.file_system_maintenance_operations

        out["maintenance_operations_in_progress"] = (
            capo_fsx.types.file_system_maintenance_operations.deserialize_aws_json_1_1(
                data["MaintenanceOperationsInProgress"]
            )
        )
    if data.get("WeeklyMaintenanceStartTime") is not None:
        out["weekly_maintenance_start_time"] = data["WeeklyMaintenanceStartTime"]
    if data.get("DailyAutomaticBackupStartTime") is not None:
        out["daily_automatic_backup_start_time"] = data["DailyAutomaticBackupStartTime"]
    if data.get("AutomaticBackupRetentionDays") is not None:
        out["automatic_backup_retention_days"] = data["AutomaticBackupRetentionDays"]
    if data.get("CopyTagsToBackups") is not None:
        out["copy_tags_to_backups"] = data["CopyTagsToBackups"]
    if data.get("Aliases") is not None:
        import capo_fsx.types.aliases

        out["aliases"] = capo_fsx.types.aliases.deserialize_aws_json_1_1(
            data["Aliases"]
        )
    if data.get("AuditLogConfiguration") is not None:
        import capo_fsx.types.windows_audit_log_configuration

        out["audit_log_configuration"] = (
            capo_fsx.types.windows_audit_log_configuration.deserialize_aws_json_1_1(
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
    if data.get("PreferredFileServerIpv6") is not None:
        out["preferred_file_server_ipv6"] = data["PreferredFileServerIpv6"]
    if data.get("FsrmConfiguration") is not None:
        import capo_fsx.types.windows_fsrm_configuration

        out["fsrm_configuration"] = (
            capo_fsx.types.windows_fsrm_configuration.deserialize_aws_json_1_1(
                data["FsrmConfiguration"]
            )
        )
    return out
