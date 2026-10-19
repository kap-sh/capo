"""Generated from Smithy shape ``com.amazonaws.bedrockagent#RetrievalFlowNodeConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.retrieval_flow_node_service_configuration


class RetrievalFlowNodeConfiguration(TypedDict, closed=True):
    service_configuration: "capo_bedrock_agent.types.retrieval_flow_node_service_configuration.RetrievalFlowNodeServiceConfiguration"
    """<p>Contains configurations for the service to use for retrieving data to return as the output from the node.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RetrievalFlowNodeConfiguration) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.retrieval_flow_node_service_configuration

    out["serviceConfiguration"] = (
        capo_bedrock_agent.types.retrieval_flow_node_service_configuration.serialize_json(
            value["service_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> RetrievalFlowNodeConfiguration:
    out: RetrievalFlowNodeConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("serviceConfiguration") is not None:
        import capo_bedrock_agent.types.retrieval_flow_node_service_configuration

        out["service_configuration"] = (
            capo_bedrock_agent.types.retrieval_flow_node_service_configuration.deserialize_json(
                data["serviceConfiguration"]
            )
        )
    else:
        import capo_bedrock_agent.types._unknown

        out["service_configuration"] = (
            capo_bedrock_agent.types._unknown.UnknownUnionMember("")
        )
    return out
