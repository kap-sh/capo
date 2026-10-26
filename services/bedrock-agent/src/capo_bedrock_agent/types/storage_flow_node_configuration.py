"""Generated from Smithy shape ``com.amazonaws.bedrockagent#StorageFlowNodeConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.storage_flow_node_service_configuration


class StorageFlowNodeConfiguration(TypedDict, closed=True):
    service_configuration: "capo_bedrock_agent.types.storage_flow_node_service_configuration.StorageFlowNodeServiceConfiguration"
    """<p>Contains configurations for the service to use for storing the input into the node.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StorageFlowNodeConfiguration) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.storage_flow_node_service_configuration

    out["serviceConfiguration"] = (
        capo_bedrock_agent.types.storage_flow_node_service_configuration.serialize_json(
            value["service_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> StorageFlowNodeConfiguration:
    out: StorageFlowNodeConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("serviceConfiguration") is not None:
        import capo_bedrock_agent.types.storage_flow_node_service_configuration

        out["service_configuration"] = (
            capo_bedrock_agent.types.storage_flow_node_service_configuration.deserialize_json(
                data["serviceConfiguration"]
            )
        )
    else:
        out["service_configuration"] = {"$unknown": {"name": ""}}
    return out
