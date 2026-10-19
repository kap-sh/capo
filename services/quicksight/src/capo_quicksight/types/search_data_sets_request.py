"""Generated from Smithy shape ``com.amazonaws.quicksight#SearchDataSetsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.data_set_search_filter_list
    import capo_quicksight.types.max_results
    import capo_quicksight.types.string


class SearchDataSetsRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The Amazon Web Services account ID.</p>"""
    filters: "capo_quicksight.types.data_set_search_filter_list.DataSetSearchFilterList"
    """<p>The filters to apply to the search.</p>"""
    next_token: NotRequired["capo_quicksight.types.string.String"]
    """<p>A pagination token that can be used in a subsequent request.</p>"""
    max_results: NotRequired["capo_quicksight.types.max_results.MaxResults"]
    """<p>The maximum number of results to be returned per request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchDataSetsRequest) -> dict:
    out: dict = {}
    import capo_quicksight.types.data_set_search_filter_list

    out["Filters"] = capo_quicksight.types.data_set_search_filter_list.serialize_json(
        value["filters"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> SearchDataSetsRequest:
    out: SearchDataSetsRequest = {}  # type: ignore[typeddict-item]
    if data.get("Filters") is not None:
        import capo_quicksight.types.data_set_search_filter_list

        out["filters"] = (
            capo_quicksight.types.data_set_search_filter_list.deserialize_json(
                data["Filters"]
            )
        )
    else:
        out["filters"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
