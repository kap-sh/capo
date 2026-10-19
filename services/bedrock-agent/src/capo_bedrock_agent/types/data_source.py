"""Generated from Smithy shape ``com.amazonaws.bedrockagent#DataSource``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.data_deletion_policy
    import capo_bedrock_agent.types.data_source_configuration
    import capo_bedrock_agent.types.data_source_status
    import capo_bedrock_agent.types.date_timestamp
    import capo_bedrock_agent.types.description
    import capo_bedrock_agent.types.failure_reasons
    import capo_bedrock_agent.types.id
    import capo_bedrock_agent.types.name
    import capo_bedrock_agent.types.server_side_encryption_configuration
    import capo_bedrock_agent.types.vector_ingestion_configuration


class DataSource(TypedDict, closed=True):
    knowledge_base_id: "capo_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the knowledge base to which the data source belongs.</p>"""
    data_source_id: "capo_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the data source.</p>"""
    name: "capo_bedrock_agent.types.name.Name"
    """<p>The name of the data source.</p>"""
    status: "capo_bedrock_agent.types.data_source_status.DataSourceStatus"
    """<p>The status of the data source. The following statuses are possible:</p> <ul> <li> <p>Available – The data source has been created and is ready for ingestion into the knowledge base.</p> </li> <li> <p>Deleting – The data source is being deleted.</p> </li> </ul>"""
    description: NotRequired["capo_bedrock_agent.types.description.Description"]
    """<p>The description of the data source.</p>"""
    data_source_configuration: (
        "capo_bedrock_agent.types.data_source_configuration.DataSourceConfiguration"
    )
    """<p>The connection configuration for the data source.</p>"""
    server_side_encryption_configuration: NotRequired[
        "capo_bedrock_agent.types.server_side_encryption_configuration.ServerSideEncryptionConfiguration"
    ]
    """<p>Contains details about the configuration of the server-side encryption.</p>"""
    vector_ingestion_configuration: NotRequired[
        "capo_bedrock_agent.types.vector_ingestion_configuration.VectorIngestionConfiguration"
    ]
    """<p>Contains details about how to ingest the documents in the data source.</p>"""
    data_deletion_policy: NotRequired[
        "capo_bedrock_agent.types.data_deletion_policy.DataDeletionPolicy"
    ]
    """<p>The data deletion policy for the data source.</p>"""
    created_at: "capo_bedrock_agent.types.date_timestamp.DateTimestamp"
    """<p>The time at which the data source was created.</p>"""
    updated_at: "capo_bedrock_agent.types.date_timestamp.DateTimestamp"
    """<p>The time at which the data source was last updated.</p>"""
    failure_reasons: NotRequired[
        "capo_bedrock_agent.types.failure_reasons.FailureReasons"
    ]
    """<p>The detailed reasons on the failure to delete a data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSource) -> dict:
    out: dict = {}
    out["knowledgeBaseId"] = value["knowledge_base_id"]
    out["dataSourceId"] = value["data_source_id"]
    out["name"] = value["name"]
    import capo_bedrock_agent.types.data_source_status

    out["status"] = capo_bedrock_agent.types.data_source_status.serialize_json(
        value["status"]
    )
    if "description" in value:
        out["description"] = value["description"]
    import capo_bedrock_agent.types.data_source_configuration

    out["dataSourceConfiguration"] = (
        capo_bedrock_agent.types.data_source_configuration.serialize_json(
            value["data_source_configuration"]
        )
    )
    if "server_side_encryption_configuration" in value:
        import capo_bedrock_agent.types.server_side_encryption_configuration

        out["serverSideEncryptionConfiguration"] = (
            capo_bedrock_agent.types.server_side_encryption_configuration.serialize_json(
                value["server_side_encryption_configuration"]
            )
        )
    if "vector_ingestion_configuration" in value:
        import capo_bedrock_agent.types.vector_ingestion_configuration

        out["vectorIngestionConfiguration"] = (
            capo_bedrock_agent.types.vector_ingestion_configuration.serialize_json(
                value["vector_ingestion_configuration"]
            )
        )
    if "data_deletion_policy" in value:
        import capo_bedrock_agent.types.data_deletion_policy

        out["dataDeletionPolicy"] = (
            capo_bedrock_agent.types.data_deletion_policy.serialize_json(
                value["data_deletion_policy"]
            )
        )
    import capo_bedrock_agent.types.date_timestamp

    out["createdAt"] = capo_bedrock_agent.types.date_timestamp.serialize_json(
        value["created_at"]
    )
    import capo_bedrock_agent.types.date_timestamp

    out["updatedAt"] = capo_bedrock_agent.types.date_timestamp.serialize_json(
        value["updated_at"]
    )
    if "failure_reasons" in value:
        import capo_bedrock_agent.types.failure_reasons

        out["failureReasons"] = capo_bedrock_agent.types.failure_reasons.serialize_json(
            value["failure_reasons"]
        )
    return out


def deserialize_json(data: dict) -> DataSource:
    out: DataSource = {}  # type: ignore[typeddict-item]
    if data.get("knowledgeBaseId") is not None:
        out["knowledge_base_id"] = data["knowledgeBaseId"]
    else:
        out["knowledge_base_id"] = ""
    if data.get("dataSourceId") is not None:
        out["data_source_id"] = data["dataSourceId"]
    else:
        out["data_source_id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("status") is not None:
        import capo_bedrock_agent.types.data_source_status

        out["status"] = capo_bedrock_agent.types.data_source_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_bedrock_agent.types.data_source_status.DataSourceStatus", ""
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("dataSourceConfiguration") is not None:
        import capo_bedrock_agent.types.data_source_configuration

        out["data_source_configuration"] = (
            capo_bedrock_agent.types.data_source_configuration.deserialize_json(
                data["dataSourceConfiguration"]
            )
        )
    else:
        raise DeserializationError("DataSource.data_source_configuration required")
    if data.get("serverSideEncryptionConfiguration") is not None:
        import capo_bedrock_agent.types.server_side_encryption_configuration

        out["server_side_encryption_configuration"] = (
            capo_bedrock_agent.types.server_side_encryption_configuration.deserialize_json(
                data["serverSideEncryptionConfiguration"]
            )
        )
    if data.get("vectorIngestionConfiguration") is not None:
        import capo_bedrock_agent.types.vector_ingestion_configuration

        out["vector_ingestion_configuration"] = (
            capo_bedrock_agent.types.vector_ingestion_configuration.deserialize_json(
                data["vectorIngestionConfiguration"]
            )
        )
    if data.get("dataDeletionPolicy") is not None:
        import capo_bedrock_agent.types.data_deletion_policy

        out["data_deletion_policy"] = (
            capo_bedrock_agent.types.data_deletion_policy.deserialize_json(
                data["dataDeletionPolicy"]
            )
        )
    if data.get("createdAt") is not None:
        import capo_bedrock_agent.types.date_timestamp

        out["created_at"] = capo_bedrock_agent.types.date_timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("updatedAt") is not None:
        import capo_bedrock_agent.types.date_timestamp

        out["updated_at"] = capo_bedrock_agent.types.date_timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("failureReasons") is not None:
        import capo_bedrock_agent.types.failure_reasons

        out["failure_reasons"] = (
            capo_bedrock_agent.types.failure_reasons.deserialize_json(
                data["failureReasons"]
            )
        )
    return out


def redact_sensitive(value: DataSource) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "data_source_configuration" in value:
        import capo_bedrock_agent.types.data_source_configuration

        out["data_source_configuration"] = (
            capo_bedrock_agent.types.data_source_configuration.redact_sensitive(
                value["data_source_configuration"]
            )
        )
    return out
