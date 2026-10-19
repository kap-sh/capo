"""Generated from Smithy shape ``com.amazonaws.connectcases#BatchGetCaseRuleResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.batch_get_case_rule_error_list
    import capo_connectcases.types.batch_get_case_rule_list
    import capo_connectcases.types.batch_get_case_rule_unprocessed_list


class BatchGetCaseRuleResponse(TypedDict, closed=True):
    case_rules: "capo_connectcases.types.batch_get_case_rule_list.BatchGetCaseRuleList"
    """<p>A list of detailed case rule information.</p>"""
    errors: "capo_connectcases.types.batch_get_case_rule_error_list.BatchGetCaseRuleErrorList"
    """<p>A list of case rule errors.</p>"""
    unprocessed_case_rules: NotRequired[
        "capo_connectcases.types.batch_get_case_rule_unprocessed_list.BatchGetCaseRuleUnprocessedList"
    ]
    """<p>A list of unprocessed case rule identifiers.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetCaseRuleResponse) -> dict:
    out: dict = {}
    import capo_connectcases.types.batch_get_case_rule_list

    out["caseRules"] = capo_connectcases.types.batch_get_case_rule_list.serialize_json(
        value["case_rules"]
    )
    import capo_connectcases.types.batch_get_case_rule_error_list

    out["errors"] = (
        capo_connectcases.types.batch_get_case_rule_error_list.serialize_json(
            value["errors"]
        )
    )
    if "unprocessed_case_rules" in value:
        import capo_connectcases.types.batch_get_case_rule_unprocessed_list

        out["unprocessedCaseRules"] = (
            capo_connectcases.types.batch_get_case_rule_unprocessed_list.serialize_json(
                value["unprocessed_case_rules"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchGetCaseRuleResponse:
    out: BatchGetCaseRuleResponse = {}  # type: ignore[typeddict-item]
    if data.get("caseRules") is not None:
        import capo_connectcases.types.batch_get_case_rule_list

        out["case_rules"] = (
            capo_connectcases.types.batch_get_case_rule_list.deserialize_json(
                data["caseRules"]
            )
        )
    else:
        out["case_rules"] = []
    if data.get("errors") is not None:
        import capo_connectcases.types.batch_get_case_rule_error_list

        out["errors"] = (
            capo_connectcases.types.batch_get_case_rule_error_list.deserialize_json(
                data["errors"]
            )
        )
    else:
        out["errors"] = []
    if data.get("unprocessedCaseRules") is not None:
        import capo_connectcases.types.batch_get_case_rule_unprocessed_list

        out["unprocessed_case_rules"] = (
            capo_connectcases.types.batch_get_case_rule_unprocessed_list.deserialize_json(
                data["unprocessedCaseRules"]
            )
        )
    return out
