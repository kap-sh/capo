"""Generated from Smithy shape ``com.amazonaws.wellarchitected#PillarItem``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.item_ids
    import capo_wellarchitected.types.pillar


class PillarItem(TypedDict, closed=True):
    pillar: "capo_wellarchitected.types.pillar.Pillar"
    """<p>The pillar this item configuration applies to.</p>"""
    ids: "capo_wellarchitected.types.item_ids.ItemIds"
    """<p>A list of item IDs to process for this pillar, such as best practice IDs, Amazon Web Services service names, or resource ARNs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PillarItem) -> dict:
    out: dict = {}
    import capo_wellarchitected.types.pillar

    out["pillar"] = capo_wellarchitected.types.pillar.serialize_json(value["pillar"])
    import capo_wellarchitected.types.item_ids

    out["ids"] = capo_wellarchitected.types.item_ids.serialize_json(value["ids"])
    return out


def deserialize_json(data: dict) -> PillarItem:
    out: PillarItem = {}  # type: ignore[typeddict-item]
    if data.get("pillar") is not None:
        import capo_wellarchitected.types.pillar

        out["pillar"] = capo_wellarchitected.types.pillar.deserialize_json(
            data["pillar"]
        )
    else:
        import typing

        out["pillar"] = typing.cast("capo_wellarchitected.types.pillar.Pillar", "")
    if data.get("ids") is not None:
        import capo_wellarchitected.types.item_ids

        out["ids"] = capo_wellarchitected.types.item_ids.deserialize_json(data["ids"])
    else:
        out["ids"] = []
    return out
