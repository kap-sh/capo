"""Generated from Smithy shape ``com.amazonaws.fsx#CreateFileSystemWindowsConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.alternate_dns_names
    import capo_fsx.types.automatic_backup_retention_days
    import capo_fsx.types.daily_time
    import capo_fsx.types.directory_id
    import capo_fsx.types.disk_iops_configuration
    import capo_fsx.types.flag
    import capo_fsx.types.megabytes_per_second
    import capo_fsx.types.self_managed_active_directory_configuration
    import capo_fsx.types.subnet_id
    import capo_fsx.types.weekly_time
    import capo_fsx.types.windows_audit_log_create_configuration
    import capo_fsx.types.windows_deployment_type
    import capo_fsx.types.windows_fsrm_configuration


class CreateFileSystemWindowsConfiguration(TypedDict, closed=True):
    active_directory_id: NotRequired["capo_fsx.types.directory_id.DirectoryId"]
    """<p>The ID for an existing Amazon Web Services Managed Microsoft Active Directory (AD) instance that the file system should join when it's created.</p>"""
    self_managed_active_directory_configuration: NotRequired[
        "capo_fsx.types.self_managed_active_directory_configuration.SelfManagedActiveDirectoryConfiguration"
    ]
    deployment_type: NotRequired[
        "capo_fsx.types.windows_deployment_type.WindowsDeploymentType"
    ]
    """<p>Specifies the file system deployment type, valid values are the following:</p> <ul> <li> <p> <code>MULTI_AZ_1</code> - Deploys a high availability file system that is configured for Multi-AZ redundancy to tolerate temporary Availability Zone (AZ) unavailability. You can only deploy a Multi-AZ file system in Amazon Web Services Regions that have a minimum of three Availability Zones. Also supports HDD storage type</p> </li> <li> <p> <code>SINGLE_AZ_1</code> - (Default) Choose to deploy a file system that is configured for single AZ redundancy.</p> </li> <li> <p> <code>SINGLE_AZ_2</code> - The latest generation Single AZ file system. Specifies a file system that is configured for single AZ redundancy and supports HDD storage type.</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/fsx/latest/WindowsGuide/high-availability-multiAZ.html"> Availability and Durability: Single-AZ and Multi-AZ File Systems</a>.</p>"""
    preferred_subnet_id: NotRequired["capo_fsx.types.subnet_id.SubnetId"]
    """<p>Required when <code>DeploymentType</code> is set to <code>MULTI_AZ_1</code>. This specifies the subnet in which you want the preferred file server to be located. For in-Amazon Web Services applications, we recommend that you launch your clients in the same Availability Zone (AZ) as your preferred file server to reduce cross-AZ data transfer costs and minimize latency. </p>"""
    throughput_capacity: NotRequired[
        "capo_fsx.types.megabytes_per_second.MegabytesPerSecond"
    ]
    """<p>Sets the throughput capacity of an Amazon FSx file system, measured in megabytes per second (MB/s), in 2 to the <i>n</i>th increments, between 2^3 (8) and 2^11 (2048).</p>"""
    weekly_maintenance_start_time: NotRequired["capo_fsx.types.weekly_time.WeeklyTime"]
    """<p>The preferred start time to perform weekly maintenance, formatted d:HH:MM in the UTC time zone, where d is the weekday number, from 1 through 7, beginning with Monday and ending with Sunday.</p>"""
    daily_automatic_backup_start_time: NotRequired[
        "capo_fsx.types.daily_time.DailyTime"
    ]
    """<p>The preferred time to take daily automatic backups, formatted HH:MM in the UTC time zone.</p>"""
    automatic_backup_retention_days: NotRequired[
        "capo_fsx.types.automatic_backup_retention_days.AutomaticBackupRetentionDays"
    ]
    """<p>The number of days to retain automatic backups. Setting this property to <code>0</code> disables automatic backups. You can retain automatic backups for a maximum of 90 days. The default is <code>30</code>.</p>"""
    copy_tags_to_backups: NotRequired["capo_fsx.types.flag.Flag"]
    """<p>A boolean flag indicating whether tags for the file system should be copied to backups. This value defaults to false. If it's set to true, all tags for the file system are copied to all automatic and user-initiated backups where the user doesn't specify tags. If this value is true, and you specify one or more tags, only the specified tags are copied to backups. If you specify one or more tags when creating a user-initiated backup, no tags are copied from the file system, regardless of this value.</p>"""
    aliases: NotRequired["capo_fsx.types.alternate_dns_names.AlternateDNSNames"]
    """<p>An array of one or more DNS alias names that you want to associate with the Amazon FSx file system. Aliases allow you to use existing DNS names to access the data in your Amazon FSx file system. You can associate up to 50 aliases with a file system at any time. You can associate additional DNS aliases after you create the file system using the AssociateFileSystemAliases operation. You can remove DNS aliases from the file system after it is created using the DisassociateFileSystemAliases operation. You only need to specify the alias name in the request payload. For more information, see <a href="https://docs.aws.amazon.com/fsx/latest/WindowsGuide/managing-dns-aliases.html">Managing DNS aliases</a> and <a href="https://docs.aws.amazon.com/fsx/latest/WindowsGuide/dns-aliases.html">Accessing data using DNS aliases</a>.</p> <p>An alias name has to meet the following requirements:</p> <ul> <li> <p>Formatted as a fully-qualified domain name (FQDN), <code>hostname.domain</code>, for example, <code>accounting.example.com</code>.</p> </li> <li> <p>Can contain alphanumeric characters, the underscore (_), and the hyphen (-).</p> </li> <li> <p>Cannot start or end with a hyphen.</p> </li> <li> <p>Can start with a numeric.</p> </li> </ul> <p>For DNS alias names, Amazon FSx stores alphabetic characters as lowercase letters (a-z), regardless of how you specify them: as uppercase letters, lowercase letters, or the corresponding letters in escape codes.</p>"""
    audit_log_configuration: NotRequired[
        "capo_fsx.types.windows_audit_log_create_configuration.WindowsAuditLogCreateConfiguration"
    ]
    """<p>The configuration that Amazon FSx for Windows File Server uses to audit and log user accesses of files, folders, and file shares on the Amazon FSx for Windows File Server file system.</p>"""
    disk_iops_configuration: NotRequired[
        "capo_fsx.types.disk_iops_configuration.DiskIopsConfiguration"
    ]
    """<p>The SSD IOPS (input/output operations per second) configuration for an Amazon FSx for Windows file system. By default, Amazon FSx automatically provisions 3 IOPS per GiB of storage capacity. You can provision additional IOPS per GiB of storage, up to the maximum limit associated with your chosen throughput capacity.</p>"""
    fsrm_configuration: NotRequired[
        "capo_fsx.types.windows_fsrm_configuration.WindowsFsrmConfiguration"
    ]
    """<p>The File Server Resource Manager (FSRM) configuration that Amazon FSx for Windows File Server uses for the file system. FSRM is disabled by default.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateFileSystemWindowsConfiguration) -> dict:
    out: dict = {}
    if "active_directory_id" in value:
        out["ActiveDirectoryId"] = value["active_directory_id"]
    if "self_managed_active_directory_configuration" in value:
        import capo_fsx.types.self_managed_active_directory_configuration

        out["SelfManagedActiveDirectoryConfiguration"] = (
            capo_fsx.types.self_managed_active_directory_configuration.serialize_aws_json_1_1(
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
    if "preferred_subnet_id" in value:
        out["PreferredSubnetId"] = value["preferred_subnet_id"]
    if "throughput_capacity" in value:
        out["ThroughputCapacity"] = value["throughput_capacity"]
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
        import capo_fsx.types.alternate_dns_names

        out["Aliases"] = capo_fsx.types.alternate_dns_names.serialize_aws_json_1_1(
            value["aliases"]
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


def deserialize_aws_json_1_1(data: dict) -> CreateFileSystemWindowsConfiguration:
    out: CreateFileSystemWindowsConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("ActiveDirectoryId") is not None:
        out["active_directory_id"] = data["ActiveDirectoryId"]
    if data.get("SelfManagedActiveDirectoryConfiguration") is not None:
        import capo_fsx.types.self_managed_active_directory_configuration

        out["self_managed_active_directory_configuration"] = (
            capo_fsx.types.self_managed_active_directory_configuration.deserialize_aws_json_1_1(
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
    if data.get("PreferredSubnetId") is not None:
        out["preferred_subnet_id"] = data["PreferredSubnetId"]
    if data.get("ThroughputCapacity") is not None:
        out["throughput_capacity"] = data["ThroughputCapacity"]
    if data.get("WeeklyMaintenanceStartTime") is not None:
        out["weekly_maintenance_start_time"] = data["WeeklyMaintenanceStartTime"]
    if data.get("DailyAutomaticBackupStartTime") is not None:
        out["daily_automatic_backup_start_time"] = data["DailyAutomaticBackupStartTime"]
    if data.get("AutomaticBackupRetentionDays") is not None:
        out["automatic_backup_retention_days"] = data["AutomaticBackupRetentionDays"]
    if data.get("CopyTagsToBackups") is not None:
        out["copy_tags_to_backups"] = data["CopyTagsToBackups"]
    if data.get("Aliases") is not None:
        import capo_fsx.types.alternate_dns_names

        out["aliases"] = capo_fsx.types.alternate_dns_names.deserialize_aws_json_1_1(
            data["Aliases"]
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
