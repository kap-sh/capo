"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#AccountIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_security_manager.types.account_id

AccountIdList: TypeAlias = list[
    "capo_network_security_manager.types.account_id.AccountId"
]


# --- restJson1 ser/de ---
def serialize_json(value: AccountIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> AccountIdList:
    return [item for item in data if item is not None]
