"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#CreateSipMediaApplicationCallRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_chime_sdk_voice.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.e164_phone_number
    import capo_chime_sdk_voice.types.non_empty_string
    import capo_chime_sdk_voice.types.sip_headers_map
    import capo_chime_sdk_voice.types.sma_create_call_arguments_map


class CreateSipMediaApplicationCallRequest(TypedDict, closed=True):
    from_phone_number: "capo_chime_sdk_voice.types.e164_phone_number.E164PhoneNumber"
    """<p>The phone number that a user calls from. This is a phone number in your Amazon Chime SDK phone number inventory.</p>"""
    to_phone_number: "capo_chime_sdk_voice.types.e164_phone_number.E164PhoneNumber"
    """<p>The phone number that the service should call.</p>"""
    sip_media_application_id: (
        "capo_chime_sdk_voice.types.non_empty_string.NonEmptyString"
    )
    """<p>The ID of the SIP media application.</p>"""
    sip_headers: NotRequired["capo_chime_sdk_voice.types.sip_headers_map.SipHeadersMap"]
    """<p>The SIP headers added to an outbound call leg.</p>"""
    arguments_map: NotRequired[
        "capo_chime_sdk_voice.types.sma_create_call_arguments_map.SMACreateCallArgumentsMap"
    ]
    """<p>Context passed to a CreateSipMediaApplication API call. For example, you could pass key-value pairs such as: <code>"FirstName": "John", "LastName": "Doe"</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSipMediaApplicationCallRequest) -> dict:
    out: dict = {}
    out["FromPhoneNumber"] = value["from_phone_number"]
    out["ToPhoneNumber"] = value["to_phone_number"]
    if "sip_headers" in value:
        import capo_chime_sdk_voice.types.sip_headers_map

        out["SipHeaders"] = capo_chime_sdk_voice.types.sip_headers_map.serialize_json(
            value["sip_headers"]
        )
    if "arguments_map" in value:
        import capo_chime_sdk_voice.types.sma_create_call_arguments_map

        out["ArgumentsMap"] = (
            capo_chime_sdk_voice.types.sma_create_call_arguments_map.serialize_json(
                value["arguments_map"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateSipMediaApplicationCallRequest:
    out: CreateSipMediaApplicationCallRequest = {}  # type: ignore[typeddict-item]
    if data.get("FromPhoneNumber") is not None:
        out["from_phone_number"] = data["FromPhoneNumber"]
    else:
        raise DeserializationError(
            "CreateSipMediaApplicationCallRequest.from_phone_number required"
        )
    if data.get("ToPhoneNumber") is not None:
        out["to_phone_number"] = data["ToPhoneNumber"]
    else:
        raise DeserializationError(
            "CreateSipMediaApplicationCallRequest.to_phone_number required"
        )
    if data.get("SipHeaders") is not None:
        import capo_chime_sdk_voice.types.sip_headers_map

        out["sip_headers"] = (
            capo_chime_sdk_voice.types.sip_headers_map.deserialize_json(
                data["SipHeaders"]
            )
        )
    if data.get("ArgumentsMap") is not None:
        import capo_chime_sdk_voice.types.sma_create_call_arguments_map

        out["arguments_map"] = (
            capo_chime_sdk_voice.types.sma_create_call_arguments_map.deserialize_json(
                data["ArgumentsMap"]
            )
        )
    return out
