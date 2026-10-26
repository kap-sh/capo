"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#ValidationError``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_partnercentral_account.errors import DeserializationError, SerializationError
from capo_partnercentral_account.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_partnercentral_account.types.business_validation_error
    import capo_partnercentral_account.types.field_validation_error


class _ValidationError_FieldValidationError(TypedDict, closed=True):
    FieldValidationError: (
        "capo_partnercentral_account.types.field_validation_error.FieldValidationError"
    )


class _ValidationError_BusinessValidationError(TypedDict, closed=True):
    BusinessValidationError: "capo_partnercentral_account.types.business_validation_error.BusinessValidationError"


ValidationError: TypeAlias = (
    _ValidationError_FieldValidationError
    | _ValidationError_BusinessValidationError
    | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ValidationError) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ValidationError: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "FieldValidationError" in value:
        import capo_partnercentral_account.types.field_validation_error

        return {
            "FieldValidationError": capo_partnercentral_account.types.field_validation_error.serialize_aws_json_1_0(
                value["FieldValidationError"]
            )
        }
    elif "BusinessValidationError" in value:
        import capo_partnercentral_account.types.business_validation_error

        return {
            "BusinessValidationError": capo_partnercentral_account.types.business_validation_error.serialize_aws_json_1_0(
                value["BusinessValidationError"]
            )
        }
    else:
        raise SerializationError("ValidationError: no variant present")


def deserialize_aws_json_1_0(data: dict) -> ValidationError:
    if data.get("FieldValidationError") is not None:
        import capo_partnercentral_account.types.field_validation_error

        return {
            "FieldValidationError": capo_partnercentral_account.types.field_validation_error.deserialize_aws_json_1_0(
                data["FieldValidationError"]
            )
        }
    elif data.get("BusinessValidationError") is not None:
        import capo_partnercentral_account.types.business_validation_error

        return {
            "BusinessValidationError": capo_partnercentral_account.types.business_validation_error.deserialize_aws_json_1_0(
                data["BusinessValidationError"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ValidationError: no recognized variant key")
