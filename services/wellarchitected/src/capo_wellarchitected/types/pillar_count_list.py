"""Generated from Smithy shape ``com.amazonaws.wellarchitected#PillarCountList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wellarchitected.types.pillar_count

PillarCountList: TypeAlias = list["capo_wellarchitected.types.pillar_count.PillarCount"]


# --- restJson1 ser/de ---
def serialize_json(value: PillarCountList) -> list:
    import capo_wellarchitected.types.pillar_count

    out: list = []
    for item in value:
        out.append(capo_wellarchitected.types.pillar_count.serialize_json(item))
    return out


def deserialize_json(data: list) -> PillarCountList:
    import capo_wellarchitected.types.pillar_count

    out: PillarCountList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_wellarchitected.types.pillar_count.deserialize_json(item))
    return out
