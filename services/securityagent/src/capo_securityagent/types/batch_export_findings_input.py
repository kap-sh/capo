"""Generated from Smithy shape ``com.amazonaws.securityagent#BatchExportFindingsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_securityagent.types.finding_id_list
    import capo_securityagent.types.issue_destination


class BatchExportFindingsInput(TypedDict, closed=True):
    agent_space_id: "str"
    """<p>The identifier of the agent space where the job exists.</p>"""
    pentest_job_id: NotRequired["str"]
    """<p>The identifier of the penetration test job. This parameter is mutually exclusive with <code>codeReviewJobId</code>.</p>"""
    code_review_job_id: NotRequired["str"]
    """<p>The identifier of the code review job. This parameter is mutually exclusive with <code>pentestJobId</code>.</p>"""
    issue_destination: "capo_securityagent.types.issue_destination.IssueDestination"
    """<p>The destination issue-tracker project the findings are exported to. Must be a connected capability of the agent space.</p>"""
    finding_ids: "capo_securityagent.types.finding_id_list.FindingIdList"
    """<p>The identifiers of the findings to export. Each must belong to the specified job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchExportFindingsInput) -> dict:
    out: dict = {}
    out["agentSpaceId"] = value["agent_space_id"]
    if "pentest_job_id" in value:
        out["pentestJobId"] = value["pentest_job_id"]
    if "code_review_job_id" in value:
        out["codeReviewJobId"] = value["code_review_job_id"]
    import capo_securityagent.types.issue_destination

    out["issueDestination"] = capo_securityagent.types.issue_destination.serialize_json(
        value["issue_destination"]
    )
    import capo_securityagent.types.finding_id_list

    out["findingIds"] = capo_securityagent.types.finding_id_list.serialize_json(
        value["finding_ids"]
    )
    return out


def deserialize_json(data: dict) -> BatchExportFindingsInput:
    out: BatchExportFindingsInput = {}  # type: ignore[typeddict-item]
    if data.get("agentSpaceId") is not None:
        out["agent_space_id"] = data["agentSpaceId"]
    else:
        raise DeserializationError("BatchExportFindingsInput.agent_space_id required")
    if data.get("pentestJobId") is not None:
        out["pentest_job_id"] = data["pentestJobId"]
    if data.get("codeReviewJobId") is not None:
        out["code_review_job_id"] = data["codeReviewJobId"]
    if data.get("issueDestination") is not None:
        import capo_securityagent.types.issue_destination

        out["issue_destination"] = (
            capo_securityagent.types.issue_destination.deserialize_json(
                data["issueDestination"]
            )
        )
    else:
        raise DeserializationError(
            "BatchExportFindingsInput.issue_destination required"
        )
    if data.get("findingIds") is not None:
        import capo_securityagent.types.finding_id_list

        out["finding_ids"] = capo_securityagent.types.finding_id_list.deserialize_json(
            data["findingIds"]
        )
    else:
        raise DeserializationError("BatchExportFindingsInput.finding_ids required")
    return out
