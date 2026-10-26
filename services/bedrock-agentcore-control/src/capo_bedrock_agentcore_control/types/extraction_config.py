"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ExtractionConfig``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)
from capo_bedrock_agentcore_control.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.llm_extraction_config


class _ExtractionConfig_llmExtractionConfig(TypedDict, closed=True):
    llmExtractionConfig: (
        "capo_bedrock_agentcore_control.types.llm_extraction_config.LlmExtractionConfig"
    )


ExtractionConfig: TypeAlias = _ExtractionConfig_llmExtractionConfig | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: ExtractionConfig) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ExtractionConfig: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "llmExtractionConfig" in value:
        import capo_bedrock_agentcore_control.types.llm_extraction_config

        return {
            "llmExtractionConfig": capo_bedrock_agentcore_control.types.llm_extraction_config.serialize_json(
                value["llmExtractionConfig"]
            )
        }
    else:
        raise SerializationError("ExtractionConfig: no variant present")


def deserialize_json(data: dict) -> ExtractionConfig:
    if data.get("llmExtractionConfig") is not None:
        import capo_bedrock_agentcore_control.types.llm_extraction_config

        return {
            "llmExtractionConfig": capo_bedrock_agentcore_control.types.llm_extraction_config.deserialize_json(
                data["llmExtractionConfig"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ExtractionConfig: no recognized variant key")


def redact_sensitive(value: ExtractionConfig) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "llmExtractionConfig" in value:
        import capo_bedrock_agentcore_control.types.llm_extraction_config

        out["llmExtractionConfig"] = (
            capo_bedrock_agentcore_control.types.llm_extraction_config.redact_sensitive(
                value["llmExtractionConfig"]
            )
        )
    return out
