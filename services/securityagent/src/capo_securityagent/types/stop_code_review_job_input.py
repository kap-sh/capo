"""Generated from Smithy shape ``com.amazonaws.securityagent#StopCodeReviewJobInput``."""

from typing_extensions import TypedDict


class StopCodeReviewJobInput(TypedDict, closed=True):
    agent_space_id: "str"
    """<p>The unique identifier of the agent space.</p>"""
    code_review_job_id: "str"
    """<p>The unique identifier of the code review job to stop.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopCodeReviewJobInput) -> dict:
    out: dict = {}
    out["agentSpaceId"] = value["agent_space_id"]
    out["codeReviewJobId"] = value["code_review_job_id"]
    return out


def deserialize_json(data: dict) -> StopCodeReviewJobInput:
    out: StopCodeReviewJobInput = {}  # type: ignore[typeddict-item]
    if data.get("agentSpaceId") is not None:
        out["agent_space_id"] = data["agentSpaceId"]
    else:
        out["agent_space_id"] = ""
    if data.get("codeReviewJobId") is not None:
        out["code_review_job_id"] = data["codeReviewJobId"]
    else:
        out["code_review_job_id"] = ""
    return out
