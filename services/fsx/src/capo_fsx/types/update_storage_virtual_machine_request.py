"""Generated from Smithy shape ``com.amazonaws.fsx#UpdateStorageVirtualMachineRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.admin_password
    import capo_fsx.types.client_request_token
    import capo_fsx.types.storage_virtual_machine_id
    import capo_fsx.types.update_svm_active_directory_configuration


class UpdateStorageVirtualMachineRequest(TypedDict, closed=True):
    active_directory_configuration: NotRequired[
        "capo_fsx.types.update_svm_active_directory_configuration.UpdateSvmActiveDirectoryConfiguration"
    ]
    """<p>Specifies updates to an SVM's Microsoft Active Directory (AD) configuration.</p>"""
    client_request_token: NotRequired[
        "capo_fsx.types.client_request_token.ClientRequestToken"
    ]
    storage_virtual_machine_id: NotRequired[
        "capo_fsx.types.storage_virtual_machine_id.StorageVirtualMachineId"
    ]
    """<p>The ID of the SVM that you want to update, in the format <code>svm-0123456789abcdef0</code>.</p>"""
    svm_admin_password: NotRequired["capo_fsx.types.admin_password.AdminPassword"]
    """<p>Specifies a new SvmAdminPassword.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateStorageVirtualMachineRequest) -> dict:
    out: dict = {}
    if "active_directory_configuration" in value:
        import capo_fsx.types.update_svm_active_directory_configuration

        out["ActiveDirectoryConfiguration"] = (
            capo_fsx.types.update_svm_active_directory_configuration.serialize_aws_json_1_1(
                value["active_directory_configuration"]
            )
        )
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "storage_virtual_machine_id" in value:
        out["StorageVirtualMachineId"] = value["storage_virtual_machine_id"]
    if "svm_admin_password" in value:
        out["SvmAdminPassword"] = value["svm_admin_password"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateStorageVirtualMachineRequest:
    out: UpdateStorageVirtualMachineRequest = {}  # type: ignore[typeddict-item]
    if data.get("ActiveDirectoryConfiguration") is not None:
        import capo_fsx.types.update_svm_active_directory_configuration

        out["active_directory_configuration"] = (
            capo_fsx.types.update_svm_active_directory_configuration.deserialize_aws_json_1_1(
                data["ActiveDirectoryConfiguration"]
            )
        )
    if data.get("ClientRequestToken") is not None:
        out["client_request_token"] = data["ClientRequestToken"]
    if data.get("StorageVirtualMachineId") is not None:
        out["storage_virtual_machine_id"] = data["StorageVirtualMachineId"]
    if data.get("SvmAdminPassword") is not None:
        out["svm_admin_password"] = data["SvmAdminPassword"]
    return out


def redact_sensitive(value: UpdateStorageVirtualMachineRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "active_directory_configuration" in value:
        import capo_fsx.types.update_svm_active_directory_configuration

        out["active_directory_configuration"] = (
            capo_fsx.types.update_svm_active_directory_configuration.redact_sensitive(
                value["active_directory_configuration"]
            )
        )
    if "svm_admin_password" in value:
        out["svm_admin_password"] = "*** Sensitive Data Redacted ***"
    return out
