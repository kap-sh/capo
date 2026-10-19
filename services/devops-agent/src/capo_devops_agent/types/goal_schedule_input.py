"""Generated from Smithy shape ``com.amazonaws.devopsagent#GoalScheduleInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.scheduler_state


class GoalScheduleInput(TypedDict, closed=True):
    state: "capo_devops_agent.types.scheduler_state.SchedulerState"
    """<p>Whether the schedule is enabled or disabled</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GoalScheduleInput) -> dict:
    out: dict = {}
    import capo_devops_agent.types.scheduler_state

    out["state"] = capo_devops_agent.types.scheduler_state.serialize_json(
        value["state"]
    )
    return out


def deserialize_json(data: dict) -> GoalScheduleInput:
    out: GoalScheduleInput = {}  # type: ignore[typeddict-item]
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
    return out
