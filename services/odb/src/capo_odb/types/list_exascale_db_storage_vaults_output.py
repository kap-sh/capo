"""Generated from Smithy shape ``com.amazonaws.odb#ListExascaleDbStorageVaultsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_odb.types.exascale_db_storage_vault_list


class ListExascaleDbStorageVaultsOutput(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
    exascale_db_storage_vaults: (
        "capo_odb.types.exascale_db_storage_vault_list.ExascaleDbStorageVaultList"
    )
    """<p>The list of Exascale storage vaults.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListExascaleDbStorageVaultsOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_odb.types.exascale_db_storage_vault_list

    out["exascaleDbStorageVaults"] = (
        capo_odb.types.exascale_db_storage_vault_list.serialize_aws_json_1_0(
            value["exascale_db_storage_vaults"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListExascaleDbStorageVaultsOutput:
    out: ListExascaleDbStorageVaultsOutput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("exascaleDbStorageVaults") is not None:
        import capo_odb.types.exascale_db_storage_vault_list

        out["exascale_db_storage_vaults"] = (
            capo_odb.types.exascale_db_storage_vault_list.deserialize_aws_json_1_0(
                data["exascaleDbStorageVaults"]
            )
        )
    else:
        out["exascale_db_storage_vaults"] = []
    return out
