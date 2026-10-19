"""Generated from Smithy shape ``com.amazonaws.mgn#FsxOntapConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.secret_arn
    import capo_mgn.types.storage_virtual_machine_id


class FsxOntapConfiguration(TypedDict, closed=True):
    storage_virtual_machine_id: (
        "capo_mgn.types.storage_virtual_machine_id.StorageVirtualMachineId"
    )
    """<p>FSx ONTAP configuration storage virtual machine ID.</p>"""
    credentials_secret_arn: "capo_mgn.types.secret_arn.SecretArn"
    """<p>FSx ONTAP configuration credentials secret ARN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FsxOntapConfiguration) -> dict:
    out: dict = {}
    out["storageVirtualMachineId"] = value["storage_virtual_machine_id"]
    out["credentialsSecretArn"] = value["credentials_secret_arn"]
    return out


def deserialize_json(data: dict) -> FsxOntapConfiguration:
    out: FsxOntapConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("storageVirtualMachineId") is not None:
        out["storage_virtual_machine_id"] = data["storageVirtualMachineId"]
    else:
        out["storage_virtual_machine_id"] = ""
    if data.get("credentialsSecretArn") is not None:
        out["credentials_secret_arn"] = data["credentialsSecretArn"]
    else:
        out["credentials_secret_arn"] = ""
    return out
