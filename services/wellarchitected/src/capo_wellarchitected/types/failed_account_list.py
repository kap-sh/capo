"""Generated from Smithy shape ``com.amazonaws.wellarchitected#FailedAccountList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wellarchitected.types.failed_account

FailedAccountList: TypeAlias = list[
    "capo_wellarchitected.types.failed_account.FailedAccount"
]


# --- restJson1 ser/de ---
def serialize_json(value: FailedAccountList) -> list:
    import capo_wellarchitected.types.failed_account

    out: list = []
    for item in value:
        out.append(capo_wellarchitected.types.failed_account.serialize_json(item))
    return out


def deserialize_json(data: list) -> FailedAccountList:
    import capo_wellarchitected.types.failed_account

    out: FailedAccountList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_wellarchitected.types.failed_account.deserialize_json(item))
    return out
