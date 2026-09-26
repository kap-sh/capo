"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#PolicySummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_security_manager.types.policy_summary

PolicySummaryList: TypeAlias = list[
    "capo_network_security_manager.types.policy_summary.PolicySummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: PolicySummaryList) -> list:
    import capo_network_security_manager.types.policy_summary

    out: list = []
    for item in value:
        out.append(
            capo_network_security_manager.types.policy_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> PolicySummaryList:
    import capo_network_security_manager.types.policy_summary

    out: PolicySummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_network_security_manager.types.policy_summary.deserialize_json(item)
        )
    return out
