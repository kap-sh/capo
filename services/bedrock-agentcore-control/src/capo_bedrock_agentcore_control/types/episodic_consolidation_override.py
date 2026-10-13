"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#EpisodicConsolidationOverride``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.prompt


class EpisodicConsolidationOverride(TypedDict, closed=True):
    append_to_prompt: "capo_bedrock_agentcore_control.types.prompt.Prompt"
    """<p>The text appended to the prompt for the consolidation step of the episodic memory strategy.</p>"""
    model_id: "str"
    """<p>The model ID used for the consolidation step of the episodic memory strategy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EpisodicConsolidationOverride) -> dict:
    out: dict = {}
    out["appendToPrompt"] = value["append_to_prompt"]
    out["modelId"] = value["model_id"]
    return out


def deserialize_json(data: dict) -> EpisodicConsolidationOverride:
    out: EpisodicConsolidationOverride = {}  # type: ignore[typeddict-item]
    if data.get("appendToPrompt") is not None:
        out["append_to_prompt"] = data["appendToPrompt"]
    else:
        raise DeserializationError(
            "EpisodicConsolidationOverride.append_to_prompt required"
        )
    if data.get("modelId") is not None:
        out["model_id"] = data["modelId"]
    else:
        raise DeserializationError("EpisodicConsolidationOverride.model_id required")
    return out


def redact_sensitive(value: EpisodicConsolidationOverride) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "append_to_prompt" in value:
        out["append_to_prompt"] = "*** Sensitive Data Redacted ***"
    return out
