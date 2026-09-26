"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#AccountReferenceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_security_manager.types.account_reference

AccountReferenceList: TypeAlias = list[
    "capo_network_security_manager.types.account_reference.AccountReference"
]


# --- restJson1 ser/de ---
def serialize_json(value: AccountReferenceList) -> list:
    import capo_network_security_manager.types.account_reference

    out: list = []
    for item in value:
        out.append(
            capo_network_security_manager.types.account_reference.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AccountReferenceList:
    import capo_network_security_manager.types.account_reference

    out: AccountReferenceList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_network_security_manager.types.account_reference.deserialize_json(item)
        )
    return out
