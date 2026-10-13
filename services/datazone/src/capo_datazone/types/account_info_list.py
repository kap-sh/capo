"""Generated from Smithy shape ``com.amazonaws.datazone#AccountInfoList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.account_info

AccountInfoList: TypeAlias = list["capo_datazone.types.account_info.AccountInfo"]


# --- restJson1 ser/de ---
def serialize_json(value: AccountInfoList) -> list:
    import capo_datazone.types.account_info

    out: list = []
    for item in value:
        out.append(capo_datazone.types.account_info.serialize_json(item))
    return out


def deserialize_json(data: list) -> AccountInfoList:
    import capo_datazone.types.account_info

    out: AccountInfoList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_datazone.types.account_info.deserialize_json(item))
    return out


def redact_sensitive(value: AccountInfoList) -> list[Any]:
    import capo_datazone.types.account_info

    return [capo_datazone.types.account_info.redact_sensitive(item) for item in value]
