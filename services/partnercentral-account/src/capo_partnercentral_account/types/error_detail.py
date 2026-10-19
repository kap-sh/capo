"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#ErrorDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_account.types.profile_validation_error_reason


class ErrorDetail(TypedDict, closed=True):
    locale: "str"
    """<p>The locale or language code for the error message.</p>"""
    message: "str"
    """<p>A human-readable description of the error.</p>"""
    reason: "capo_partnercentral_account.types.profile_validation_error_reason.ProfileValidationErrorReason"
    """<p>A machine-readable code or reason for the error.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ErrorDetail) -> dict:
    out: dict = {}
    out["Locale"] = value["locale"]
    out["Message"] = value["message"]
    import capo_partnercentral_account.types.profile_validation_error_reason

    out["Reason"] = (
        capo_partnercentral_account.types.profile_validation_error_reason.serialize_aws_json_1_0(
            value["reason"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ErrorDetail:
    out: ErrorDetail = {}  # type: ignore[typeddict-item]
    if data.get("Locale") is not None:
        out["locale"] = data["Locale"]
    else:
        out["locale"] = ""
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        out["message"] = ""
    if data.get("Reason") is not None:
        import capo_partnercentral_account.types.profile_validation_error_reason

        out["reason"] = (
            capo_partnercentral_account.types.profile_validation_error_reason.deserialize_aws_json_1_0(
                data["Reason"]
            )
        )
    else:
        import typing

        out["reason"] = typing.cast(
            "capo_partnercentral_account.types.profile_validation_error_reason.ProfileValidationErrorReason",
            "",
        )
    return out
