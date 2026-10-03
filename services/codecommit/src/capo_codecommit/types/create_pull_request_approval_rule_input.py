"""Generated from Smithy shape ``com.amazonaws.codecommit#CreatePullRequestApprovalRuleInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_codecommit.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codecommit.types.approval_rule_content
    import capo_codecommit.types.approval_rule_name
    import capo_codecommit.types.pull_request_id


class CreatePullRequestApprovalRuleInput(TypedDict, closed=True):
    pull_request_id: "capo_codecommit.types.pull_request_id.PullRequestId"
    """<p>The system-generated ID of the pull request for which you want to create the approval rule.</p>"""
    approval_rule_name: "capo_codecommit.types.approval_rule_name.ApprovalRuleName"
    """<p>The name for the approval rule.</p>"""
    approval_rule_content: (
        "capo_codecommit.types.approval_rule_content.ApprovalRuleContent"
    )
    """<p>The content of the approval rule, including the number of approvals needed and the structure of an approval pool defined for approvals, if any. For more information about approval pools, see the CodeCommit User Guide.</p> <note> <p>When you create the content of the approval rule, you can specify approvers in an approval pool in one of two ways:</p> <ul> <li> <p> <b>CodeCommitApprovers</b>: This option only requires an Amazon Web Services account and a resource. It can be used for both IAM users and federated access users whose name matches the provided resource name. This is a very powerful option that offers a great deal of flexibility. For example, if you specify the Amazon Web Services account <i>123456789012</i> and <i>Mary_Major</i>, all of the following would be counted as approvals coming from that user:</p> <ul> <li> <p>An IAM user in the account (arn:aws:iam::<i>123456789012</i>:user/<i>Mary_Major</i>)</p> </li> <li> <p>A federated user identified in IAM as Mary_Major (arn:aws:sts::<i>123456789012</i>:federated-user/<i>Mary_Major</i>)</p> </li> </ul> <p>This option does not recognize an active session of someone assuming the role of CodeCommitReview with a role session name of <i>Mary_Major</i> (arn:aws:sts::<i>123456789012</i>:assumed-role/CodeCommitReview/<i>Mary_Major</i>) unless you include a wildcard (*Mary_Major).</p> </li> <li> <p> <b>Fully qualified ARN</b>: This option allows you to specify the fully qualified Amazon Resource Name (ARN) of the IAM user or role. </p> </li> </ul> <p>For more information about IAM ARNs, wildcards, and formats, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html">IAM Identifiers</a> in the <i>IAM User Guide</i>.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreatePullRequestApprovalRuleInput) -> dict:
    out: dict = {}
    out["pullRequestId"] = value["pull_request_id"]
    out["approvalRuleName"] = value["approval_rule_name"]
    out["approvalRuleContent"] = value["approval_rule_content"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreatePullRequestApprovalRuleInput:
    out: CreatePullRequestApprovalRuleInput = {}  # type: ignore[typeddict-item]
    if data.get("pullRequestId") is not None:
        out["pull_request_id"] = data["pullRequestId"]
    else:
        raise DeserializationError(
            "CreatePullRequestApprovalRuleInput.pull_request_id required"
        )
    if data.get("approvalRuleName") is not None:
        out["approval_rule_name"] = data["approvalRuleName"]
    else:
        raise DeserializationError(
            "CreatePullRequestApprovalRuleInput.approval_rule_name required"
        )
    if data.get("approvalRuleContent") is not None:
        out["approval_rule_content"] = data["approvalRuleContent"]
    else:
        raise DeserializationError(
            "CreatePullRequestApprovalRuleInput.approval_rule_content required"
        )
    return out
