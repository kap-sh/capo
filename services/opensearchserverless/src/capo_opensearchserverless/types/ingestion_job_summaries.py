"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#IngestionJobSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_opensearchserverless.types.ingestion_job_summary

IngestionJobSummaries: TypeAlias = list[
    "capo_opensearchserverless.types.ingestion_job_summary.IngestionJobSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IngestionJobSummaries) -> list:
    import capo_opensearchserverless.types.ingestion_job_summary

    out: list = []
    for item in value:
        out.append(
            capo_opensearchserverless.types.ingestion_job_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> IngestionJobSummaries:
    import capo_opensearchserverless.types.ingestion_job_summary

    out: IngestionJobSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_opensearchserverless.types.ingestion_job_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out
