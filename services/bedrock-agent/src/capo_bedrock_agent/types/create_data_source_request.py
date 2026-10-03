"""Generated from Smithy shape ``com.amazonaws.bedrockagent#CreateDataSourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.client_token
    import capo_bedrock_agent.types.data_deletion_policy
    import capo_bedrock_agent.types.data_source_configuration
    import capo_bedrock_agent.types.description
    import capo_bedrock_agent.types.id
    import capo_bedrock_agent.types.name
    import capo_bedrock_agent.types.server_side_encryption_configuration
    import capo_bedrock_agent.types.vector_ingestion_configuration


class CreateDataSourceRequest(TypedDict, closed=True):
    knowledge_base_id: "capo_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the knowledge base to which to add the data source.</p>"""
    client_token: NotRequired["capo_bedrock_agent.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>"""
    name: "capo_bedrock_agent.types.name.Name"
    """<p>The name of the data source.</p>"""
    description: NotRequired["capo_bedrock_agent.types.description.Description"]
    """<p>A description of the data source.</p>"""
    data_source_configuration: (
        "capo_bedrock_agent.types.data_source_configuration.DataSourceConfiguration"
    )
    """<p>The connection configuration for the data source.</p>"""
    data_deletion_policy: NotRequired[
        "capo_bedrock_agent.types.data_deletion_policy.DataDeletionPolicy"
    ]
    """<p>The data deletion policy for the data source.</p> <p>You can set the data deletion policy to:</p> <ul> <li> <p>DELETE: Deletes all data from your data source that’s converted into vector embeddings upon deletion of a knowledge base or data source resource. Note that the <b>vector store itself is not deleted</b>, only the data. This flag is ignored if an Amazon Web Services account is deleted.</p> </li> <li> <p>RETAIN: Retains all data from your data source that’s converted into vector embeddings upon deletion of a knowledge base or data source resource. Note that the <b>vector store itself is not deleted</b> if you delete a knowledge base or data source resource.</p> </li> </ul> <note> <p>For managed knowledge bases, the only supported option is <code>DELETE</code>, which is also the default.</p> </note>"""
    server_side_encryption_configuration: NotRequired[
        "capo_bedrock_agent.types.server_side_encryption_configuration.ServerSideEncryptionConfiguration"
    ]
    """<p>Contains details about the server-side encryption for the data source.</p>"""
    vector_ingestion_configuration: NotRequired[
        "capo_bedrock_agent.types.vector_ingestion_configuration.VectorIngestionConfiguration"
    ]
    """<p>Contains details about how to ingest the documents in the data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDataSourceRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
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


def deserialize_json(data: dict) -> CreateDataSourceRequest:
    out: CreateDataSourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateDataSourceRequest.name required")
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
            "CreateDataSourceRequest.data_source_configuration required"
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
