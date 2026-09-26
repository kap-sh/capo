"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#ScopeSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_security_manager.types.scope_summary

ScopeSummaryList: TypeAlias = list[
    "capo_network_security_manager.types.scope_summary.ScopeSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ScopeSummaryList) -> list:
    import capo_network_security_manager.types.scope_summary

    out: list = []
    for item in value:
        out.append(
            capo_network_security_manager.types.scope_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ScopeSummaryList:
    import capo_network_security_manager.types.scope_summary

    out: ScopeSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_network_security_manager.types.scope_summary.deserialize_json(item)
        )
    return out
