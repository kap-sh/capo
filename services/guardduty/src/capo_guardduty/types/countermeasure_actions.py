"""Generated from Smithy shape ``com.amazonaws.guardduty#CountermeasureActions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.countermeasure_action

CountermeasureActions: TypeAlias = list[
    "capo_guardduty.types.countermeasure_action.CountermeasureAction"
]


# --- restJson1 ser/de ---
def serialize_json(value: CountermeasureActions) -> list:
    import capo_guardduty.types.countermeasure_action

    out: list = []
    for item in value:
        out.append(capo_guardduty.types.countermeasure_action.serialize_json(item))
    return out


def deserialize_json(data: list) -> CountermeasureActions:
    import capo_guardduty.types.countermeasure_action

    out: CountermeasureActions = []
    for item in data:
        if item is None:
            continue
        out.append(capo_guardduty.types.countermeasure_action.deserialize_json(item))
    return out
