"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#AzureFlowLogStorageAccountScope``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.azure_region
    import capo_observabilityadmin.types.azure_storage_account_id_list


class AzureFlowLogStorageAccountScope(TypedDict, closed=True):
    region: "capo_observabilityadmin.types.azure_region.AzureRegion"
    """<p>The Azure Region of the Storage Accounts, for example <code>eastus</code>.</p>"""
    storage_account_ids: "capo_observabilityadmin.types.azure_storage_account_id_list.AzureStorageAccountIdList"
    """<p>The Azure Resource Manager IDs of the Storage Accounts.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AzureFlowLogStorageAccountScope) -> dict:
    out: dict = {}
    out["Region"] = value["region"]
    import capo_observabilityadmin.types.azure_storage_account_id_list

    out["StorageAccountIds"] = (
        capo_observabilityadmin.types.azure_storage_account_id_list.serialize_json(
            value["storage_account_ids"]
        )
    )
    return out


def deserialize_json(data: dict) -> AzureFlowLogStorageAccountScope:
    out: AzureFlowLogStorageAccountScope = {}  # type: ignore[typeddict-item]
    if data.get("Region") is not None:
        out["region"] = data["Region"]
    else:
        out["region"] = ""
    if data.get("StorageAccountIds") is not None:
        import capo_observabilityadmin.types.azure_storage_account_id_list

        out["storage_account_ids"] = (
            capo_observabilityadmin.types.azure_storage_account_id_list.deserialize_json(
                data["StorageAccountIds"]
            )
        )
    else:
        out["storage_account_ids"] = []
    return out
