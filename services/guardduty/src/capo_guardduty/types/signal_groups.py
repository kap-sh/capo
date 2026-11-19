"""Generated from Smithy shape ``com.amazonaws.guardduty#SignalGroups``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.signal_group

SignalGroups: TypeAlias = list["capo_guardduty.types.signal_group.SignalGroup"]


# --- restJson1 ser/de ---
def serialize_json(value: SignalGroups) -> list:
    import capo_guardduty.types.signal_group

    out: list = []
    for item in value:
        out.append(capo_guardduty.types.signal_group.serialize_json(item))
    return out


def deserialize_json(data: list) -> SignalGroups:
    import capo_guardduty.types.signal_group

    out: SignalGroups = []
    for item in data:
        if item is None:
            continue
        out.append(capo_guardduty.types.signal_group.deserialize_json(item))
    return out
