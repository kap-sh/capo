"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#PromptConfigurations``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.prompt_configuration

PromptConfigurations: TypeAlias = list[
    "capo_bedrock_agent_runtime.types.prompt_configuration.PromptConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: PromptConfigurations) -> list:
    import capo_bedrock_agent_runtime.types.prompt_configuration

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agent_runtime.types.prompt_configuration.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> PromptConfigurations:
    import capo_bedrock_agent_runtime.types.prompt_configuration

    out: PromptConfigurations = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agent_runtime.types.prompt_configuration.deserialize_json(item)
        )
    return out


def redact_sensitive(value: PromptConfigurations) -> list[Any]:
    import capo_bedrock_agent_runtime.types.prompt_configuration

    return [
        capo_bedrock_agent_runtime.types.prompt_configuration.redact_sensitive(item)
        for item in value
    ]
