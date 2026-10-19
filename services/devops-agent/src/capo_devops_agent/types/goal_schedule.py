"""Generated from Smithy shape ``com.amazonaws.devopsagent#GoalSchedule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.scheduler_state


class GoalSchedule(TypedDict, closed=True):
    state: "capo_devops_agent.types.scheduler_state.SchedulerState"
    """<p>Whether the schedule is enabled or disabled</p>"""
    expression: NotRequired["str"]
    """<p>Schedule expression (e.g., 'rate(7 days)')</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GoalSchedule) -> dict:
    out: dict = {}
    import capo_devops_agent.types.scheduler_state

    out["state"] = capo_devops_agent.types.scheduler_state.serialize_json(
        value["state"]
    )
    if "expression" in value:
        out["expression"] = value["expression"]
    return out


def deserialize_json(data: dict) -> GoalSchedule:
    out: GoalSchedule = {}  # type: ignore[typeddict-item]
    if data.get("state") is not None:
        import capo_devops_agent.types.scheduler_state

        out["state"] = capo_devops_agent.types.scheduler_state.deserialize_json(
            data["state"]
        )
    else:
        import typing

        out["state"] = typing.cast(
            "capo_devops_agent.types.scheduler_state.SchedulerState", ""
        )
    if data.get("expression") is not None:
        out["expression"] = data["expression"]
    return out
