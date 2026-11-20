"""Generated from Smithy shape ``com.amazonaws.accountaccessruntime#AccessDetailsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_account_access_runtime.types.access_details

AccessDetailsList: TypeAlias = list[
    "capo_account_access_runtime.types.access_details.AccessDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: AccessDetailsList) -> list:
    import capo_account_access_runtime.types.access_details

    out: list = []
    for item in value:
        out.append(
            capo_account_access_runtime.types.access_details.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AccessDetailsList:
    import capo_account_access_runtime.types.access_details

    out: AccessDetailsList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_account_access_runtime.types.access_details.deserialize_json(item)
        )
    return out
