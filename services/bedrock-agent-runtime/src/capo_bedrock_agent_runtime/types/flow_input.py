"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.flow_input_content
    import capo_bedrock_agent_runtime.types.node_input_name
    import capo_bedrock_agent_runtime.types.node_name
    import capo_bedrock_agent_runtime.types.node_output_name


class FlowInput(TypedDict, closed=True):
    node_name: "capo_bedrock_agent_runtime.types.node_name.NodeName"
    """<p>The name of the flow input node that begins the prompt flow.</p>"""
    node_output_name: NotRequired[
        "capo_bedrock_agent_runtime.types.node_output_name.NodeOutputName"
    ]
    """<p>The name of the output from the flow input node that begins the prompt flow.</p>"""
    content: "capo_bedrock_agent_runtime.types.flow_input_content.FlowInputContent"
    """<p>Contains information about an input into the prompt flow.</p>"""
    node_input_name: NotRequired[
        "capo_bedrock_agent_runtime.types.node_input_name.NodeInputName"
    ]
    """<p>The name of the input from the flow input node.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FlowInput) -> dict:
    out: dict = {}
    out["nodeName"] = value["node_name"]
    if "node_output_name" in value:
        out["nodeOutputName"] = value["node_output_name"]
    import capo_bedrock_agent_runtime.types.flow_input_content

    out["content"] = capo_bedrock_agent_runtime.types.flow_input_content.serialize_json(
        value["content"]
    )
    if "node_input_name" in value:
        out["nodeInputName"] = value["node_input_name"]
    return out


def deserialize_json(data: dict) -> FlowInput:
    out: FlowInput = {}  # type: ignore[typeddict-item]
    if data.get("nodeName") is not None:
        out["node_name"] = data["nodeName"]
    else:
        out["node_name"] = ""
    if data.get("nodeOutputName") is not None:
        out["node_output_name"] = data["nodeOutputName"]
    if data.get("content") is not None:
        import capo_bedrock_agent_runtime.types.flow_input_content

        out["content"] = (
            capo_bedrock_agent_runtime.types.flow_input_content.deserialize_json(
                data["content"]
            )
        )
    else:
        import capo_bedrock_agent_runtime.types._unknown

        out["content"] = capo_bedrock_agent_runtime.types._unknown.UnknownUnionMember(
            ""
        )
    if data.get("nodeInputName") is not None:
        out["node_input_name"] = data["nodeInputName"]
    return out


def redact_sensitive(value: FlowInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "content" in value:
        out["content"] = "*** Sensitive Data Redacted ***"
    return out
