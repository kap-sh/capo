"""Generated from Smithy shape ``com.amazonaws.bedrockagent#RetrievalFlowNodeServiceConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agent.errors import DeserializationError, SerializationError
from capo_bedrock_agent.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agent.types.retrieval_flow_node_s3_configuration


class _RetrievalFlowNodeServiceConfiguration_s3(TypedDict, closed=True):
    s3: "capo_bedrock_agent.types.retrieval_flow_node_s3_configuration.RetrievalFlowNodeS3Configuration"


RetrievalFlowNodeServiceConfiguration: TypeAlias = (
    _RetrievalFlowNodeServiceConfiguration_s3 | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: RetrievalFlowNodeServiceConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"RetrievalFlowNodeServiceConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "s3" in value:
        import capo_bedrock_agent.types.retrieval_flow_node_s3_configuration

        return {
            "s3": capo_bedrock_agent.types.retrieval_flow_node_s3_configuration.serialize_json(
                value["s3"]
            )
        }
    else:
        raise SerializationError(
            "RetrievalFlowNodeServiceConfiguration: no variant present"
        )


def deserialize_json(data: dict) -> RetrievalFlowNodeServiceConfiguration:
    if data.get("s3") is not None:
        import capo_bedrock_agent.types.retrieval_flow_node_s3_configuration

        return {
            "s3": capo_bedrock_agent.types.retrieval_flow_node_s3_configuration.deserialize_json(
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
            "RetrievalFlowNodeServiceConfiguration: no recognized variant key"
        )
