"""Generated from Smithy shape ``com.amazonaws.mediaconnect#SrtCallerRouterOutputConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.srt_encryption_configuration


class SrtCallerRouterOutputConfiguration(TypedDict, closed=True):
    destination_address: "str"
    """<p>The destination IP address for the SRT protocol in caller mode.</p>"""
    destination_port: "int"
    """<p>The destination port number for the SRT protocol in caller mode.</p>"""
    minimum_latency_milliseconds: "int"
    """<p>The minimum latency in milliseconds for the SRT protocol in caller mode.</p>"""
    stream_id: NotRequired["str"]
    """<p>The stream ID for the SRT protocol in caller mode.</p>"""
    encryption_configuration: NotRequired[
        "capo_mediaconnect.types.srt_encryption_configuration.SrtEncryptionConfiguration"
    ]
    """<p>Defines the encryption settings for an SRT caller output, including the encryption key configuration and associated parameters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SrtCallerRouterOutputConfiguration) -> dict:
    out: dict = {}
    out["destinationAddress"] = value["destination_address"]
    out["destinationPort"] = value["destination_port"]
    out["minimumLatencyMilliseconds"] = value["minimum_latency_milliseconds"]
    if "stream_id" in value:
        out["streamId"] = value["stream_id"]
    if "encryption_configuration" in value:
        import capo_mediaconnect.types.srt_encryption_configuration

        out["encryptionConfiguration"] = (
            capo_mediaconnect.types.srt_encryption_configuration.serialize_json(
                value["encryption_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> SrtCallerRouterOutputConfiguration:
    out: SrtCallerRouterOutputConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("destinationAddress") is not None:
        out["destination_address"] = data["destinationAddress"]
    else:
        out["destination_address"] = ""
    if data.get("destinationPort") is not None:
        out["destination_port"] = data["destinationPort"]
    else:
        out["destination_port"] = 0
    if data.get("minimumLatencyMilliseconds") is not None:
        out["minimum_latency_milliseconds"] = data["minimumLatencyMilliseconds"]
    else:
        out["minimum_latency_milliseconds"] = 0
    if data.get("streamId") is not None:
        out["stream_id"] = data["streamId"]
    if data.get("encryptionConfiguration") is not None:
        import capo_mediaconnect.types.srt_encryption_configuration

        out["encryption_configuration"] = (
            capo_mediaconnect.types.srt_encryption_configuration.deserialize_json(
                data["encryptionConfiguration"]
            )
        )
    return out
