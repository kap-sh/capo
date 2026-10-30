"""Generated from Smithy shape ``com.amazonaws.continuum#CweIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_continuum.types.cwe_id

CweIdList: TypeAlias = list["capo_continuum.types.cwe_id.CweId"]


# --- restJson1 ser/de ---
def serialize_json(value: CweIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> CweIdList:
    return [item for item in data if item is not None]
