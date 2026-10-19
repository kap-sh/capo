"""Generated from Smithy shape ``com.amazonaws.codecommit#UpdateApprovalRuleTemplateDescriptionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.approval_rule_template_description
    import capo_codecommit.types.approval_rule_template_name


class UpdateApprovalRuleTemplateDescriptionInput(TypedDict, closed=True):
    approval_rule_template_name: (
        "capo_codecommit.types.approval_rule_template_name.ApprovalRuleTemplateName"
    )
    """<p>The name of the template for which you want to update the description.</p>"""
    approval_rule_template_description: "capo_codecommit.types.approval_rule_template_description.ApprovalRuleTemplateDescription"
    """<p>The updated description of the approval rule template.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateApprovalRuleTemplateDescriptionInput) -> dict:
    out: dict = {}
    out["approvalRuleTemplateName"] = value["approval_rule_template_name"]
    out["approvalRuleTemplateDescription"] = value["approval_rule_template_description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateApprovalRuleTemplateDescriptionInput:
    out: UpdateApprovalRuleTemplateDescriptionInput = {}  # type: ignore[typeddict-item]
    if data.get("approvalRuleTemplateName") is not None:
        out["approval_rule_template_name"] = data["approvalRuleTemplateName"]
    else:
        out["approval_rule_template_name"] = ""
    if data.get("approvalRuleTemplateDescription") is not None:
        out["approval_rule_template_description"] = data[
            "approvalRuleTemplateDescription"
        ]
    else:
        out["approval_rule_template_description"] = ""
    return out
