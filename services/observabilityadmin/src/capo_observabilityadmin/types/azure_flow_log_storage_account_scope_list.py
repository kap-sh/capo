"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#AzureFlowLogStorageAccountScopeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_observabilityadmin.types.azure_flow_log_storage_account_scope

AzureFlowLogStorageAccountScopeList: TypeAlias = list[
    "capo_observabilityadmin.types.azure_flow_log_storage_account_scope.AzureFlowLogStorageAccountScope"
]


# --- restJson1 ser/de ---
def serialize_json(value: AzureFlowLogStorageAccountScopeList) -> list:
    import capo_observabilityadmin.types.azure_flow_log_storage_account_scope

    out: list = []
    for item in value:
        out.append(
            capo_observabilityadmin.types.azure_flow_log_storage_account_scope.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AzureFlowLogStorageAccountScopeList:
    import capo_observabilityadmin.types.azure_flow_log_storage_account_scope

    out: AzureFlowLogStorageAccountScopeList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_observabilityadmin.types.azure_flow_log_storage_account_scope.deserialize_json(
                item
            )
        )
    return out
