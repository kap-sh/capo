"""Generated from Smithy shape ``com.amazonaws.connect#ContactLensRedactionEntitiesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.string

ContactLensRedactionEntitiesList: TypeAlias = list["capo_connect.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: ContactLensRedactionEntitiesList) -> list:
    return list(value)


def deserialize_json(data: list) -> ContactLensRedactionEntitiesList:
    return [item for item in data if item is not None]
