"""Generated from Smithy shape ``com.amazonaws.codecommit#CreateApprovalRuleTemplateInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codecommit.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codecommit.types.approval_rule_template_content
    import capo_codecommit.types.approval_rule_template_description
    import capo_codecommit.types.approval_rule_template_name


class CreateApprovalRuleTemplateInput(TypedDict, closed=True):
    approval_rule_template_name: (
        "capo_codecommit.types.approval_rule_template_name.ApprovalRuleTemplateName"
    )
    """<p>The name of the approval rule template. Provide descriptive names, because this name is applied to the approval rules created automatically in associated repositories.</p>"""
    approval_rule_template_content: "capo_codecommit.types.approval_rule_template_content.ApprovalRuleTemplateContent"
    """<p>The content of the approval rule that is created on pull requests in associated repositories. If you specify one or more destination references (branches), approval rules are created in an associated repository only if their destination references (branches) match those specified in the template.</p> <note> <p>When you create the content of the approval rule template, you can specify approvers in an approval pool in one of two ways:</p> <ul> <li> <p> <b>CodeCommitApprovers</b>: This option only requires an Amazon Web Services account and a resource. It can be used for both IAM users and federated access users whose name matches the provided resource name. This is a very powerful option that offers a great deal of flexibility. For example, if you specify the Amazon Web Services account <i>123456789012</i> and <i>Mary_Major</i>, all of the following are counted as approvals coming from that user:</p> <ul> <li> <p>An IAM user in the account (arn:aws:iam::<i>123456789012</i>:user/<i>Mary_Major</i>)</p> </li> <li> <p>A federated user identified in IAM as Mary_Major (arn:aws:sts::<i>123456789012</i>:federated-user/<i>Mary_Major</i>)</p> </li> </ul> <p>This option does not recognize an active session of someone assuming the role of CodeCommitReview with a role session name of <i>Mary_Major</i> (arn:aws:sts::<i>123456789012</i>:assumed-role/CodeCommitReview/<i>Mary_Major</i>) unless you include a wildcard (*Mary_Major).</p> </li> <li> <p> <b>Fully qualified ARN</b>: This option allows you to specify the fully qualified Amazon Resource Name (ARN) of the IAM user or role. </p> </li> </ul> <p>For more information about IAM ARNs, wildcards, and formats, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html">IAM Identifiers</a> in the <i>IAM User Guide</i>.</p> </note>"""
    approval_rule_template_description: NotRequired[
        "capo_codecommit.types.approval_rule_template_description.ApprovalRuleTemplateDescription"
    ]
    """<p>The description of the approval rule template. Consider providing a description that explains what this template does and when it might be appropriate to associate it with repositories.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateApprovalRuleTemplateInput) -> dict:
    out: dict = {}
    out["approvalRuleTemplateName"] = value["approval_rule_template_name"]
    out["approvalRuleTemplateContent"] = value["approval_rule_template_content"]
    if "approval_rule_template_description" in value:
        out["approvalRuleTemplateDescription"] = value[
            "approval_rule_template_description"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateApprovalRuleTemplateInput:
    out: CreateApprovalRuleTemplateInput = {}  # type: ignore[typeddict-item]
    if data.get("approvalRuleTemplateName") is not None:
        out["approval_rule_template_name"] = data["approvalRuleTemplateName"]
    else:
        raise DeserializationError(
            "CreateApprovalRuleTemplateInput.approval_rule_template_name required"
        )
    if data.get("approvalRuleTemplateContent") is not None:
        out["approval_rule_template_content"] = data["approvalRuleTemplateContent"]
    else:
        raise DeserializationError(
            "CreateApprovalRuleTemplateInput.approval_rule_template_content required"
        )
    if data.get("approvalRuleTemplateDescription") is not None:
        out["approval_rule_template_description"] = data[
            "approvalRuleTemplateDescription"
        ]
    return out
