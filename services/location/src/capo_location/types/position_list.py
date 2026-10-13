"""Generated from Smithy shape ``com.amazonaws.location#PositionList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_location.types.position

PositionList: TypeAlias = list["capo_location.types.position.Position"]


# --- restJson1 ser/de ---
def serialize_json(value: PositionList) -> list:
    import capo_location.types.position

    out: list = []
    for item in value:
        out.append(capo_location.types.position.serialize_json(item))
    return out


def deserialize_json(data: list) -> PositionList:
    import capo_location.types.position

    out: PositionList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_location.types.position.deserialize_json(item))
    return out


def redact_sensitive(value: PositionList) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
