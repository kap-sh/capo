"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#IngestionJobDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_opensearchserverless.types.collection_id
    import capo_opensearchserverless.types.ingestion_alerts
    import capo_opensearchserverless.types.ingestion_failure_reasons
    import capo_opensearchserverless.types.ingestion_index_name
    import capo_opensearchserverless.types.ingestion_job_id
    import capo_opensearchserverless.types.ingestion_job_name
    import capo_opensearchserverless.types.ingestion_job_resource_arn
    import capo_opensearchserverless.types.ingestion_job_source
    import capo_opensearchserverless.types.ingestion_job_status
    import capo_opensearchserverless.types.ingestion_state
    import capo_opensearchserverless.types.ingestion_statistics


class IngestionJobDetail(TypedDict, closed=True):
    ingestion_job_id: NotRequired[
        "capo_opensearchserverless.types.ingestion_job_id.IngestionJobId"
    ]
    """<p>The unique identifier of the ingestion job.</p>"""
    arn: NotRequired[
        "capo_opensearchserverless.types.ingestion_job_resource_arn.IngestionJobResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the ingestion job.</p>"""
    collection_id: NotRequired[
        "capo_opensearchserverless.types.collection_id.CollectionId"
    ]
    """<p>The unique identifier of the collection that the ingestion job belongs to.</p>"""
    ingestion_job_name: NotRequired[
        "capo_opensearchserverless.types.ingestion_job_name.IngestionJobName"
    ]
    """<p>The name of the ingestion job.</p>"""
    index_name: NotRequired[
        "capo_opensearchserverless.types.ingestion_index_name.IngestionIndexName"
    ]
    """<p>The name of the index that documents are ingested into.</p>"""
    failure_index_name: NotRequired[
        "capo_opensearchserverless.types.ingestion_index_name.IngestionIndexName"
    ]
    """<p>The name of the index where documents that fail to be ingested are recorded.</p>"""
    source: NotRequired[
        "capo_opensearchserverless.types.ingestion_job_source.IngestionJobSource"
    ]
    """<p>The Amazon S3 source that the ingestion job ingests data from.</p>"""
    status: NotRequired[
        "capo_opensearchserverless.types.ingestion_job_status.IngestionJobStatus"
    ]
    """<p>The current lifecycle status of the ingestion job. For example, <code>CREATING</code>, <code>ACTIVE</code>, <code>COMPLETED</code>, or <code>CANCELLED</code>.</p>"""
    state: NotRequired["capo_opensearchserverless.types.ingestion_state.IngestionState"]
    """<p>The current processing state of the ingestion job. For example, <code>SCANNING</code>, <code>INGESTION_IN_PROGRESS</code>, or <code>INGESTION_COMPLETE</code>.</p>"""
    statistics: NotRequired[
        "capo_opensearchserverless.types.ingestion_statistics.IngestionStatistics"
    ]
    """<p>Processing statistics for the ingestion job, such as the number of Amazon S3 objects discovered, ingested, and failed.</p>"""
    revision: NotRequired["int"]
    """<p>The revision number of the ingestion job.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The date and time when the ingestion job was created.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The date and time when the ingestion job was last updated.</p>"""
    failure_reasons: NotRequired[
        "capo_opensearchserverless.types.ingestion_failure_reasons.IngestionFailureReasons"
    ]
    """<p>The reasons that the ingestion job reached a terminal failure state, if applicable.</p>"""
    active_alerts: NotRequired[
        "capo_opensearchserverless.types.ingestion_alerts.IngestionAlerts"
    ]
    """<p>Active alerts about operational issues that currently affect the ingestion job. Alerts are cleared when the issue is resolved.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IngestionJobDetail) -> dict:
    out: dict = {}
    if "ingestion_job_id" in value:
        out["ingestionJobId"] = value["ingestion_job_id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "collection_id" in value:
        out["collectionId"] = value["collection_id"]
    if "ingestion_job_name" in value:
        out["ingestionJobName"] = value["ingestion_job_name"]
    if "index_name" in value:
        out["indexName"] = value["index_name"]
    if "failure_index_name" in value:
        out["failureIndexName"] = value["failure_index_name"]
    if "source" in value:
        import capo_opensearchserverless.types.ingestion_job_source

        out["source"] = (
            capo_opensearchserverless.types.ingestion_job_source.serialize_aws_json_1_0(
                value["source"]
            )
        )
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


def deserialize_aws_json_1_0(data: dict) -> IngestionJobDetail:
    out: IngestionJobDetail = {}  # type: ignore[typeddict-item]
    if data.get("ingestionJobId") is not None:
        out["ingestion_job_id"] = data["ingestionJobId"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("collectionId") is not None:
        out["collection_id"] = data["collectionId"]
    if data.get("ingestionJobName") is not None:
        out["ingestion_job_name"] = data["ingestionJobName"]
    if data.get("indexName") is not None:
        out["index_name"] = data["indexName"]
    if data.get("failureIndexName") is not None:
        out["failure_index_name"] = data["failureIndexName"]
    if data.get("source") is not None:
        import capo_opensearchserverless.types.ingestion_job_source

        out["source"] = (
            capo_opensearchserverless.types.ingestion_job_source.deserialize_aws_json_1_0(
                data["source"]
            )
        )
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
