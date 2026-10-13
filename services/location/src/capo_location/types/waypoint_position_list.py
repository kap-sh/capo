"""Generated from Smithy shape ``com.amazonaws.location#WaypointPositionList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_location.types.position

WaypointPositionList: TypeAlias = list["capo_location.types.position.Position"]


# --- restJson1 ser/de ---
def serialize_json(value: WaypointPositionList) -> list:
    import capo_location.types.position

    out: list = []
    for item in value:
        out.append(capo_location.types.position.serialize_json(item))
    return out


def deserialize_json(data: list) -> WaypointPositionList:
    import capo_location.types.position

    out: WaypointPositionList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_location.types.position.deserialize_json(item))
    return out


def redact_sensitive(value: WaypointPositionList) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
