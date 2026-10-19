"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#DiscardRegistrationVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.registration_id_or_arn


class DiscardRegistrationVersionRequest(TypedDict, closed=True):
    registration_id: (
        "capo_pinpoint_sms_voice_v2.types.registration_id_or_arn.RegistrationIdOrArn"
    )
    """<p>The unique identifier for the registration.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DiscardRegistrationVersionRequest) -> dict:
    out: dict = {}
    out["RegistrationId"] = value["registration_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DiscardRegistrationVersionRequest:
    out: DiscardRegistrationVersionRequest = {}  # type: ignore[typeddict-item]
    if data.get("RegistrationId") is not None:
        out["registration_id"] = data["RegistrationId"]
    else:
        out["registration_id"] = ""
    return out
