"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#ValidationExceptionError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.validation_exception_error_code


class ValidationExceptionError(TypedDict, closed=True):
    field_name: NotRequired["str"]
    """<p>Specifies the field name with the invalid value.</p>"""
    message: "str"
    """<p>Specifies the detailed error message for the invalid field value.</p>"""
    code: "capo_partnercentral_selling.types.validation_exception_error_code.ValidationExceptionErrorCode"
    """<p>Specifies the error code for the invalid field value.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ValidationExceptionError) -> dict:
    out: dict = {}
    if "field_name" in value:
        out["FieldName"] = value["field_name"]
    out["Message"] = value["message"]
    import capo_partnercentral_selling.types.validation_exception_error_code

    out["Code"] = (
        capo_partnercentral_selling.types.validation_exception_error_code.serialize_aws_json_1_0(
            value["code"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ValidationExceptionError:
    out: ValidationExceptionError = {}  # type: ignore[typeddict-item]
    if data.get("FieldName") is not None:
        out["field_name"] = data["FieldName"]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        out["message"] = ""
    if data.get("Code") is not None:
        import capo_partnercentral_selling.types.validation_exception_error_code

        out["code"] = (
            capo_partnercentral_selling.types.validation_exception_error_code.deserialize_aws_json_1_0(
                data["Code"]
            )
        )
    else:
        import typing

        out["code"] = typing.cast(
            "capo_partnercentral_selling.types.validation_exception_error_code.ValidationExceptionErrorCode",
            "",
        )
    return out
