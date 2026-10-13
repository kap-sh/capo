"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#EpisodicOverrideConsolidationConfigurationInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.prompt


class EpisodicOverrideConsolidationConfigurationInput(TypedDict, closed=True):
    append_to_prompt: "capo_bedrock_agentcore_control.types.prompt.Prompt"
    """<p>The text to append to the prompt for the consolidation step of the episodic memory strategy.</p>"""
    model_id: "str"
    """<p>The model ID to use for the consolidation step of the episodic memory strategy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EpisodicOverrideConsolidationConfigurationInput) -> dict:
    out: dict = {}
    out["appendToPrompt"] = value["append_to_prompt"]
    out["modelId"] = value["model_id"]
    return out


def deserialize_json(data: dict) -> EpisodicOverrideConsolidationConfigurationInput:
    out: EpisodicOverrideConsolidationConfigurationInput = {}  # type: ignore[typeddict-item]
    if data.get("appendToPrompt") is not None:
        out["append_to_prompt"] = data["appendToPrompt"]
    else:
        raise DeserializationError(
            "EpisodicOverrideConsolidationConfigurationInput.append_to_prompt required"
        )
    if data.get("modelId") is not None:
        out["model_id"] = data["modelId"]
    else:
        raise DeserializationError(
            "EpisodicOverrideConsolidationConfigurationInput.model_id required"
        )
    return out


def redact_sensitive(
    value: EpisodicOverrideConsolidationConfigurationInput,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "append_to_prompt" in value:
        out["append_to_prompt"] = "*** Sensitive Data Redacted ***"
    return out
