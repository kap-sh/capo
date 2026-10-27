"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#GetIngestionStreamRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_opensearchserverless.types.collection_id
    import capo_opensearchserverless.types.ingestion_stream_id


class GetIngestionStreamRequest(TypedDict, closed=True):
    collection_id: "capo_opensearchserverless.types.collection_id.CollectionId"
    """<p>The unique identifier of the collection that the ingestion stream belongs to.</p>"""
    ingestion_stream_id: (
        "capo_opensearchserverless.types.ingestion_stream_id.IngestionStreamId"
    )
    """<p>The unique identifier of the ingestion stream to retrieve.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetIngestionStreamRequest) -> dict:
    out: dict = {}
    out["collectionId"] = value["collection_id"]
    out["ingestionStreamId"] = value["ingestion_stream_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetIngestionStreamRequest:
    out: GetIngestionStreamRequest = {}  # type: ignore[typeddict-item]
    if data.get("collectionId") is not None:
        out["collection_id"] = data["collectionId"]
    else:
        out["collection_id"] = ""
    if data.get("ingestionStreamId") is not None:
        out["ingestion_stream_id"] = data["ingestionStreamId"]
    else:
        out["ingestion_stream_id"] = ""
    return out
