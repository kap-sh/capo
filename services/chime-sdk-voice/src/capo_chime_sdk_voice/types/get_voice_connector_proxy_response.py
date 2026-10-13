"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#GetVoiceConnectorProxyResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.proxy


class GetVoiceConnectorProxyResponse(TypedDict, closed=True):
    proxy: NotRequired["capo_chime_sdk_voice.types.proxy.Proxy"]
    """<p>The proxy configuration details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetVoiceConnectorProxyResponse) -> dict:
    out: dict = {}
    if "proxy" in value:
        import capo_chime_sdk_voice.types.proxy

        out["Proxy"] = capo_chime_sdk_voice.types.proxy.serialize_json(value["proxy"])
    return out


def deserialize_json(data: dict) -> GetVoiceConnectorProxyResponse:
    out: GetVoiceConnectorProxyResponse = {}  # type: ignore[typeddict-item]
    if data.get("Proxy") is not None:
        import capo_chime_sdk_voice.types.proxy

        out["proxy"] = capo_chime_sdk_voice.types.proxy.deserialize_json(data["Proxy"])
    return out


def redact_sensitive(value: GetVoiceConnectorProxyResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "proxy" in value:
        import capo_chime_sdk_voice.types.proxy

        out["proxy"] = capo_chime_sdk_voice.types.proxy.redact_sensitive(value["proxy"])
    return out
