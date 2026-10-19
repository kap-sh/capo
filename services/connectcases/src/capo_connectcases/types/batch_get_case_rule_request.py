"""Generated from Smithy shape ``com.amazonaws.connectcases#BatchGetCaseRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.case_rule_identifier_list
    import capo_connectcases.types.domain_id


class BatchGetCaseRuleRequest(TypedDict, closed=True):
    domain_id: "capo_connectcases.types.domain_id.DomainId"
    """<p>Unique identifier of a Cases domain.</p>"""
    case_rules: (
        "capo_connectcases.types.case_rule_identifier_list.CaseRuleIdentifierList"
    )
    """<p>A list of case rule identifiers.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetCaseRuleRequest) -> dict:
    out: dict = {}
    import capo_connectcases.types.case_rule_identifier_list

    out["caseRules"] = capo_connectcases.types.case_rule_identifier_list.serialize_json(
        value["case_rules"]
    )
    return out


def deserialize_json(data: dict) -> BatchGetCaseRuleRequest:
    out: BatchGetCaseRuleRequest = {}  # type: ignore[typeddict-item]
    if data.get("caseRules") is not None:
        import capo_connectcases.types.case_rule_identifier_list

        out["case_rules"] = (
            capo_connectcases.types.case_rule_identifier_list.deserialize_json(
                data["caseRules"]
            )
        )
    else:
        out["case_rules"] = []
    return out
