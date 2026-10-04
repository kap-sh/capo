"""Generated from Smithy shape ``com.amazonaws.bedrockagent#IngestionJob``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.date_timestamp
    import capo_bedrock_agent.types.description
    import capo_bedrock_agent.types.failure_reasons
    import capo_bedrock_agent.types.id
    import capo_bedrock_agent.types.ingestion_job_statistics
    import capo_bedrock_agent.types.ingestion_job_status


class IngestionJob(TypedDict, closed=True):
    knowledge_base_id: "capo_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the knowledge for the data ingestion job.</p>"""
    data_source_id: "capo_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the data source for the data ingestion job.</p>"""
    ingestion_job_id: "capo_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the data ingestion job.</p>"""
    description: NotRequired["capo_bedrock_agent.types.description.Description"]
    """<p>The description of the data ingestion job.</p>"""
    status: "capo_bedrock_agent.types.ingestion_job_status.IngestionJobStatus"
    """<p>The status of the data ingestion job.</p>"""
    statistics: NotRequired[
        "capo_bedrock_agent.types.ingestion_job_statistics.IngestionJobStatistics"
    ]
    """<p>Contains statistics about the data ingestion job.</p>"""
    failure_reasons: NotRequired[
        "capo_bedrock_agent.types.failure_reasons.FailureReasons"
    ]
    """<p>A list of reasons that the data ingestion job failed.</p>"""
    started_at: "capo_bedrock_agent.types.date_timestamp.DateTimestamp"
    """<p>The time the data ingestion job started.</p> <p>If you stop a data ingestion job, the <code>startedAt</code> time is the time the job was started before the job was stopped.</p>"""
    updated_at: "capo_bedrock_agent.types.date_timestamp.DateTimestamp"
    """<p>The time the data ingestion job was last updated.</p> <p>If you stop a data ingestion job, the <code>updatedAt</code> time is the time the job was stopped.</p>"""
    text_ready_at: NotRequired["capo_bedrock_agent.types.date_timestamp.DateTimestamp"]
    """<p>The time at which all text content in the data ingestion job finished extraction and became available to query.</p> <p>This time isn't returned until text extraction is complete for all the documents in the job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IngestionJob) -> dict:
    out: dict = {}
    out["knowledgeBaseId"] = value["knowledge_base_id"]
    out["dataSourceId"] = value["data_source_id"]
    out["ingestionJobId"] = value["ingestion_job_id"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_bedrock_agent.types.ingestion_job_status

    out["status"] = capo_bedrock_agent.types.ingestion_job_status.serialize_json(
        value["status"]
    )
    if "statistics" in value:
        import capo_bedrock_agent.types.ingestion_job_statistics

        out["statistics"] = (
            capo_bedrock_agent.types.ingestion_job_statistics.serialize_json(
                value["statistics"]
            )
        )
    if "failure_reasons" in value:
        import capo_bedrock_agent.types.failure_reasons

        out["failureReasons"] = capo_bedrock_agent.types.failure_reasons.serialize_json(
            value["failure_reasons"]
        )
    import capo_bedrock_agent.types.date_timestamp

    out["startedAt"] = capo_bedrock_agent.types.date_timestamp.serialize_json(
        value["started_at"]
    )
    import capo_bedrock_agent.types.date_timestamp

    out["updatedAt"] = capo_bedrock_agent.types.date_timestamp.serialize_json(
        value["updated_at"]
    )
    if "text_ready_at" in value:
        import capo_bedrock_agent.types.date_timestamp

        out["textReadyAt"] = capo_bedrock_agent.types.date_timestamp.serialize_json(
            value["text_ready_at"]
        )
    return out


def deserialize_json(data: dict) -> IngestionJob:
    out: IngestionJob = {}  # type: ignore[typeddict-item]
    if data.get("knowledgeBaseId") is not None:
        out["knowledge_base_id"] = data["knowledgeBaseId"]
    else:
        raise DeserializationError("IngestionJob.knowledge_base_id required")
    if data.get("dataSourceId") is not None:
        out["data_source_id"] = data["dataSourceId"]
    else:
        raise DeserializationError("IngestionJob.data_source_id required")
    if data.get("ingestionJobId") is not None:
        out["ingestion_job_id"] = data["ingestionJobId"]
    else:
        raise DeserializationError("IngestionJob.ingestion_job_id required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("status") is not None:
        import capo_bedrock_agent.types.ingestion_job_status

        out["status"] = capo_bedrock_agent.types.ingestion_job_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("IngestionJob.status required")
    if data.get("statistics") is not None:
        import capo_bedrock_agent.types.ingestion_job_statistics

        out["statistics"] = (
            capo_bedrock_agent.types.ingestion_job_statistics.deserialize_json(
                data["statistics"]
            )
        )
    if data.get("failureReasons") is not None:
        import capo_bedrock_agent.types.failure_reasons

        out["failure_reasons"] = (
            capo_bedrock_agent.types.failure_reasons.deserialize_json(
                data["failureReasons"]
            )
        )
    if data.get("startedAt") is not None:
        import capo_bedrock_agent.types.date_timestamp

        out["started_at"] = capo_bedrock_agent.types.date_timestamp.deserialize_json(
            data["startedAt"]
        )
    else:
        raise DeserializationError("IngestionJob.started_at required")
    if data.get("updatedAt") is not None:
        import capo_bedrock_agent.types.date_timestamp

        out["updated_at"] = capo_bedrock_agent.types.date_timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("IngestionJob.updated_at required")
    if data.get("textReadyAt") is not None:
        import capo_bedrock_agent.types.date_timestamp

        out["text_ready_at"] = capo_bedrock_agent.types.date_timestamp.deserialize_json(
            data["textReadyAt"]
        )
    return out
