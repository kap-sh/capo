"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#GetIngestionJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_opensearchserverless.types.collection_id
    import capo_opensearchserverless.types.ingestion_job_id


class GetIngestionJobRequest(TypedDict, closed=True):
    collection_id: "capo_opensearchserverless.types.collection_id.CollectionId"
    """<p>The unique identifier of the collection that the ingestion job belongs to.</p>"""
    ingestion_job_id: "capo_opensearchserverless.types.ingestion_job_id.IngestionJobId"
    """<p>The unique identifier of the ingestion job to retrieve.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetIngestionJobRequest) -> dict:
    out: dict = {}
    out["collectionId"] = value["collection_id"]
    out["ingestionJobId"] = value["ingestion_job_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetIngestionJobRequest:
    out: GetIngestionJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("collectionId") is not None:
        out["collection_id"] = data["collectionId"]
    else:
        out["collection_id"] = ""
    if data.get("ingestionJobId") is not None:
        out["ingestion_job_id"] = data["ingestionJobId"]
    else:
        out["ingestion_job_id"] = ""
    return out
