"""Generated from Smithy shape ``com.amazonaws.quicksight#SearchAgentsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.agent_search_filter_list
    import capo_quicksight.types.agents_max_results
    import capo_quicksight.types.aws_account_id


class SearchAgentsRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the agents.</p>"""
    filters: "capo_quicksight.types.agent_search_filter_list.AgentSearchFilterList"
    """<p>The filters to apply when searching agents.</p>"""
    max_results: NotRequired[
        "capo_quicksight.types.agents_max_results.AgentsMaxResults"
    ]
    """<p>The maximum number of results to return.</p>"""
    next_token: NotRequired["str"]
    """<p>The token for the next set of results, or null if there are no more results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchAgentsRequest) -> dict:
    out: dict = {}
    import capo_quicksight.types.agent_search_filter_list

    out["Filters"] = capo_quicksight.types.agent_search_filter_list.serialize_json(
        value["filters"]
    )
    return out


def deserialize_json(data: dict) -> SearchAgentsRequest:
    out: SearchAgentsRequest = {}  # type: ignore[typeddict-item]
    if data.get("Filters") is not None:
        import capo_quicksight.types.agent_search_filter_list

        out["filters"] = (
            capo_quicksight.types.agent_search_filter_list.deserialize_json(
                data["Filters"]
            )
        )
    else:
        out["filters"] = []
    return out
