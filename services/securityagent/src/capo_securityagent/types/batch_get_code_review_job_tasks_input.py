"""Generated from Smithy shape ``com.amazonaws.securityagent#BatchGetCodeReviewJobTasksInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.task_id_list


class BatchGetCodeReviewJobTasksInput(TypedDict, closed=True):
    agent_space_id: "str"
    """<p>The unique identifier of the agent space that contains the tasks.</p>"""
    code_review_job_task_ids: "capo_securityagent.types.task_id_list.TaskIdList"
    """<p>The list of task identifiers to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetCodeReviewJobTasksInput) -> dict:
    out: dict = {}
    out["agentSpaceId"] = value["agent_space_id"]
    import capo_securityagent.types.task_id_list

    out["codeReviewJobTaskIds"] = capo_securityagent.types.task_id_list.serialize_json(
        value["code_review_job_task_ids"]
    )
    return out


def deserialize_json(data: dict) -> BatchGetCodeReviewJobTasksInput:
    out: BatchGetCodeReviewJobTasksInput = {}  # type: ignore[typeddict-item]
    if data.get("agentSpaceId") is not None:
        out["agent_space_id"] = data["agentSpaceId"]
    else:
        out["agent_space_id"] = ""
    if data.get("codeReviewJobTaskIds") is not None:
        import capo_securityagent.types.task_id_list

        out["code_review_job_task_ids"] = (
            capo_securityagent.types.task_id_list.deserialize_json(
                data["codeReviewJobTaskIds"]
            )
        )
    else:
        out["code_review_job_task_ids"] = []
    return out
