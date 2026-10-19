"""Generated from Smithy shape ``com.amazonaws.codecommit#UpdateApprovalRuleTemplateContentInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.approval_rule_template_content
    import capo_codecommit.types.approval_rule_template_name
    import capo_codecommit.types.rule_content_sha256


class UpdateApprovalRuleTemplateContentInput(TypedDict, closed=True):
    approval_rule_template_name: (
        "capo_codecommit.types.approval_rule_template_name.ApprovalRuleTemplateName"
    )
    """<p>The name of the approval rule template where you want to update the content of the rule. </p>"""
    new_rule_content: "capo_codecommit.types.approval_rule_template_content.ApprovalRuleTemplateContent"
    """<p>The content that replaces the existing content of the rule. Content statements must be complete. You cannot provide only the changes.</p>"""
    existing_rule_content_sha256: NotRequired[
        "capo_codecommit.types.rule_content_sha256.RuleContentSha256"
    ]
    """<p>The SHA-256 hash signature for the content of the approval rule. You can retrieve this information by using <a>GetPullRequest</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateApprovalRuleTemplateContentInput) -> dict:
    out: dict = {}
    out["approvalRuleTemplateName"] = value["approval_rule_template_name"]
    out["newRuleContent"] = value["new_rule_content"]
    if "existing_rule_content_sha256" in value:
        out["existingRuleContentSha256"] = value["existing_rule_content_sha256"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateApprovalRuleTemplateContentInput:
    out: UpdateApprovalRuleTemplateContentInput = {}  # type: ignore[typeddict-item]
    if data.get("approvalRuleTemplateName") is not None:
        out["approval_rule_template_name"] = data["approvalRuleTemplateName"]
    else:
        out["approval_rule_template_name"] = ""
    if data.get("newRuleContent") is not None:
        out["new_rule_content"] = data["newRuleContent"]
    else:
        out["new_rule_content"] = ""
    if data.get("existingRuleContentSha256") is not None:
        out["existing_rule_content_sha256"] = data["existingRuleContentSha256"]
    return out
