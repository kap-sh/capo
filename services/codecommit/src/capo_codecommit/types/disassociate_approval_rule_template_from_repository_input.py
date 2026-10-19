"""Generated from Smithy shape ``com.amazonaws.codecommit#DisassociateApprovalRuleTemplateFromRepositoryInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.approval_rule_template_name
    import capo_codecommit.types.repository_name


class DisassociateApprovalRuleTemplateFromRepositoryInput(TypedDict, closed=True):
    approval_rule_template_name: (
        "capo_codecommit.types.approval_rule_template_name.ApprovalRuleTemplateName"
    )
    """<p>The name of the approval rule template to disassociate from a specified repository.</p>"""
    repository_name: "capo_codecommit.types.repository_name.RepositoryName"
    """<p>The name of the repository you want to disassociate from the template.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DisassociateApprovalRuleTemplateFromRepositoryInput,
) -> dict:
    out: dict = {}
    out["approvalRuleTemplateName"] = value["approval_rule_template_name"]
    out["repositoryName"] = value["repository_name"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DisassociateApprovalRuleTemplateFromRepositoryInput:
    out: DisassociateApprovalRuleTemplateFromRepositoryInput = {}  # type: ignore[typeddict-item]
    if data.get("approvalRuleTemplateName") is not None:
        out["approval_rule_template_name"] = data["approvalRuleTemplateName"]
    else:
        out["approval_rule_template_name"] = ""
    if data.get("repositoryName") is not None:
        out["repository_name"] = data["repositoryName"]
    else:
        out["repository_name"] = ""
    return out
