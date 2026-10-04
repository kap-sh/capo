"""Generated from Smithy shape ``com.amazonaws.mediatailor#BeaconEventTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediatailor.types.beacon_event_type

BeaconEventTypeList: TypeAlias = list[
    "capo_mediatailor.types.beacon_event_type.BeaconEventType"
]


# --- restJson1 ser/de ---
def serialize_json(value: BeaconEventTypeList) -> list:
    import capo_mediatailor.types.beacon_event_type

    out: list = []
    for item in value:
        out.append(capo_mediatailor.types.beacon_event_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> BeaconEventTypeList:
    import capo_mediatailor.types.beacon_event_type

    out: BeaconEventTypeList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_mediatailor.types.beacon_event_type.deserialize_json(item))
    return out
