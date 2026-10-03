"""Generated from Smithy shape ``com.amazonaws.eventbridge#ListEndpointsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridge.types.endpoint_name
    import capo_eventbridge.types.home_region
    import capo_eventbridge.types.limit_max100
    import capo_eventbridge.types.next_token


class ListEndpointsRequest(TypedDict, closed=True):
    name_prefix: NotRequired["capo_eventbridge.types.endpoint_name.EndpointName"]
    """<p>A value that will return a subset of the endpoints associated with this account. For example, <code>"NamePrefix": "ABC"</code> will return all endpoints with "ABC" in the name.</p>"""
    home_region: NotRequired["capo_eventbridge.types.home_region.HomeRegion"]
    """<p>The primary Region of the endpoints associated with this account. For example <code>"HomeRegion": "us-east-1"</code>.</p>"""
    next_token: NotRequired["capo_eventbridge.types.next_token.NextToken"]
    """<p>The token returned by a previous call, which you can use to retrieve the next set of results.</p> <p>The value of <code>nextToken</code> is a unique pagination token for each page. To retrieve the next page of results, make the call again using the returned token. Keep all other arguments unchanged.</p> <p> Using an expired pagination token results in an <code>HTTP 400 InvalidToken</code> error.</p>"""
    max_results: NotRequired["capo_eventbridge.types.limit_max100.LimitMax100"]
    """<p>The maximum number of results returned by the call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListEndpointsRequest) -> dict:
    out: dict = {}
    if "name_prefix" in value:
        out["NamePrefix"] = value["name_prefix"]
    if "home_region" in value:
        out["HomeRegion"] = value["home_region"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListEndpointsRequest:
    out: ListEndpointsRequest = {}  # type: ignore[typeddict-item]
    if data.get("NamePrefix") is not None:
        out["name_prefix"] = data["NamePrefix"]
    if data.get("HomeRegion") is not None:
        out["home_region"] = data["HomeRegion"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
