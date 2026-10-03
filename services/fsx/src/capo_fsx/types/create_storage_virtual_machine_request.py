"""Generated from Smithy shape ``com.amazonaws.fsx#CreateStorageVirtualMachineRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.admin_password
    import capo_fsx.types.client_request_token
    import capo_fsx.types.create_svm_active_directory_configuration
    import capo_fsx.types.file_system_id
    import capo_fsx.types.storage_virtual_machine_name
    import capo_fsx.types.storage_virtual_machine_root_volume_security_style
    import capo_fsx.types.tags


class CreateStorageVirtualMachineRequest(TypedDict, closed=True):
    active_directory_configuration: NotRequired[
        "capo_fsx.types.create_svm_active_directory_configuration.CreateSvmActiveDirectoryConfiguration"
    ]
    """<p>Describes the self-managed Microsoft Active Directory to which you want to join the SVM. Joining an Active Directory provides user authentication and access control for SMB clients, including Microsoft Windows and macOS clients accessing the file system.</p>"""
    client_request_token: NotRequired[
        "capo_fsx.types.client_request_token.ClientRequestToken"
    ]
    file_system_id: NotRequired["capo_fsx.types.file_system_id.FileSystemId"]
    name: NotRequired[
        "capo_fsx.types.storage_virtual_machine_name.StorageVirtualMachineName"
    ]
    """<p>The name of the SVM.</p>"""
    svm_admin_password: NotRequired["capo_fsx.types.admin_password.AdminPassword"]
    """<p>The password to use when managing the SVM using the NetApp ONTAP CLI or REST API. If you do not specify a password, you can still use the file system's <code>fsxadmin</code> user to manage the SVM.</p>"""
    tags: NotRequired["capo_fsx.types.tags.Tags"]
    root_volume_security_style: NotRequired[
        "capo_fsx.types.storage_virtual_machine_root_volume_security_style.StorageVirtualMachineRootVolumeSecurityStyle"
    ]
    """<p>The security style of the root volume of the SVM. Specify one of the following values:</p> <ul> <li> <p> <code>UNIX</code> if the file system is managed by a UNIX administrator, the majority of users are NFS clients, and an application accessing the data uses a UNIX user as the service account.</p> </li> <li> <p> <code>NTFS</code> if the file system is managed by a Microsoft Windows administrator, the majority of users are SMB clients, and an application accessing the data uses a Microsoft Windows user as the service account.</p> </li> <li> <p> <code>MIXED</code> This is an advanced setting. For more information, see <a href="https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/volume-security-style.html">Volume security style</a> in the Amazon FSx for NetApp ONTAP User Guide.</p> </li> </ul> <p></p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateStorageVirtualMachineRequest) -> dict:
    out: dict = {}
    if "active_directory_configuration" in value:
        import capo_fsx.types.create_svm_active_directory_configuration

        out["ActiveDirectoryConfiguration"] = (
            capo_fsx.types.create_svm_active_directory_configuration.serialize_aws_json_1_1(
                value["active_directory_configuration"]
            )
        )
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "file_system_id" in value:
        out["FileSystemId"] = value["file_system_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "svm_admin_password" in value:
        out["SvmAdminPassword"] = value["svm_admin_password"]
    if "tags" in value:
        import capo_fsx.types.tags

        out["Tags"] = capo_fsx.types.tags.serialize_aws_json_1_1(value["tags"])
    if "root_volume_security_style" in value:
        import capo_fsx.types.storage_virtual_machine_root_volume_security_style

        out["RootVolumeSecurityStyle"] = (
            capo_fsx.types.storage_virtual_machine_root_volume_security_style.serialize_aws_json_1_1(
                value["root_volume_security_style"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateStorageVirtualMachineRequest:
    out: CreateStorageVirtualMachineRequest = {}  # type: ignore[typeddict-item]
    if data.get("ActiveDirectoryConfiguration") is not None:
        import capo_fsx.types.create_svm_active_directory_configuration

        out["active_directory_configuration"] = (
            capo_fsx.types.create_svm_active_directory_configuration.deserialize_aws_json_1_1(
                data["ActiveDirectoryConfiguration"]
            )
        )
    if data.get("ClientRequestToken") is not None:
        out["client_request_token"] = data["ClientRequestToken"]
    if data.get("FileSystemId") is not None:
        out["file_system_id"] = data["FileSystemId"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("SvmAdminPassword") is not None:
        out["svm_admin_password"] = data["SvmAdminPassword"]
    if data.get("Tags") is not None:
        import capo_fsx.types.tags

        out["tags"] = capo_fsx.types.tags.deserialize_aws_json_1_1(data["Tags"])
    if data.get("RootVolumeSecurityStyle") is not None:
        import capo_fsx.types.storage_virtual_machine_root_volume_security_style

        out["root_volume_security_style"] = (
            capo_fsx.types.storage_virtual_machine_root_volume_security_style.deserialize_aws_json_1_1(
                data["RootVolumeSecurityStyle"]
            )
        )
    return out
