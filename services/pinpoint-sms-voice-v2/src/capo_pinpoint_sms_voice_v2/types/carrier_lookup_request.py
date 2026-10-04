"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#CarrierLookupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.carrier_lookup_input_phone_number_type


class CarrierLookupRequest(TypedDict, closed=True):
    phone_number: "capo_pinpoint_sms_voice_v2.types.carrier_lookup_input_phone_number_type.CarrierLookupInputPhoneNumberType"
    """<p>The phone number that you want to retrieve information about. You can provide the phone number in various formats including special characters such as parentheses, brackets, spaces, hyphens, periods, and commas. The service automatically converts the input to E164 format for processing.</p>"""
    enable_cleansing: NotRequired["bool"]
    """<p>Specifies whether the service cleanses the phone number that you provide. When set to <code>true</code>, the service normalizes the phone number according to the destination country's national numbering plan and dialing rules. The service returns the cleansed number in E.164 format in the <code>E164PhoneNumber</code> field and returns the number that you provided in the <code>OriginalPhoneNumber</code> field.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CarrierLookupRequest) -> dict:
    out: dict = {}
    out["PhoneNumber"] = value["phone_number"]
    if "enable_cleansing" in value:
        out["EnableCleansing"] = value["enable_cleansing"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CarrierLookupRequest:
    out: CarrierLookupRequest = {}  # type: ignore[typeddict-item]
    if data.get("PhoneNumber") is not None:
        out["phone_number"] = data["PhoneNumber"]
    else:
        raise DeserializationError("CarrierLookupRequest.phone_number required")
    if data.get("EnableCleansing") is not None:
        out["enable_cleansing"] = data["EnableCleansing"]
    return out
