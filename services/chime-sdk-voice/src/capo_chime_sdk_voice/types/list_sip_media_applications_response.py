"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#ListSipMediaApplicationsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.next_token_string
    import capo_chime_sdk_voice.types.sip_media_application_list


class ListSipMediaApplicationsResponse(TypedDict, closed=True):
    sip_media_applications: NotRequired[
        "capo_chime_sdk_voice.types.sip_media_application_list.SipMediaApplicationList"
    ]
    """<p>The list of SIP media applications and application details.</p>"""
    next_token: NotRequired[
        "capo_chime_sdk_voice.types.next_token_string.NextTokenString"
    ]
    """<p>The token used to return the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSipMediaApplicationsResponse) -> dict:
    out: dict = {}
    if "sip_media_applications" in value:
        import capo_chime_sdk_voice.types.sip_media_application_list

        out["SipMediaApplications"] = (
            capo_chime_sdk_voice.types.sip_media_application_list.serialize_json(
                value["sip_media_applications"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSipMediaApplicationsResponse:
    out: ListSipMediaApplicationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("SipMediaApplications") is not None:
        import capo_chime_sdk_voice.types.sip_media_application_list

        out["sip_media_applications"] = (
            capo_chime_sdk_voice.types.sip_media_application_list.deserialize_json(
                data["SipMediaApplications"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListSipMediaApplicationsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "sip_media_applications" in value:
        import capo_chime_sdk_voice.types.sip_media_application_list

        out["sip_media_applications"] = (
            capo_chime_sdk_voice.types.sip_media_application_list.redact_sensitive(
                value["sip_media_applications"]
            )
        )
    return out
