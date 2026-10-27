"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#CancelIngestionJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearchserverless.types.client_token
    import capo_opensearchserverless.types.collection_id
    import capo_opensearchserverless.types.ingestion_job_id


class CancelIngestionJobRequest(TypedDict, closed=True):
    collection_id: "capo_opensearchserverless.types.collection_id.CollectionId"
    """<p>The unique identifier of the collection that the ingestion job belongs to.</p>"""
    ingestion_job_id: "capo_opensearchserverless.types.ingestion_job_id.IngestionJobId"
    """<p>The unique identifier of the ingestion job to cancel.</p>"""
    client_token: NotRequired[
        "capo_opensearchserverless.types.client_token.ClientToken"
    ]
    """<p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CancelIngestionJobRequest) -> dict:
    out: dict = {}
    out["collectionId"] = value["collection_id"]
    out["ingestionJobId"] = value["ingestion_job_id"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CancelIngestionJobRequest:
    out: CancelIngestionJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("collectionId") is not None:
        out["collection_id"] = data["collectionId"]
    else:
        out["collection_id"] = ""
    if data.get("ingestionJobId") is not None:
        out["ingestion_job_id"] = data["ingestionJobId"]
    else:
        out["ingestion_job_id"] = ""
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
