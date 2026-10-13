"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#StrategyConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.consolidation_configuration
    import capo_bedrock_agentcore_control.types.extraction_configuration
    import capo_bedrock_agentcore_control.types.override_type
    import capo_bedrock_agentcore_control.types.reflection_configuration
    import capo_bedrock_agentcore_control.types.self_managed_configuration


class StrategyConfiguration(TypedDict, closed=True):
    type: NotRequired["capo_bedrock_agentcore_control.types.override_type.OverrideType"]
    """<p>The type of override for the strategy configuration.</p>"""
    extraction: NotRequired[
        "capo_bedrock_agentcore_control.types.extraction_configuration.ExtractionConfiguration"
    ]
    """<p>The extraction configuration for the memory strategy.</p>"""
    consolidation: NotRequired[
        "capo_bedrock_agentcore_control.types.consolidation_configuration.ConsolidationConfiguration"
    ]
    """<p>The consolidation configuration for the memory strategy.</p>"""
    reflection: NotRequired[
        "capo_bedrock_agentcore_control.types.reflection_configuration.ReflectionConfiguration"
    ]
    """<p>The reflection configuration for the memory strategy.</p>"""
    self_managed_configuration: NotRequired[
        "capo_bedrock_agentcore_control.types.self_managed_configuration.SelfManagedConfiguration"
    ]
    """<p>Self-managed configuration settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StrategyConfiguration) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_bedrock_agentcore_control.types.override_type

        out["type"] = capo_bedrock_agentcore_control.types.override_type.serialize_json(
            value["type"]
        )
    if "extraction" in value:
        import capo_bedrock_agentcore_control.types.extraction_configuration

        out["extraction"] = (
            capo_bedrock_agentcore_control.types.extraction_configuration.serialize_json(
                value["extraction"]
            )
        )
    if "consolidation" in value:
        import capo_bedrock_agentcore_control.types.consolidation_configuration

        out["consolidation"] = (
            capo_bedrock_agentcore_control.types.consolidation_configuration.serialize_json(
                value["consolidation"]
            )
        )
    if "reflection" in value:
        import capo_bedrock_agentcore_control.types.reflection_configuration

        out["reflection"] = (
            capo_bedrock_agentcore_control.types.reflection_configuration.serialize_json(
                value["reflection"]
            )
        )
    if "self_managed_configuration" in value:
        import capo_bedrock_agentcore_control.types.self_managed_configuration

        out["selfManagedConfiguration"] = (
            capo_bedrock_agentcore_control.types.self_managed_configuration.serialize_json(
                value["self_managed_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> StrategyConfiguration:
    out: StrategyConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_bedrock_agentcore_control.types.override_type

        out["type"] = (
            capo_bedrock_agentcore_control.types.override_type.deserialize_json(
                data["type"]
            )
        )
    if data.get("extraction") is not None:
        import capo_bedrock_agentcore_control.types.extraction_configuration

        out["extraction"] = (
            capo_bedrock_agentcore_control.types.extraction_configuration.deserialize_json(
                data["extraction"]
            )
        )
    if data.get("consolidation") is not None:
        import capo_bedrock_agentcore_control.types.consolidation_configuration

        out["consolidation"] = (
            capo_bedrock_agentcore_control.types.consolidation_configuration.deserialize_json(
                data["consolidation"]
            )
        )
    if data.get("reflection") is not None:
        import capo_bedrock_agentcore_control.types.reflection_configuration

        out["reflection"] = (
            capo_bedrock_agentcore_control.types.reflection_configuration.deserialize_json(
                data["reflection"]
            )
        )
    if data.get("selfManagedConfiguration") is not None:
        import capo_bedrock_agentcore_control.types.self_managed_configuration

        out["self_managed_configuration"] = (
            capo_bedrock_agentcore_control.types.self_managed_configuration.deserialize_json(
                data["selfManagedConfiguration"]
            )
        )
    return out


def redact_sensitive(value: StrategyConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "extraction" in value:
        import capo_bedrock_agentcore_control.types.extraction_configuration

        out["extraction"] = (
            capo_bedrock_agentcore_control.types.extraction_configuration.redact_sensitive(
                value["extraction"]
            )
        )
    if "consolidation" in value:
        import capo_bedrock_agentcore_control.types.consolidation_configuration

        out["consolidation"] = (
            capo_bedrock_agentcore_control.types.consolidation_configuration.redact_sensitive(
                value["consolidation"]
            )
        )
    if "reflection" in value:
        import capo_bedrock_agentcore_control.types.reflection_configuration

        out["reflection"] = (
            capo_bedrock_agentcore_control.types.reflection_configuration.redact_sensitive(
                value["reflection"]
            )
        )
    return out
