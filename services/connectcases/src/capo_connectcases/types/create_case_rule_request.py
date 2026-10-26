"""Generated from Smithy shape ``com.amazonaws.connectcases#CreateCaseRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.case_rule_description
    import capo_connectcases.types.case_rule_details
    import capo_connectcases.types.case_rule_name
    import capo_connectcases.types.domain_id


class CreateCaseRuleRequest(TypedDict, closed=True):
    domain_id: "capo_connectcases.types.domain_id.DomainId"
    """<p>Unique identifier of a Cases domain.</p>"""
    name: "capo_connectcases.types.case_rule_name.CaseRuleName"
    """<p>Name of the case rule.</p>"""
    description: NotRequired[
        "capo_connectcases.types.case_rule_description.CaseRuleDescription"
    ]
    """<p>The description of a case rule.</p>"""
    rule: "capo_connectcases.types.case_rule_details.CaseRuleDetails"
    """<p>Represents what rule type should take place, under what conditions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCaseRuleRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_connectcases.types.case_rule_details

    out["rule"] = capo_connectcases.types.case_rule_details.serialize_json(
        value["rule"]
    )
    return out


def deserialize_json(data: dict) -> CreateCaseRuleRequest:
    out: CreateCaseRuleRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("rule") is not None:
        import capo_connectcases.types.case_rule_details

        out["rule"] = capo_connectcases.types.case_rule_details.deserialize_json(
            data["rule"]
        )
    else:
        out["rule"] = {"$unknown": {"name": ""}}
    return out
