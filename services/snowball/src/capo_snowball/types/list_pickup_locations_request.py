"""Generated from Smithy shape ``com.amazonaws.snowball#ListPickupLocationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_snowball.types.list_limit
    import capo_snowball.types.string


class ListPickupLocationsRequest(TypedDict, closed=True):
    max_results: NotRequired["capo_snowball.types.list_limit.ListLimit"]
    """<p>The maximum number of locations to list per page.</p>"""
    next_token: NotRequired["capo_snowball.types.string.String"]
    """<p>HTTP requests are stateless. To identify what object comes "next" in the list of <code>ListPickupLocationsRequest</code> objects, you have the option of specifying <code>NextToken</code> as the starting point for your returned list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListPickupLocationsRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListPickupLocationsRequest:
    out: ListPickupLocationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
