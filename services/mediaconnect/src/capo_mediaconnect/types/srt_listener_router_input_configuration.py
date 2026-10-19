"""Generated from Smithy shape ``com.amazonaws.mediaconnect#SrtListenerRouterInputConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.srt_decryption_configuration


class SrtListenerRouterInputConfiguration(TypedDict, closed=True):
    port: "int"
    """<p>The port number for the SRT protocol in listener mode.</p>"""
    minimum_latency_milliseconds: "int"
    """<p>The minimum latency in milliseconds for the SRT protocol in listener mode.</p>"""
    decryption_configuration: NotRequired[
        "capo_mediaconnect.types.srt_decryption_configuration.SrtDecryptionConfiguration"
    ]
    """<p>Specifies the decryption settings for an SRT listener input, including the encryption key configuration and associated parameters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SrtListenerRouterInputConfiguration) -> dict:
    out: dict = {}
    out["port"] = value["port"]
    out["minimumLatencyMilliseconds"] = value["minimum_latency_milliseconds"]
    if "decryption_configuration" in value:
        import capo_mediaconnect.types.srt_decryption_configuration

        out["decryptionConfiguration"] = (
            capo_mediaconnect.types.srt_decryption_configuration.serialize_json(
                value["decryption_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> SrtListenerRouterInputConfiguration:
    out: SrtListenerRouterInputConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("port") is not None:
        out["port"] = data["port"]
    else:
        out["port"] = 0
    if data.get("minimumLatencyMilliseconds") is not None:
        out["minimum_latency_milliseconds"] = data["minimumLatencyMilliseconds"]
    else:
        out["minimum_latency_milliseconds"] = 0
    if data.get("decryptionConfiguration") is not None:
        import capo_mediaconnect.types.srt_decryption_configuration

        out["decryption_configuration"] = (
            capo_mediaconnect.types.srt_decryption_configuration.deserialize_json(
                data["decryptionConfiguration"]
            )
        )
    return out
