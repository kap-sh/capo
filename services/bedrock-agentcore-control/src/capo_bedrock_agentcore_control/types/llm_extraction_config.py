"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#LlmExtractionConfig``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.definition
    import capo_bedrock_agentcore_control.types.llm_extraction_instruction
    import capo_bedrock_agentcore_control.types.validation


class LlmExtractionConfig(TypedDict, closed=True):
    llm_extraction_instruction: NotRequired[
        "capo_bedrock_agentcore_control.types.llm_extraction_instruction.LlmExtractionInstruction"
    ]
    """<p>Instructions for extraction. Supports built-in operators like LATEST_VALUE or custom natural-language instructions.</p>"""
    definition: "capo_bedrock_agentcore_control.types.definition.Definition"
    """<p>Description of what this metadata field represents.</p>"""
    validation: NotRequired[
        "capo_bedrock_agentcore_control.types.validation.Validation"
    ]
    """<p>Validation rules to constrain extracted values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LlmExtractionConfig) -> dict:
    out: dict = {}
    if "llm_extraction_instruction" in value:
        out["llmExtractionInstruction"] = value["llm_extraction_instruction"]
    out["definition"] = value["definition"]
    if "validation" in value:
        import capo_bedrock_agentcore_control.types.validation

        out["validation"] = (
            capo_bedrock_agentcore_control.types.validation.serialize_json(
                value["validation"]
            )
        )
    return out


def deserialize_json(data: dict) -> LlmExtractionConfig:
    out: LlmExtractionConfig = {}  # type: ignore[typeddict-item]
    if data.get("llmExtractionInstruction") is not None:
        out["llm_extraction_instruction"] = data["llmExtractionInstruction"]
    if data.get("definition") is not None:
        out["definition"] = data["definition"]
    else:
        out["definition"] = ""
    if data.get("validation") is not None:
        import capo_bedrock_agentcore_control.types.validation

        out["validation"] = (
            capo_bedrock_agentcore_control.types.validation.deserialize_json(
                data["validation"]
            )
        )
    return out


def redact_sensitive(value: LlmExtractionConfig) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "llm_extraction_instruction" in value:
        out["llm_extraction_instruction"] = "*** Sensitive Data Redacted ***"
    if "definition" in value:
        out["definition"] = "*** Sensitive Data Redacted ***"
    return out
