"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#UpdateProxySessionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.capability_list
    import capo_chime_sdk_voice.types.non_empty_string128
    import capo_chime_sdk_voice.types.positive_integer
    import capo_chime_sdk_voice.types.voice_connector_id


class UpdateProxySessionRequest(TypedDict, closed=True):
    voice_connector_id: "capo_chime_sdk_voice.types.voice_connector_id.VoiceConnectorId"
    """<p>The Voice Connector ID.</p>"""
    proxy_session_id: "capo_chime_sdk_voice.types.non_empty_string128.NonEmptyString128"
    """<p>The proxy session ID.</p>"""
    capabilities: "capo_chime_sdk_voice.types.capability_list.CapabilityList"
    """<p>The proxy session capabilities.</p>"""
    expiry_minutes: NotRequired[
        "capo_chime_sdk_voice.types.positive_integer.PositiveInteger"
    ]
    """<p>The number of minutes allowed for the proxy session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateProxySessionRequest) -> dict:
    out: dict = {}
    import capo_chime_sdk_voice.types.capability_list

    out["Capabilities"] = capo_chime_sdk_voice.types.capability_list.serialize_json(
        value["capabilities"]
    )
    if "expiry_minutes" in value:
        out["ExpiryMinutes"] = value["expiry_minutes"]
    return out


def deserialize_json(data: dict) -> UpdateProxySessionRequest:
    out: UpdateProxySessionRequest = {}  # type: ignore[typeddict-item]
    if data.get("Capabilities") is not None:
        import capo_chime_sdk_voice.types.capability_list

        out["capabilities"] = (
            capo_chime_sdk_voice.types.capability_list.deserialize_json(
                data["Capabilities"]
            )
        )
    else:
        out["capabilities"] = []
    if data.get("ExpiryMinutes") is not None:
        out["expiry_minutes"] = data["ExpiryMinutes"]
    return out
