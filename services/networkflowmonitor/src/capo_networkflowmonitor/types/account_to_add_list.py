"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#AccountToAddList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_networkflowmonitor.types.account_to_add

AccountToAddList: TypeAlias = list[
    "capo_networkflowmonitor.types.account_to_add.AccountToAdd"
]


# --- restJson1 ser/de ---
def serialize_json(value: AccountToAddList) -> list:
    import capo_networkflowmonitor.types.account_to_add

    out: list = []
    for item in value:
        out.append(capo_networkflowmonitor.types.account_to_add.serialize_json(item))
    return out


def deserialize_json(data: list) -> AccountToAddList:
    import capo_networkflowmonitor.types.account_to_add

    out: AccountToAddList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_networkflowmonitor.types.account_to_add.deserialize_json(item))
    return out
