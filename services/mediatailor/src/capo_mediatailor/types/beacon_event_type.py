"""Generated from Smithy shape ``com.amazonaws.mediatailor#BeaconEventType``."""

from typing import Literal, TypeAlias, cast

"""<p>A player operation event that MediaTailor can report on. Only the player can detect when a viewer performs this action, so MediaTailor doesn't send these beacons itself.</p>"""
BeaconEventType: TypeAlias = Literal[
    "MUTE",
    "UNMUTE",
    "PAUSE",
    "SKIP",
]


# --- restJson1 ser/de ---
def serialize_json(value: BeaconEventType) -> str:
    return value


def deserialize_json(data: str) -> BeaconEventType:
    return cast(BeaconEventType, data)
