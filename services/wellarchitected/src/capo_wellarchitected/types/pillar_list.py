"""Generated from Smithy shape ``com.amazonaws.wellarchitected#PillarList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wellarchitected.types.pillar

PillarList: TypeAlias = list["capo_wellarchitected.types.pillar.Pillar"]


# --- restJson1 ser/de ---
def serialize_json(value: PillarList) -> list:
    import capo_wellarchitected.types.pillar

    out: list = []
    for item in value:
        out.append(capo_wellarchitected.types.pillar.serialize_json(item))
    return out


def deserialize_json(data: list) -> PillarList:
    import capo_wellarchitected.types.pillar

    out: PillarList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_wellarchitected.types.pillar.deserialize_json(item))
    return out
