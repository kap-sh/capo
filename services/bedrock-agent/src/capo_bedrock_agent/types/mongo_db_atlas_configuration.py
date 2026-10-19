"""Generated from Smithy shape ``com.amazonaws.bedrockagent#MongoDbAtlasConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.mongo_db_atlas_collection_name
    import capo_bedrock_agent.types.mongo_db_atlas_database_name
    import capo_bedrock_agent.types.mongo_db_atlas_endpoint
    import capo_bedrock_agent.types.mongo_db_atlas_endpoint_service_name
    import capo_bedrock_agent.types.mongo_db_atlas_field_mapping
    import capo_bedrock_agent.types.mongo_db_atlas_index_name
    import capo_bedrock_agent.types.secret_arn


class MongoDbAtlasConfiguration(TypedDict, closed=True):
    endpoint: "capo_bedrock_agent.types.mongo_db_atlas_endpoint.MongoDbAtlasEndpoint"
    """<p>The endpoint URL of your MongoDB Atlas cluster for your knowledge base.</p>"""
    database_name: (
        "capo_bedrock_agent.types.mongo_db_atlas_database_name.MongoDbAtlasDatabaseName"
    )
    """<p>The database name in your MongoDB Atlas cluster for your knowledge base.</p>"""
    collection_name: "capo_bedrock_agent.types.mongo_db_atlas_collection_name.MongoDbAtlasCollectionName"
    """<p>The collection name of the knowledge base in MongoDB Atlas.</p>"""
    vector_index_name: (
        "capo_bedrock_agent.types.mongo_db_atlas_index_name.MongoDbAtlasIndexName"
    )
    """<p>The name of the MongoDB Atlas vector search index.</p>"""
    credentials_secret_arn: "capo_bedrock_agent.types.secret_arn.SecretArn"
    """<p>The Amazon Resource Name (ARN) of the secret that you created in Secrets Manager that contains user credentials for your MongoDB Atlas cluster.</p>"""
    field_mapping: (
        "capo_bedrock_agent.types.mongo_db_atlas_field_mapping.MongoDbAtlasFieldMapping"
    )
    """<p>Contains the names of the fields to which to map information about the vector store.</p>"""
    endpoint_service_name: NotRequired[
        "capo_bedrock_agent.types.mongo_db_atlas_endpoint_service_name.MongoDbAtlasEndpointServiceName"
    ]
    """<p>The name of the VPC endpoint service in your account that is connected to your MongoDB Atlas cluster.</p>"""
    text_index_name: NotRequired[
        "capo_bedrock_agent.types.mongo_db_atlas_index_name.MongoDbAtlasIndexName"
    ]
    """<p>The name of the text search index in the MongoDB collection. This is required for using the hybrid search feature.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MongoDbAtlasConfiguration) -> dict:
    out: dict = {}
    out["endpoint"] = value["endpoint"]
    out["databaseName"] = value["database_name"]
    out["collectionName"] = value["collection_name"]
    out["vectorIndexName"] = value["vector_index_name"]
    out["credentialsSecretArn"] = value["credentials_secret_arn"]
    import capo_bedrock_agent.types.mongo_db_atlas_field_mapping

    out["fieldMapping"] = (
        capo_bedrock_agent.types.mongo_db_atlas_field_mapping.serialize_json(
            value["field_mapping"]
        )
    )
    if "endpoint_service_name" in value:
        out["endpointServiceName"] = value["endpoint_service_name"]
    if "text_index_name" in value:
        out["textIndexName"] = value["text_index_name"]
    return out


def deserialize_json(data: dict) -> MongoDbAtlasConfiguration:
    out: MongoDbAtlasConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("endpoint") is not None:
        out["endpoint"] = data["endpoint"]
    else:
        out["endpoint"] = ""
    if data.get("databaseName") is not None:
        out["database_name"] = data["databaseName"]
    else:
        out["database_name"] = ""
    if data.get("collectionName") is not None:
        out["collection_name"] = data["collectionName"]
    else:
        out["collection_name"] = ""
    if data.get("vectorIndexName") is not None:
        out["vector_index_name"] = data["vectorIndexName"]
    else:
        out["vector_index_name"] = ""
    if data.get("credentialsSecretArn") is not None:
        out["credentials_secret_arn"] = data["credentialsSecretArn"]
    else:
        out["credentials_secret_arn"] = ""
    if data.get("fieldMapping") is not None:
        import capo_bedrock_agent.types.mongo_db_atlas_field_mapping

        out["field_mapping"] = (
            capo_bedrock_agent.types.mongo_db_atlas_field_mapping.deserialize_json(
                data["fieldMapping"]
            )
        )
    else:
        raise DeserializationError("MongoDbAtlasConfiguration.field_mapping required")
    if data.get("endpointServiceName") is not None:
        out["endpoint_service_name"] = data["endpointServiceName"]
    if data.get("textIndexName") is not None:
        out["text_index_name"] = data["textIndexName"]
    return out
