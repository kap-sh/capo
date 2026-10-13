"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#NodeOutputNextList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.node_output_next

NodeOutputNextList: TypeAlias = list[
    "capo_bedrock_agent_runtime.types.node_output_next.NodeOutputNext"
]


# --- restJson1 ser/de ---
def serialize_json(value: NodeOutputNextList) -> list:
    import capo_bedrock_agent_runtime.types.node_output_next

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agent_runtime.types.node_output_next.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> NodeOutputNextList:
    import capo_bedrock_agent_runtime.types.node_output_next

    out: NodeOutputNextList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agent_runtime.types.node_output_next.deserialize_json(item)
        )
    return out


def redact_sensitive(value: NodeOutputNextList) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
