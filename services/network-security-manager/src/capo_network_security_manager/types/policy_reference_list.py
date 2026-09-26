"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#PolicyReferenceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_security_manager.types.policy_reference

PolicyReferenceList: TypeAlias = list[
    "capo_network_security_manager.types.policy_reference.PolicyReference"
]


# --- restJson1 ser/de ---
def serialize_json(value: PolicyReferenceList) -> list:
    import capo_network_security_manager.types.policy_reference

    out: list = []
    for item in value:
        out.append(
            capo_network_security_manager.types.policy_reference.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> PolicyReferenceList:
    import capo_network_security_manager.types.policy_reference

    out: PolicyReferenceList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_network_security_manager.types.policy_reference.deserialize_json(item)
        )
    return out
