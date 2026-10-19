"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#ListScheduledReportsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bcm_dashboards.types.max_results
    import capo_bcm_dashboards.types.next_page_token


class ListScheduledReportsRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_bcm_dashboards.types.next_page_token.NextPageToken"]
    """<p>The token for the next page of results. Use the value returned in the previous response.</p>"""
    max_results: NotRequired["capo_bcm_dashboards.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in a single call. Valid range is 1 to 100. The default value is 50.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListScheduledReportsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListScheduledReportsRequest:
    out: ListScheduledReportsRequest = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out
