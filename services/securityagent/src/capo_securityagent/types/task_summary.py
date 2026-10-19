"""Generated from Smithy shape ``com.amazonaws.securityagent#TaskSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_securityagent.types.risk_type
    import capo_securityagent.types.task_execution_status


class TaskSummary(TypedDict, closed=True):
    task_id: "str"
    """<p>The unique identifier of the task.</p>"""
    pentest_id: NotRequired["str"]
    """<p>The unique identifier of the pentest associated with the task.</p>"""
    pentest_job_id: NotRequired["str"]
    """<p>The unique identifier of the pentest job that contains the task.</p>"""
    agent_space_id: NotRequired["str"]
    """<p>The unique identifier of the agent space.</p>"""
    title: NotRequired["str"]
    """<p>The title of the task.</p>"""
    risk_type: NotRequired["capo_securityagent.types.risk_type.RiskType"]
    """<p>The type of security risk the task is testing for.</p>"""
    execution_status: NotRequired[
        "capo_securityagent.types.task_execution_status.TaskExecutionStatus"
    ]
    """<p>The current execution status of the task.</p>"""
    task_hours: NotRequired["float"]
    """<p>The number of active work hours consumed by the task during execution.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The date and time the task was created, in UTC format.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The date and time the task was last updated, in UTC format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TaskSummary) -> dict:
    out: dict = {}
    out["taskId"] = value["task_id"]
    if "pentest_id" in value:
        out["pentestId"] = value["pentest_id"]
    if "pentest_job_id" in value:
        out["pentestJobId"] = value["pentest_job_id"]
    if "agent_space_id" in value:
        out["agentSpaceId"] = value["agent_space_id"]
    if "title" in value:
        out["title"] = value["title"]
    if "risk_type" in value:
        import capo_securityagent.types.risk_type

        out["riskType"] = capo_securityagent.types.risk_type.serialize_json(
            value["risk_type"]
        )
    if "execution_status" in value:
        import capo_securityagent.types.task_execution_status

        out["executionStatus"] = (
            capo_securityagent.types.task_execution_status.serialize_json(
                value["execution_status"]
            )
        )
    if "task_hours" in value:
        out["taskHours"] = (
            "NaN"
            if value["task_hours"] != value["task_hours"]
            else "Infinity"
            if value["task_hours"] == float("inf")
            else "-Infinity"
            if value["task_hours"] == float("-inf")
            else value["task_hours"]
        )
    if "created_at" in value:
        import capo_securityagent._protocol.serialize

        out["createdAt"] = capo_securityagent._protocol.serialize.fmt_date_time(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_securityagent._protocol.serialize

        out["updatedAt"] = capo_securityagent._protocol.serialize.fmt_date_time(
            value["updated_at"]
        )
    return out


def deserialize_json(data: dict) -> TaskSummary:
    out: TaskSummary = {}  # type: ignore[typeddict-item]
    if data.get("taskId") is not None:
        out["task_id"] = data["taskId"]
    else:
        out["task_id"] = ""
    if data.get("pentestId") is not None:
        out["pentest_id"] = data["pentestId"]
    if data.get("pentestJobId") is not None:
        out["pentest_job_id"] = data["pentestJobId"]
    if data.get("agentSpaceId") is not None:
        out["agent_space_id"] = data["agentSpaceId"]
    if data.get("title") is not None:
        out["title"] = data["title"]
    if data.get("riskType") is not None:
        import capo_securityagent.types.risk_type

        out["risk_type"] = capo_securityagent.types.risk_type.deserialize_json(
            data["riskType"]
        )
    if data.get("executionStatus") is not None:
        import capo_securityagent.types.task_execution_status

        out["execution_status"] = (
            capo_securityagent.types.task_execution_status.deserialize_json(
                data["executionStatus"]
            )
        )
    if data.get("taskHours") is not None:
        out["task_hours"] = float(data["taskHours"])
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    if data.get("updatedAt") is not None:
        import datetime

        out["updated_at"] = datetime.datetime.fromisoformat(
            data["updatedAt"].replace("Z", "+00:00")
        )
    return out
