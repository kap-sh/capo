"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ModifyStrategyConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.modify_consolidation_configuration
    import capo_bedrock_agentcore_control.types.modify_extraction_configuration
    import capo_bedrock_agentcore_control.types.modify_reflection_configuration
    import capo_bedrock_agentcore_control.types.modify_self_managed_configuration


class ModifyStrategyConfiguration(TypedDict, closed=True):
    extraction: NotRequired[
        "capo_bedrock_agentcore_control.types.modify_extraction_configuration.ModifyExtractionConfiguration"
    ]
    """<p>The updated extraction configuration.</p>"""
    consolidation: NotRequired[
        "capo_bedrock_agentcore_control.types.modify_consolidation_configuration.ModifyConsolidationConfiguration"
    ]
    """<p>The updated consolidation configuration.</p>"""
    reflection: NotRequired[
        "capo_bedrock_agentcore_control.types.modify_reflection_configuration.ModifyReflectionConfiguration"
    ]
    """<p>The updated reflection configuration.</p>"""
    self_managed_configuration: NotRequired[
        "capo_bedrock_agentcore_control.types.modify_self_managed_configuration.ModifySelfManagedConfiguration"
    ]
    """<p>The updated self-managed configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ModifyStrategyConfiguration) -> dict:
    out: dict = {}
    if "extraction" in value:
        import capo_bedrock_agentcore_control.types.modify_extraction_configuration

        out["extraction"] = (
            capo_bedrock_agentcore_control.types.modify_extraction_configuration.serialize_json(
                value["extraction"]
            )
        )
    if "consolidation" in value:
        import capo_bedrock_agentcore_control.types.modify_consolidation_configuration

        out["consolidation"] = (
            capo_bedrock_agentcore_control.types.modify_consolidation_configuration.serialize_json(
                value["consolidation"]
            )
        )
    if "reflection" in value:
        import capo_bedrock_agentcore_control.types.modify_reflection_configuration

        out["reflection"] = (
            capo_bedrock_agentcore_control.types.modify_reflection_configuration.serialize_json(
                value["reflection"]
            )
        )
    if "self_managed_configuration" in value:
        import capo_bedrock_agentcore_control.types.modify_self_managed_configuration

        out["selfManagedConfiguration"] = (
            capo_bedrock_agentcore_control.types.modify_self_managed_configuration.serialize_json(
                value["self_managed_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> ModifyStrategyConfiguration:
    out: ModifyStrategyConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("extraction") is not None:
        import capo_bedrock_agentcore_control.types.modify_extraction_configuration

        out["extraction"] = (
            capo_bedrock_agentcore_control.types.modify_extraction_configuration.deserialize_json(
                data["extraction"]
            )
        )
    if data.get("consolidation") is not None:
        import capo_bedrock_agentcore_control.types.modify_consolidation_configuration

        out["consolidation"] = (
            capo_bedrock_agentcore_control.types.modify_consolidation_configuration.deserialize_json(
                data["consolidation"]
            )
        )
    if data.get("reflection") is not None:
        import capo_bedrock_agentcore_control.types.modify_reflection_configuration

        out["reflection"] = (
            capo_bedrock_agentcore_control.types.modify_reflection_configuration.deserialize_json(
                data["reflection"]
            )
        )
    if data.get("selfManagedConfiguration") is not None:
        import capo_bedrock_agentcore_control.types.modify_self_managed_configuration

        out["self_managed_configuration"] = (
            capo_bedrock_agentcore_control.types.modify_self_managed_configuration.deserialize_json(
                data["selfManagedConfiguration"]
            )
        )
    return out


def redact_sensitive(value: ModifyStrategyConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "extraction" in value:
        import capo_bedrock_agentcore_control.types.modify_extraction_configuration

        out["extraction"] = (
            capo_bedrock_agentcore_control.types.modify_extraction_configuration.redact_sensitive(
                value["extraction"]
            )
        )
    if "consolidation" in value:
        import capo_bedrock_agentcore_control.types.modify_consolidation_configuration

        out["consolidation"] = (
            capo_bedrock_agentcore_control.types.modify_consolidation_configuration.redact_sensitive(
                value["consolidation"]
            )
        )
    if "reflection" in value:
        import capo_bedrock_agentcore_control.types.modify_reflection_configuration

        out["reflection"] = (
            capo_bedrock_agentcore_control.types.modify_reflection_configuration.redact_sensitive(
                value["reflection"]
            )
        )
    return out
