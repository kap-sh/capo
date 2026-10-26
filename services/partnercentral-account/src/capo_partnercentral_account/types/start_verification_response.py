"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#StartVerificationResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_account.types.date_time
    import capo_partnercentral_account.types.verification_response_details
    import capo_partnercentral_account.types.verification_status
    import capo_partnercentral_account.types.verification_status_reason
    import capo_partnercentral_account.types.verification_type


class StartVerificationResponse(TypedDict, closed=True):
    verification_type: (
        "capo_partnercentral_account.types.verification_type.VerificationType"
    )
    """<p>The type of verification that was started based on the provided verification details.</p>"""
    verification_status: (
        "capo_partnercentral_account.types.verification_status.VerificationStatus"
    )
    """<p>The initial status of the verification process after it has been started. Typically this will be pending or in-progress.</p>"""
    verification_status_reason: NotRequired[
        "capo_partnercentral_account.types.verification_status_reason.VerificationStatusReason"
    ]
    """<p>Additional information about the initial verification status, including any immediate feedback about the submitted verification details.</p>"""
    verification_response_details: "capo_partnercentral_account.types.verification_response_details.VerificationResponseDetails"
    """<p>Initial response details specific to the type of verification started, which may include next steps or additional requirements.</p>"""
    started_at: "capo_partnercentral_account.types.date_time.DateTime"
    """<p>The timestamp when the verification process was successfully initiated.</p>"""
    completed_at: NotRequired["capo_partnercentral_account.types.date_time.DateTime"]
    """<p>The timestamp when the verification process was completed. This field is typically null for newly started verifications unless they complete immediately.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StartVerificationResponse) -> dict:
    out: dict = {}
    import capo_partnercentral_account.types.verification_type

    out["VerificationType"] = (
        capo_partnercentral_account.types.verification_type.serialize_aws_json_1_0(
            value["verification_type"]
        )
    )
    import capo_partnercentral_account.types.verification_status

    out["VerificationStatus"] = (
        capo_partnercentral_account.types.verification_status.serialize_aws_json_1_0(
            value["verification_status"]
        )
    )
    if "verification_status_reason" in value:
        out["VerificationStatusReason"] = value["verification_status_reason"]
    import capo_partnercentral_account.types.verification_response_details

    out["VerificationResponseDetails"] = (
        capo_partnercentral_account.types.verification_response_details.serialize_aws_json_1_0(
            value["verification_response_details"]
        )
    )
    import capo_partnercentral_account.types.date_time

    out["StartedAt"] = (
        capo_partnercentral_account.types.date_time.serialize_aws_json_1_0(
            value["started_at"]
        )
    )
    if "completed_at" in value:
        import capo_partnercentral_account.types.date_time

        out["CompletedAt"] = (
            capo_partnercentral_account.types.date_time.serialize_aws_json_1_0(
                value["completed_at"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> StartVerificationResponse:
    out: StartVerificationResponse = {}  # type: ignore[typeddict-item]
    if data.get("VerificationType") is not None:
        import capo_partnercentral_account.types.verification_type

        out["verification_type"] = (
            capo_partnercentral_account.types.verification_type.deserialize_aws_json_1_0(
                data["VerificationType"]
            )
        )
    else:
        import typing

        out["verification_type"] = typing.cast(
            "capo_partnercentral_account.types.verification_type.VerificationType", ""
        )
    if data.get("VerificationStatus") is not None:
        import capo_partnercentral_account.types.verification_status

        out["verification_status"] = (
            capo_partnercentral_account.types.verification_status.deserialize_aws_json_1_0(
                data["VerificationStatus"]
            )
        )
    else:
        import typing

        out["verification_status"] = typing.cast(
            "capo_partnercentral_account.types.verification_status.VerificationStatus",
            "",
        )
    if data.get("VerificationStatusReason") is not None:
        out["verification_status_reason"] = data["VerificationStatusReason"]
    if data.get("VerificationResponseDetails") is not None:
        import capo_partnercentral_account.types.verification_response_details

        out["verification_response_details"] = (
            capo_partnercentral_account.types.verification_response_details.deserialize_aws_json_1_0(
                data["VerificationResponseDetails"]
            )
        )
    else:
        out["verification_response_details"] = {"$unknown": {"name": ""}}
    if data.get("StartedAt") is not None:
        import capo_partnercentral_account.types.date_time

        out["started_at"] = (
            capo_partnercentral_account.types.date_time.deserialize_aws_json_1_0(
                data["StartedAt"]
            )
        )
    else:
        import datetime

        out["started_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("CompletedAt") is not None:
        import capo_partnercentral_account.types.date_time

        out["completed_at"] = (
            capo_partnercentral_account.types.date_time.deserialize_aws_json_1_0(
                data["CompletedAt"]
            )
        )
    return out


def redact_sensitive(value: StartVerificationResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "verification_response_details" in value:
        import capo_partnercentral_account.types.verification_response_details

        out["verification_response_details"] = (
            capo_partnercentral_account.types.verification_response_details.redact_sensitive(
                value["verification_response_details"]
            )
        )
    return out
