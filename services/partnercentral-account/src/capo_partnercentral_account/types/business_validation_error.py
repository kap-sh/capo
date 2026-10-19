"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#BusinessValidationError``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_account.types.business_validation_code


class BusinessValidationError(TypedDict, closed=True):
    message: "str"
    """<p>A description of the business validation error.</p>"""
    code: "capo_partnercentral_account.types.business_validation_code.BusinessValidationCode"
    """<p>A code identifying the specific business validation error.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BusinessValidationError) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    import capo_partnercentral_account.types.business_validation_code

    out["Code"] = (
        capo_partnercentral_account.types.business_validation_code.serialize_aws_json_1_0(
            value["code"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> BusinessValidationError:
    out: BusinessValidationError = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        out["message"] = ""
    if data.get("Code") is not None:
        import capo_partnercentral_account.types.business_validation_code

        out["code"] = (
            capo_partnercentral_account.types.business_validation_code.deserialize_aws_json_1_0(
                data["Code"]
            )
        )
    else:
        import typing

        out["code"] = typing.cast(
            "capo_partnercentral_account.types.business_validation_code.BusinessValidationCode",
            "",
        )
    return out
