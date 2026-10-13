"""Generated from Smithy shape ``com.amazonaws.detective#AccountList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_detective.types.account

AccountList: TypeAlias = list["capo_detective.types.account.Account"]


# --- restJson1 ser/de ---
def serialize_json(value: AccountList) -> list:
    import capo_detective.types.account

    out: list = []
    for item in value:
        out.append(capo_detective.types.account.serialize_json(item))
    return out


def deserialize_json(data: list) -> AccountList:
    import capo_detective.types.account

    out: AccountList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_detective.types.account.deserialize_json(item))
    return out


def redact_sensitive(value: AccountList) -> list[Any]:
    import capo_detective.types.account

    return [capo_detective.types.account.redact_sensitive(item) for item in value]
