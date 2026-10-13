"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ConsolidationConfiguration``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.custom_consolidation_configuration


class _ConsolidationConfiguration_customConsolidationConfiguration(
    TypedDict, closed=True
):
    customConsolidationConfiguration: "capo_bedrock_agentcore_control.types.custom_consolidation_configuration.CustomConsolidationConfiguration"


ConsolidationConfiguration: TypeAlias = (
    _ConsolidationConfiguration_customConsolidationConfiguration
)


# --- restJson1 ser/de ---
def serialize_json(value: ConsolidationConfiguration) -> dict:
    if "customConsolidationConfiguration" in value:
        import capo_bedrock_agentcore_control.types.custom_consolidation_configuration

        return {
            "customConsolidationConfiguration": capo_bedrock_agentcore_control.types.custom_consolidation_configuration.serialize_json(
                value["customConsolidationConfiguration"]
            )
        }
    else:
        raise SerializationError("ConsolidationConfiguration: no variant present")


def deserialize_json(data: dict) -> ConsolidationConfiguration:
    if data.get("customConsolidationConfiguration") is not None:
        import capo_bedrock_agentcore_control.types.custom_consolidation_configuration

        return {
            "customConsolidationConfiguration": capo_bedrock_agentcore_control.types.custom_consolidation_configuration.deserialize_json(
                data["customConsolidationConfiguration"]
            )
        }
    else:
        raise DeserializationError(
            "ConsolidationConfiguration: no recognized variant key"
        )


def redact_sensitive(value: ConsolidationConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "customConsolidationConfiguration" in value:
        import capo_bedrock_agentcore_control.types.custom_consolidation_configuration

        out["customConsolidationConfiguration"] = (
            capo_bedrock_agentcore_control.types.custom_consolidation_configuration.redact_sensitive(
                value["customConsolidationConfiguration"]
            )
        )
    return out
