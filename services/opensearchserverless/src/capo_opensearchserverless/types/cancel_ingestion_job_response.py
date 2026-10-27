"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#CancelIngestionJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearchserverless.types.collection_id
    import capo_opensearchserverless.types.ingestion_job_id
    import capo_opensearchserverless.types.ingestion_job_name
    import capo_opensearchserverless.types.ingestion_job_status


class CancelIngestionJobResponse(TypedDict, closed=True):
    ingestion_job_id: NotRequired[
        "capo_opensearchserverless.types.ingestion_job_id.IngestionJobId"
    ]
    """<p>The unique identifier of the cancelled ingestion job.</p>"""
    collection_id: NotRequired[
        "capo_opensearchserverless.types.collection_id.CollectionId"
    ]
    """<p>The unique identifier of the collection that the ingestion job belongs to.</p>"""
    ingestion_job_name: NotRequired[
        "capo_opensearchserverless.types.ingestion_job_name.IngestionJobName"
    ]
    """<p>The name of the cancelled ingestion job.</p>"""
    status: NotRequired[
        "capo_opensearchserverless.types.ingestion_job_status.IngestionJobStatus"
    ]
    """<p>The current status of the ingestion job.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CancelIngestionJobResponse) -> dict:
    out: dict = {}
    if "ingestion_job_id" in value:
        out["ingestionJobId"] = value["ingestion_job_id"]
    if "collection_id" in value:
        out["collectionId"] = value["collection_id"]
    if "ingestion_job_name" in value:
        out["ingestionJobName"] = value["ingestion_job_name"]
    if "status" in value:
        out["status"] = value["status"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CancelIngestionJobResponse:
    out: CancelIngestionJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("ingestionJobId") is not None:
        out["ingestion_job_id"] = data["ingestionJobId"]
    if data.get("collectionId") is not None:
        out["collection_id"] = data["collectionId"]
    if data.get("ingestionJobName") is not None:
        out["ingestion_job_name"] = data["ingestionJobName"]
    if data.get("status") is not None:
        out["status"] = data["status"]
    return out
