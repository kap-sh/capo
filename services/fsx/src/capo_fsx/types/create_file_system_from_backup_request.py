"""Generated from Smithy shape ``com.amazonaws.fsx#CreateFileSystemFromBackupRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.backup_id
    import capo_fsx.types.client_request_token
    import capo_fsx.types.create_file_system_lustre_configuration
    import capo_fsx.types.create_file_system_open_zfs_configuration
    import capo_fsx.types.create_file_system_windows_configuration
    import capo_fsx.types.file_system_type_version
    import capo_fsx.types.kms_key_id
    import capo_fsx.types.network_type
    import capo_fsx.types.security_group_ids
    import capo_fsx.types.storage_capacity
    import capo_fsx.types.storage_type
    import capo_fsx.types.subnet_ids
    import capo_fsx.types.tags


class CreateFileSystemFromBackupRequest(TypedDict, closed=True):
    backup_id: NotRequired["capo_fsx.types.backup_id.BackupId"]
    client_request_token: NotRequired[
        "capo_fsx.types.client_request_token.ClientRequestToken"
    ]
    """<p>A string of up to 63 ASCII characters that Amazon FSx uses to ensure idempotent creation. This string is automatically filled on your behalf when you use the Command Line Interface (CLI) or an Amazon Web Services SDK.</p>"""
    subnet_ids: NotRequired["capo_fsx.types.subnet_ids.SubnetIds"]
    """<p>Specifies the IDs of the subnets that the file system will be accessible from. For Windows <code>MULTI_AZ_1</code> file system deployment types, provide exactly two subnet IDs, one for the preferred file server and one for the standby file server. You specify one of these subnets as the preferred subnet using the <code>WindowsConfiguration > PreferredSubnetID</code> property.</p> <p>Windows <code>SINGLE_AZ_1</code> and <code>SINGLE_AZ_2</code> file system deployment types, Lustre file systems, and OpenZFS file systems provide exactly one subnet ID. The file server is launched in that subnet's Availability Zone.</p>"""
    security_group_ids: NotRequired[
        "capo_fsx.types.security_group_ids.SecurityGroupIds"
    ]
    """<p>A list of IDs for the security groups that apply to the specified network interfaces created for file system access. These security groups apply to all network interfaces. This value isn't returned in later <code>DescribeFileSystem</code> requests.</p>"""
    tags: NotRequired["capo_fsx.types.tags.Tags"]
    """<p>The tags to be applied to the file system at file system creation. The key value of the <code>Name</code> tag appears in the console as the file system name.</p>"""
    windows_configuration: NotRequired[
        "capo_fsx.types.create_file_system_windows_configuration.CreateFileSystemWindowsConfiguration"
    ]
    """<p>The configuration for this Microsoft Windows file system.</p>"""
    lustre_configuration: NotRequired[
        "capo_fsx.types.create_file_system_lustre_configuration.CreateFileSystemLustreConfiguration"
    ]
    storage_type: NotRequired["capo_fsx.types.storage_type.StorageType"]
    """<p>Sets the storage type for the Windows, OpenZFS, or Lustre file system that you're creating from a backup. Valid values are <code>SSD</code>, <code>HDD</code>, and <code>INTELLIGENT_TIERING</code>.</p> <ul> <li> <p>Set to <code>SSD</code> to use solid state drive storage. SSD is supported on all Windows and OpenZFS deployment types.</p> </li> <li> <p>Set to <code>HDD</code> to use hard disk drive storage. HDD is supported on <code>SINGLE_AZ_2</code> and <code>MULTI_AZ_1</code> FSx for Windows File Server file system deployment types.</p> </li> <li> <p>Set to <code>INTELLIGENT_TIERING</code> to use fully elastic, intelligently-tiered storage. Intelligent-Tiering is only available for OpenZFS file systems with the Multi-AZ deployment type and for Lustre file systems with the Persistent_2 deployment type.</p> </li> </ul> <p> The default value is <code>SSD</code>. </p> <note> <p>HDD and SSD storage types have different minimum storage capacity requirements. A restored file system's storage capacity is tied to the file system that was backed up. You can create a file system that uses HDD storage from a backup of a file system that used SSD storage if the original SSD file system had a storage capacity of at least 2000 GiB.</p> </note>"""
    kms_key_id: NotRequired["capo_fsx.types.kms_key_id.KmsKeyId"]
    file_system_type_version: NotRequired[
        "capo_fsx.types.file_system_type_version.FileSystemTypeVersion"
    ]
    """<p>Sets the version for the Amazon FSx for Lustre file system that you're creating from a backup. Valid values are <code>2.10</code>, <code>2.12</code>, and <code>2.15</code>.</p> <p>You can enter a Lustre version that is newer than the backup's <code>FileSystemTypeVersion</code> setting. If you don't enter a newer Lustre version, it defaults to the backup's setting.</p>"""
    open_zfs_configuration: NotRequired[
        "capo_fsx.types.create_file_system_open_zfs_configuration.CreateFileSystemOpenZFSConfiguration"
    ]
    """<p>The OpenZFS configuration for the file system that's being created. </p>"""
    storage_capacity: NotRequired["capo_fsx.types.storage_capacity.StorageCapacity"]
    """<p>Sets the storage capacity of the OpenZFS file system that you're creating from a backup, in gibibytes (GiB). Valid values are from 64 GiB up to 524,288 GiB (512 TiB). However, the value that you specify must be equal to or greater than the backup's storage capacity value. If you don't use the <code>StorageCapacity</code> parameter, the default is the backup's <code>StorageCapacity</code> value.</p> <p>If used to create a file system other than OpenZFS, you must provide a value that matches the backup's <code>StorageCapacity</code> value. If you provide any other value, Amazon FSx responds with an HTTP status code 400 Bad Request. </p>"""
    network_type: NotRequired["capo_fsx.types.network_type.NetworkType"]
    """<p>Sets the network type for the Amazon FSx for OpenZFS file system that you're creating from a backup.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateFileSystemFromBackupRequest) -> dict:
    out: dict = {}
    if "backup_id" in value:
        out["BackupId"] = value["backup_id"]
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "subnet_ids" in value:
        import capo_fsx.types.subnet_ids

        out["SubnetIds"] = capo_fsx.types.subnet_ids.serialize_aws_json_1_1(
            value["subnet_ids"]
        )
    if "security_group_ids" in value:
        import capo_fsx.types.security_group_ids

        out["SecurityGroupIds"] = (
            capo_fsx.types.security_group_ids.serialize_aws_json_1_1(
                value["security_group_ids"]
            )
        )
    if "tags" in value:
        import capo_fsx.types.tags

        out["Tags"] = capo_fsx.types.tags.serialize_aws_json_1_1(value["tags"])
    if "windows_configuration" in value:
        import capo_fsx.types.create_file_system_windows_configuration

        out["WindowsConfiguration"] = (
            capo_fsx.types.create_file_system_windows_configuration.serialize_aws_json_1_1(
                value["windows_configuration"]
            )
        )
    if "lustre_configuration" in value:
        import capo_fsx.types.create_file_system_lustre_configuration

        out["LustreConfiguration"] = (
            capo_fsx.types.create_file_system_lustre_configuration.serialize_aws_json_1_1(
                value["lustre_configuration"]
            )
        )
    if "storage_type" in value:
        import capo_fsx.types.storage_type

        out["StorageType"] = capo_fsx.types.storage_type.serialize_aws_json_1_1(
            value["storage_type"]
        )
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "file_system_type_version" in value:
        out["FileSystemTypeVersion"] = value["file_system_type_version"]
    if "open_zfs_configuration" in value:
        import capo_fsx.types.create_file_system_open_zfs_configuration

        out["OpenZFSConfiguration"] = (
            capo_fsx.types.create_file_system_open_zfs_configuration.serialize_aws_json_1_1(
                value["open_zfs_configuration"]
            )
        )
    if "storage_capacity" in value:
        out["StorageCapacity"] = value["storage_capacity"]
    if "network_type" in value:
        import capo_fsx.types.network_type

        out["NetworkType"] = capo_fsx.types.network_type.serialize_aws_json_1_1(
            value["network_type"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateFileSystemFromBackupRequest:
    out: CreateFileSystemFromBackupRequest = {}  # type: ignore[typeddict-item]
    if data.get("BackupId") is not None:
        out["backup_id"] = data["BackupId"]
    if data.get("ClientRequestToken") is not None:
        out["client_request_token"] = data["ClientRequestToken"]
    if data.get("SubnetIds") is not None:
        import capo_fsx.types.subnet_ids

        out["subnet_ids"] = capo_fsx.types.subnet_ids.deserialize_aws_json_1_1(
            data["SubnetIds"]
        )
    if data.get("SecurityGroupIds") is not None:
        import capo_fsx.types.security_group_ids

        out["security_group_ids"] = (
            capo_fsx.types.security_group_ids.deserialize_aws_json_1_1(
                data["SecurityGroupIds"]
            )
        )
    if data.get("Tags") is not None:
        import capo_fsx.types.tags

        out["tags"] = capo_fsx.types.tags.deserialize_aws_json_1_1(data["Tags"])
    if data.get("WindowsConfiguration") is not None:
        import capo_fsx.types.create_file_system_windows_configuration

        out["windows_configuration"] = (
            capo_fsx.types.create_file_system_windows_configuration.deserialize_aws_json_1_1(
                data["WindowsConfiguration"]
            )
        )
    if data.get("LustreConfiguration") is not None:
        import capo_fsx.types.create_file_system_lustre_configuration

        out["lustre_configuration"] = (
            capo_fsx.types.create_file_system_lustre_configuration.deserialize_aws_json_1_1(
                data["LustreConfiguration"]
            )
        )
    if data.get("StorageType") is not None:
        import capo_fsx.types.storage_type

        out["storage_type"] = capo_fsx.types.storage_type.deserialize_aws_json_1_1(
            data["StorageType"]
        )
    if data.get("KmsKeyId") is not None:
        out["kms_key_id"] = data["KmsKeyId"]
    if data.get("FileSystemTypeVersion") is not None:
        out["file_system_type_version"] = data["FileSystemTypeVersion"]
    if data.get("OpenZFSConfiguration") is not None:
        import capo_fsx.types.create_file_system_open_zfs_configuration

        out["open_zfs_configuration"] = (
            capo_fsx.types.create_file_system_open_zfs_configuration.deserialize_aws_json_1_1(
                data["OpenZFSConfiguration"]
            )
        )
    if data.get("StorageCapacity") is not None:
        out["storage_capacity"] = data["StorageCapacity"]
    if data.get("NetworkType") is not None:
        import capo_fsx.types.network_type

        out["network_type"] = capo_fsx.types.network_type.deserialize_aws_json_1_1(
            data["NetworkType"]
        )
    return out


def redact_sensitive(value: CreateFileSystemFromBackupRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "windows_configuration" in value:
        import capo_fsx.types.create_file_system_windows_configuration

        out["windows_configuration"] = (
            capo_fsx.types.create_file_system_windows_configuration.redact_sensitive(
                value["windows_configuration"]
            )
        )
    return out
