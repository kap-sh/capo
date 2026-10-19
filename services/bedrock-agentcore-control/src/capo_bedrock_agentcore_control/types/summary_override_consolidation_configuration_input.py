"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#SummaryOverrideConsolidationConfigurationInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.prompt


class SummaryOverrideConsolidationConfigurationInput(TypedDict, closed=True):
    append_to_prompt: "capo_bedrock_agentcore_control.types.prompt.Prompt"
    """<p>The text to append to the prompt for summary consolidation.</p>"""
    model_id: "str"
    """<p>The model ID to use for summary consolidation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SummaryOverrideConsolidationConfigurationInput) -> dict:
    out: dict = {}
    out["appendToPrompt"] = value["append_to_prompt"]
    out["modelId"] = value["model_id"]
    return out


def deserialize_json(data: dict) -> SummaryOverrideConsolidationConfigurationInput:
    out: SummaryOverrideConsolidationConfigurationInput = {}  # type: ignore[typeddict-item]
    if data.get("appendToPrompt") is not None:
        out["append_to_prompt"] = data["appendToPrompt"]
    else:
        out["append_to_prompt"] = ""
    if data.get("modelId") is not None:
        out["model_id"] = data["modelId"]
    else:
        out["model_id"] = ""
    return out


def redact_sensitive(
    value: SummaryOverrideConsolidationConfigurationInput,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "append_to_prompt" in value:
        out["append_to_prompt"] = "*** Sensitive Data Redacted ***"
    return out
