"""Generated from Smithy shape ``com.amazonaws.wellarchitected#PillarCount``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.pillar


class PillarCount(TypedDict, closed=True):
    pillar: "capo_wellarchitected.types.pillar.Pillar"
    """<p>Well-Architected pillar this count is attributed to.</p>"""
    count: "int"
    """<p>Non-negative count of recommendations in the report that are attributed to this pillar.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PillarCount) -> dict:
    out: dict = {}
    import capo_wellarchitected.types.pillar

    out["pillar"] = capo_wellarchitected.types.pillar.serialize_json(value["pillar"])
    out["count"] = value["count"]
    return out


def deserialize_json(data: dict) -> PillarCount:
    out: PillarCount = {}  # type: ignore[typeddict-item]
    if data.get("pillar") is not None:
        import capo_wellarchitected.types.pillar

        out["pillar"] = capo_wellarchitected.types.pillar.deserialize_json(
            data["pillar"]
        )
    else:
        import typing

        out["pillar"] = typing.cast("capo_wellarchitected.types.pillar.Pillar", "")
    if data.get("count") is not None:
        out["count"] = data["count"]
    else:
        out["count"] = 0
    return out
