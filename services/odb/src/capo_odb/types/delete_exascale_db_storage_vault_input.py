"""Generated from Smithy shape ``com.amazonaws.odb#DeleteExascaleDbStorageVaultInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_odb.types.resource_id_or_arn


class DeleteExascaleDbStorageVaultInput(TypedDict, closed=True):
    exascale_db_storage_vault_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn"
    """<p>The unique identifier of the Exascale storage vault to delete.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteExascaleDbStorageVaultInput) -> dict:
    out: dict = {}
    out["exascaleDbStorageVaultId"] = value["exascale_db_storage_vault_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteExascaleDbStorageVaultInput:
    out: DeleteExascaleDbStorageVaultInput = {}  # type: ignore[typeddict-item]
    if data.get("exascaleDbStorageVaultId") is not None:
        out["exascale_db_storage_vault_id"] = data["exascaleDbStorageVaultId"]
    else:
        out["exascale_db_storage_vault_id"] = ""
    return out
