"""Generated from Smithy shape ``com.amazonaws.connectcases#CaseRuleSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.case_rule_arn
    import capo_connectcases.types.case_rule_description
    import capo_connectcases.types.case_rule_id
    import capo_connectcases.types.case_rule_name
    import capo_connectcases.types.rule_type


class CaseRuleSummary(TypedDict, closed=True):
    case_rule_id: "capo_connectcases.types.case_rule_id.CaseRuleId"
    """<p>Unique identifier of a case rule.</p>"""
    name: "capo_connectcases.types.case_rule_name.CaseRuleName"
    """<p>Name of the case rule.</p>"""
    case_rule_arn: "capo_connectcases.types.case_rule_arn.CaseRuleArn"
    """<p>The Amazon Resource Name (ARN) of the case rule. </p>"""
    rule_type: "capo_connectcases.types.rule_type.RuleType"
    """<p>Possible types for a rule.</p>"""
    description: NotRequired[
        "capo_connectcases.types.case_rule_description.CaseRuleDescription"
    ]
    """<p>Description of a case rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CaseRuleSummary) -> dict:
    out: dict = {}
    out["caseRuleId"] = value["case_rule_id"]
    out["name"] = value["name"]
    out["caseRuleArn"] = value["case_rule_arn"]
    out["ruleType"] = value["rule_type"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> CaseRuleSummary:
    out: CaseRuleSummary = {}  # type: ignore[typeddict-item]
    if data.get("caseRuleId") is not None:
        out["case_rule_id"] = data["caseRuleId"]
    else:
        out["case_rule_id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("caseRuleArn") is not None:
        out["case_rule_arn"] = data["caseRuleArn"]
    else:
        out["case_rule_arn"] = ""
    if data.get("ruleType") is not None:
        out["rule_type"] = data["ruleType"]
    else:
        out["rule_type"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    return out
