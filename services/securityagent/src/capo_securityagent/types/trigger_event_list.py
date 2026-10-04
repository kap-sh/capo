"""Generated from Smithy shape ``com.amazonaws.securityagent#TriggerEventList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityagent.types.trigger_event

TriggerEventList: TypeAlias = list[
    "capo_securityagent.types.trigger_event.TriggerEvent"
]


# --- restJson1 ser/de ---
def serialize_json(value: TriggerEventList) -> list:
    import capo_securityagent.types.trigger_event

    out: list = []
    for item in value:
        out.append(capo_securityagent.types.trigger_event.serialize_json(item))
    return out


def deserialize_json(data: list) -> TriggerEventList:
    import capo_securityagent.types.trigger_event

    out: TriggerEventList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_securityagent.types.trigger_event.deserialize_json(item))
    return out
