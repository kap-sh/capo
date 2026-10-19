"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#SubmitRegistrationVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.registration_id_or_arn


class SubmitRegistrationVersionRequest(TypedDict, closed=True):
    registration_id: (
        "capo_pinpoint_sms_voice_v2.types.registration_id_or_arn.RegistrationIdOrArn"
    )
    """<p>The unique identifier for the registration.</p>"""
    aws_review: NotRequired["bool"]
    """<p>Set to true to request AWS review of the registration. When enabled, AWS will perform additional validation and review of the registration submission before processing.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SubmitRegistrationVersionRequest) -> dict:
    out: dict = {}
    out["RegistrationId"] = value["registration_id"]
    if "aws_review" in value:
        out["AwsReview"] = value["aws_review"]
    return out


def deserialize_aws_json_1_0(data: dict) -> SubmitRegistrationVersionRequest:
    out: SubmitRegistrationVersionRequest = {}  # type: ignore[typeddict-item]
    if data.get("RegistrationId") is not None:
        out["registration_id"] = data["RegistrationId"]
    else:
        raise DeserializationError(
            "SubmitRegistrationVersionRequest.registration_id required"
        )
    if data.get("AwsReview") is not None:
        out["aws_review"] = data["AwsReview"]
    return out
