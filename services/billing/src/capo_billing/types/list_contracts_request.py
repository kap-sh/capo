"""Generated from Smithy shape ``com.amazonaws.billing#ListContractsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_billing.types.page_token


class ListContractsRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_billing.types.page_token.PageToken"]
    """<p>The pagination token that indicates the next set of results to retrieve.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of contracts to return in a single call. Minimum value of 1, maximum value of 100.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListContractsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListContractsRequest:
    out: ListContractsRequest = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out
