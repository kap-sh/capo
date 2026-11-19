"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#GenerationSource``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError, SerializationError
from capo_bedrock_agentcore.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.trace_generation_source


class GenerationSourceTraceGenerationMember(TypedDict, closed=True):
    traceGeneration: (
        "capo_bedrock_agentcore.types.trace_generation_source.TraceGenerationSource"
    )


GenerationSource: TypeAlias = GenerationSourceTraceGenerationMember | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: GenerationSource) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"GenerationSource: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "traceGeneration" in value:
        import capo_bedrock_agentcore.types.trace_generation_source

        return {
            "traceGeneration": capo_bedrock_agentcore.types.trace_generation_source.serialize_json(
                value["traceGeneration"]
            )
        }
    else:
        raise SerializationError("GenerationSource: no variant present")


def deserialize_json(data: dict) -> GenerationSource:
    if data.get("traceGeneration") is not None:
        import capo_bedrock_agentcore.types.trace_generation_source

        return {
            "traceGeneration": capo_bedrock_agentcore.types.trace_generation_source.deserialize_json(
                data["traceGeneration"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("GenerationSource: no recognized variant key")
