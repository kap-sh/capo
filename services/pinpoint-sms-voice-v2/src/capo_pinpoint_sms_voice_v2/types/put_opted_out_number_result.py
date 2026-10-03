"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#PutOptedOutNumberResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_pinpoint_sms_voice_v2.types.opt_out_list_name
    import capo_pinpoint_sms_voice_v2.types.phone_number


class PutOptedOutNumberResult(TypedDict, closed=True):
    opt_out_list_arn: NotRequired["str"]
    """<p>The OptOutListArn that the phone number was removed from.</p>"""
    opt_out_list_name: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.opt_out_list_name.OptOutListName"
    ]
    """<p>The OptOutListName that the phone number was removed from.</p>"""
    opted_out_number: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.phone_number.PhoneNumber"
    ]
    """<p>The phone number that was added to the OptOutList.</p>"""
    opted_out_timestamp: NotRequired["datetime.datetime"]
    """<p>The time that the phone number was added to the OptOutList, in <a href="https://www.epochconverter.com/">UNIX epoch time</a> format.</p>"""
    end_user_opted_out: "bool"
    """<p>This is true if it was the end user who requested their phone number be removed. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PutOptedOutNumberResult) -> dict:
    out: dict = {}
    if "opt_out_list_arn" in value:
        out["OptOutListArn"] = value["opt_out_list_arn"]
    if "opt_out_list_name" in value:
        out["OptOutListName"] = value["opt_out_list_name"]
    if "opted_out_number" in value:
        out["OptedOutNumber"] = value["opted_out_number"]
    if "opted_out_timestamp" in value:
        import capo_pinpoint_sms_voice_v2.types._prelude.timestamp

        out["OptedOutTimestamp"] = (
            capo_pinpoint_sms_voice_v2.types._prelude.timestamp.serialize_aws_json_1_0(
                value["opted_out_timestamp"]
            )
        )
    out["EndUserOptedOut"] = value.get("end_user_opted_out", False)
    return out


def deserialize_aws_json_1_0(data: dict) -> PutOptedOutNumberResult:
    out: PutOptedOutNumberResult = {}  # type: ignore[typeddict-item]
    if data.get("OptOutListArn") is not None:
        out["opt_out_list_arn"] = data["OptOutListArn"]
    if data.get("OptOutListName") is not None:
        out["opt_out_list_name"] = data["OptOutListName"]
    if data.get("OptedOutNumber") is not None:
        out["opted_out_number"] = data["OptedOutNumber"]
    if data.get("OptedOutTimestamp") is not None:
        import capo_pinpoint_sms_voice_v2.types._prelude.timestamp

        out["opted_out_timestamp"] = (
            capo_pinpoint_sms_voice_v2.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["OptedOutTimestamp"]
            )
        )
    if data.get("EndUserOptedOut") is not None:
        out["end_user_opted_out"] = data["EndUserOptedOut"]
    else:
        out["end_user_opted_out"] = False
    return out
