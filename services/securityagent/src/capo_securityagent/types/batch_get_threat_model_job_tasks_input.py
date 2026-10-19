"""Generated from Smithy shape ``com.amazonaws.securityagent#BatchGetThreatModelJobTasksInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.task_id_list


class BatchGetThreatModelJobTasksInput(TypedDict, closed=True):
    agent_space_id: "str"
    """<p>The unique identifier of the agent space that contains the tasks.</p>"""
    threat_model_job_task_ids: "capo_securityagent.types.task_id_list.TaskIdList"
    """<p>The list of task identifiers to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetThreatModelJobTasksInput) -> dict:
    out: dict = {}
    out["agentSpaceId"] = value["agent_space_id"]
    import capo_securityagent.types.task_id_list

    out["threatModelJobTaskIds"] = capo_securityagent.types.task_id_list.serialize_json(
        value["threat_model_job_task_ids"]
    )
    return out


def deserialize_json(data: dict) -> BatchGetThreatModelJobTasksInput:
    out: BatchGetThreatModelJobTasksInput = {}  # type: ignore[typeddict-item]
    if data.get("agentSpaceId") is not None:
        out["agent_space_id"] = data["agentSpaceId"]
    else:
        out["agent_space_id"] = ""
    if data.get("threatModelJobTaskIds") is not None:
        import capo_securityagent.types.task_id_list

        out["threat_model_job_task_ids"] = (
            capo_securityagent.types.task_id_list.deserialize_json(
                data["threatModelJobTaskIds"]
            )
        )
    else:
        out["threat_model_job_task_ids"] = []
    return out
