"""Generated from Smithy shape ``com.amazonaws.securityagent#BatchDisassociateFindingIssueInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.finding_id_list


class BatchDisassociateFindingIssueInput(TypedDict, closed=True):
    agent_space_id: "str"
    """<p>The identifier of the agent space where the job exists.</p>"""
    pentest_job_id: NotRequired["str"]
    """<p>The identifier of the penetration test job. This parameter is mutually exclusive with <code>codeReviewJobId</code>.</p>"""
    code_review_job_id: NotRequired["str"]
    """<p>The identifier of the code review job. This parameter is mutually exclusive with <code>pentestJobId</code>.</p>"""
    finding_ids: "capo_securityagent.types.finding_id_list.FindingIdList"
    """<p>The identifiers of the findings to disassociate from their issues. Each must belong to the specified job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDisassociateFindingIssueInput) -> dict:
    out: dict = {}
    out["agentSpaceId"] = value["agent_space_id"]
    if "pentest_job_id" in value:
        out["pentestJobId"] = value["pentest_job_id"]
    if "code_review_job_id" in value:
        out["codeReviewJobId"] = value["code_review_job_id"]
    import capo_securityagent.types.finding_id_list

    out["findingIds"] = capo_securityagent.types.finding_id_list.serialize_json(
        value["finding_ids"]
    )
    return out


def deserialize_json(data: dict) -> BatchDisassociateFindingIssueInput:
    out: BatchDisassociateFindingIssueInput = {}  # type: ignore[typeddict-item]
    if data.get("agentSpaceId") is not None:
        out["agent_space_id"] = data["agentSpaceId"]
    else:
        out["agent_space_id"] = ""
    if data.get("pentestJobId") is not None:
        out["pentest_job_id"] = data["pentestJobId"]
    if data.get("codeReviewJobId") is not None:
        out["code_review_job_id"] = data["codeReviewJobId"]
    if data.get("findingIds") is not None:
        import capo_securityagent.types.finding_id_list

        out["finding_ids"] = capo_securityagent.types.finding_id_list.deserialize_json(
            data["findingIds"]
        )
    else:
        out["finding_ids"] = []
    return out
