"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ModifyExtractionConfiguration``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)
from capo_bedrock_agentcore_control.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.custom_extraction_configuration_input


class _ModifyExtractionConfiguration_customExtractionConfiguration(
    TypedDict, closed=True
):
    customExtractionConfiguration: "capo_bedrock_agentcore_control.types.custom_extraction_configuration_input.CustomExtractionConfigurationInput"


ModifyExtractionConfiguration: TypeAlias = (
    _ModifyExtractionConfiguration_customExtractionConfiguration | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ModifyExtractionConfiguration) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"ModifyExtractionConfiguration: cannot serialize unknown variant {value.name!r}"
        )
    elif "customExtractionConfiguration" in value:
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
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError(
            "ModifyExtractionConfiguration: no recognized variant key"
        )


def redact_sensitive(
    value: ModifyExtractionConfiguration,
) -> dict[str, Any] | UnknownUnionMember:
    if isinstance(value, UnknownUnionMember):
        return value
    out: dict[str, Any] = dict(value)
    if "customExtractionConfiguration" in value:
        import capo_bedrock_agentcore_control.types.custom_extraction_configuration_input

        out["customExtractionConfiguration"] = (
            capo_bedrock_agentcore_control.types.custom_extraction_configuration_input.redact_sensitive(
                value["customExtractionConfiguration"]
            )
        )
    return out
