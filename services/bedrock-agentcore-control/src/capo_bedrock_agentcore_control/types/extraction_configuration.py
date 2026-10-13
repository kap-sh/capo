"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ExtractionConfiguration``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.custom_extraction_configuration


class _ExtractionConfiguration_customExtractionConfiguration(TypedDict, closed=True):
    customExtractionConfiguration: "capo_bedrock_agentcore_control.types.custom_extraction_configuration.CustomExtractionConfiguration"


ExtractionConfiguration: TypeAlias = (
    _ExtractionConfiguration_customExtractionConfiguration
)


# --- restJson1 ser/de ---
def serialize_json(value: ExtractionConfiguration) -> dict:
    if "customExtractionConfiguration" in value:
        import capo_bedrock_agentcore_control.types.custom_extraction_configuration

        return {
            "customExtractionConfiguration": capo_bedrock_agentcore_control.types.custom_extraction_configuration.serialize_json(
                value["customExtractionConfiguration"]
            )
        }
    else:
        raise SerializationError("ExtractionConfiguration: no variant present")


def deserialize_json(data: dict) -> ExtractionConfiguration:
    if data.get("customExtractionConfiguration") is not None:
        import capo_bedrock_agentcore_control.types.custom_extraction_configuration

        return {
            "customExtractionConfiguration": capo_bedrock_agentcore_control.types.custom_extraction_configuration.deserialize_json(
                data["customExtractionConfiguration"]
            )
        }
    else:
        raise DeserializationError("ExtractionConfiguration: no recognized variant key")


def redact_sensitive(value: ExtractionConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "customExtractionConfiguration" in value:
        import capo_bedrock_agentcore_control.types.custom_extraction_configuration

        out["customExtractionConfiguration"] = (
            capo_bedrock_agentcore_control.types.custom_extraction_configuration.redact_sensitive(
                value["customExtractionConfiguration"]
            )
        )
    return out
