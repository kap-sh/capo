"""Generated from Smithy shape ``com.amazonaws.securityagent#ThreatModelJobTaskSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_securityagent.types.task_execution_status


class ThreatModelJobTaskSummary(TypedDict, closed=True):
    task_id: "str"
    """<p>The unique identifier of the task.</p>"""
    threat_model_id: NotRequired["str"]
    """<p>The unique identifier of the threat model associated with the task.</p>"""
    threat_model_job_id: NotRequired["str"]
    """<p>The unique identifier of the threat model job that contains the task.</p>"""
    agent_space_id: NotRequired["str"]
    """<p>The unique identifier of the agent space.</p>"""
    title: NotRequired["str"]
    """<p>The title of the task.</p>"""
    execution_status: NotRequired[
        "capo_securityagent.types.task_execution_status.TaskExecutionStatus"
    ]
    """<p>The current execution status of the task.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The date and time the task was created, in UTC format.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The date and time the task was last updated, in UTC format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ThreatModelJobTaskSummary) -> dict:
    out: dict = {}
    out["taskId"] = value["task_id"]
    if "threat_model_id" in value:
        out["threatModelId"] = value["threat_model_id"]
    if "threat_model_job_id" in value:
        out["threatModelJobId"] = value["threat_model_job_id"]
    if "agent_space_id" in value:
        out["agentSpaceId"] = value["agent_space_id"]
    if "title" in value:
        out["title"] = value["title"]
    if "execution_status" in value:
        import capo_securityagent.types.task_execution_status

        out["executionStatus"] = (
            capo_securityagent.types.task_execution_status.serialize_json(
                value["execution_status"]
            )
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


def deserialize_json(data: dict) -> ThreatModelJobTaskSummary:
    out: ThreatModelJobTaskSummary = {}  # type: ignore[typeddict-item]
    if data.get("taskId") is not None:
        out["task_id"] = data["taskId"]
    else:
        out["task_id"] = ""
    if data.get("threatModelId") is not None:
        out["threat_model_id"] = data["threatModelId"]
    if data.get("threatModelJobId") is not None:
        out["threat_model_job_id"] = data["threatModelJobId"]
    if data.get("agentSpaceId") is not None:
        out["agent_space_id"] = data["agentSpaceId"]
    if data.get("title") is not None:
        out["title"] = data["title"]
    if data.get("executionStatus") is not None:
        import capo_securityagent.types.task_execution_status

        out["execution_status"] = (
            capo_securityagent.types.task_execution_status.deserialize_json(
                data["executionStatus"]
            )
        )
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
