"""Generated from Smithy shape ``com.amazonaws.connectcases#TemplateRule``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.case_rule_id
    import capo_connectcases.types.field_id


class TemplateRule(TypedDict, closed=True):
    case_rule_id: "capo_connectcases.types.case_rule_id.CaseRuleId"
    """<p>Unique identifier of a case rule.</p>"""
    field_id: "capo_connectcases.types.field_id.FieldId"
    """<p>Unique identifier of a field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TemplateRule) -> dict:
    out: dict = {}
    out["caseRuleId"] = value["case_rule_id"]
    out["fieldId"] = value.get("field_id", "NULL")
    return out


def deserialize_json(data: dict) -> TemplateRule:
    out: TemplateRule = {}  # type: ignore[typeddict-item]
    if data.get("caseRuleId") is not None:
        out["case_rule_id"] = data["caseRuleId"]
    else:
        out["case_rule_id"] = ""
    if data.get("fieldId") is not None:
        out["field_id"] = data["fieldId"]
    else:
        out["field_id"] = "NULL"
    return out
