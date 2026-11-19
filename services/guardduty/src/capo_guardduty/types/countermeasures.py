"""Generated from Smithy shape ``com.amazonaws.guardduty#Countermeasures``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.countermeasure

Countermeasures: TypeAlias = list["capo_guardduty.types.countermeasure.Countermeasure"]


# --- restJson1 ser/de ---
def serialize_json(value: Countermeasures) -> list:
    import capo_guardduty.types.countermeasure

    out: list = []
    for item in value:
        out.append(capo_guardduty.types.countermeasure.serialize_json(item))
    return out


def deserialize_json(data: list) -> Countermeasures:
    import capo_guardduty.types.countermeasure

    out: Countermeasures = []
    for item in data:
        if item is None:
            continue
        out.append(capo_guardduty.types.countermeasure.deserialize_json(item))
    return out
