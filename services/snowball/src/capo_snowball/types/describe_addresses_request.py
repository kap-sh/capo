"""Generated from Smithy shape ``com.amazonaws.snowball#DescribeAddressesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_snowball.types.list_limit
    import capo_snowball.types.string


class DescribeAddressesRequest(TypedDict, closed=True):
    max_results: NotRequired["capo_snowball.types.list_limit.ListLimit"]
    """<p>The number of <code>ADDRESS</code> objects to return.</p>"""
    next_token: NotRequired["capo_snowball.types.string.String"]
    """<p>HTTP requests are stateless. To identify what object comes "next" in the list of <code>ADDRESS</code> objects, you have the option of specifying a value for <code>NextToken</code> as the starting point for your list of returned addresses.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAddressesRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAddressesRequest:
    out: DescribeAddressesRequest = {}  # type: ignore[typeddict-item]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
