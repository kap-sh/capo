"""Generated from Smithy shape ``com.amazonaws.wellarchitected#GetAgentGoalResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_wellarchitected.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wellarchitected.types.goal_summary


class GetAgentGoalResponse(TypedDict, closed=True):
    goal: "capo_wellarchitected.types.goal_summary.GoalSummary"
    """<p>The retrieved goal summary.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAgentGoalResponse) -> dict:
    out: dict = {}
    import capo_wellarchitected.types.goal_summary

    out["goal"] = capo_wellarchitected.types.goal_summary.serialize_json(value["goal"])
    return out


def deserialize_json(data: dict) -> GetAgentGoalResponse:
    out: GetAgentGoalResponse = {}  # type: ignore[typeddict-item]
    if data.get("goal") is not None:
        import capo_wellarchitected.types.goal_summary

        out["goal"] = capo_wellarchitected.types.goal_summary.deserialize_json(
            data["goal"]
        )
    else:
        raise DeserializationError("GetAgentGoalResponse.goal required")
    return out


def redact_sensitive(value: GetAgentGoalResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "goal" in value:
        import capo_wellarchitected.types.goal_summary

        out["goal"] = capo_wellarchitected.types.goal_summary.redact_sensitive(
            value["goal"]
        )
    return out
