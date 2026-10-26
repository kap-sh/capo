"""Generated from Smithy shape ``com.amazonaws.b2bi#X12ValidationRule``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_b2bi.errors import DeserializationError, SerializationError
from capo_b2bi.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_b2bi.types.x12_code_list_validation_rule
    import capo_b2bi.types.x12_element_length_validation_rule
    import capo_b2bi.types.x12_element_requirement_validation_rule


class _X12ValidationRule_codeListValidationRule(TypedDict, closed=True):
    codeListValidationRule: (
        "capo_b2bi.types.x12_code_list_validation_rule.X12CodeListValidationRule"
    )


class _X12ValidationRule_elementLengthValidationRule(TypedDict, closed=True):
    elementLengthValidationRule: "capo_b2bi.types.x12_element_length_validation_rule.X12ElementLengthValidationRule"


class _X12ValidationRule_elementRequirementValidationRule(TypedDict, closed=True):
    elementRequirementValidationRule: "capo_b2bi.types.x12_element_requirement_validation_rule.X12ElementRequirementValidationRule"


X12ValidationRule: TypeAlias = (
    _X12ValidationRule_codeListValidationRule
    | _X12ValidationRule_elementLengthValidationRule
    | _X12ValidationRule_elementRequirementValidationRule
    | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: X12ValidationRule) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"X12ValidationRule: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "codeListValidationRule" in value:
        import capo_b2bi.types.x12_code_list_validation_rule

        return {
            "codeListValidationRule": capo_b2bi.types.x12_code_list_validation_rule.serialize_aws_json_1_0(
                value["codeListValidationRule"]
            )
        }
    elif "elementLengthValidationRule" in value:
        import capo_b2bi.types.x12_element_length_validation_rule

        return {
            "elementLengthValidationRule": capo_b2bi.types.x12_element_length_validation_rule.serialize_aws_json_1_0(
                value["elementLengthValidationRule"]
            )
        }
    elif "elementRequirementValidationRule" in value:
        import capo_b2bi.types.x12_element_requirement_validation_rule

        return {
            "elementRequirementValidationRule": capo_b2bi.types.x12_element_requirement_validation_rule.serialize_aws_json_1_0(
                value["elementRequirementValidationRule"]
            )
        }
    else:
        raise SerializationError("X12ValidationRule: no variant present")


def deserialize_aws_json_1_0(data: dict) -> X12ValidationRule:
    if data.get("codeListValidationRule") is not None:
        import capo_b2bi.types.x12_code_list_validation_rule

        return {
            "codeListValidationRule": capo_b2bi.types.x12_code_list_validation_rule.deserialize_aws_json_1_0(
                data["codeListValidationRule"]
            )
        }
    elif data.get("elementLengthValidationRule") is not None:
        import capo_b2bi.types.x12_element_length_validation_rule

        return {
            "elementLengthValidationRule": capo_b2bi.types.x12_element_length_validation_rule.deserialize_aws_json_1_0(
                data["elementLengthValidationRule"]
            )
        }
    elif data.get("elementRequirementValidationRule") is not None:
        import capo_b2bi.types.x12_element_requirement_validation_rule

        return {
            "elementRequirementValidationRule": capo_b2bi.types.x12_element_requirement_validation_rule.deserialize_aws_json_1_0(
                data["elementRequirementValidationRule"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("X12ValidationRule: no recognized variant key")
