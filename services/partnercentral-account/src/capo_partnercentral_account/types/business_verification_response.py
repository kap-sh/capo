"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#BusinessVerificationResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_partnercentral_account.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_account.types.business_verification_details
    import capo_partnercentral_account.types.completion_url
    import capo_partnercentral_account.types.date_time


class BusinessVerificationResponse(TypedDict, closed=True):
    business_verification_details: "capo_partnercentral_account.types.business_verification_details.BusinessVerificationDetails"
    """<p>The business verification details that were processed and verified, potentially including additional information discovered during the verification process.</p>"""
    completion_url: NotRequired[
        "capo_partnercentral_account.types.completion_url.CompletionUrl"
    ]
    """<p>A secure URL where the registrant can complete additional verification steps, such as document upload or identity confirmation through a third-party verification service.</p>"""
    completion_url_expires_at: NotRequired[
        "capo_partnercentral_account.types.date_time.DateTime"
    ]
    """<p>The timestamp when the completion URL expires and is no longer valid for accessing the verification workflow.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BusinessVerificationResponse) -> dict:
    out: dict = {}
    import capo_partnercentral_account.types.business_verification_details

    out["BusinessVerificationDetails"] = (
        capo_partnercentral_account.types.business_verification_details.serialize_aws_json_1_0(
            value["business_verification_details"]
        )
    )
    if "completion_url" in value:
        out["CompletionUrl"] = value["completion_url"]
    if "completion_url_expires_at" in value:
        import capo_partnercentral_account.types.date_time

        out["CompletionUrlExpiresAt"] = (
            capo_partnercentral_account.types.date_time.serialize_aws_json_1_0(
                value["completion_url_expires_at"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> BusinessVerificationResponse:
    out: BusinessVerificationResponse = {}  # type: ignore[typeddict-item]
    if data.get("BusinessVerificationDetails") is not None:
        import capo_partnercentral_account.types.business_verification_details

        out["business_verification_details"] = (
            capo_partnercentral_account.types.business_verification_details.deserialize_aws_json_1_0(
                data["BusinessVerificationDetails"]
            )
        )
    else:
        raise DeserializationError(
            "BusinessVerificationResponse.business_verification_details required"
        )
    if data.get("CompletionUrl") is not None:
        out["completion_url"] = data["CompletionUrl"]
    if data.get("CompletionUrlExpiresAt") is not None:
        import capo_partnercentral_account.types.date_time

        out["completion_url_expires_at"] = (
            capo_partnercentral_account.types.date_time.deserialize_aws_json_1_0(
                data["CompletionUrlExpiresAt"]
            )
        )
    return out


def redact_sensitive(value: BusinessVerificationResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "business_verification_details" in value:
        import capo_partnercentral_account.types.business_verification_details

        out["business_verification_details"] = (
            capo_partnercentral_account.types.business_verification_details.redact_sensitive(
                value["business_verification_details"]
            )
        )
    return out
