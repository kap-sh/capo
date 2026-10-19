"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#NodeInputExecutionChainItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.flow_control_node_type
    import capo_bedrock_agent_runtime.types.node_name


class NodeInputExecutionChainItem(TypedDict, closed=True):
    node_name: "capo_bedrock_agent_runtime.types.node_name.NodeName"
    """<p>The name of the node in the execution chain.</p>"""
    index: NotRequired["int"]
    """<p>The index position of this item in the execution chain.</p>"""
    type: "capo_bedrock_agent_runtime.types.flow_control_node_type.FlowControlNodeType"
    """<p>The type of execution chain item. Supported values are Iterator and Loop.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NodeInputExecutionChainItem) -> dict:
    out: dict = {}
    out["nodeName"] = value["node_name"]
    if "index" in value:
        out["index"] = value["index"]
    import capo_bedrock_agent_runtime.types.flow_control_node_type

    out["type"] = (
        capo_bedrock_agent_runtime.types.flow_control_node_type.serialize_json(
            value["type"]
        )
    )
    return out


def deserialize_json(data: dict) -> NodeInputExecutionChainItem:
    out: NodeInputExecutionChainItem = {}  # type: ignore[typeddict-item]
    if data.get("nodeName") is not None:
        out["node_name"] = data["nodeName"]
    else:
        out["node_name"] = ""
    if data.get("index") is not None:
        out["index"] = data["index"]
    if data.get("type") is not None:
        import capo_bedrock_agent_runtime.types.flow_control_node_type

        out["type"] = (
            capo_bedrock_agent_runtime.types.flow_control_node_type.deserialize_json(
                data["type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_bedrock_agent_runtime.types.flow_control_node_type.FlowControlNodeType",
            "",
        )
    return out
