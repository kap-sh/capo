"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#CustomClaimValidationsType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_agent_registry_control.types.custom_claim_validation_type

CustomClaimValidationsType: TypeAlias = list[
    "capo_agent_registry_control.types.custom_claim_validation_type.CustomClaimValidationType"
]


# --- restJson1 ser/de ---
def serialize_json(value: CustomClaimValidationsType) -> list:
    import capo_agent_registry_control.types.custom_claim_validation_type

    out: list = []
    for item in value:
        out.append(
            capo_agent_registry_control.types.custom_claim_validation_type.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> CustomClaimValidationsType:
    import capo_agent_registry_control.types.custom_claim_validation_type

    out: CustomClaimValidationsType = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_agent_registry_control.types.custom_claim_validation_type.deserialize_json(
                item
            )
        )
    return out
