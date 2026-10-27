"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#IngestionStreamDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_opensearchserverless.types.collection_id
    import capo_opensearchserverless.types.ingestion_alerts
    import capo_opensearchserverless.types.ingestion_failure_reasons
    import capo_opensearchserverless.types.ingestion_index_name
    import capo_opensearchserverless.types.ingestion_state
    import capo_opensearchserverless.types.ingestion_statistics
    import capo_opensearchserverless.types.ingestion_stream_id
    import capo_opensearchserverless.types.ingestion_stream_name
    import capo_opensearchserverless.types.ingestion_stream_resource_arn
    import capo_opensearchserverless.types.ingestion_stream_source
    import capo_opensearchserverless.types.ingestion_stream_status
    import capo_opensearchserverless.types.role_arn


class IngestionStreamDetail(TypedDict, closed=True):
    ingestion_stream_id: NotRequired[
        "capo_opensearchserverless.types.ingestion_stream_id.IngestionStreamId"
    ]
    """<p>The unique identifier of the ingestion stream.</p>"""
    arn: NotRequired[
        "capo_opensearchserverless.types.ingestion_stream_resource_arn.IngestionStreamResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the ingestion stream.</p>"""
    collection_id: NotRequired[
        "capo_opensearchserverless.types.collection_id.CollectionId"
    ]
    """<p>The unique identifier of the collection that the ingestion stream belongs to.</p>"""
    ingestion_stream_name: NotRequired[
        "capo_opensearchserverless.types.ingestion_stream_name.IngestionStreamName"
    ]
    """<p>The name of the ingestion stream.</p>"""
    index_name: NotRequired[
        "capo_opensearchserverless.types.ingestion_index_name.IngestionIndexName"
    ]
    """<p>The name of the index that documents are ingested into.</p>"""
    failure_index_name: NotRequired[
        "capo_opensearchserverless.types.ingestion_index_name.IngestionIndexName"
    ]
    """<p>The name of the index where documents that fail to be ingested are recorded.</p>"""
    source: NotRequired[
        "capo_opensearchserverless.types.ingestion_stream_source.IngestionStreamSource"
    ]
    """<p>The Amazon S3 source that the ingestion stream ingests data from.</p>"""
    role_arn: NotRequired["capo_opensearchserverless.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM role that OpenSearch Serverless assumes to read data from the source.</p>"""
    status: NotRequired[
        "capo_opensearchserverless.types.ingestion_stream_status.IngestionStreamStatus"
    ]
    """<p>The current lifecycle status of the ingestion stream. For example, <code>CREATING</code>, <code>ACTIVE</code>, or <code>DELETING</code>.</p>"""
    state: NotRequired["capo_opensearchserverless.types.ingestion_state.IngestionState"]
    """<p>The current processing state of the ingestion stream. For example, <code>STARTING</code> or <code>INGESTION_IN_PROGRESS</code>.</p>"""
    statistics: NotRequired[
        "capo_opensearchserverless.types.ingestion_statistics.IngestionStatistics"
    ]
    """<p>Processing statistics for the ingestion stream, such as the number of Amazon S3 objects discovered, ingested, and failed.</p>"""
    revision: NotRequired["int"]
    """<p>The revision number of the ingestion stream.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The date and time when the ingestion stream was created.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The date and time when the ingestion stream was last updated.</p>"""
    failure_reasons: NotRequired[
        "capo_opensearchserverless.types.ingestion_failure_reasons.IngestionFailureReasons"
    ]
    """<p>The reasons that the ingestion stream reached a terminal failure state, if applicable.</p>"""
    active_alerts: NotRequired[
        "capo_opensearchserverless.types.ingestion_alerts.IngestionAlerts"
    ]
    """<p>Active alerts about operational issues that currently affect the ingestion stream. Alerts are cleared when the issue is resolved.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IngestionStreamDetail) -> dict:
    out: dict = {}
    if "ingestion_stream_id" in value:
        out["ingestionStreamId"] = value["ingestion_stream_id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "collection_id" in value:
        out["collectionId"] = value["collection_id"]
    if "ingestion_stream_name" in value:
        out["ingestionStreamName"] = value["ingestion_stream_name"]
    if "index_name" in value:
        out["indexName"] = value["index_name"]
    if "failure_index_name" in value:
        out["failureIndexName"] = value["failure_index_name"]
    if "source" in value:
        import capo_opensearchserverless.types.ingestion_stream_source

        out["source"] = (
            capo_opensearchserverless.types.ingestion_stream_source.serialize_aws_json_1_0(
                value["source"]
            )
        )
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "status" in value:
        out["status"] = value["status"]
    if "state" in value:
        out["state"] = value["state"]
    if "statistics" in value:
        import capo_opensearchserverless.types.ingestion_statistics

        out["statistics"] = (
            capo_opensearchserverless.types.ingestion_statistics.serialize_aws_json_1_0(
                value["statistics"]
            )
        )
    if "revision" in value:
        out["revision"] = value["revision"]
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
    if "failure_reasons" in value:
        import capo_opensearchserverless.types.ingestion_failure_reasons

        out["failureReasons"] = (
            capo_opensearchserverless.types.ingestion_failure_reasons.serialize_aws_json_1_0(
                value["failure_reasons"]
            )
        )
    if "active_alerts" in value:
        import capo_opensearchserverless.types.ingestion_alerts

        out["activeAlerts"] = (
            capo_opensearchserverless.types.ingestion_alerts.serialize_aws_json_1_0(
                value["active_alerts"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> IngestionStreamDetail:
    out: IngestionStreamDetail = {}  # type: ignore[typeddict-item]
    if data.get("ingestionStreamId") is not None:
        out["ingestion_stream_id"] = data["ingestionStreamId"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("collectionId") is not None:
        out["collection_id"] = data["collectionId"]
    if data.get("ingestionStreamName") is not None:
        out["ingestion_stream_name"] = data["ingestionStreamName"]
    if data.get("indexName") is not None:
        out["index_name"] = data["indexName"]
    if data.get("failureIndexName") is not None:
        out["failure_index_name"] = data["failureIndexName"]
    if data.get("source") is not None:
        import capo_opensearchserverless.types.ingestion_stream_source

        out["source"] = (
            capo_opensearchserverless.types.ingestion_stream_source.deserialize_aws_json_1_0(
                data["source"]
            )
        )
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("state") is not None:
        out["state"] = data["state"]
    if data.get("statistics") is not None:
        import capo_opensearchserverless.types.ingestion_statistics

        out["statistics"] = (
            capo_opensearchserverless.types.ingestion_statistics.deserialize_aws_json_1_0(
                data["statistics"]
            )
        )
    if data.get("revision") is not None:
        out["revision"] = data["revision"]
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
    if data.get("failureReasons") is not None:
        import capo_opensearchserverless.types.ingestion_failure_reasons

        out["failure_reasons"] = (
            capo_opensearchserverless.types.ingestion_failure_reasons.deserialize_aws_json_1_0(
                data["failureReasons"]
            )
        )
    if data.get("activeAlerts") is not None:
        import capo_opensearchserverless.types.ingestion_alerts

        out["active_alerts"] = (
            capo_opensearchserverless.types.ingestion_alerts.deserialize_aws_json_1_0(
                data["activeAlerts"]
            )
        )
    return out
