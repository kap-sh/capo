"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowInputField``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.flow_execution_content
    import capo_bedrock_agent_runtime.types.node_input_name


class FlowInputField(TypedDict, closed=True):
    name: "capo_bedrock_agent_runtime.types.node_input_name.NodeInputName"
    """<p>The name of the input field as defined in the flow's input schema.</p>"""
    content: (
        "capo_bedrock_agent_runtime.types.flow_execution_content.FlowExecutionContent"
    )
    """<p>The content of the input field, which can contain text or structured data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FlowInputField) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_bedrock_agent_runtime.types.flow_execution_content

    out["content"] = (
        capo_bedrock_agent_runtime.types.flow_execution_content.serialize_json(
            value["content"]
        )
    )
    return out


def deserialize_json(data: dict) -> FlowInputField:
    out: FlowInputField = {}  # type: ignore[typeddict-item]
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
        out["content"] = {"$unknown": {"name": ""}}
    return out
