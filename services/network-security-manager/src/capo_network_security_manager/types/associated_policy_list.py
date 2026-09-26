"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#AssociatedPolicyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_security_manager.types.associated_policy

AssociatedPolicyList: TypeAlias = list[
    "capo_network_security_manager.types.associated_policy.AssociatedPolicy"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssociatedPolicyList) -> list:
    import capo_network_security_manager.types.associated_policy

    out: list = []
    for item in value:
        out.append(
            capo_network_security_manager.types.associated_policy.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AssociatedPolicyList:
    import capo_network_security_manager.types.associated_policy

    out: AssociatedPolicyList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_network_security_manager.types.associated_policy.deserialize_json(item)
        )
    return out
