"""Generated from Smithy shape ``com.amazonaws.securityagent#TriggerFilterGroups``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityagent.types.trigger_filter_group

TriggerFilterGroups: TypeAlias = list[
    "capo_securityagent.types.trigger_filter_group.TriggerFilterGroup"
]


# --- restJson1 ser/de ---
def serialize_json(value: TriggerFilterGroups) -> list:
    import capo_securityagent.types.trigger_filter_group

    out: list = []
    for item in value:
        out.append(capo_securityagent.types.trigger_filter_group.serialize_json(item))
    return out


def deserialize_json(data: list) -> TriggerFilterGroups:
    import capo_securityagent.types.trigger_filter_group

    out: TriggerFilterGroups = []
    for item in data:
        if item is None:
            continue
        out.append(capo_securityagent.types.trigger_filter_group.deserialize_json(item))
    return out
