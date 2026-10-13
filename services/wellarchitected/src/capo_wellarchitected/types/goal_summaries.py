"""Generated from Smithy shape ``com.amazonaws.wellarchitected#GoalSummaries``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_wellarchitected.types.goal_summary

GoalSummaries: TypeAlias = list["capo_wellarchitected.types.goal_summary.GoalSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: GoalSummaries) -> list:
    import capo_wellarchitected.types.goal_summary

    out: list = []
    for item in value:
        out.append(capo_wellarchitected.types.goal_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> GoalSummaries:
    import capo_wellarchitected.types.goal_summary

    out: GoalSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(capo_wellarchitected.types.goal_summary.deserialize_json(item))
    return out


def redact_sensitive(value: GoalSummaries) -> list[Any]:
    import capo_wellarchitected.types.goal_summary

    return [
        capo_wellarchitected.types.goal_summary.redact_sensitive(item) for item in value
    ]
