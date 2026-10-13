"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#InputFiles``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.input_file

InputFiles: TypeAlias = list["capo_bedrock_agent_runtime.types.input_file.InputFile"]


# --- restJson1 ser/de ---
def serialize_json(value: InputFiles) -> list:
    import capo_bedrock_agent_runtime.types.input_file

    out: list = []
    for item in value:
        out.append(capo_bedrock_agent_runtime.types.input_file.serialize_json(item))
    return out


def deserialize_json(data: list) -> InputFiles:
    import capo_bedrock_agent_runtime.types.input_file

    out: InputFiles = []
    for item in data:
        if item is None:
            continue
        out.append(capo_bedrock_agent_runtime.types.input_file.deserialize_json(item))
    return out


def redact_sensitive(value: InputFiles) -> list[Any]:
    import capo_bedrock_agent_runtime.types.input_file

    return [
        capo_bedrock_agent_runtime.types.input_file.redact_sensitive(item)
        for item in value
    ]
