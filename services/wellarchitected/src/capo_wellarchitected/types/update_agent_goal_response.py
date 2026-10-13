"""Generated from Smithy shape ``com.amazonaws.wellarchitected#UpdateAgentGoalResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_wellarchitected.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wellarchitected.types.goal_summary


class UpdateAgentGoalResponse(TypedDict, closed=True):
    goal: "capo_wellarchitected.types.goal_summary.GoalSummary"
    """<p>The updated goal summary.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAgentGoalResponse) -> dict:
    out: dict = {}
    import capo_wellarchitected.types.goal_summary

    out["goal"] = capo_wellarchitected.types.goal_summary.serialize_json(value["goal"])
    return out


def deserialize_json(data: dict) -> UpdateAgentGoalResponse:
    out: UpdateAgentGoalResponse = {}  # type: ignore[typeddict-item]
    if data.get("goal") is not None:
        import capo_wellarchitected.types.goal_summary

        out["goal"] = capo_wellarchitected.types.goal_summary.deserialize_json(
            data["goal"]
        )
    else:
        raise DeserializationError("UpdateAgentGoalResponse.goal required")
    return out


def redact_sensitive(value: UpdateAgentGoalResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "goal" in value:
        import capo_wellarchitected.types.goal_summary

        out["goal"] = capo_wellarchitected.types.goal_summary.redact_sensitive(
            value["goal"]
        )
    return out
