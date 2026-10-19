"""Generated from Smithy shape ``com.amazonaws.opensearch#ListDataSourceAttachmentsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.id
    import capo_opensearch.types.integer
    import capo_opensearch.types.string


class ListDataSourceAttachmentsRequest(TypedDict, closed=True):
    id: "capo_opensearch.types.id.Id"
    """<p>The unique identifier or name of the OpenSearch application to list attachments for.</p>"""
    next_token: NotRequired["capo_opensearch.types.string.String"]
    """<p>The pagination token from a previous call to retrieve the next set of results.</p>"""
    max_results: NotRequired["capo_opensearch.types.integer.Integer"]
    """<p>The maximum number of results to return per page. The default is 50.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDataSourceAttachmentsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListDataSourceAttachmentsRequest:
    out: ListDataSourceAttachmentsRequest = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out
