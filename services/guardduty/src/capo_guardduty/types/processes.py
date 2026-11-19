"""Generated from Smithy shape ``com.amazonaws.guardduty#Processes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.process

Processes: TypeAlias = list["capo_guardduty.types.process.Process"]


# --- restJson1 ser/de ---
def serialize_json(value: Processes) -> list:
    import capo_guardduty.types.process

    out: list = []
    for item in value:
        out.append(capo_guardduty.types.process.serialize_json(item))
    return out


def deserialize_json(data: list) -> Processes:
    import capo_guardduty.types.process

    out: Processes = []
    for item in data:
        if item is None:
            continue
        out.append(capo_guardduty.types.process.deserialize_json(item))
    return out
