"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#GetVerificationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_account.types.verification_type


class GetVerificationRequest(TypedDict, closed=True):
    verification_type: (
        "capo_partnercentral_account.types.verification_type.VerificationType"
    )
    """<p>The type of verification to retrieve information for. Valid values include business verification for company registration details and registrant verification for individual identity confirmation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetVerificationRequest) -> dict:
    out: dict = {}
    import capo_partnercentral_account.types.verification_type

    out["VerificationType"] = (
        capo_partnercentral_account.types.verification_type.serialize_aws_json_1_0(
            value["verification_type"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetVerificationRequest:
    out: GetVerificationRequest = {}  # type: ignore[typeddict-item]
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
    return out
