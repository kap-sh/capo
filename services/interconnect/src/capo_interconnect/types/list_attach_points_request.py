"""Generated from Smithy shape ``com.amazonaws.interconnect#ListAttachPointsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_interconnect.types.environment_id
    import capo_interconnect.types.max_results
    import capo_interconnect.types.next_token


class ListAttachPointsRequest(TypedDict, closed=True):
    environment_id: "capo_interconnect.types.environment_id.EnvironmentId"
    """<p>The identifier of the <a>Environment</a> for which to list valid Attach Points.</p>"""
    max_results: NotRequired["capo_interconnect.types.max_results.MaxResults"]
    """<p>The max number of list results in a single paginated response.</p>"""
    next_token: NotRequired["capo_interconnect.types.next_token.NextToken"]
    """<p>A pagination token from a previous paginated response indicating you wish to get the next page.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListAttachPointsRequest) -> dict:
    out: dict = {}
    out["environmentId"] = value["environment_id"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListAttachPointsRequest:
    out: ListAttachPointsRequest = {}  # type: ignore[typeddict-item]
    if data.get("environmentId") is not None:
        out["environment_id"] = data["environmentId"]
    else:
        out["environment_id"] = ""
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
