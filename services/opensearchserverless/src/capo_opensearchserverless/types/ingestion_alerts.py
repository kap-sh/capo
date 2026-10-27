"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#IngestionAlerts``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_opensearchserverless.types.ingestion_alert

IngestionAlerts: TypeAlias = list[
    "capo_opensearchserverless.types.ingestion_alert.IngestionAlert"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IngestionAlerts) -> list:
    import capo_opensearchserverless.types.ingestion_alert

    out: list = []
    for item in value:
        out.append(
            capo_opensearchserverless.types.ingestion_alert.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> IngestionAlerts:
    import capo_opensearchserverless.types.ingestion_alert

    out: IngestionAlerts = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_opensearchserverless.types.ingestion_alert.deserialize_aws_json_1_0(
                item
            )
        )
    return out
