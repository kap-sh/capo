"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#UpdateSipMediaApplicationRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.non_empty_string
    import capo_chime_sdk_voice.types.sip_media_application_endpoint_list
    import capo_chime_sdk_voice.types.sip_media_application_name


class UpdateSipMediaApplicationRequest(TypedDict, closed=True):
    sip_media_application_id: (
        "capo_chime_sdk_voice.types.non_empty_string.NonEmptyString"
    )
    """<p>The SIP media application ID.</p>"""
    name: NotRequired[
        "capo_chime_sdk_voice.types.sip_media_application_name.SipMediaApplicationName"
    ]
    """<p>The new name for the specified SIP media application.</p>"""
    endpoints: NotRequired[
        "capo_chime_sdk_voice.types.sip_media_application_endpoint_list.SipMediaApplicationEndpointList"
    ]
    """<p>The new set of endpoints for the specified SIP media application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSipMediaApplicationRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "endpoints" in value:
        import capo_chime_sdk_voice.types.sip_media_application_endpoint_list

        out["Endpoints"] = (
            capo_chime_sdk_voice.types.sip_media_application_endpoint_list.serialize_json(
                value["endpoints"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateSipMediaApplicationRequest:
    out: UpdateSipMediaApplicationRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Endpoints") is not None:
        import capo_chime_sdk_voice.types.sip_media_application_endpoint_list

        out["endpoints"] = (
            capo_chime_sdk_voice.types.sip_media_application_endpoint_list.deserialize_json(
                data["Endpoints"]
            )
        )
    return out


def redact_sensitive(value: UpdateSipMediaApplicationRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "endpoints" in value:
        import capo_chime_sdk_voice.types.sip_media_application_endpoint_list

        out["endpoints"] = (
            capo_chime_sdk_voice.types.sip_media_application_endpoint_list.redact_sensitive(
                value["endpoints"]
            )
        )
    return out
