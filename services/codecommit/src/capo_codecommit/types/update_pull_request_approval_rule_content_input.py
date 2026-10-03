"""Generated from Smithy shape ``com.amazonaws.codecommit#UpdatePullRequestApprovalRuleContentInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codecommit.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codecommit.types.approval_rule_content
    import capo_codecommit.types.approval_rule_name
    import capo_codecommit.types.pull_request_id
    import capo_codecommit.types.rule_content_sha256


class UpdatePullRequestApprovalRuleContentInput(TypedDict, closed=True):
    pull_request_id: "capo_codecommit.types.pull_request_id.PullRequestId"
    """<p>The system-generated ID of the pull request.</p>"""
    approval_rule_name: "capo_codecommit.types.approval_rule_name.ApprovalRuleName"
    """<p>The name of the approval rule you want to update.</p>"""
    existing_rule_content_sha256: NotRequired[
        "capo_codecommit.types.rule_content_sha256.RuleContentSha256"
    ]
    """<p>The SHA-256 hash signature for the content of the approval rule. You can retrieve this information by using <a>GetPullRequest</a>.</p>"""
    new_rule_content: "capo_codecommit.types.approval_rule_content.ApprovalRuleContent"
    """<p>The updated content for the approval rule.</p> <note> <p>When you update the content of the approval rule, you can specify approvers in an approval pool in one of two ways:</p> <ul> <li> <p> <b>CodeCommitApprovers</b>: This option only requires an Amazon Web Services account and a resource. It can be used for both IAM users and federated access users whose name matches the provided resource name. This is a very powerful option that offers a great deal of flexibility. For example, if you specify the Amazon Web Services account <i>123456789012</i> and <i>Mary_Major</i>, all of the following are counted as approvals coming from that user:</p> <ul> <li> <p>An IAM user in the account (arn:aws:iam::<i>123456789012</i>:user/<i>Mary_Major</i>)</p> </li> <li> <p>A federated user identified in IAM as Mary_Major (arn:aws:sts::<i>123456789012</i>:federated-user/<i>Mary_Major</i>)</p> </li> </ul> <p>This option does not recognize an active session of someone assuming the role of CodeCommitReview with a role session name of <i>Mary_Major</i> (arn:aws:sts::<i>123456789012</i>:assumed-role/CodeCommitReview/<i>Mary_Major</i>) unless you include a wildcard (*Mary_Major).</p> </li> <li> <p> <b>Fully qualified ARN</b>: This option allows you to specify the fully qualified Amazon Resource Name (ARN) of the IAM user or role. </p> </li> </ul> <p>For more information about IAM ARNs, wildcards, and formats, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html">IAM Identifiers</a> in the <i>IAM User Guide</i>.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdatePullRequestApprovalRuleContentInput) -> dict:
    out: dict = {}
    out["pullRequestId"] = value["pull_request_id"]
    out["approvalRuleName"] = value["approval_rule_name"]
    if "existing_rule_content_sha256" in value:
        out["existingRuleContentSha256"] = value["existing_rule_content_sha256"]
    out["newRuleContent"] = value["new_rule_content"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdatePullRequestApprovalRuleContentInput:
    out: UpdatePullRequestApprovalRuleContentInput = {}  # type: ignore[typeddict-item]
    if data.get("pullRequestId") is not None:
        out["pull_request_id"] = data["pullRequestId"]
    else:
        raise DeserializationError(
            "UpdatePullRequestApprovalRuleContentInput.pull_request_id required"
        )
    if data.get("approvalRuleName") is not None:
        out["approval_rule_name"] = data["approvalRuleName"]
    else:
        raise DeserializationError(
            "UpdatePullRequestApprovalRuleContentInput.approval_rule_name required"
        )
    if data.get("existingRuleContentSha256") is not None:
        out["existing_rule_content_sha256"] = data["existingRuleContentSha256"]
    if data.get("newRuleContent") is not None:
        out["new_rule_content"] = data["newRuleContent"]
    else:
        raise DeserializationError(
            "UpdatePullRequestApprovalRuleContentInput.new_rule_content required"
        )
    return out
