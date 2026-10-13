"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#ListVectorEnrichmentJobInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker_geospatial.types.next_token
    import capo_sagemaker_geospatial.types.sort_order


class ListVectorEnrichmentJobInput(TypedDict, closed=True):
    status_equals: NotRequired["str"]
    """<p>A filter that retrieves only jobs with a specific status.</p>"""
    sort_order: NotRequired["capo_sagemaker_geospatial.types.sort_order.SortOrder"]
    """<p>An optional value that specifies whether you want the results sorted in <code>Ascending</code> or <code>Descending</code> order.</p>"""
    sort_by: NotRequired["str"]
    """<p>The parameter by which to sort the results.</p>"""
    next_token: NotRequired["capo_sagemaker_geospatial.types.next_token.NextToken"]
    """<p>If the previous response was truncated, you receive this token. Use it in your next request to receive the next set of results.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of items to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListVectorEnrichmentJobInput) -> dict:
    out: dict = {}
    if "status_equals" in value:
        out["StatusEquals"] = value["status_equals"]
    if "sort_order" in value:
        out["SortOrder"] = value["sort_order"]
    if "sort_by" in value:
        out["SortBy"] = value["sort_by"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListVectorEnrichmentJobInput:
    out: ListVectorEnrichmentJobInput = {}  # type: ignore[typeddict-item]
    if data.get("StatusEquals") is not None:
        out["status_equals"] = data["StatusEquals"]
    if data.get("SortOrder") is not None:
        out["sort_order"] = data["SortOrder"]
    if data.get("SortBy") is not None:
        out["sort_by"] = data["SortBy"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out


def redact_sensitive(value: ListVectorEnrichmentJobInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "next_token" in value:
        out["next_token"] = "*** Sensitive Data Redacted ***"
    return out
