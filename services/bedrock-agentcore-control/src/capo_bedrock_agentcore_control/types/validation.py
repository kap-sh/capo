"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#Validation``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)
from capo_bedrock_agentcore_control.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.number_validation
    import capo_bedrock_agentcore_control.types.string_list_validation
    import capo_bedrock_agentcore_control.types.string_validation


class ValidationStringValidationMember(TypedDict, closed=True):
    stringValidation: (
        "capo_bedrock_agentcore_control.types.string_validation.StringValidation"
    )


class ValidationStringListValidationMember(TypedDict, closed=True):
    stringListValidation: "capo_bedrock_agentcore_control.types.string_list_validation.StringListValidation"


class ValidationNumberValidationMember(TypedDict, closed=True):
    numberValidation: (
        "capo_bedrock_agentcore_control.types.number_validation.NumberValidation"
    )


Validation: TypeAlias = (
    ValidationStringValidationMember
    | ValidationStringListValidationMember
    | ValidationNumberValidationMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: Validation) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"Validation: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "stringValidation" in value:
        import capo_bedrock_agentcore_control.types.string_validation

        return {
            "stringValidation": capo_bedrock_agentcore_control.types.string_validation.serialize_json(
                value["stringValidation"]
            )
        }
    elif "stringListValidation" in value:
        import capo_bedrock_agentcore_control.types.string_list_validation

        return {
            "stringListValidation": capo_bedrock_agentcore_control.types.string_list_validation.serialize_json(
                value["stringListValidation"]
            )
        }
    elif "numberValidation" in value:
        import capo_bedrock_agentcore_control.types.number_validation

        return {
            "numberValidation": capo_bedrock_agentcore_control.types.number_validation.serialize_json(
                value["numberValidation"]
            )
        }
    else:
        raise SerializationError("Validation: no variant present")


def deserialize_json(data: dict) -> Validation:
    if data.get("stringValidation") is not None:
        import capo_bedrock_agentcore_control.types.string_validation

        return {
            "stringValidation": capo_bedrock_agentcore_control.types.string_validation.deserialize_json(
                data["stringValidation"]
            )
        }
    elif data.get("stringListValidation") is not None:
        import capo_bedrock_agentcore_control.types.string_list_validation

        return {
            "stringListValidation": capo_bedrock_agentcore_control.types.string_list_validation.deserialize_json(
                data["stringListValidation"]
            )
        }
    elif data.get("numberValidation") is not None:
        import capo_bedrock_agentcore_control.types.number_validation

        return {
            "numberValidation": capo_bedrock_agentcore_control.types.number_validation.deserialize_json(
                data["numberValidation"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("Validation: no recognized variant key")
