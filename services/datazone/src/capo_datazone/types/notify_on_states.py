"""Generated from Smithy shape ``com.amazonaws.datazone#NotifyOnStates``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.notify_on_state

NotifyOnStates: TypeAlias = list["capo_datazone.types.notify_on_state.NotifyOnState"]


# --- restJson1 ser/de ---
def serialize_json(value: NotifyOnStates) -> list:
    import capo_datazone.types.notify_on_state

    out: list = []
    for item in value:
        out.append(capo_datazone.types.notify_on_state.serialize_json(item))
    return out


def deserialize_json(data: list) -> NotifyOnStates:
    import capo_datazone.types.notify_on_state

    out: NotifyOnStates = []
    for item in data:
        if item is None:
            continue
        out.append(capo_datazone.types.notify_on_state.deserialize_json(item))
    return out
