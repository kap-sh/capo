"""Generated from Smithy shape ``com.amazonaws.guardduty#Countermeasure``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.countermeasure_actions
    import capo_guardduty.types.defense_tactic
    import capo_guardduty.types.string


class Countermeasure(TypedDict, closed=True):
    defense_tactic: NotRequired["capo_guardduty.types.defense_tactic.DefenseTactic"]
    """<p>The defensive tactic. Possible values are <code>Isolate</code>, <code>Evict</code>, <code>Restore</code>, <code>Harden</code>, and <code>Detect</code>.</p>"""
    actions: NotRequired[
        "capo_guardduty.types.countermeasure_actions.CountermeasureActions"
    ]
    """<p>The actions for the defensive tactic.</p>"""
    description: NotRequired["capo_guardduty.types.string.String"]
    """<p>A description of the countermeasure.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Countermeasure) -> dict:
    out: dict = {}
    if "defense_tactic" in value:
        import capo_guardduty.types.defense_tactic

        out["defenseTactic"] = capo_guardduty.types.defense_tactic.serialize_json(
            value["defense_tactic"]
        )
    if "actions" in value:
        import capo_guardduty.types.countermeasure_actions

        out["actions"] = capo_guardduty.types.countermeasure_actions.serialize_json(
            value["actions"]
        )
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> Countermeasure:
    out: Countermeasure = {}  # type: ignore[typeddict-item]
    if data.get("defenseTactic") is not None:
        import capo_guardduty.types.defense_tactic

        out["defense_tactic"] = capo_guardduty.types.defense_tactic.deserialize_json(
            data["defenseTactic"]
        )
    if data.get("actions") is not None:
        import capo_guardduty.types.countermeasure_actions

        out["actions"] = capo_guardduty.types.countermeasure_actions.deserialize_json(
            data["actions"]
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    return out
