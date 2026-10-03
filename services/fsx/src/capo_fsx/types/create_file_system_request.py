"""Generated from Smithy shape ``com.amazonaws.fsx#CreateFileSystemRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.client_request_token
    import capo_fsx.types.create_file_system_lustre_configuration
    import capo_fsx.types.create_file_system_ontap_configuration
    import capo_fsx.types.create_file_system_open_zfs_configuration
    import capo_fsx.types.create_file_system_windows_configuration
    import capo_fsx.types.file_system_type
    import capo_fsx.types.file_system_type_version
    import capo_fsx.types.kms_key_id
    import capo_fsx.types.network_type
    import capo_fsx.types.security_group_ids
    import capo_fsx.types.storage_capacity
    import capo_fsx.types.storage_type
    import capo_fsx.types.subnet_ids
    import capo_fsx.types.tags


class CreateFileSystemRequest(TypedDict, closed=True):
    client_request_token: NotRequired[
        "capo_fsx.types.client_request_token.ClientRequestToken"
    ]
    """<p>A string of up to 63 ASCII characters that Amazon FSx uses to ensure idempotent creation. This string is automatically filled on your behalf when you use the Command Line Interface (CLI) or an Amazon Web Services SDK.</p>"""
    file_system_type: NotRequired["capo_fsx.types.file_system_type.FileSystemType"]
    """<p>The type of Amazon FSx file system to create. Valid values are <code>WINDOWS</code>, <code>LUSTRE</code>, <code>ONTAP</code>, and <code>OPENZFS</code>.</p>"""
    storage_capacity: NotRequired["capo_fsx.types.storage_capacity.StorageCapacity"]
    """<p>Sets the storage capacity of the file system that you're creating, in gibibytes (GiB).</p> <p> <b>FSx for Lustre file systems</b> - The amount of storage capacity that you can configure depends on the value that you set for <code>StorageType</code> and the Lustre <code>DeploymentType</code>, as follows:</p> <ul> <li> <p>For <code>SCRATCH_2</code>, <code>PERSISTENT_2</code>, and <code>PERSISTENT_1</code> deployment types using SSD storage type, the valid values are 1200 GiB, 2400 GiB, and increments of 2400 GiB.</p> </li> <li> <p>For <code>PERSISTENT_1</code> HDD file systems, valid values are increments of 6000 GiB for 12 MB/s/TiB file systems and increments of 1800 GiB for 40 MB/s/TiB file systems.</p> </li> <li> <p>For <code>SCRATCH_1</code> deployment type, valid values are 1200 GiB, 2400 GiB, and increments of 3600 GiB.</p> </li> </ul> <p> <b>FSx for ONTAP file systems</b> - The amount of storage capacity that you can configure depends on the value of the <code>HAPairs</code> property. The minimum value is calculated as 1,024 * <code>HAPairs</code> and the maximum is calculated as 524,288 * <code>HAPairs</code>. </p> <p> <b>FSx for OpenZFS file systems</b> - The amount of storage capacity that you can configure is from 64 GiB up to 524,288 GiB (512 TiB).</p> <p> <b>FSx for Windows File Server file systems</b> - The amount of storage capacity that you can configure depends on the value that you set for <code>StorageType</code> as follows:</p> <ul> <li> <p>For SSD storage, valid values are 32 GiB-65,536 GiB (64 TiB).</p> </li> <li> <p>For HDD storage, valid values are 2000 GiB-65,536 GiB (64 TiB).</p> </li> </ul>"""
    storage_type: NotRequired["capo_fsx.types.storage_type.StorageType"]
    """<p>Sets the storage class for the file system that you're creating. Valid values are <code>SSD</code>, <code>HDD</code>, and <code>INTELLIGENT_TIERING</code>.</p> <ul> <li> <p>Set to <code>SSD</code> to use solid state drive storage. SSD is supported on all Windows, Lustre, ONTAP, and OpenZFS deployment types.</p> </li> <li> <p>Set to <code>HDD</code> to use hard disk drive storage, which is supported on <code>SINGLE_AZ_2</code> and <code>MULTI_AZ_1</code> Windows file system deployment types, and on <code>PERSISTENT_1</code> Lustre file system deployment types.</p> </li> <li> <p>Set to <code>INTELLIGENT_TIERING</code> to use fully elastic, intelligently-tiered storage. Intelligent-Tiering is only available for OpenZFS file systems with the Multi-AZ deployment type and for Lustre file systems with the Persistent_2 deployment type.</p> </li> </ul> <p>Default value is <code>SSD</code>. For more information, see <a href="https://docs.aws.amazon.com/fsx/latest/WindowsGuide/optimize-fsx-costs.html#storage-type-options"> Storage type options</a> in the <i>FSx for Windows File Server User Guide</i>, <a href="https://docs.aws.amazon.com/fsx/latest/LustreGuide/using-fsx-lustre.html#lustre-storage-classes">FSx for Lustre storage classes</a> in the <i>FSx for Lustre User Guide</i>, and <a href="https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/performance-intelligent-tiering">Working with Intelligent-Tiering</a> in the <i>Amazon FSx for OpenZFS User Guide</i>.</p>"""
    subnet_ids: NotRequired["capo_fsx.types.subnet_ids.SubnetIds"]
    """<p>Specifies the IDs of the subnets that the file system will be accessible from. For Windows and ONTAP <code>MULTI_AZ_1</code> deployment types,provide exactly two subnet IDs, one for the preferred file server and one for the standby file server. You specify one of these subnets as the preferred subnet using the <code>WindowsConfiguration > PreferredSubnetID</code> or <code>OntapConfiguration > PreferredSubnetID</code> properties. For more information about Multi-AZ file system configuration, see <a href="https://docs.aws.amazon.com/fsx/latest/WindowsGuide/high-availability-multiAZ.html"> Availability and durability: Single-AZ and Multi-AZ file systems</a> in the <i>Amazon FSx for Windows User Guide</i> and <a href="https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/high-availability-multiAZ.html"> Availability and durability</a> in the <i>Amazon FSx for ONTAP User Guide</i>.</p> <p>For Windows <code>SINGLE_AZ_1</code> and <code>SINGLE_AZ_2</code> and all Lustre deployment types, provide exactly one subnet ID. The file server is launched in that subnet's Availability Zone.</p>"""
    security_group_ids: NotRequired[
        "capo_fsx.types.security_group_ids.SecurityGroupIds"
    ]
    """<p>A list of IDs specifying the security groups to apply to all network interfaces created for file system access. This list isn't returned in later requests to describe the file system.</p> <important> <p>You must specify a security group if you are creating a Multi-AZ FSx for ONTAP file system in a VPC subnet that has been shared with you.</p> </important>"""
    tags: NotRequired["capo_fsx.types.tags.Tags"]
    """<p>The tags to apply to the file system that's being created. The key value of the <code>Name</code> tag appears in the console as the file system name.</p>"""
    kms_key_id: NotRequired["capo_fsx.types.kms_key_id.KmsKeyId"]
    windows_configuration: NotRequired[
        "capo_fsx.types.create_file_system_windows_configuration.CreateFileSystemWindowsConfiguration"
    ]
    """<p>The Microsoft Windows configuration for the file system that's being created.</p>"""
    lustre_configuration: NotRequired[
        "capo_fsx.types.create_file_system_lustre_configuration.CreateFileSystemLustreConfiguration"
    ]
    ontap_configuration: NotRequired[
        "capo_fsx.types.create_file_system_ontap_configuration.CreateFileSystemOntapConfiguration"
    ]
    file_system_type_version: NotRequired[
        "capo_fsx.types.file_system_type_version.FileSystemTypeVersion"
    ]
    """<p>For FSx for Lustre file systems, sets the Lustre version for the file system that you're creating. Valid values are <code>2.10</code>, <code>2.12</code>, and <code>2.15</code>:</p> <ul> <li> <p> <code>2.10</code> is supported by the Scratch and Persistent_1 Lustre deployment types.</p> </li> <li> <p> <code>2.12</code> is supported by all Lustre deployment types, except for <code>PERSISTENT_2</code> with a metadata configuration mode.</p> </li> <li> <p> <code>2.15</code> is supported by all Lustre deployment types and is recommended for all new file systems.</p> </li> </ul> <p>Default value is <code>2.10</code>, except for the following deployments:</p> <ul> <li> <p>Default value is <code>2.12</code> when <code>DeploymentType</code> is set to <code>PERSISTENT_2</code> without a metadata configuration mode.</p> </li> <li> <p>Default value is <code>2.15</code> when <code>DeploymentType</code> is set to <code>PERSISTENT_2</code> with a metadata configuration mode.</p> </li> </ul>"""
    open_zfs_configuration: NotRequired[
        "capo_fsx.types.create_file_system_open_zfs_configuration.CreateFileSystemOpenZFSConfiguration"
    ]
    """<p>The OpenZFS configuration for the file system that's being created.</p>"""
    network_type: NotRequired["capo_fsx.types.network_type.NetworkType"]
    """<p>The network type of the Amazon FSx file system that you are creating. Valid values are <code>IPV4</code> (which supports IPv4 only) and <code>DUAL</code> (for dual-stack mode, which supports both IPv4 and IPv6). The default is <code>IPV4</code>. Supported for FSx for OpenZFS, FSx for ONTAP, and FSx for Windows File Server file systems.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateFileSystemRequest) -> dict:
    out: dict = {}
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "file_system_type" in value:
        import capo_fsx.types.file_system_type

        out["FileSystemType"] = capo_fsx.types.file_system_type.serialize_aws_json_1_1(
            value["file_system_type"]
        )
    if "storage_capacity" in value:
        out["StorageCapacity"] = value["storage_capacity"]
    if "storage_type" in value:
        import capo_fsx.types.storage_type

        out["StorageType"] = capo_fsx.types.storage_type.serialize_aws_json_1_1(
            value["storage_type"]
        )
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
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
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
    if "ontap_configuration" in value:
        import capo_fsx.types.create_file_system_ontap_configuration

        out["OntapConfiguration"] = (
            capo_fsx.types.create_file_system_ontap_configuration.serialize_aws_json_1_1(
                value["ontap_configuration"]
            )
        )
    if "file_system_type_version" in value:
        out["FileSystemTypeVersion"] = value["file_system_type_version"]
    if "open_zfs_configuration" in value:
        import capo_fsx.types.create_file_system_open_zfs_configuration

        out["OpenZFSConfiguration"] = (
            capo_fsx.types.create_file_system_open_zfs_configuration.serialize_aws_json_1_1(
                value["open_zfs_configuration"]
            )
        )
    if "network_type" in value:
        import capo_fsx.types.network_type

        out["NetworkType"] = capo_fsx.types.network_type.serialize_aws_json_1_1(
            value["network_type"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateFileSystemRequest:
    out: CreateFileSystemRequest = {}  # type: ignore[typeddict-item]
    if data.get("ClientRequestToken") is not None:
        out["client_request_token"] = data["ClientRequestToken"]
    if data.get("FileSystemType") is not None:
        import capo_fsx.types.file_system_type

        out["file_system_type"] = (
            capo_fsx.types.file_system_type.deserialize_aws_json_1_1(
                data["FileSystemType"]
            )
        )
    if data.get("StorageCapacity") is not None:
        out["storage_capacity"] = data["StorageCapacity"]
    if data.get("StorageType") is not None:
        import capo_fsx.types.storage_type

        out["storage_type"] = capo_fsx.types.storage_type.deserialize_aws_json_1_1(
            data["StorageType"]
        )
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
    if data.get("KmsKeyId") is not None:
        out["kms_key_id"] = data["KmsKeyId"]
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
    if data.get("OntapConfiguration") is not None:
        import capo_fsx.types.create_file_system_ontap_configuration

        out["ontap_configuration"] = (
            capo_fsx.types.create_file_system_ontap_configuration.deserialize_aws_json_1_1(
                data["OntapConfiguration"]
            )
        )
    if data.get("FileSystemTypeVersion") is not None:
        out["file_system_type_version"] = data["FileSystemTypeVersion"]
    if data.get("OpenZFSConfiguration") is not None:
        import capo_fsx.types.create_file_system_open_zfs_configuration

        out["open_zfs_configuration"] = (
            capo_fsx.types.create_file_system_open_zfs_configuration.deserialize_aws_json_1_1(
                data["OpenZFSConfiguration"]
            )
        )
    if data.get("NetworkType") is not None:
        import capo_fsx.types.network_type

        out["network_type"] = capo_fsx.types.network_type.deserialize_aws_json_1_1(
            data["NetworkType"]
        )
    return out
