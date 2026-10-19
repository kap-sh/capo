"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowOutputField``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.flow_execution_content
    import capo_bedrock_agent_runtime.types.node_output_name


class FlowOutputField(TypedDict, closed=True):
    name: "capo_bedrock_agent_runtime.types.node_output_name.NodeOutputName"
    """<p>The name of the output field as defined in the flow's output schema.</p>"""
    content: (
        "capo_bedrock_agent_runtime.types.flow_execution_content.FlowExecutionContent"
    )
    """<p>The content of the output field, which can contain text or structured data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FlowOutputField) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_bedrock_agent_runtime.types.flow_execution_content

    out["content"] = (
        capo_bedrock_agent_runtime.types.flow_execution_content.serialize_json(
            value["content"]
        )
    )
    return out


def deserialize_json(data: dict) -> FlowOutputField:
    out: FlowOutputField = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("content") is not None:
        import capo_bedrock_agent_runtime.types.flow_execution_content

        out["content"] = (
            capo_bedrock_agent_runtime.types.flow_execution_content.deserialize_json(
                data["content"]
            )
        )
    else:
        import capo_bedrock_agent_runtime.types._unknown

        out["content"] = capo_bedrock_agent_runtime.types._unknown.UnknownUnionMember(
            ""
        )
    return out
