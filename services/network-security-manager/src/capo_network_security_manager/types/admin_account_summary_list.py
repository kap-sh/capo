"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#AdminAccountSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_security_manager.types.admin_account_summary

AdminAccountSummaryList: TypeAlias = list[
    "capo_network_security_manager.types.admin_account_summary.AdminAccountSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AdminAccountSummaryList) -> list:
    import capo_network_security_manager.types.admin_account_summary

    out: list = []
    for item in value:
        out.append(
            capo_network_security_manager.types.admin_account_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AdminAccountSummaryList:
    import capo_network_security_manager.types.admin_account_summary

    out: AdminAccountSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_network_security_manager.types.admin_account_summary.deserialize_json(
                item
            )
        )
    return out
