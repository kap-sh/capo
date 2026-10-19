"""Generated from Smithy shape ``com.amazonaws.connect#SearchRulesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.approximate_total_count
    import capo_connect.types.next_token2500
    import capo_connect.types.rule_search_summary_list


class SearchRulesResponse(TypedDict, closed=True):
    rules: "capo_connect.types.rule_search_summary_list.RuleSearchSummaryList"
    """<p>Information about the rules.</p>"""
    approximate_total_count: NotRequired[
        "capo_connect.types.approximate_total_count.ApproximateTotalCount"
    ]
    """<p>The total number of rules which matched your search query.</p>"""
    next_token: NotRequired["capo_connect.types.next_token2500.NextToken2500"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchRulesResponse) -> dict:
    out: dict = {}
    import capo_connect.types.rule_search_summary_list

    out["Rules"] = capo_connect.types.rule_search_summary_list.serialize_json(
        value["rules"]
    )
    if "approximate_total_count" in value:
        out["ApproximateTotalCount"] = value["approximate_total_count"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> SearchRulesResponse:
    out: SearchRulesResponse = {}  # type: ignore[typeddict-item]
    if data.get("Rules") is not None:
        import capo_connect.types.rule_search_summary_list

        out["rules"] = capo_connect.types.rule_search_summary_list.deserialize_json(
            data["Rules"]
        )
    else:
        out["rules"] = []
    if data.get("ApproximateTotalCount") is not None:
        out["approximate_total_count"] = data["ApproximateTotalCount"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
