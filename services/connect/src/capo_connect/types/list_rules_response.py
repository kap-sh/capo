"""Generated from Smithy shape ``com.amazonaws.connect#ListRulesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.next_token
    import capo_connect.types.rule_summary_list


class ListRulesResponse(TypedDict, closed=True):
    rule_summary_list: "capo_connect.types.rule_summary_list.RuleSummaryList"
    """<p>Summary information about a rule.</p>"""
    next_token: NotRequired["capo_connect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRulesResponse) -> dict:
    out: dict = {}
    import capo_connect.types.rule_summary_list

    out["RuleSummaryList"] = capo_connect.types.rule_summary_list.serialize_json(
        value["rule_summary_list"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRulesResponse:
    out: ListRulesResponse = {}  # type: ignore[typeddict-item]
    if data.get("RuleSummaryList") is not None:
        import capo_connect.types.rule_summary_list

        out["rule_summary_list"] = (
            capo_connect.types.rule_summary_list.deserialize_json(
                data["RuleSummaryList"]
            )
        )
    else:
        out["rule_summary_list"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
