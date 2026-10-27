"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#IngestionFailureReasons``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_opensearchserverless.types.ingestion_failure_reason

IngestionFailureReasons: TypeAlias = list[
    "capo_opensearchserverless.types.ingestion_failure_reason.IngestionFailureReason"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IngestionFailureReasons) -> list:
    import capo_opensearchserverless.types.ingestion_failure_reason

    out: list = []
    for item in value:
        out.append(
            capo_opensearchserverless.types.ingestion_failure_reason.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> IngestionFailureReasons:
    import capo_opensearchserverless.types.ingestion_failure_reason

    out: IngestionFailureReasons = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_opensearchserverless.types.ingestion_failure_reason.deserialize_aws_json_1_0(
                item
            )
        )
    return out
