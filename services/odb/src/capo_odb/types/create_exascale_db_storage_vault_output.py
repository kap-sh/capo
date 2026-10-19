"""Generated from Smithy shape ``com.amazonaws.odb#CreateExascaleDbStorageVaultOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_odb.types.resource_status


class CreateExascaleDbStorageVaultOutput(TypedDict, closed=True):
    display_name: NotRequired["str"]
    """<p>The user-friendly name for the Exascale storage vault.</p>"""
    status: NotRequired["capo_odb.types.resource_status.ResourceStatus"]
    """<p>The current status of the Exascale storage vault.</p>"""
    status_reason: NotRequired["str"]
    """<p>Additional information about the status of the Exascale storage vault.</p>"""
    exascale_db_storage_vault_id: "str"
    """<p>The unique identifier of the Exascale storage vault.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateExascaleDbStorageVaultOutput) -> dict:
    out: dict = {}
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "status" in value:
        import capo_odb.types.resource_status

        out["status"] = capo_odb.types.resource_status.serialize_aws_json_1_0(
            value["status"]
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    out["exascaleDbStorageVaultId"] = value["exascale_db_storage_vault_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateExascaleDbStorageVaultOutput:
    out: CreateExascaleDbStorageVaultOutput = {}  # type: ignore[typeddict-item]
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    if data.get("status") is not None:
        import capo_odb.types.resource_status

        out["status"] = capo_odb.types.resource_status.deserialize_aws_json_1_0(
            data["status"]
        )
    if data.get("statusReason") is not None:
        out["status_reason"] = data["statusReason"]
    if data.get("exascaleDbStorageVaultId") is not None:
        out["exascale_db_storage_vault_id"] = data["exascaleDbStorageVaultId"]
    else:
        out["exascale_db_storage_vault_id"] = ""
    return out
