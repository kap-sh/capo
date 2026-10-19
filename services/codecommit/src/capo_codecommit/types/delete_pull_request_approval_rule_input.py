"""Generated from Smithy shape ``com.amazonaws.codecommit#DeletePullRequestApprovalRuleInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.approval_rule_name
    import capo_codecommit.types.pull_request_id


class DeletePullRequestApprovalRuleInput(TypedDict, closed=True):
    pull_request_id: "capo_codecommit.types.pull_request_id.PullRequestId"
    """<p>The system-generated ID of the pull request that contains the approval rule you want to delete.</p>"""
    approval_rule_name: "capo_codecommit.types.approval_rule_name.ApprovalRuleName"
    """<p>The name of the approval rule you want to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeletePullRequestApprovalRuleInput) -> dict:
    out: dict = {}
    out["pullRequestId"] = value["pull_request_id"]
    out["approvalRuleName"] = value["approval_rule_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeletePullRequestApprovalRuleInput:
    out: DeletePullRequestApprovalRuleInput = {}  # type: ignore[typeddict-item]
    if data.get("pullRequestId") is not None:
        out["pull_request_id"] = data["pullRequestId"]
    else:
        out["pull_request_id"] = ""
    if data.get("approvalRuleName") is not None:
        out["approval_rule_name"] = data["approvalRuleName"]
    else:
        out["approval_rule_name"] = ""
    return out
