"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ModifyConsolidationConfiguration``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)
from capo_bedrock_agentcore_control.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.custom_consolidation_configuration_input


class _ModifyConsolidationConfiguration_customConsolidationConfiguration(
    TypedDict, closed=True
):
    customConsolidationConfiguration: "capo_bedrock_agentcore_control.types.custom_consolidation_configuration_input.CustomConsolidationConfigurationInput"


ModifyConsolidationConfiguration: TypeAlias = (
    _ModifyConsolidationConfiguration_customConsolidationConfiguration
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ModifyConsolidationConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ModifyConsolidationConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "customConsolidationConfiguration" in value:
        import capo_bedrock_agentcore_control.types.custom_consolidation_configuration_input

        return {
            "customConsolidationConfiguration": capo_bedrock_agentcore_control.types.custom_consolidation_configuration_input.serialize_json(
                value["customConsolidationConfiguration"]
            )
        }
    else:
        raise SerializationError("ModifyConsolidationConfiguration: no variant present")


def deserialize_json(data: dict) -> ModifyConsolidationConfiguration:
    if data.get("customConsolidationConfiguration") is not None:
        import capo_bedrock_agentcore_control.types.custom_consolidation_configuration_input

        return {
            "customConsolidationConfiguration": capo_bedrock_agentcore_control.types.custom_consolidation_configuration_input.deserialize_json(
                data["customConsolidationConfiguration"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "ModifyConsolidationConfiguration: no recognized variant key"
        )


def redact_sensitive(value: ModifyConsolidationConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "customConsolidationConfiguration" in value:
        import capo_bedrock_agentcore_control.types.custom_consolidation_configuration_input

        out["customConsolidationConfiguration"] = (
            capo_bedrock_agentcore_control.types.custom_consolidation_configuration_input.redact_sensitive(
                value["customConsolidationConfiguration"]
            )
        )
    return out
