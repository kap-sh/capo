"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#AzureStorageAccountIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_observabilityadmin.types.azure_storage_account_id

AzureStorageAccountIdList: TypeAlias = list[
    "capo_observabilityadmin.types.azure_storage_account_id.AzureStorageAccountId"
]


# --- restJson1 ser/de ---
def serialize_json(value: AzureStorageAccountIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> AzureStorageAccountIdList:
    return [item for item in data if item is not None]
