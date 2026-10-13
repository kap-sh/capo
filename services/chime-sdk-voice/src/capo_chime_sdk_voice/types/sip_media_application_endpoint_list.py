"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#SipMediaApplicationEndpointList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.sip_media_application_endpoint

SipMediaApplicationEndpointList: TypeAlias = list[
    "capo_chime_sdk_voice.types.sip_media_application_endpoint.SipMediaApplicationEndpoint"
]


# --- restJson1 ser/de ---
def serialize_json(value: SipMediaApplicationEndpointList) -> list:
    import capo_chime_sdk_voice.types.sip_media_application_endpoint

    out: list = []
    for item in value:
        out.append(
            capo_chime_sdk_voice.types.sip_media_application_endpoint.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> SipMediaApplicationEndpointList:
    import capo_chime_sdk_voice.types.sip_media_application_endpoint

    out: SipMediaApplicationEndpointList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_chime_sdk_voice.types.sip_media_application_endpoint.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: SipMediaApplicationEndpointList) -> list[Any]:
    import capo_chime_sdk_voice.types.sip_media_application_endpoint

    return [
        capo_chime_sdk_voice.types.sip_media_application_endpoint.redact_sensitive(item)
        for item in value
    ]
