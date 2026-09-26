"""Generated from Smithy shape ``com.amazonaws.accountaccess#EntitlementsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_account_access.types.entitlements_list_member

EntitlementsList: TypeAlias = list[
    "capo_account_access.types.entitlements_list_member.EntitlementsListMember"
]


# --- restJson1 ser/de ---
def serialize_json(value: EntitlementsList) -> list:
    import capo_account_access.types.entitlements_list_member

    out: list = []
    for item in value:
        out.append(
            capo_account_access.types.entitlements_list_member.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> EntitlementsList:
    import capo_account_access.types.entitlements_list_member

    out: EntitlementsList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_account_access.types.entitlements_list_member.deserialize_json(item)
        )
    return out
