"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#CreateProxySessionResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.proxy_session


class CreateProxySessionResponse(TypedDict, closed=True):
    proxy_session: NotRequired["capo_chime_sdk_voice.types.proxy_session.ProxySession"]
    """<p>The proxy session details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateProxySessionResponse) -> dict:
    out: dict = {}
    if "proxy_session" in value:
        import capo_chime_sdk_voice.types.proxy_session

        out["ProxySession"] = capo_chime_sdk_voice.types.proxy_session.serialize_json(
            value["proxy_session"]
        )
    return out


def deserialize_json(data: dict) -> CreateProxySessionResponse:
    out: CreateProxySessionResponse = {}  # type: ignore[typeddict-item]
    if data.get("ProxySession") is not None:
        import capo_chime_sdk_voice.types.proxy_session

        out["proxy_session"] = (
            capo_chime_sdk_voice.types.proxy_session.deserialize_json(
                data["ProxySession"]
            )
        )
    return out


def redact_sensitive(value: CreateProxySessionResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "proxy_session" in value:
        import capo_chime_sdk_voice.types.proxy_session

        out["proxy_session"] = (
            capo_chime_sdk_voice.types.proxy_session.redact_sensitive(
                value["proxy_session"]
            )
        )
    return out
