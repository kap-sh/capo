"""Generated from Smithy shape ``com.amazonaws.guardduty#AttackPhases``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.attack_phase

AttackPhases: TypeAlias = list["capo_guardduty.types.attack_phase.AttackPhase"]


# --- restJson1 ser/de ---
def serialize_json(value: AttackPhases) -> list:
    import capo_guardduty.types.attack_phase

    out: list = []
    for item in value:
        out.append(capo_guardduty.types.attack_phase.serialize_json(item))
    return out


def deserialize_json(data: list) -> AttackPhases:
    import capo_guardduty.types.attack_phase

    out: AttackPhases = []
    for item in data:
        if item is None:
            continue
        out.append(capo_guardduty.types.attack_phase.deserialize_json(item))
    return out
