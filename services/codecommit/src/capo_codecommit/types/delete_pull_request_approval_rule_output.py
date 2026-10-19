"""Generated from Smithy shape ``com.amazonaws.codecommit#DeletePullRequestApprovalRuleOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.approval_rule_id


class DeletePullRequestApprovalRuleOutput(TypedDict, closed=True):
    approval_rule_id: "capo_codecommit.types.approval_rule_id.ApprovalRuleId"
    """<p>The ID of the deleted approval rule. </p> <note> <p>If the approval rule was deleted in an earlier API call, the response is 200 OK without content.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeletePullRequestApprovalRuleOutput) -> dict:
    out: dict = {}
    out["approvalRuleId"] = value["approval_rule_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeletePullRequestApprovalRuleOutput:
    out: DeletePullRequestApprovalRuleOutput = {}  # type: ignore[typeddict-item]
    if data.get("approvalRuleId") is not None:
        out["approval_rule_id"] = data["approvalRuleId"]
    else:
        out["approval_rule_id"] = ""
    return out
