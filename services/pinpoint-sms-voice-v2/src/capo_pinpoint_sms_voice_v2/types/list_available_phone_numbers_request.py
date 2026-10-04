"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#ListAvailablePhoneNumbersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.iso_country_code
    import capo_pinpoint_sms_voice_v2.types.list_available_phone_numbers_max_results
    import capo_pinpoint_sms_voice_v2.types.next_token
    import capo_pinpoint_sms_voice_v2.types.number_capability_list
    import capo_pinpoint_sms_voice_v2.types.number_preference_list
    import capo_pinpoint_sms_voice_v2.types.registration_id_or_arn
    import capo_pinpoint_sms_voice_v2.types.searchable_number_type


class ListAvailablePhoneNumbersRequest(TypedDict, closed=True):
    iso_country_code: "capo_pinpoint_sms_voice_v2.types.iso_country_code.IsoCountryCode"
    """<p>The two-character code, in ISO 3166-1 alpha-2 format, for the country or region in which to search for available phone numbers. This operation currently supports only <code>US</code>.</p>"""
    number_capabilities: (
        "capo_pinpoint_sms_voice_v2.types.number_capability_list.NumberCapabilityList"
    )
    """<p>The capabilities to filter by, such as SMS. Only phone numbers that support all of the specified capabilities are returned.</p>"""
    number_type: (
        "capo_pinpoint_sms_voice_v2.types.searchable_number_type.SearchableNumberType"
    )
    """<p>The type of phone number to search for.</p>"""
    registration_id: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.registration_id_or_arn.RegistrationIdOrArn"
    ]
    """<p>The registration associated with the request. A registration is required for regulated number types. You can specify either:</p> <ul> <li> <p>The unique identifier of the registration.</p> </li> <li> <p>The Amazon Resource Name (ARN) of the registration.</p> </li> </ul>"""
    number_preference: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.number_preference_list.NumberPreferenceList"
    ]
    """<p>An optional selection preference used to return only phone numbers that match a specific digit pattern, such as numbers that start with, end with, or contain a particular sequence. You can specify at most one preference. Number preferences apply only to <code>TEN_DLC</code> numbers in the <code>US</code>.</p>"""
    next_token: NotRequired["capo_pinpoint_sms_voice_v2.types.next_token.NextToken"]
    """<p>The token returned from a previous request to retrieve the next page of results.</p>"""
    max_results: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.list_available_phone_numbers_max_results.ListAvailablePhoneNumbersMaxResults"
    ]
    """<p>The maximum number of results to return per page. If you don't specify a value, the default is 10.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListAvailablePhoneNumbersRequest) -> dict:
    out: dict = {}
    out["IsoCountryCode"] = value["iso_country_code"]
    import capo_pinpoint_sms_voice_v2.types.number_capability_list

    out["NumberCapabilities"] = (
        capo_pinpoint_sms_voice_v2.types.number_capability_list.serialize_aws_json_1_0(
            value["number_capabilities"]
        )
    )
    out["NumberType"] = value["number_type"]
    if "registration_id" in value:
        out["RegistrationId"] = value["registration_id"]
    if "number_preference" in value:
        import capo_pinpoint_sms_voice_v2.types.number_preference_list

        out["NumberPreference"] = (
            capo_pinpoint_sms_voice_v2.types.number_preference_list.serialize_aws_json_1_0(
                value["number_preference"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListAvailablePhoneNumbersRequest:
    out: ListAvailablePhoneNumbersRequest = {}  # type: ignore[typeddict-item]
    if data.get("IsoCountryCode") is not None:
        out["iso_country_code"] = data["IsoCountryCode"]
    else:
        raise DeserializationError(
            "ListAvailablePhoneNumbersRequest.iso_country_code required"
        )
    if data.get("NumberCapabilities") is not None:
        import capo_pinpoint_sms_voice_v2.types.number_capability_list

        out["number_capabilities"] = (
            capo_pinpoint_sms_voice_v2.types.number_capability_list.deserialize_aws_json_1_0(
                data["NumberCapabilities"]
            )
        )
    else:
        raise DeserializationError(
            "ListAvailablePhoneNumbersRequest.number_capabilities required"
        )
    if data.get("NumberType") is not None:
        out["number_type"] = data["NumberType"]
    else:
        raise DeserializationError(
            "ListAvailablePhoneNumbersRequest.number_type required"
        )
    if data.get("RegistrationId") is not None:
        out["registration_id"] = data["RegistrationId"]
    if data.get("NumberPreference") is not None:
        import capo_pinpoint_sms_voice_v2.types.number_preference_list

        out["number_preference"] = (
            capo_pinpoint_sms_voice_v2.types.number_preference_list.deserialize_aws_json_1_0(
                data["NumberPreference"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
