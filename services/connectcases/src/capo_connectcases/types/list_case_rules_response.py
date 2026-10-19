"""Generated from Smithy shape ``com.amazonaws.connectcases#ListCaseRulesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.case_rule_summary_list
    import capo_connectcases.types.next_token


class ListCaseRulesResponse(TypedDict, closed=True):
    case_rules: "capo_connectcases.types.case_rule_summary_list.CaseRuleSummaryList"
    """<p>A list of field summary objects.</p>"""
    next_token: NotRequired["capo_connectcases.types.next_token.NextToken"]
    """<p>The token for the next set of results. This is null if there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCaseRulesResponse) -> dict:
    out: dict = {}
    import capo_connectcases.types.case_rule_summary_list

    out["caseRules"] = capo_connectcases.types.case_rule_summary_list.serialize_json(
        value["case_rules"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListCaseRulesResponse:
    out: ListCaseRulesResponse = {}  # type: ignore[typeddict-item]
    if data.get("caseRules") is not None:
        import capo_connectcases.types.case_rule_summary_list

        out["case_rules"] = (
            capo_connectcases.types.case_rule_summary_list.deserialize_json(
                data["caseRules"]
            )
        )
    else:
        out["case_rules"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
