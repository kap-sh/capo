"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#StartVerificationRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_account.types.client_token
    import capo_partnercentral_account.types.verification_details


class StartVerificationRequest(TypedDict, closed=True):
    client_token: NotRequired[
        "capo_partnercentral_account.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This prevents duplicate verification processes from being started accidentally.</p>"""
    verification_details: NotRequired[
        "capo_partnercentral_account.types.verification_details.VerificationDetails"
    ]
    """<p>The specific details required for the verification process, including business information for business verification or personal information for registrant verification.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StartVerificationRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "verification_details" in value:
        import capo_partnercentral_account.types.verification_details

        out["VerificationDetails"] = (
            capo_partnercentral_account.types.verification_details.serialize_aws_json_1_0(
                value["verification_details"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> StartVerificationRequest:
    out: StartVerificationRequest = {}  # type: ignore[typeddict-item]
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("VerificationDetails") is not None:
        import capo_partnercentral_account.types.verification_details

        out["verification_details"] = (
            capo_partnercentral_account.types.verification_details.deserialize_aws_json_1_0(
                data["VerificationDetails"]
            )
        )
    return out


def redact_sensitive(value: StartVerificationRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "verification_details" in value:
        import capo_partnercentral_account.types.verification_details

        out["verification_details"] = (
            capo_partnercentral_account.types.verification_details.redact_sensitive(
                value["verification_details"]
            )
        )
    return out
