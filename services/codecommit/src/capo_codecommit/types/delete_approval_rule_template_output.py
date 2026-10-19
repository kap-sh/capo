"""Generated from Smithy shape ``com.amazonaws.codecommit#DeleteApprovalRuleTemplateOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.approval_rule_template_id


class DeleteApprovalRuleTemplateOutput(TypedDict, closed=True):
    approval_rule_template_id: (
        "capo_codecommit.types.approval_rule_template_id.ApprovalRuleTemplateId"
    )
    """<p>The system-generated ID of the deleted approval rule template. If the template has been previously deleted, the only response is a 200 OK.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteApprovalRuleTemplateOutput) -> dict:
    out: dict = {}
    out["approvalRuleTemplateId"] = value["approval_rule_template_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteApprovalRuleTemplateOutput:
    out: DeleteApprovalRuleTemplateOutput = {}  # type: ignore[typeddict-item]
    if data.get("approvalRuleTemplateId") is not None:
        out["approval_rule_template_id"] = data["approvalRuleTemplateId"]
    else:
        out["approval_rule_template_id"] = ""
    return out
