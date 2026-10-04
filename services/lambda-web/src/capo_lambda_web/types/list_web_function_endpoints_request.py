"""Generated from Smithy shape ``com.amazonaws.lambdaweb#ListWebFunctionEndpointsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda_web.types.filter_list
    import capo_lambda_web.types.function_name
    import capo_lambda_web.types.max_results
    import capo_lambda_web.types.next_token


class ListWebFunctionEndpointsRequest(TypedDict, closed=True):
    function_name: "capo_lambda_web.types.function_name.FunctionName"
    """<p>The name of the web function. You can specify the function name or the function ARN. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>"""
    filters: NotRequired["capo_lambda_web.types.filter_list.FilterList"]
    """<p>A list of filters to apply to the results. Supported filter names: <code>authType</code>, <code>autoDeploymentMode</code>, <code>endpointType</code>, <code>state</code>, and <code>updateStatus</code>.</p>"""
    max_results: "capo_lambda_web.types.max_results.MaxResults"
    """<p>The maximum number of results to return in a single call. Minimum value of 1, maximum value of 50. Default is 50.</p>"""
    next_token: NotRequired["capo_lambda_web.types.next_token.NextToken"]
    """<p>The pagination token that's returned by a previous request to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWebFunctionEndpointsRequest) -> dict:
    out: dict = {}
    if "filters" in value:
        import capo_lambda_web.types.filter_list

        out["filters"] = capo_lambda_web.types.filter_list.serialize_json(
            value["filters"]
        )
    out["maxResults"] = value.get("max_results", 50)
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListWebFunctionEndpointsRequest:
    out: ListWebFunctionEndpointsRequest = {}  # type: ignore[typeddict-item]
    if data.get("filters") is not None:
        import capo_lambda_web.types.filter_list

        out["filters"] = capo_lambda_web.types.filter_list.deserialize_json(
            data["filters"]
        )
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    else:
        out["max_results"] = 50
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
