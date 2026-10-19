"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#PutOptedOutNumberRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.opt_out_list_name_or_arn
    import capo_pinpoint_sms_voice_v2.types.phone_number


class PutOptedOutNumberRequest(TypedDict, closed=True):
    opt_out_list_name: (
        "capo_pinpoint_sms_voice_v2.types.opt_out_list_name_or_arn.OptOutListNameOrArn"
    )
    """<p>The OptOutListName or OptOutListArn to add the phone number to.</p> <important> <p>If you are using a shared End User Messaging SMS resource then you must use the full Amazon Resource Name(ARN).</p> </important>"""
    opted_out_number: "capo_pinpoint_sms_voice_v2.types.phone_number.PhoneNumber"
    """<p>The phone number to add to the OptOutList in E.164 format.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PutOptedOutNumberRequest) -> dict:
    out: dict = {}
    out["OptOutListName"] = value["opt_out_list_name"]
    out["OptedOutNumber"] = value["opted_out_number"]
    return out


def deserialize_aws_json_1_0(data: dict) -> PutOptedOutNumberRequest:
    out: PutOptedOutNumberRequest = {}  # type: ignore[typeddict-item]
    if data.get("OptOutListName") is not None:
        out["opt_out_list_name"] = data["OptOutListName"]
    else:
        out["opt_out_list_name"] = ""
    if data.get("OptedOutNumber") is not None:
        out["opted_out_number"] = data["OptedOutNumber"]
    else:
        out["opted_out_number"] = ""
    return out
