"""Generated from Smithy shape ``com.amazonaws.guardduty#Attacks``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.attack

Attacks: TypeAlias = list["capo_guardduty.types.attack.Attack"]


# --- restJson1 ser/de ---
def serialize_json(value: Attacks) -> list:
    import capo_guardduty.types.attack

    out: list = []
    for item in value:
        out.append(capo_guardduty.types.attack.serialize_json(item))
    return out


def deserialize_json(data: list) -> Attacks:
    import capo_guardduty.types.attack

    out: Attacks = []
    for item in data:
        if item is None:
            continue
        out.append(capo_guardduty.types.attack.deserialize_json(item))
    return out
