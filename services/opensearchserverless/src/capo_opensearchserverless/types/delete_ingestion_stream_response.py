"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#DeleteIngestionStreamResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearchserverless.types.collection_id
    import capo_opensearchserverless.types.ingestion_stream_id
    import capo_opensearchserverless.types.ingestion_stream_name
    import capo_opensearchserverless.types.ingestion_stream_status


class DeleteIngestionStreamResponse(TypedDict, closed=True):
    ingestion_stream_id: NotRequired[
        "capo_opensearchserverless.types.ingestion_stream_id.IngestionStreamId"
    ]
    """<p>The unique identifier of the deleted ingestion stream.</p>"""
    collection_id: NotRequired[
        "capo_opensearchserverless.types.collection_id.CollectionId"
    ]
    """<p>The unique identifier of the collection that the ingestion stream belonged to.</p>"""
    ingestion_stream_name: NotRequired[
        "capo_opensearchserverless.types.ingestion_stream_name.IngestionStreamName"
    ]
    """<p>The name of the deleted ingestion stream.</p>"""
    status: NotRequired[
        "capo_opensearchserverless.types.ingestion_stream_status.IngestionStreamStatus"
    ]
    """<p>The current status of the ingestion stream.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteIngestionStreamResponse) -> dict:
    out: dict = {}
    if "ingestion_stream_id" in value:
        out["ingestionStreamId"] = value["ingestion_stream_id"]
    if "collection_id" in value:
        out["collectionId"] = value["collection_id"]
    if "ingestion_stream_name" in value:
        out["ingestionStreamName"] = value["ingestion_stream_name"]
    if "status" in value:
        out["status"] = value["status"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteIngestionStreamResponse:
    out: DeleteIngestionStreamResponse = {}  # type: ignore[typeddict-item]
    if data.get("ingestionStreamId") is not None:
        out["ingestion_stream_id"] = data["ingestionStreamId"]
    if data.get("collectionId") is not None:
        out["collection_id"] = data["collectionId"]
    if data.get("ingestionStreamName") is not None:
        out["ingestion_stream_name"] = data["ingestionStreamName"]
    if data.get("status") is not None:
        out["status"] = data["status"]
    return out
