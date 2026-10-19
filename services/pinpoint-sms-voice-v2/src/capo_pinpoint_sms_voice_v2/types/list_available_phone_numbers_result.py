"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#ListAvailablePhoneNumbersResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.available_phone_number_list
    import capo_pinpoint_sms_voice_v2.types.next_token


class ListAvailablePhoneNumbersResult(TypedDict, closed=True):
    available_phone_numbers: "capo_pinpoint_sms_voice_v2.types.available_phone_number_list.AvailablePhoneNumberList"
    """<p>An array of phone numbers, in E.164 format, that are available to request based on the specified filters.</p>"""
    next_token: NotRequired["capo_pinpoint_sms_voice_v2.types.next_token.NextToken"]
    """<p>The token to include in the next request to retrieve the next page of results. This value is null when there are no more results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListAvailablePhoneNumbersResult) -> dict:
    out: dict = {}
    import capo_pinpoint_sms_voice_v2.types.available_phone_number_list

    out["AvailablePhoneNumbers"] = (
        capo_pinpoint_sms_voice_v2.types.available_phone_number_list.serialize_aws_json_1_0(
            value["available_phone_numbers"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListAvailablePhoneNumbersResult:
    out: ListAvailablePhoneNumbersResult = {}  # type: ignore[typeddict-item]
    if data.get("AvailablePhoneNumbers") is not None:
        import capo_pinpoint_sms_voice_v2.types.available_phone_number_list

        out["available_phone_numbers"] = (
            capo_pinpoint_sms_voice_v2.types.available_phone_number_list.deserialize_aws_json_1_0(
                data["AvailablePhoneNumbers"]
            )
        )
    else:
        out["available_phone_numbers"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
