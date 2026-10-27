"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#IngestionStreamSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_opensearchserverless.types.ingestion_index_name
    import capo_opensearchserverless.types.ingestion_stream_id
    import capo_opensearchserverless.types.ingestion_stream_name
    import capo_opensearchserverless.types.ingestion_stream_resource_arn
    import capo_opensearchserverless.types.ingestion_stream_status


class IngestionStreamSummary(TypedDict, closed=True):
    ingestion_stream_id: NotRequired[
        "capo_opensearchserverless.types.ingestion_stream_id.IngestionStreamId"
    ]
    """<p>The unique identifier of the ingestion stream.</p>"""
    arn: NotRequired[
        "capo_opensearchserverless.types.ingestion_stream_resource_arn.IngestionStreamResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the ingestion stream.</p>"""
    ingestion_stream_name: NotRequired[
        "capo_opensearchserverless.types.ingestion_stream_name.IngestionStreamName"
    ]
    """<p>The name of the ingestion stream.</p>"""
    index_name: NotRequired[
        "capo_opensearchserverless.types.ingestion_index_name.IngestionIndexName"
    ]
    """<p>The name of the index that documents are ingested into.</p>"""
    status: NotRequired[
        "capo_opensearchserverless.types.ingestion_stream_status.IngestionStreamStatus"
    ]
    """<p>The current lifecycle status of the ingestion stream.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The date and time when the ingestion stream was created.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The date and time when the ingestion stream was last updated.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IngestionStreamSummary) -> dict:
    out: dict = {}
    if "ingestion_stream_id" in value:
        out["ingestionStreamId"] = value["ingestion_stream_id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "ingestion_stream_name" in value:
        out["ingestionStreamName"] = value["ingestion_stream_name"]
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


def deserialize_aws_json_1_0(data: dict) -> IngestionStreamSummary:
    out: IngestionStreamSummary = {}  # type: ignore[typeddict-item]
    if data.get("ingestionStreamId") is not None:
        out["ingestion_stream_id"] = data["ingestionStreamId"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("ingestionStreamName") is not None:
        out["ingestion_stream_name"] = data["ingestionStreamName"]
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
