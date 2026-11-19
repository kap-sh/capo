"""Generated from Smithy shape ``com.amazonaws.guardduty#TimeWindowGroups``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.time_window_group

TimeWindowGroups: TypeAlias = list[
    "capo_guardduty.types.time_window_group.TimeWindowGroup"
]


# --- restJson1 ser/de ---
def serialize_json(value: TimeWindowGroups) -> list:
    import capo_guardduty.types.time_window_group

    out: list = []
    for item in value:
        out.append(capo_guardduty.types.time_window_group.serialize_json(item))
    return out


def deserialize_json(data: list) -> TimeWindowGroups:
    import capo_guardduty.types.time_window_group

    out: TimeWindowGroups = []
    for item in data:
        if item is None:
            continue
        out.append(capo_guardduty.types.time_window_group.deserialize_json(item))
    return out
