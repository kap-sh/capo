"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#IngestionJobSource``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_opensearchserverless.errors import DeserializationError

if TYPE_CHECKING:
    import capo_opensearchserverless.types.ingestion_job_s3_source


class IngestionJobSource(TypedDict, closed=True):
    s3: "capo_opensearchserverless.types.ingestion_job_s3_source.IngestionJobS3Source"
    """<p>The Amazon S3 source configuration for the ingestion job.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IngestionJobSource) -> dict:
    out: dict = {}
    import capo_opensearchserverless.types.ingestion_job_s3_source

    out["s3"] = (
        capo_opensearchserverless.types.ingestion_job_s3_source.serialize_aws_json_1_0(
            value["s3"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> IngestionJobSource:
    out: IngestionJobSource = {}  # type: ignore[typeddict-item]
    if data.get("s3") is not None:
        import capo_opensearchserverless.types.ingestion_job_s3_source

        out["s3"] = (
            capo_opensearchserverless.types.ingestion_job_s3_source.deserialize_aws_json_1_0(
                data["s3"]
            )
        )
    else:
        raise DeserializationError("IngestionJobSource.s3 required")
    return out
