"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#EpisodicOverrideConfigurationInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.episodic_override_consolidation_configuration_input
    import capo_bedrock_agentcore_control.types.episodic_override_extraction_configuration_input
    import capo_bedrock_agentcore_control.types.episodic_override_reflection_configuration_input


class EpisodicOverrideConfigurationInput(TypedDict, closed=True):
    extraction: NotRequired[
        "capo_bedrock_agentcore_control.types.episodic_override_extraction_configuration_input.EpisodicOverrideExtractionConfigurationInput"
    ]
    """<p>Contains configurations for overriding the extraction step of the episodic memory strategy.</p>"""
    consolidation: NotRequired[
        "capo_bedrock_agentcore_control.types.episodic_override_consolidation_configuration_input.EpisodicOverrideConsolidationConfigurationInput"
    ]
    """<p>Contains configurations for overriding the consolidation step of the episodic memory strategy.</p>"""
    reflection: NotRequired[
        "capo_bedrock_agentcore_control.types.episodic_override_reflection_configuration_input.EpisodicOverrideReflectionConfigurationInput"
    ]
    """<p>Contains configurations for overriding the reflection step of the episodic memory strategy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EpisodicOverrideConfigurationInput) -> dict:
    out: dict = {}
    if "extraction" in value:
        import capo_bedrock_agentcore_control.types.episodic_override_extraction_configuration_input

        out["extraction"] = (
            capo_bedrock_agentcore_control.types.episodic_override_extraction_configuration_input.serialize_json(
                value["extraction"]
            )
        )
    if "consolidation" in value:
        import capo_bedrock_agentcore_control.types.episodic_override_consolidation_configuration_input

        out["consolidation"] = (
            capo_bedrock_agentcore_control.types.episodic_override_consolidation_configuration_input.serialize_json(
                value["consolidation"]
            )
        )
    if "reflection" in value:
        import capo_bedrock_agentcore_control.types.episodic_override_reflection_configuration_input

        out["reflection"] = (
            capo_bedrock_agentcore_control.types.episodic_override_reflection_configuration_input.serialize_json(
                value["reflection"]
            )
        )
    return out


def deserialize_json(data: dict) -> EpisodicOverrideConfigurationInput:
    out: EpisodicOverrideConfigurationInput = {}  # type: ignore[typeddict-item]
    if data.get("extraction") is not None:
        import capo_bedrock_agentcore_control.types.episodic_override_extraction_configuration_input

        out["extraction"] = (
            capo_bedrock_agentcore_control.types.episodic_override_extraction_configuration_input.deserialize_json(
                data["extraction"]
            )
        )
    if data.get("consolidation") is not None:
        import capo_bedrock_agentcore_control.types.episodic_override_consolidation_configuration_input

        out["consolidation"] = (
            capo_bedrock_agentcore_control.types.episodic_override_consolidation_configuration_input.deserialize_json(
                data["consolidation"]
            )
        )
    if data.get("reflection") is not None:
        import capo_bedrock_agentcore_control.types.episodic_override_reflection_configuration_input

        out["reflection"] = (
            capo_bedrock_agentcore_control.types.episodic_override_reflection_configuration_input.deserialize_json(
                data["reflection"]
            )
        )
    return out


def redact_sensitive(value: EpisodicOverrideConfigurationInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "extraction" in value:
        import capo_bedrock_agentcore_control.types.episodic_override_extraction_configuration_input

        out["extraction"] = (
            capo_bedrock_agentcore_control.types.episodic_override_extraction_configuration_input.redact_sensitive(
                value["extraction"]
            )
        )
    if "consolidation" in value:
        import capo_bedrock_agentcore_control.types.episodic_override_consolidation_configuration_input

        out["consolidation"] = (
            capo_bedrock_agentcore_control.types.episodic_override_consolidation_configuration_input.redact_sensitive(
                value["consolidation"]
            )
        )
    if "reflection" in value:
        import capo_bedrock_agentcore_control.types.episodic_override_reflection_configuration_input

        out["reflection"] = (
            capo_bedrock_agentcore_control.types.episodic_override_reflection_configuration_input.redact_sensitive(
                value["reflection"]
            )
        )
    return out
