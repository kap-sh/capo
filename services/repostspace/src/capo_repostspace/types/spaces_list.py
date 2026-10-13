"""Generated from Smithy shape ``com.amazonaws.repostspace#SpacesList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_repostspace.types.space_data

SpacesList: TypeAlias = list["capo_repostspace.types.space_data.SpaceData"]


# --- restJson1 ser/de ---
def serialize_json(value: SpacesList) -> list:
    import capo_repostspace.types.space_data

    out: list = []
    for item in value:
        out.append(capo_repostspace.types.space_data.serialize_json(item))
    return out


def deserialize_json(data: list) -> SpacesList:
    import capo_repostspace.types.space_data

    out: SpacesList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_repostspace.types.space_data.deserialize_json(item))
    return out


def redact_sensitive(value: SpacesList) -> list[Any]:
    import capo_repostspace.types.space_data

    return [capo_repostspace.types.space_data.redact_sensitive(item) for item in value]
