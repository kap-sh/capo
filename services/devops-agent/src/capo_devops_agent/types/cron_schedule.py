"""Generated from Smithy shape ``com.amazonaws.devopsagent#CronSchedule``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_devops_agent.types.schedule_expression


class CronSchedule(TypedDict, closed=True):
    expression: "capo_devops_agent.types.schedule_expression.ScheduleExpression"
    """<p>EventBridge cron or rate expression that anchors the flexible window</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CronSchedule) -> dict:
    out: dict = {}
    out["expression"] = value["expression"]
    return out


def deserialize_json(data: dict) -> CronSchedule:
    out: CronSchedule = {}  # type: ignore[typeddict-item]
    if data.get("expression") is not None:
        out["expression"] = data["expression"]
    else:
        raise DeserializationError("CronSchedule.expression required")
    return out
