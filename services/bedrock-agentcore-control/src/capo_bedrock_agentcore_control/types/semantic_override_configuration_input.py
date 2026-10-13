"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#SemanticOverrideConfigurationInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.semantic_override_consolidation_configuration_input
    import capo_bedrock_agentcore_control.types.semantic_override_extraction_configuration_input


class SemanticOverrideConfigurationInput(TypedDict, closed=True):
    extraction: NotRequired[
        "capo_bedrock_agentcore_control.types.semantic_override_extraction_configuration_input.SemanticOverrideExtractionConfigurationInput"
    ]
    """<p>The extraction configuration for a semantic override.</p>"""
    consolidation: NotRequired[
        "capo_bedrock_agentcore_control.types.semantic_override_consolidation_configuration_input.SemanticOverrideConsolidationConfigurationInput"
    ]
    """<p>The consolidation configuration for a semantic override.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SemanticOverrideConfigurationInput) -> dict:
    out: dict = {}
    if "extraction" in value:
        import capo_bedrock_agentcore_control.types.semantic_override_extraction_configuration_input

        out["extraction"] = (
            capo_bedrock_agentcore_control.types.semantic_override_extraction_configuration_input.serialize_json(
                value["extraction"]
            )
        )
    if "consolidation" in value:
        import capo_bedrock_agentcore_control.types.semantic_override_consolidation_configuration_input

        out["consolidation"] = (
            capo_bedrock_agentcore_control.types.semantic_override_consolidation_configuration_input.serialize_json(
                value["consolidation"]
            )
        )
    return out


def deserialize_json(data: dict) -> SemanticOverrideConfigurationInput:
    out: SemanticOverrideConfigurationInput = {}  # type: ignore[typeddict-item]
    if data.get("extraction") is not None:
        import capo_bedrock_agentcore_control.types.semantic_override_extraction_configuration_input

        out["extraction"] = (
            capo_bedrock_agentcore_control.types.semantic_override_extraction_configuration_input.deserialize_json(
                data["extraction"]
            )
        )
    if data.get("consolidation") is not None:
        import capo_bedrock_agentcore_control.types.semantic_override_consolidation_configuration_input

        out["consolidation"] = (
            capo_bedrock_agentcore_control.types.semantic_override_consolidation_configuration_input.deserialize_json(
                data["consolidation"]
            )
        )
    return out


def redact_sensitive(value: SemanticOverrideConfigurationInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "extraction" in value:
        import capo_bedrock_agentcore_control.types.semantic_override_extraction_configuration_input

        out["extraction"] = (
            capo_bedrock_agentcore_control.types.semantic_override_extraction_configuration_input.redact_sensitive(
                value["extraction"]
            )
        )
    if "consolidation" in value:
        import capo_bedrock_agentcore_control.types.semantic_override_consolidation_configuration_input

        out["consolidation"] = (
            capo_bedrock_agentcore_control.types.semantic_override_consolidation_configuration_input.redact_sensitive(
                value["consolidation"]
            )
        )
    return out
