"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#ListIngestionStreamsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearchserverless.types.collection_id


class ListIngestionStreamsRequest(TypedDict, closed=True):
    collection_id: "capo_opensearchserverless.types.collection_id.CollectionId"
    """<p>The unique identifier of the collection to list ingestion streams for.</p>"""
    next_token: NotRequired["str"]
    """<p>If your initial <code>ListIngestionStreams</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>ListIngestionStreams</code> operations, which returns results in the next page.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of results to return. Valid values are 1–100. If you don't specify a value, the default is 100. You can use <code>nextToken</code> to get the next page of results.</p> <p>A response can contain fewer results than <code>maxResults</code>, or no results, and still include a <code>nextToken</code>. To retrieve all results, continue to make the call with the returned <code>nextToken</code> until no <code>nextToken</code> is returned.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListIngestionStreamsRequest) -> dict:
    out: dict = {}
    out["collectionId"] = value["collection_id"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListIngestionStreamsRequest:
    out: ListIngestionStreamsRequest = {}  # type: ignore[typeddict-item]
    if data.get("collectionId") is not None:
        out["collection_id"] = data["collectionId"]
    else:
        out["collection_id"] = ""
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out
