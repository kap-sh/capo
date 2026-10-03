"""Generated from Smithy shape ``com.amazonaws.fsx#UpdateFileSystemRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.client_request_token
    import capo_fsx.types.file_system_id
    import capo_fsx.types.file_system_type_version
    import capo_fsx.types.network_type
    import capo_fsx.types.storage_capacity
    import capo_fsx.types.storage_type
    import capo_fsx.types.update_file_system_lustre_configuration
    import capo_fsx.types.update_file_system_ontap_configuration
    import capo_fsx.types.update_file_system_open_zfs_configuration
    import capo_fsx.types.update_file_system_windows_configuration


class UpdateFileSystemRequest(TypedDict, closed=True):
    file_system_id: NotRequired["capo_fsx.types.file_system_id.FileSystemId"]
    """<p>The ID of the file system that you are updating.</p>"""
    client_request_token: NotRequired[
        "capo_fsx.types.client_request_token.ClientRequestToken"
    ]
    """<p>A string of up to 63 ASCII characters that Amazon FSx uses to ensure idempotent updates. This string is automatically filled on your behalf when you use the Command Line Interface (CLI) or an Amazon Web Services SDK.</p>"""
    storage_capacity: NotRequired["capo_fsx.types.storage_capacity.StorageCapacity"]
    """<p>Use this parameter to increase the storage capacity of an FSx for Windows File Server, FSx for Lustre, FSx for OpenZFS, or FSx for ONTAP file system. For second-generation FSx for ONTAP file systems, you can also decrease the storage capacity. Specifies the storage capacity target value, in GiB, for the file system that you're updating. </p> <note> <p>You can't make a storage capacity increase request if there is an existing storage capacity increase request in progress.</p> </note> <p>For Lustre file systems, the storage capacity target value can be the following:</p> <ul> <li> <p>For <code>SCRATCH_2</code>, <code>PERSISTENT_1</code>, and <code>PERSISTENT_2 SSD</code> deployment types, valid values are in multiples of 2400 GiB. The value must be greater than the current storage capacity.</p> </li> <li> <p>For <code>PERSISTENT HDD</code> file systems, valid values are multiples of 6000 GiB for 12-MBps throughput per TiB file systems and multiples of 1800 GiB for 40-MBps throughput per TiB file systems. The values must be greater than the current storage capacity.</p> </li> <li> <p>For <code>SCRATCH_1</code> file systems, you can't increase the storage capacity.</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/fsx/latest/LustreGuide/managing-storage-capacity.html">Managing storage and throughput capacity</a> in the <i>FSx for Lustre User Guide</i>.</p> <p>For FSx for OpenZFS file systems, the storage capacity target value must be at least 10 percent greater than the current storage capacity value. For more information, see <a href="https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/managing-storage-capacity.html">Managing storage capacity</a> in the <i>FSx for OpenZFS User Guide</i>.</p> <p>For Windows file systems, the storage capacity target value must be at least 10 percent greater than the current storage capacity value. To increase storage capacity, the file system must have at least 16 MBps of throughput capacity. For more information, see <a href="https://docs.aws.amazon.com/fsx/latest/WindowsGuide/managing-storage-capacity.html">Managing storage capacity</a> in the <i>Amazon FSxfor Windows File Server User Guide</i>.</p> <p>For ONTAP file systems, when increasing storage capacity, the storage capacity target value must be at least 10 percent greater than the current storage capacity value. When decreasing storage capacity on second-generation file systems, the target value must be at least 9 percent smaller than the current SSD storage capacity. For more information, see <a href="https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/storage-capacity-and-IOPS.html">File system storage capacity and IOPS</a> in the Amazon FSx for NetApp ONTAP User Guide.</p>"""
    windows_configuration: NotRequired[
        "capo_fsx.types.update_file_system_windows_configuration.UpdateFileSystemWindowsConfiguration"
    ]
    """<p>The configuration updates for an Amazon FSx for Windows File Server file system.</p>"""
    lustre_configuration: NotRequired[
        "capo_fsx.types.update_file_system_lustre_configuration.UpdateFileSystemLustreConfiguration"
    ]
    ontap_configuration: NotRequired[
        "capo_fsx.types.update_file_system_ontap_configuration.UpdateFileSystemOntapConfiguration"
    ]
    open_zfs_configuration: NotRequired[
        "capo_fsx.types.update_file_system_open_zfs_configuration.UpdateFileSystemOpenZFSConfiguration"
    ]
    """<p>The configuration updates for an FSx for OpenZFS file system.</p>"""
    storage_type: NotRequired["capo_fsx.types.storage_type.StorageType"]
    file_system_type_version: NotRequired[
        "capo_fsx.types.file_system_type_version.FileSystemTypeVersion"
    ]
    """<p>The Lustre version you are updating an FSx for Lustre file system to. Valid values are <code>2.12</code> and <code>2.15</code>. The value you choose must be newer than the file system's current Lustre version.</p>"""
    network_type: NotRequired["capo_fsx.types.network_type.NetworkType"]
    """<p>Changes the network type of an FSx for OpenZFS file system.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateFileSystemRequest) -> dict:
    out: dict = {}
    if "file_system_id" in value:
        out["FileSystemId"] = value["file_system_id"]
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "storage_capacity" in value:
        out["StorageCapacity"] = value["storage_capacity"]
    if "windows_configuration" in value:
        import capo_fsx.types.update_file_system_windows_configuration

        out["WindowsConfiguration"] = (
            capo_fsx.types.update_file_system_windows_configuration.serialize_aws_json_1_1(
                value["windows_configuration"]
            )
        )
    if "lustre_configuration" in value:
        import capo_fsx.types.update_file_system_lustre_configuration

        out["LustreConfiguration"] = (
            capo_fsx.types.update_file_system_lustre_configuration.serialize_aws_json_1_1(
                value["lustre_configuration"]
            )
        )
    if "ontap_configuration" in value:
        import capo_fsx.types.update_file_system_ontap_configuration

        out["OntapConfiguration"] = (
            capo_fsx.types.update_file_system_ontap_configuration.serialize_aws_json_1_1(
                value["ontap_configuration"]
            )
        )
    if "open_zfs_configuration" in value:
        import capo_fsx.types.update_file_system_open_zfs_configuration

        out["OpenZFSConfiguration"] = (
            capo_fsx.types.update_file_system_open_zfs_configuration.serialize_aws_json_1_1(
                value["open_zfs_configuration"]
            )
        )
    if "storage_type" in value:
        import capo_fsx.types.storage_type

        out["StorageType"] = capo_fsx.types.storage_type.serialize_aws_json_1_1(
            value["storage_type"]
        )
    if "file_system_type_version" in value:
        out["FileSystemTypeVersion"] = value["file_system_type_version"]
    if "network_type" in value:
        import capo_fsx.types.network_type

        out["NetworkType"] = capo_fsx.types.network_type.serialize_aws_json_1_1(
            value["network_type"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateFileSystemRequest:
    out: UpdateFileSystemRequest = {}  # type: ignore[typeddict-item]
    if data.get("FileSystemId") is not None:
        out["file_system_id"] = data["FileSystemId"]
    if data.get("ClientRequestToken") is not None:
        out["client_request_token"] = data["ClientRequestToken"]
    if data.get("StorageCapacity") is not None:
        out["storage_capacity"] = data["StorageCapacity"]
    if data.get("WindowsConfiguration") is not None:
        import capo_fsx.types.update_file_system_windows_configuration

        out["windows_configuration"] = (
            capo_fsx.types.update_file_system_windows_configuration.deserialize_aws_json_1_1(
                data["WindowsConfiguration"]
            )
        )
    if data.get("LustreConfiguration") is not None:
        import capo_fsx.types.update_file_system_lustre_configuration

        out["lustre_configuration"] = (
            capo_fsx.types.update_file_system_lustre_configuration.deserialize_aws_json_1_1(
                data["LustreConfiguration"]
            )
        )
    if data.get("OntapConfiguration") is not None:
        import capo_fsx.types.update_file_system_ontap_configuration

        out["ontap_configuration"] = (
            capo_fsx.types.update_file_system_ontap_configuration.deserialize_aws_json_1_1(
                data["OntapConfiguration"]
            )
        )
    if data.get("OpenZFSConfiguration") is not None:
        import capo_fsx.types.update_file_system_open_zfs_configuration

        out["open_zfs_configuration"] = (
            capo_fsx.types.update_file_system_open_zfs_configuration.deserialize_aws_json_1_1(
                data["OpenZFSConfiguration"]
            )
        )
    if data.get("StorageType") is not None:
        import capo_fsx.types.storage_type

        out["storage_type"] = capo_fsx.types.storage_type.deserialize_aws_json_1_1(
            data["StorageType"]
        )
    if data.get("FileSystemTypeVersion") is not None:
        out["file_system_type_version"] = data["FileSystemTypeVersion"]
    if data.get("NetworkType") is not None:
        import capo_fsx.types.network_type

        out["network_type"] = capo_fsx.types.network_type.deserialize_aws_json_1_1(
            data["NetworkType"]
        )
    return out
