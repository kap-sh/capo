"""Generated from Smithy shape ``com.amazonaws.bedrockagent#StorageFlowNodeServiceConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agent.errors import DeserializationError, SerializationError
from capo_bedrock_agent.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agent.types.storage_flow_node_s3_configuration


class _StorageFlowNodeServiceConfiguration_s3(TypedDict, closed=True):
    s3: "capo_bedrock_agent.types.storage_flow_node_s3_configuration.StorageFlowNodeS3Configuration"


StorageFlowNodeServiceConfiguration: TypeAlias = (
    _StorageFlowNodeServiceConfiguration_s3 | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: StorageFlowNodeServiceConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"StorageFlowNodeServiceConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "s3" in value:
        import capo_bedrock_agent.types.storage_flow_node_s3_configuration

        return {
            "s3": capo_bedrock_agent.types.storage_flow_node_s3_configuration.serialize_json(
                value["s3"]
            )
        }
    else:
        raise SerializationError(
            "StorageFlowNodeServiceConfiguration: no variant present"
        )


def deserialize_json(data: dict) -> StorageFlowNodeServiceConfiguration:
    if data.get("s3") is not None:
        import capo_bedrock_agent.types.storage_flow_node_s3_configuration

        return {
            "s3": capo_bedrock_agent.types.storage_flow_node_s3_configuration.deserialize_json(
                data["s3"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "StorageFlowNodeServiceConfiguration: no recognized variant key"
        )
