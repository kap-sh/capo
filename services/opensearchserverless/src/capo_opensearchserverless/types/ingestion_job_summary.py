"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#IngestionJobSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_opensearchserverless.types.ingestion_index_name
    import capo_opensearchserverless.types.ingestion_job_id
    import capo_opensearchserverless.types.ingestion_job_name
    import capo_opensearchserverless.types.ingestion_job_resource_arn
    import capo_opensearchserverless.types.ingestion_job_status


class IngestionJobSummary(TypedDict, closed=True):
    ingestion_job_id: NotRequired[
        "capo_opensearchserverless.types.ingestion_job_id.IngestionJobId"
    ]
    """<p>The unique identifier of the ingestion job.</p>"""
    arn: NotRequired[
        "capo_opensearchserverless.types.ingestion_job_resource_arn.IngestionJobResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the ingestion job.</p>"""
    ingestion_job_name: NotRequired[
        "capo_opensearchserverless.types.ingestion_job_name.IngestionJobName"
    ]
    """<p>The name of the ingestion job.</p>"""
    index_name: NotRequired[
        "capo_opensearchserverless.types.ingestion_index_name.IngestionIndexName"
    ]
    """<p>The name of the index that documents are ingested into.</p>"""
    status: NotRequired[
        "capo_opensearchserverless.types.ingestion_job_status.IngestionJobStatus"
    ]
    """<p>The current lifecycle status of the ingestion job.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The date and time when the ingestion job was created.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The date and time when the ingestion job was last updated.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IngestionJobSummary) -> dict:
    out: dict = {}
    if "ingestion_job_id" in value:
        out["ingestionJobId"] = value["ingestion_job_id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "ingestion_job_name" in value:
        out["ingestionJobName"] = value["ingestion_job_name"]
    if "index_name" in value:
        out["indexName"] = value["index_name"]
    if "status" in value:
        out["status"] = value["status"]
    if "created_at" in value:
        import capo_opensearchserverless.types._prelude.timestamp

        out["createdAt"] = (
            capo_opensearchserverless.types._prelude.timestamp.serialize_aws_json_1_0(
                value["created_at"]
            )
        )
    if "updated_at" in value:
        import capo_opensearchserverless.types._prelude.timestamp

        out["updatedAt"] = (
            capo_opensearchserverless.types._prelude.timestamp.serialize_aws_json_1_0(
                value["updated_at"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> IngestionJobSummary:
    out: IngestionJobSummary = {}  # type: ignore[typeddict-item]
    if data.get("ingestionJobId") is not None:
        out["ingestion_job_id"] = data["ingestionJobId"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("ingestionJobName") is not None:
        out["ingestion_job_name"] = data["ingestionJobName"]
    if data.get("indexName") is not None:
        out["index_name"] = data["indexName"]
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("createdAt") is not None:
        import capo_opensearchserverless.types._prelude.timestamp

        out["created_at"] = (
            capo_opensearchserverless.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["createdAt"]
            )
        )
    if data.get("updatedAt") is not None:
        import capo_opensearchserverless.types._prelude.timestamp

        out["updated_at"] = (
            capo_opensearchserverless.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["updatedAt"]
            )
        )
    return out
