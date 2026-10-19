"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#ValidationExceptionField``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_benefits.types.validation_exception_error_code


class ValidationExceptionField(TypedDict, closed=True):
    name: "str"
    """<p>The name of the field that failed validation.</p>"""
    message: "str"
    """<p>A detailed message explaining why the field validation failed.</p>"""
    code: NotRequired[
        "capo_partnercentral_benefits.types.validation_exception_error_code.ValidationExceptionErrorCode"
    ]
    """<p>An error code explaining why the field validation failed.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ValidationExceptionField) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Message"] = value["message"]
    if "code" in value:
        import capo_partnercentral_benefits.types.validation_exception_error_code

        out["Code"] = (
            capo_partnercentral_benefits.types.validation_exception_error_code.serialize_aws_json_1_0(
                value["code"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ValidationExceptionField:
    out: ValidationExceptionField = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        out["message"] = ""
    if data.get("Code") is not None:
        import capo_partnercentral_benefits.types.validation_exception_error_code

        out["code"] = (
            capo_partnercentral_benefits.types.validation_exception_error_code.deserialize_aws_json_1_0(
                data["Code"]
            )
        )
    return out
