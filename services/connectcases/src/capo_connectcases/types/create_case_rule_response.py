"""Generated from Smithy shape ``com.amazonaws.connectcases#CreateCaseRuleResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.case_rule_arn
    import capo_connectcases.types.case_rule_id


class CreateCaseRuleResponse(TypedDict, closed=True):
    case_rule_id: "capo_connectcases.types.case_rule_id.CaseRuleId"
    """<p>Unique identifier of a case rule.</p>"""
    case_rule_arn: "capo_connectcases.types.case_rule_arn.CaseRuleArn"
    """<p>The Amazon Resource Name (ARN) of a case rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCaseRuleResponse) -> dict:
    out: dict = {}
    out["caseRuleId"] = value["case_rule_id"]
    out["caseRuleArn"] = value["case_rule_arn"]
    return out


def deserialize_json(data: dict) -> CreateCaseRuleResponse:
    out: CreateCaseRuleResponse = {}  # type: ignore[typeddict-item]
    if data.get("caseRuleId") is not None:
        out["case_rule_id"] = data["caseRuleId"]
    else:
        out["case_rule_id"] = ""
    if data.get("caseRuleArn") is not None:
        out["case_rule_arn"] = data["caseRuleArn"]
    else:
        out["case_rule_arn"] = ""
    return out
