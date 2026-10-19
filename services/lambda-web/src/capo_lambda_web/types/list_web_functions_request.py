"""Generated from Smithy shape ``com.amazonaws.lambdaweb#ListWebFunctionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda_web.types.filter_list
    import capo_lambda_web.types.max_results
    import capo_lambda_web.types.next_token


class ListWebFunctionsRequest(TypedDict, closed=True):
    filters: NotRequired["capo_lambda_web.types.filter_list.FilterList"]
    """<p>A list of filters to apply to the results. The only supported filter name is <code>state</code>. If you don't specify a filter, the operation returns all web functions.</p>"""
    max_results: NotRequired["capo_lambda_web.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in a single call. Minimum value of 1, maximum value of 50. Default is 50.</p>"""
    next_token: NotRequired["capo_lambda_web.types.next_token.NextToken"]
    """<p>The pagination token that's returned by a previous request to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWebFunctionsRequest) -> dict:
    out: dict = {}
    if "filters" in value:
        import capo_lambda_web.types.filter_list

        out["filters"] = capo_lambda_web.types.filter_list.serialize_json(
            value["filters"]
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListWebFunctionsRequest:
    out: ListWebFunctionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("filters") is not None:
        import capo_lambda_web.types.filter_list

        out["filters"] = capo_lambda_web.types.filter_list.deserialize_json(
            data["filters"]
        )
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
