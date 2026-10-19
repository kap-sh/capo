"""Generated from Smithy shape ``com.amazonaws.codeconnections#ListHostsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeconnections.types.max_results
    import capo_codeconnections.types.next_token


class ListHostsInput(TypedDict, closed=True):
    max_results: NotRequired["capo_codeconnections.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>"""
    next_token: NotRequired["capo_codeconnections.types.next_token.NextToken"]
    """<p>The token that was returned from the previous <code>ListHosts</code> call, which can be used to return the next set of hosts in the list.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListHostsInput) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListHostsInput:
    out: ListHostsInput = {}  # type: ignore[typeddict-item]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
