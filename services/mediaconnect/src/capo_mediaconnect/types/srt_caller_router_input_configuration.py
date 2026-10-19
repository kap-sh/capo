"""Generated from Smithy shape ``com.amazonaws.mediaconnect#SrtCallerRouterInputConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.srt_decryption_configuration


class SrtCallerRouterInputConfiguration(TypedDict, closed=True):
    source_address: "str"
    """<p>The source IP address for the SRT protocol in caller mode.</p>"""
    source_port: "int"
    """<p>The source port number for the SRT protocol in caller mode.</p>"""
    minimum_latency_milliseconds: "int"
    """<p>The minimum latency in milliseconds for the SRT protocol in caller mode.</p>"""
    stream_id: NotRequired["str"]
    """<p>The stream ID for the SRT protocol in caller mode.</p>"""
    decryption_configuration: NotRequired[
        "capo_mediaconnect.types.srt_decryption_configuration.SrtDecryptionConfiguration"
    ]
    """<p>Specifies the decryption settings for an SRT caller input, including the encryption key configuration and associated parameters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SrtCallerRouterInputConfiguration) -> dict:
    out: dict = {}
    out["sourceAddress"] = value["source_address"]
    out["sourcePort"] = value["source_port"]
    out["minimumLatencyMilliseconds"] = value["minimum_latency_milliseconds"]
    if "stream_id" in value:
        out["streamId"] = value["stream_id"]
    if "decryption_configuration" in value:
        import capo_mediaconnect.types.srt_decryption_configuration

        out["decryptionConfiguration"] = (
            capo_mediaconnect.types.srt_decryption_configuration.serialize_json(
                value["decryption_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> SrtCallerRouterInputConfiguration:
    out: SrtCallerRouterInputConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("sourceAddress") is not None:
        out["source_address"] = data["sourceAddress"]
    else:
        out["source_address"] = ""
    if data.get("sourcePort") is not None:
        out["source_port"] = data["sourcePort"]
    else:
        out["source_port"] = 0
    if data.get("minimumLatencyMilliseconds") is not None:
        out["minimum_latency_milliseconds"] = data["minimumLatencyMilliseconds"]
    else:
        out["minimum_latency_milliseconds"] = 0
    if data.get("streamId") is not None:
        out["stream_id"] = data["streamId"]
    if data.get("decryptionConfiguration") is not None:
        import capo_mediaconnect.types.srt_decryption_configuration

        out["decryption_configuration"] = (
            capo_mediaconnect.types.srt_decryption_configuration.deserialize_json(
                data["decryptionConfiguration"]
            )
        )
    return out
