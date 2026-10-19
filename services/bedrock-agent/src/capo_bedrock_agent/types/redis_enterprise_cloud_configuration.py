"""Generated from Smithy shape ``com.amazonaws.bedrockagent#RedisEnterpriseCloudConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.redis_enterprise_cloud_endpoint
    import capo_bedrock_agent.types.redis_enterprise_cloud_field_mapping
    import capo_bedrock_agent.types.redis_enterprise_cloud_index_name
    import capo_bedrock_agent.types.secret_arn


class RedisEnterpriseCloudConfiguration(TypedDict, closed=True):
    endpoint: "capo_bedrock_agent.types.redis_enterprise_cloud_endpoint.RedisEnterpriseCloudEndpoint"
    """<p>The endpoint URL of the Redis Enterprise Cloud database.</p>"""
    vector_index_name: "capo_bedrock_agent.types.redis_enterprise_cloud_index_name.RedisEnterpriseCloudIndexName"
    """<p>The name of the vector index.</p>"""
    credentials_secret_arn: "capo_bedrock_agent.types.secret_arn.SecretArn"
    """<p>The Amazon Resource Name (ARN) of the secret that you created in Secrets Manager that is linked to your Redis Enterprise Cloud database.</p>"""
    field_mapping: "capo_bedrock_agent.types.redis_enterprise_cloud_field_mapping.RedisEnterpriseCloudFieldMapping"
    """<p>Contains the names of the fields to which to map information about the vector store.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RedisEnterpriseCloudConfiguration) -> dict:
    out: dict = {}
    out["endpoint"] = value["endpoint"]
    out["vectorIndexName"] = value["vector_index_name"]
    out["credentialsSecretArn"] = value["credentials_secret_arn"]
    import capo_bedrock_agent.types.redis_enterprise_cloud_field_mapping

    out["fieldMapping"] = (
        capo_bedrock_agent.types.redis_enterprise_cloud_field_mapping.serialize_json(
            value["field_mapping"]
        )
    )
    return out


def deserialize_json(data: dict) -> RedisEnterpriseCloudConfiguration:
    out: RedisEnterpriseCloudConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("endpoint") is not None:
        out["endpoint"] = data["endpoint"]
    else:
        out["endpoint"] = ""
    if data.get("vectorIndexName") is not None:
        out["vector_index_name"] = data["vectorIndexName"]
    else:
        out["vector_index_name"] = ""
    if data.get("credentialsSecretArn") is not None:
        out["credentials_secret_arn"] = data["credentialsSecretArn"]
    else:
        out["credentials_secret_arn"] = ""
    if data.get("fieldMapping") is not None:
        import capo_bedrock_agent.types.redis_enterprise_cloud_field_mapping

        out["field_mapping"] = (
            capo_bedrock_agent.types.redis_enterprise_cloud_field_mapping.deserialize_json(
                data["fieldMapping"]
            )
        )
    else:
        raise DeserializationError(
            "RedisEnterpriseCloudConfiguration.field_mapping required"
        )
    return out
