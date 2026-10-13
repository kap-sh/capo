"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#Citations``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.citation

Citations: TypeAlias = list["capo_bedrock_agent_runtime.types.citation.Citation"]


# --- restJson1 ser/de ---
def serialize_json(value: Citations) -> list:
    import capo_bedrock_agent_runtime.types.citation

    out: list = []
    for item in value:
        out.append(capo_bedrock_agent_runtime.types.citation.serialize_json(item))
    return out


def deserialize_json(data: list) -> Citations:
    import capo_bedrock_agent_runtime.types.citation

    out: Citations = []
    for item in data:
        if item is None:
            continue
        out.append(capo_bedrock_agent_runtime.types.citation.deserialize_json(item))
    return out


def redact_sensitive(value: Citations) -> list[Any]:
    import capo_bedrock_agent_runtime.types.citation

    return [
        capo_bedrock_agent_runtime.types.citation.redact_sensitive(item)
        for item in value
    ]
