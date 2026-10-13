"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#GetSipMediaApplicationResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.sip_media_application


class GetSipMediaApplicationResponse(TypedDict, closed=True):
    sip_media_application: NotRequired[
        "capo_chime_sdk_voice.types.sip_media_application.SipMediaApplication"
    ]
    """<p>The details of the SIP media application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSipMediaApplicationResponse) -> dict:
    out: dict = {}
    if "sip_media_application" in value:
        import capo_chime_sdk_voice.types.sip_media_application

        out["SipMediaApplication"] = (
            capo_chime_sdk_voice.types.sip_media_application.serialize_json(
                value["sip_media_application"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetSipMediaApplicationResponse:
    out: GetSipMediaApplicationResponse = {}  # type: ignore[typeddict-item]
    if data.get("SipMediaApplication") is not None:
        import capo_chime_sdk_voice.types.sip_media_application

        out["sip_media_application"] = (
            capo_chime_sdk_voice.types.sip_media_application.deserialize_json(
                data["SipMediaApplication"]
            )
        )
    return out


def redact_sensitive(value: GetSipMediaApplicationResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "sip_media_application" in value:
        import capo_chime_sdk_voice.types.sip_media_application

        out["sip_media_application"] = (
            capo_chime_sdk_voice.types.sip_media_application.redact_sensitive(
                value["sip_media_application"]
            )
        )
    return out
