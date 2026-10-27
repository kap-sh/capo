"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#CreateIngestionJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearchserverless.types.ingestion_job_detail


class CreateIngestionJobResponse(TypedDict, closed=True):
    ingestion_job_detail: NotRequired[
        "capo_opensearchserverless.types.ingestion_job_detail.IngestionJobDetail"
    ]
    """<p>Details about the created ingestion job.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateIngestionJobResponse) -> dict:
    out: dict = {}
    if "ingestion_job_detail" in value:
        import capo_opensearchserverless.types.ingestion_job_detail

        out["ingestionJobDetail"] = (
            capo_opensearchserverless.types.ingestion_job_detail.serialize_aws_json_1_0(
                value["ingestion_job_detail"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateIngestionJobResponse:
    out: CreateIngestionJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("ingestionJobDetail") is not None:
        import capo_opensearchserverless.types.ingestion_job_detail

        out["ingestion_job_detail"] = (
            capo_opensearchserverless.types.ingestion_job_detail.deserialize_aws_json_1_0(
                data["ingestionJobDetail"]
            )
        )
    return out
