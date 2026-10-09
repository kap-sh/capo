"""Generated from Smithy shape ``com.amazonaws.devopsagent#ScheduleCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.schedule_expression
    import capo_devops_agent.types.schedule_spec


class ScheduleCondition(TypedDict, closed=True):
    expression: NotRequired[
        "capo_devops_agent.types.schedule_expression.ScheduleExpression"
    ]
    """<p>EventBridge cron or rate expression. Required for existing request and response compatibility. For a structured schedule response, this is the expression derived by Backlog.</p>"""
    spec: NotRequired["capo_devops_agent.types.schedule_spec.ScheduleSpec"]
    """<p>Structured schedule source of truth (cron | timeRange). On CreateTrigger supply exactly one of spec or expression. Present in responses together with the derived expression for structured triggers.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScheduleCondition) -> dict:
    out: dict = {}
    if "expression" in value:
        out["expression"] = value["expression"]
    if "spec" in value:
        import capo_devops_agent.types.schedule_spec

        out["spec"] = capo_devops_agent.types.schedule_spec.serialize_json(
            value["spec"]
        )
    return out


def deserialize_json(data: dict) -> ScheduleCondition:
    out: ScheduleCondition = {}  # type: ignore[typeddict-item]
    if data.get("expression") is not None:
        out["expression"] = data["expression"]
    if data.get("spec") is not None:
        import capo_devops_agent.types.schedule_spec

        out["spec"] = capo_devops_agent.types.schedule_spec.deserialize_json(
            data["spec"]
        )
    return out
