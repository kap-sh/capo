"""Generated from Smithy shape ``com.amazonaws.bedrockagent#IngestionJobSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.date_timestamp
    import capo_bedrock_agent.types.description
    import capo_bedrock_agent.types.id
    import capo_bedrock_agent.types.ingestion_job_statistics
    import capo_bedrock_agent.types.ingestion_job_status


class IngestionJobSummary(TypedDict, closed=True):
    knowledge_base_id: "capo_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the knowledge base for the data ingestion job.</p>"""
    data_source_id: "capo_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the data source for the data ingestion job.</p>"""
    ingestion_job_id: "capo_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the data ingestion job.</p>"""
    description: NotRequired["capo_bedrock_agent.types.description.Description"]
    """<p>The description of the data ingestion job.</p>"""
    status: "capo_bedrock_agent.types.ingestion_job_status.IngestionJobStatus"
    """<p>The status of the data ingestion job.</p>"""
    started_at: "capo_bedrock_agent.types.date_timestamp.DateTimestamp"
    """<p>The time the data ingestion job started.</p>"""
    updated_at: "capo_bedrock_agent.types.date_timestamp.DateTimestamp"
    """<p>The time the data ingestion job was last updated.</p>"""
    text_ready_at: NotRequired["capo_bedrock_agent.types.date_timestamp.DateTimestamp"]
    """<p>The time at which all text content in the data ingestion job finished extraction and became available to query.</p> <p>This time isn't returned until text extraction is complete for all the documents in the job.</p>"""
    statistics: NotRequired[
        "capo_bedrock_agent.types.ingestion_job_statistics.IngestionJobStatistics"
    ]
    """<p>Contains statistics for the data ingestion job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IngestionJobSummary) -> dict:
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
    if "statistics" in value:
        import capo_bedrock_agent.types.ingestion_job_statistics

        out["statistics"] = (
            capo_bedrock_agent.types.ingestion_job_statistics.serialize_json(
                value["statistics"]
            )
        )
    return out


def deserialize_json(data: dict) -> IngestionJobSummary:
    out: IngestionJobSummary = {}  # type: ignore[typeddict-item]
    if data.get("knowledgeBaseId") is not None:
        out["knowledge_base_id"] = data["knowledgeBaseId"]
    else:
        raise DeserializationError("IngestionJobSummary.knowledge_base_id required")
    if data.get("dataSourceId") is not None:
        out["data_source_id"] = data["dataSourceId"]
    else:
        raise DeserializationError("IngestionJobSummary.data_source_id required")
    if data.get("ingestionJobId") is not None:
        out["ingestion_job_id"] = data["ingestionJobId"]
    else:
        raise DeserializationError("IngestionJobSummary.ingestion_job_id required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("status") is not None:
        import capo_bedrock_agent.types.ingestion_job_status

        out["status"] = capo_bedrock_agent.types.ingestion_job_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("IngestionJobSummary.status required")
    if data.get("startedAt") is not None:
        import capo_bedrock_agent.types.date_timestamp

        out["started_at"] = capo_bedrock_agent.types.date_timestamp.deserialize_json(
            data["startedAt"]
        )
    else:
        raise DeserializationError("IngestionJobSummary.started_at required")
    if data.get("updatedAt") is not None:
        import capo_bedrock_agent.types.date_timestamp

        out["updated_at"] = capo_bedrock_agent.types.date_timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("IngestionJobSummary.updated_at required")
    if data.get("textReadyAt") is not None:
        import capo_bedrock_agent.types.date_timestamp

        out["text_ready_at"] = capo_bedrock_agent.types.date_timestamp.deserialize_json(
            data["textReadyAt"]
        )
    if data.get("statistics") is not None:
        import capo_bedrock_agent.types.ingestion_job_statistics

        out["statistics"] = (
            capo_bedrock_agent.types.ingestion_job_statistics.deserialize_json(
                data["statistics"]
            )
        )
    return out
