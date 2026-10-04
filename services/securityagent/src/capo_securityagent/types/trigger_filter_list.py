"""Generated from Smithy shape ``com.amazonaws.securityagent#TriggerFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityagent.types.trigger_filter

TriggerFilterList: TypeAlias = list[
    "capo_securityagent.types.trigger_filter.TriggerFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: TriggerFilterList) -> list:
    import capo_securityagent.types.trigger_filter

    out: list = []
    for item in value:
        out.append(capo_securityagent.types.trigger_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> TriggerFilterList:
    import capo_securityagent.types.trigger_filter

    out: TriggerFilterList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_securityagent.types.trigger_filter.deserialize_json(item))
    return out
