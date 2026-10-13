"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#SemanticOverrideConsolidationConfigurationInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.prompt


class SemanticOverrideConsolidationConfigurationInput(TypedDict, closed=True):
    append_to_prompt: "capo_bedrock_agentcore_control.types.prompt.Prompt"
    """<p>The text to append to the prompt for semantic consolidation.</p>"""
    model_id: "str"
    """<p>The model ID to use for semantic consolidation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SemanticOverrideConsolidationConfigurationInput) -> dict:
    out: dict = {}
    out["appendToPrompt"] = value["append_to_prompt"]
    out["modelId"] = value["model_id"]
    return out


def deserialize_json(data: dict) -> SemanticOverrideConsolidationConfigurationInput:
    out: SemanticOverrideConsolidationConfigurationInput = {}  # type: ignore[typeddict-item]
    if data.get("appendToPrompt") is not None:
        out["append_to_prompt"] = data["appendToPrompt"]
    else:
        raise DeserializationError(
            "SemanticOverrideConsolidationConfigurationInput.append_to_prompt required"
        )
    if data.get("modelId") is not None:
        out["model_id"] = data["modelId"]
    else:
        raise DeserializationError(
            "SemanticOverrideConsolidationConfigurationInput.model_id required"
        )
    return out


def redact_sensitive(
    value: SemanticOverrideConsolidationConfigurationInput,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "append_to_prompt" in value:
        out["append_to_prompt"] = "*** Sensitive Data Redacted ***"
    return out
