"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#AzureCustomerManagedFlowLogs``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.azure_flow_log_storage_account_scope_list


class AzureCustomerManagedFlowLogs(TypedDict, closed=True):
    storage_accounts: "capo_observabilityadmin.types.azure_flow_log_storage_account_scope_list.AzureFlowLogStorageAccountScopeList"
    """<p>The Storage Accounts that store your Flow Logs, listed by Azure Region. Each Region can appear only once, and each Storage Account can appear only once across all Regions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AzureCustomerManagedFlowLogs) -> dict:
    out: dict = {}
    import capo_observabilityadmin.types.azure_flow_log_storage_account_scope_list

    out["StorageAccounts"] = (
        capo_observabilityadmin.types.azure_flow_log_storage_account_scope_list.serialize_json(
            value["storage_accounts"]
        )
    )
    return out


def deserialize_json(data: dict) -> AzureCustomerManagedFlowLogs:
    out: AzureCustomerManagedFlowLogs = {}  # type: ignore[typeddict-item]
    if data.get("StorageAccounts") is not None:
        import capo_observabilityadmin.types.azure_flow_log_storage_account_scope_list

        out["storage_accounts"] = (
            capo_observabilityadmin.types.azure_flow_log_storage_account_scope_list.deserialize_json(
                data["StorageAccounts"]
            )
        )
    else:
        out["storage_accounts"] = []
    return out
