"""Generated from Smithy shape ``com.amazonaws.wellarchitected#Scope``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.goal_id_list
    import capo_wellarchitected.types.pillar_items
    import capo_wellarchitected.types.pillars


class Scope(TypedDict, closed=True):
    pillars: "capo_wellarchitected.types.pillars.Pillars"
    """<p>The Well-Architected Tool Framework pillars to include in the generation scope.</p>"""
    goal_ids: NotRequired["capo_wellarchitected.types.goal_id_list.GoalIdList"]
    """<p>Specific goal IDs to focus on during recommendation generation.</p>"""
    items: NotRequired["capo_wellarchitected.types.pillar_items.PillarItems"]
    """<p>Optional per-pillar item filtering configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Scope) -> dict:
    out: dict = {}
    import capo_wellarchitected.types.pillars

    out["pillars"] = capo_wellarchitected.types.pillars.serialize_json(value["pillars"])
    if "goal_ids" in value:
        import capo_wellarchitected.types.goal_id_list

        out["goalIds"] = capo_wellarchitected.types.goal_id_list.serialize_json(
            value["goal_ids"]
        )
    if "items" in value:
        import capo_wellarchitected.types.pillar_items

        out["items"] = capo_wellarchitected.types.pillar_items.serialize_json(
            value["items"]
        )
    return out


def deserialize_json(data: dict) -> Scope:
    out: Scope = {}  # type: ignore[typeddict-item]
    if data.get("pillars") is not None:
        import capo_wellarchitected.types.pillars

        out["pillars"] = capo_wellarchitected.types.pillars.deserialize_json(
            data["pillars"]
        )
    else:
        out["pillars"] = []
    if data.get("goalIds") is not None:
        import capo_wellarchitected.types.goal_id_list

        out["goal_ids"] = capo_wellarchitected.types.goal_id_list.deserialize_json(
            data["goalIds"]
        )
    if data.get("items") is not None:
        import capo_wellarchitected.types.pillar_items

        out["items"] = capo_wellarchitected.types.pillar_items.deserialize_json(
            data["items"]
        )
    return out
