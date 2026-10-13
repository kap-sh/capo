"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ModifyExtractionConfiguration``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.custom_extraction_configuration_input


class _ModifyExtractionConfiguration_customExtractionConfiguration(
    TypedDict, closed=True
):
    customExtractionConfiguration: "capo_bedrock_agentcore_control.types.custom_extraction_configuration_input.CustomExtractionConfigurationInput"


ModifyExtractionConfiguration: TypeAlias = (
    _ModifyExtractionConfiguration_customExtractionConfiguration
)


# --- restJson1 ser/de ---
def serialize_json(value: ModifyExtractionConfiguration) -> dict:
    if "customExtractionConfiguration" in value:
        import capo_bedrock_agentcore_control.types.custom_extraction_configuration_input

        return {
            "customExtractionConfiguration": capo_bedrock_agentcore_control.types.custom_extraction_configuration_input.serialize_json(
                value["customExtractionConfiguration"]
            )
        }
    else:
        raise SerializationError("ModifyExtractionConfiguration: no variant present")


def deserialize_json(data: dict) -> ModifyExtractionConfiguration:
    if data.get("customExtractionConfiguration") is not None:
        import capo_bedrock_agentcore_control.types.custom_extraction_configuration_input

        return {
            "customExtractionConfiguration": capo_bedrock_agentcore_control.types.custom_extraction_configuration_input.deserialize_json(
                data["customExtractionConfiguration"]
            )
        }
    else:
        raise DeserializationError(
            "ModifyExtractionConfiguration: no recognized variant key"
        )


def redact_sensitive(value: ModifyExtractionConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "customExtractionConfiguration" in value:
        import capo_bedrock_agentcore_control.types.custom_extraction_configuration_input

        out["customExtractionConfiguration"] = (
            capo_bedrock_agentcore_control.types.custom_extraction_configuration_input.redact_sensitive(
                value["customExtractionConfiguration"]
            )
        )
    return out
