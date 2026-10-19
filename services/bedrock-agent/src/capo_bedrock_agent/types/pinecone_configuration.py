"""Generated from Smithy shape ``com.amazonaws.bedrockagent#PineconeConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.pinecone_connection_string
    import capo_bedrock_agent.types.pinecone_field_mapping
    import capo_bedrock_agent.types.pinecone_namespace
    import capo_bedrock_agent.types.secret_arn


class PineconeConfiguration(TypedDict, closed=True):
    connection_string: (
        "capo_bedrock_agent.types.pinecone_connection_string.PineconeConnectionString"
    )
    """<p>The endpoint URL for your index management page.</p>"""
    credentials_secret_arn: "capo_bedrock_agent.types.secret_arn.SecretArn"
    """<p>The Amazon Resource Name (ARN) of the secret that you created in Secrets Manager that is linked to your Pinecone API key.</p>"""
    namespace: NotRequired[
        "capo_bedrock_agent.types.pinecone_namespace.PineconeNamespace"
    ]
    """<p>The namespace to be used to write new data to your database.</p>"""
    field_mapping: (
        "capo_bedrock_agent.types.pinecone_field_mapping.PineconeFieldMapping"
    )
    """<p>Contains the names of the fields to which to map information about the vector store.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PineconeConfiguration) -> dict:
    out: dict = {}
    out["connectionString"] = value["connection_string"]
    out["credentialsSecretArn"] = value["credentials_secret_arn"]
    if "namespace" in value:
        out["namespace"] = value["namespace"]
    import capo_bedrock_agent.types.pinecone_field_mapping

    out["fieldMapping"] = (
        capo_bedrock_agent.types.pinecone_field_mapping.serialize_json(
            value["field_mapping"]
        )
    )
    return out


def deserialize_json(data: dict) -> PineconeConfiguration:
    out: PineconeConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("connectionString") is not None:
        out["connection_string"] = data["connectionString"]
    else:
        out["connection_string"] = ""
    if data.get("credentialsSecretArn") is not None:
        out["credentials_secret_arn"] = data["credentialsSecretArn"]
    else:
        out["credentials_secret_arn"] = ""
    if data.get("namespace") is not None:
        out["namespace"] = data["namespace"]
    if data.get("fieldMapping") is not None:
        import capo_bedrock_agent.types.pinecone_field_mapping

        out["field_mapping"] = (
            capo_bedrock_agent.types.pinecone_field_mapping.deserialize_json(
                data["fieldMapping"]
            )
        )
    else:
        raise DeserializationError("PineconeConfiguration.field_mapping required")
    return out
