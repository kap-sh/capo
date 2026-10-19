"""Generated from Smithy shape ``com.amazonaws.codecommit#UpdateApprovalRuleTemplateNameInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.approval_rule_template_name


class UpdateApprovalRuleTemplateNameInput(TypedDict, closed=True):
    old_approval_rule_template_name: (
        "capo_codecommit.types.approval_rule_template_name.ApprovalRuleTemplateName"
    )
    """<p>The current name of the approval rule template.</p>"""
    new_approval_rule_template_name: (
        "capo_codecommit.types.approval_rule_template_name.ApprovalRuleTemplateName"
    )
    """<p>The new name you want to apply to the approval rule template.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateApprovalRuleTemplateNameInput) -> dict:
    out: dict = {}
    out["oldApprovalRuleTemplateName"] = value["old_approval_rule_template_name"]
    out["newApprovalRuleTemplateName"] = value["new_approval_rule_template_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateApprovalRuleTemplateNameInput:
    out: UpdateApprovalRuleTemplateNameInput = {}  # type: ignore[typeddict-item]
    if data.get("oldApprovalRuleTemplateName") is not None:
        out["old_approval_rule_template_name"] = data["oldApprovalRuleTemplateName"]
    else:
        out["old_approval_rule_template_name"] = ""
    if data.get("newApprovalRuleTemplateName") is not None:
        out["new_approval_rule_template_name"] = data["newApprovalRuleTemplateName"]
    else:
        out["new_approval_rule_template_name"] = ""
    return out
