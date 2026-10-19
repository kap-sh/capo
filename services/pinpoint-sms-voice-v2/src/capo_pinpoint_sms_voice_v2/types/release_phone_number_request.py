"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#ReleasePhoneNumberRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.phone_number_id_or_arn


class ReleasePhoneNumberRequest(TypedDict, closed=True):
    phone_number_id: (
        "capo_pinpoint_sms_voice_v2.types.phone_number_id_or_arn.PhoneNumberIdOrArn"
    )
    """<p>The PhoneNumberId or PhoneNumberArn of the phone number to release. You can use <a>DescribePhoneNumbers</a> to get the values for PhoneNumberId and PhoneNumberArn.</p> <important> <p>If you are using a shared End User Messaging SMS resource then you must use the full Amazon Resource Name(ARN).</p> </important>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ReleasePhoneNumberRequest) -> dict:
    out: dict = {}
    out["PhoneNumberId"] = value["phone_number_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ReleasePhoneNumberRequest:
    out: ReleasePhoneNumberRequest = {}  # type: ignore[typeddict-item]
    if data.get("PhoneNumberId") is not None:
        out["phone_number_id"] = data["PhoneNumberId"]
    else:
        out["phone_number_id"] = ""
    return out
