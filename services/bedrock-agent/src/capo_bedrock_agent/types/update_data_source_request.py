"""Generated from Smithy shape ``com.amazonaws.bedrockagent#UpdateDataSourceRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.data_deletion_policy
    import capo_bedrock_agent.types.data_source_configuration
    import capo_bedrock_agent.types.description
    import capo_bedrock_agent.types.id
    import capo_bedrock_agent.types.name
    import capo_bedrock_agent.types.server_side_encryption_configuration
    import capo_bedrock_agent.types.vector_ingestion_configuration


class UpdateDataSourceRequest(TypedDict, closed=True):
    knowledge_base_id: "capo_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the knowledge base for the data source.</p>"""
    data_source_id: "capo_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the data source.</p>"""
    name: "capo_bedrock_agent.types.name.Name"
    """<p>Specifies a new name for the data source.</p>"""
    description: NotRequired["capo_bedrock_agent.types.description.Description"]
    """<p>Specifies a new description for the data source.</p>"""
    data_source_configuration: (
        "capo_bedrock_agent.types.data_source_configuration.DataSourceConfiguration"
    )
    """<p>The connection configuration for the data source that you want to update.</p>"""
    data_deletion_policy: NotRequired[
        "capo_bedrock_agent.types.data_deletion_policy.DataDeletionPolicy"
    ]
    """<p>The data deletion policy for the data source that you want to update.</p>"""
    server_side_encryption_configuration: NotRequired[
        "capo_bedrock_agent.types.server_side_encryption_configuration.ServerSideEncryptionConfiguration"
    ]
    """<p>Contains details about server-side encryption of the data source.</p>"""
    vector_ingestion_configuration: NotRequired[
        "capo_bedrock_agent.types.vector_ingestion_configuration.VectorIngestionConfiguration"
    ]
    """<p>Contains details about how to ingest the documents in the data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDataSourceRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_bedrock_agent.types.data_source_configuration

    out["dataSourceConfiguration"] = (
        capo_bedrock_agent.types.data_source_configuration.serialize_json(
            value["data_source_configuration"]
        )
    )
    if "data_deletion_policy" in value:
        import capo_bedrock_agent.types.data_deletion_policy

        out["dataDeletionPolicy"] = (
            capo_bedrock_agent.types.data_deletion_policy.serialize_json(
                value["data_deletion_policy"]
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
    return out


def deserialize_json(data: dict) -> UpdateDataSourceRequest:
    out: UpdateDataSourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
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
        raise DeserializationError(
            "UpdateDataSourceRequest.data_source_configuration required"
        )
    if data.get("dataDeletionPolicy") is not None:
        import capo_bedrock_agent.types.data_deletion_policy

        out["data_deletion_policy"] = (
            capo_bedrock_agent.types.data_deletion_policy.deserialize_json(
                data["dataDeletionPolicy"]
            )
        )
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
    return out


def redact_sensitive(value: UpdateDataSourceRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "data_source_configuration" in value:
        import capo_bedrock_agent.types.data_source_configuration

        out["data_source_configuration"] = (
            capo_bedrock_agent.types.data_source_configuration.redact_sensitive(
                value["data_source_configuration"]
            )
        )
    return out
