"""Generated from Smithy shape ``com.amazonaws.guardduty#SharedBehaviors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.shared_behavior

SharedBehaviors: TypeAlias = list["capo_guardduty.types.shared_behavior.SharedBehavior"]


# --- restJson1 ser/de ---
def serialize_json(value: SharedBehaviors) -> list:
    import capo_guardduty.types.shared_behavior

    out: list = []
    for item in value:
        out.append(capo_guardduty.types.shared_behavior.serialize_json(item))
    return out


def deserialize_json(data: list) -> SharedBehaviors:
    import capo_guardduty.types.shared_behavior

    out: SharedBehaviors = []
    for item in data:
        if item is None:
            continue
        out.append(capo_guardduty.types.shared_behavior.deserialize_json(item))
    return out
