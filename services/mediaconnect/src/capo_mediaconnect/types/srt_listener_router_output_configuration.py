"""Generated from Smithy shape ``com.amazonaws.mediaconnect#SrtListenerRouterOutputConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.srt_encryption_configuration


class SrtListenerRouterOutputConfiguration(TypedDict, closed=True):
    port: "int"
    """<p>The port number for the SRT protocol in listener mode.</p>"""
    minimum_latency_milliseconds: "int"
    """<p>The minimum latency in milliseconds for the SRT protocol in listener mode.</p>"""
    encryption_configuration: NotRequired[
        "capo_mediaconnect.types.srt_encryption_configuration.SrtEncryptionConfiguration"
    ]
    """<p>Defines the encryption settings for an SRT listener output, including the encryption key configuration and associated parameters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SrtListenerRouterOutputConfiguration) -> dict:
    out: dict = {}
    out["port"] = value["port"]
    out["minimumLatencyMilliseconds"] = value["minimum_latency_milliseconds"]
    if "encryption_configuration" in value:
        import capo_mediaconnect.types.srt_encryption_configuration

        out["encryptionConfiguration"] = (
            capo_mediaconnect.types.srt_encryption_configuration.serialize_json(
                value["encryption_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> SrtListenerRouterOutputConfiguration:
    out: SrtListenerRouterOutputConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("port") is not None:
        out["port"] = data["port"]
    else:
        out["port"] = 0
    if data.get("minimumLatencyMilliseconds") is not None:
        out["minimum_latency_milliseconds"] = data["minimumLatencyMilliseconds"]
    else:
        out["minimum_latency_milliseconds"] = 0
    if data.get("encryptionConfiguration") is not None:
        import capo_mediaconnect.types.srt_encryption_configuration

        out["encryption_configuration"] = (
            capo_mediaconnect.types.srt_encryption_configuration.deserialize_json(
                data["encryptionConfiguration"]
            )
        )
    return out
