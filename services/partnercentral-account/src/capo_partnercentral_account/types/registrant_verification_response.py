"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#RegistrantVerificationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_account.types.completion_url
    import capo_partnercentral_account.types.date_time


class RegistrantVerificationResponse(TypedDict, closed=True):
    completion_url: "capo_partnercentral_account.types.completion_url.CompletionUrl"
    """<p>A secure URL where the registrant can complete additional verification steps, such as document upload or identity confirmation through a third-party verification service.</p>"""
    completion_url_expires_at: "capo_partnercentral_account.types.date_time.DateTime"
    """<p>The timestamp when the completion URL expires and is no longer valid for accessing the verification workflow.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RegistrantVerificationResponse) -> dict:
    out: dict = {}
    out["CompletionUrl"] = value["completion_url"]
    import capo_partnercentral_account.types.date_time

    out["CompletionUrlExpiresAt"] = (
        capo_partnercentral_account.types.date_time.serialize_aws_json_1_0(
            value["completion_url_expires_at"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> RegistrantVerificationResponse:
    out: RegistrantVerificationResponse = {}  # type: ignore[typeddict-item]
    if data.get("CompletionUrl") is not None:
        out["completion_url"] = data["CompletionUrl"]
    else:
        out["completion_url"] = ""
    if data.get("CompletionUrlExpiresAt") is not None:
        import capo_partnercentral_account.types.date_time

        out["completion_url_expires_at"] = (
            capo_partnercentral_account.types.date_time.deserialize_aws_json_1_0(
                data["CompletionUrlExpiresAt"]
            )
        )
    else:
        import datetime

        out["completion_url_expires_at"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
