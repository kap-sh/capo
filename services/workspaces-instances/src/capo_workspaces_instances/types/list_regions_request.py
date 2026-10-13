"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#ListRegionsRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_instances.types.max_results
    import capo_workspaces_instances.types.next_token


class ListRegionsRequest(TypedDict, closed=True):
    max_results: NotRequired["capo_workspaces_instances.types.max_results.MaxResults"]
    """<p>Maximum number of regions to return in a single API call. Enables pagination of region results.</p>"""
    next_token: NotRequired["capo_workspaces_instances.types.next_token.NextToken"]
    """<p>Pagination token for retrieving subsequent pages of region results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListRegionsRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListRegionsRequest:
    out: ListRegionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListRegionsRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "next_token" in value:
        out["next_token"] = "*** Sensitive Data Redacted ***"
    return out
