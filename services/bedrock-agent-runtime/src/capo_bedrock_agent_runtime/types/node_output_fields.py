"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#NodeOutputFields``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.node_output_field

NodeOutputFields: TypeAlias = list[
    "capo_bedrock_agent_runtime.types.node_output_field.NodeOutputField"
]


# --- restJson1 ser/de ---
def serialize_json(value: NodeOutputFields) -> list:
    import capo_bedrock_agent_runtime.types.node_output_field

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agent_runtime.types.node_output_field.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> NodeOutputFields:
    import capo_bedrock_agent_runtime.types.node_output_field

    out: NodeOutputFields = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agent_runtime.types.node_output_field.deserialize_json(item)
        )
    return out


def redact_sensitive(value: NodeOutputFields) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
