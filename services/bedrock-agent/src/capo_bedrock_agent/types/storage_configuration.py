"""Generated from Smithy shape ``com.amazonaws.bedrockagent#StorageConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.knowledge_base_storage_type
    import capo_bedrock_agent.types.mongo_db_atlas_configuration
    import capo_bedrock_agent.types.neptune_analytics_configuration
    import capo_bedrock_agent.types.open_search_managed_cluster_configuration
    import capo_bedrock_agent.types.open_search_serverless_configuration
    import capo_bedrock_agent.types.pinecone_configuration
    import capo_bedrock_agent.types.rds_configuration
    import capo_bedrock_agent.types.redis_enterprise_cloud_configuration
    import capo_bedrock_agent.types.s3_vectors_configuration


class StorageConfiguration(TypedDict, closed=True):
    type: (
        "capo_bedrock_agent.types.knowledge_base_storage_type.KnowledgeBaseStorageType"
    )
    """<p>The vector store service in which the knowledge base is stored.</p>"""
    opensearch_serverless_configuration: NotRequired[
        "capo_bedrock_agent.types.open_search_serverless_configuration.OpenSearchServerlessConfiguration"
    ]
    """<p>Contains the storage configuration of the knowledge base in Amazon OpenSearch Service.</p>"""
    opensearch_managed_cluster_configuration: NotRequired[
        "capo_bedrock_agent.types.open_search_managed_cluster_configuration.OpenSearchManagedClusterConfiguration"
    ]
    """<p>Contains details about the storage configuration of the knowledge base in OpenSearch Managed Cluster. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-setup-osm.html">Create a vector index in Amazon OpenSearch Service</a>.</p>"""
    pinecone_configuration: NotRequired[
        "capo_bedrock_agent.types.pinecone_configuration.PineconeConfiguration"
    ]
    """<p>Contains the storage configuration of the knowledge base in Pinecone.</p>"""
    redis_enterprise_cloud_configuration: NotRequired[
        "capo_bedrock_agent.types.redis_enterprise_cloud_configuration.RedisEnterpriseCloudConfiguration"
    ]
    """<p>Contains the storage configuration of the knowledge base in Redis Enterprise Cloud.</p>"""
    rds_configuration: NotRequired[
        "capo_bedrock_agent.types.rds_configuration.RdsConfiguration"
    ]
    """<p>Contains details about the storage configuration of the knowledge base in Amazon RDS. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-setup-rds.html">Create a vector index in Amazon RDS</a>.</p>"""
    mongo_db_atlas_configuration: NotRequired[
        "capo_bedrock_agent.types.mongo_db_atlas_configuration.MongoDbAtlasConfiguration"
    ]
    """<p>Contains the storage configuration of the knowledge base in MongoDB Atlas.</p>"""
    neptune_analytics_configuration: NotRequired[
        "capo_bedrock_agent.types.neptune_analytics_configuration.NeptuneAnalyticsConfiguration"
    ]
    """<p>Contains details about the Neptune Analytics configuration of the knowledge base in Amazon Neptune. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-setup-neptune.html">Create a vector index in Amazon Neptune Analytics.</a>.</p>"""
    s3_vectors_configuration: NotRequired[
        "capo_bedrock_agent.types.s3_vectors_configuration.S3VectorsConfiguration"
    ]
    """<p>The configuration settings for storing knowledge base data using S3 vectors. This includes vector index information and S3 bucket details for vector storage.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StorageConfiguration) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.knowledge_base_storage_type

    out["type"] = capo_bedrock_agent.types.knowledge_base_storage_type.serialize_json(
        value["type"]
    )
    if "opensearch_serverless_configuration" in value:
        import capo_bedrock_agent.types.open_search_serverless_configuration

        out["opensearchServerlessConfiguration"] = (
            capo_bedrock_agent.types.open_search_serverless_configuration.serialize_json(
                value["opensearch_serverless_configuration"]
            )
        )
    if "opensearch_managed_cluster_configuration" in value:
        import capo_bedrock_agent.types.open_search_managed_cluster_configuration

        out["opensearchManagedClusterConfiguration"] = (
            capo_bedrock_agent.types.open_search_managed_cluster_configuration.serialize_json(
                value["opensearch_managed_cluster_configuration"]
            )
        )
    if "pinecone_configuration" in value:
        import capo_bedrock_agent.types.pinecone_configuration

        out["pineconeConfiguration"] = (
            capo_bedrock_agent.types.pinecone_configuration.serialize_json(
                value["pinecone_configuration"]
            )
        )
    if "redis_enterprise_cloud_configuration" in value:
        import capo_bedrock_agent.types.redis_enterprise_cloud_configuration

        out["redisEnterpriseCloudConfiguration"] = (
            capo_bedrock_agent.types.redis_enterprise_cloud_configuration.serialize_json(
                value["redis_enterprise_cloud_configuration"]
            )
        )
    if "rds_configuration" in value:
        import capo_bedrock_agent.types.rds_configuration

        out["rdsConfiguration"] = (
            capo_bedrock_agent.types.rds_configuration.serialize_json(
                value["rds_configuration"]
            )
        )
    if "mongo_db_atlas_configuration" in value:
        import capo_bedrock_agent.types.mongo_db_atlas_configuration

        out["mongoDbAtlasConfiguration"] = (
            capo_bedrock_agent.types.mongo_db_atlas_configuration.serialize_json(
                value["mongo_db_atlas_configuration"]
            )
        )
    if "neptune_analytics_configuration" in value:
        import capo_bedrock_agent.types.neptune_analytics_configuration

        out["neptuneAnalyticsConfiguration"] = (
            capo_bedrock_agent.types.neptune_analytics_configuration.serialize_json(
                value["neptune_analytics_configuration"]
            )
        )
    if "s3_vectors_configuration" in value:
        import capo_bedrock_agent.types.s3_vectors_configuration

        out["s3VectorsConfiguration"] = (
            capo_bedrock_agent.types.s3_vectors_configuration.serialize_json(
                value["s3_vectors_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> StorageConfiguration:
    out: StorageConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_bedrock_agent.types.knowledge_base_storage_type

        out["type"] = (
            capo_bedrock_agent.types.knowledge_base_storage_type.deserialize_json(
                data["type"]
            )
        )
    else:
        raise DeserializationError("StorageConfiguration.type required")
    if data.get("opensearchServerlessConfiguration") is not None:
        import capo_bedrock_agent.types.open_search_serverless_configuration

        out["opensearch_serverless_configuration"] = (
            capo_bedrock_agent.types.open_search_serverless_configuration.deserialize_json(
                data["opensearchServerlessConfiguration"]
            )
        )
    if data.get("opensearchManagedClusterConfiguration") is not None:
        import capo_bedrock_agent.types.open_search_managed_cluster_configuration

        out["opensearch_managed_cluster_configuration"] = (
            capo_bedrock_agent.types.open_search_managed_cluster_configuration.deserialize_json(
                data["opensearchManagedClusterConfiguration"]
            )
        )
    if data.get("pineconeConfiguration") is not None:
        import capo_bedrock_agent.types.pinecone_configuration

        out["pinecone_configuration"] = (
            capo_bedrock_agent.types.pinecone_configuration.deserialize_json(
                data["pineconeConfiguration"]
            )
        )
    if data.get("redisEnterpriseCloudConfiguration") is not None:
        import capo_bedrock_agent.types.redis_enterprise_cloud_configuration

        out["redis_enterprise_cloud_configuration"] = (
            capo_bedrock_agent.types.redis_enterprise_cloud_configuration.deserialize_json(
                data["redisEnterpriseCloudConfiguration"]
            )
        )
    if data.get("rdsConfiguration") is not None:
        import capo_bedrock_agent.types.rds_configuration

        out["rds_configuration"] = (
            capo_bedrock_agent.types.rds_configuration.deserialize_json(
                data["rdsConfiguration"]
            )
        )
    if data.get("mongoDbAtlasConfiguration") is not None:
        import capo_bedrock_agent.types.mongo_db_atlas_configuration

        out["mongo_db_atlas_configuration"] = (
            capo_bedrock_agent.types.mongo_db_atlas_configuration.deserialize_json(
                data["mongoDbAtlasConfiguration"]
            )
        )
    if data.get("neptuneAnalyticsConfiguration") is not None:
        import capo_bedrock_agent.types.neptune_analytics_configuration

        out["neptune_analytics_configuration"] = (
            capo_bedrock_agent.types.neptune_analytics_configuration.deserialize_json(
                data["neptuneAnalyticsConfiguration"]
            )
        )
    if data.get("s3VectorsConfiguration") is not None:
        import capo_bedrock_agent.types.s3_vectors_configuration

        out["s3_vectors_configuration"] = (
            capo_bedrock_agent.types.s3_vectors_configuration.deserialize_json(
                data["s3VectorsConfiguration"]
            )
        )
    return out
