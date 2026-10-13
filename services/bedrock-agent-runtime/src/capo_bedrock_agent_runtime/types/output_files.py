"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#OutputFiles``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.output_file

OutputFiles: TypeAlias = list["capo_bedrock_agent_runtime.types.output_file.OutputFile"]


# --- restJson1 ser/de ---
def serialize_json(value: OutputFiles) -> list:
    import capo_bedrock_agent_runtime.types.output_file

    out: list = []
    for item in value:
        out.append(capo_bedrock_agent_runtime.types.output_file.serialize_json(item))
    return out


def deserialize_json(data: list) -> OutputFiles:
    import capo_bedrock_agent_runtime.types.output_file

    out: OutputFiles = []
    for item in data:
        if item is None:
            continue
        out.append(capo_bedrock_agent_runtime.types.output_file.deserialize_json(item))
    return out


def redact_sensitive(value: OutputFiles) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
