"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#OptedOutNumberInformation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_pinpoint_sms_voice_v2.types.phone_number


class OptedOutNumberInformation(TypedDict, closed=True):
    opted_out_number: "capo_pinpoint_sms_voice_v2.types.phone_number.PhoneNumber"
    """<p>The phone number that is opted out.</p>"""
    opted_out_timestamp: "datetime.datetime"
    """<p>The time that the op tout occurred, in <a href="https://www.epochconverter.com/">UNIX epoch time</a> format.</p>"""
    end_user_opted_out: "bool"
    """<p>This is set to true if it was the end recipient that opted out.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OptedOutNumberInformation) -> dict:
    out: dict = {}
    out["OptedOutNumber"] = value["opted_out_number"]
    import capo_pinpoint_sms_voice_v2.types._prelude.timestamp

    out["OptedOutTimestamp"] = (
        capo_pinpoint_sms_voice_v2.types._prelude.timestamp.serialize_aws_json_1_0(
            value["opted_out_timestamp"]
        )
    )
    out["EndUserOptedOut"] = value.get("end_user_opted_out", False)
    return out


def deserialize_aws_json_1_0(data: dict) -> OptedOutNumberInformation:
    out: OptedOutNumberInformation = {}  # type: ignore[typeddict-item]
    if data.get("OptedOutNumber") is not None:
        out["opted_out_number"] = data["OptedOutNumber"]
    else:
        raise DeserializationError(
            "OptedOutNumberInformation.opted_out_number required"
        )
    if data.get("OptedOutTimestamp") is not None:
        import capo_pinpoint_sms_voice_v2.types._prelude.timestamp

        out["opted_out_timestamp"] = (
            capo_pinpoint_sms_voice_v2.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["OptedOutTimestamp"]
            )
        )
    else:
        raise DeserializationError(
            "OptedOutNumberInformation.opted_out_timestamp required"
        )
    if data.get("EndUserOptedOut") is not None:
        out["end_user_opted_out"] = data["EndUserOptedOut"]
    else:
        out["end_user_opted_out"] = False
    return out
