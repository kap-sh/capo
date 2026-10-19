"""Generated from Smithy shape ``com.amazonaws.securityagent#StartCodeReviewJobInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.diff_source


class StartCodeReviewJobInput(TypedDict, closed=True):
    agent_space_id: "str"
    """<p>The unique identifier of the agent space.</p>"""
    code_review_id: "str"
    """<p>The unique identifier of the code review to start a job for.</p>"""
    diff_source: NotRequired["capo_securityagent.types.diff_source.DiffSource"]
    """<p>Source of the diff for a differential scan. When present, the job analyzes only the changed lines instead of performing a full scan.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartCodeReviewJobInput) -> dict:
    out: dict = {}
    out["agentSpaceId"] = value["agent_space_id"]
    out["codeReviewId"] = value["code_review_id"]
    if "diff_source" in value:
        import capo_securityagent.types.diff_source

        out["diffSource"] = capo_securityagent.types.diff_source.serialize_json(
            value["diff_source"]
        )
    return out


def deserialize_json(data: dict) -> StartCodeReviewJobInput:
    out: StartCodeReviewJobInput = {}  # type: ignore[typeddict-item]
    if data.get("agentSpaceId") is not None:
        out["agent_space_id"] = data["agentSpaceId"]
    else:
        out["agent_space_id"] = ""
    if data.get("codeReviewId") is not None:
        out["code_review_id"] = data["codeReviewId"]
    else:
        out["code_review_id"] = ""
    if data.get("diffSource") is not None:
        import capo_securityagent.types.diff_source

        out["diff_source"] = capo_securityagent.types.diff_source.deserialize_json(
            data["diffSource"]
        )
    return out
