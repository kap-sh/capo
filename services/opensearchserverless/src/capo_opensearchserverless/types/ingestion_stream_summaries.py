"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#IngestionStreamSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_opensearchserverless.types.ingestion_stream_summary

IngestionStreamSummaries: TypeAlias = list[
    "capo_opensearchserverless.types.ingestion_stream_summary.IngestionStreamSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IngestionStreamSummaries) -> list:
    import capo_opensearchserverless.types.ingestion_stream_summary

    out: list = []
    for item in value:
        out.append(
            capo_opensearchserverless.types.ingestion_stream_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> IngestionStreamSummaries:
    import capo_opensearchserverless.types.ingestion_stream_summary

    out: IngestionStreamSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_opensearchserverless.types.ingestion_stream_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out
