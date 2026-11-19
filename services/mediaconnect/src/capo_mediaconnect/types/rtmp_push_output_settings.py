"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RtmpPushOutputSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.tls_encryption


class RtmpPushOutputSettings(TypedDict, closed=True):
    application_name: NotRequired["str"]
    """<p>The name of the RTMP application on the destination server. Together with the stream name, the application name forms the RTMP URL path, in the pattern <code>rtmp://destinationAddress/applicationName/streamName</code>.</p>"""
    stream_name: NotRequired["str"]
    """<p>The name of the RTMP stream that the output publishes to the destination application. The stream name forms the final segment of the RTMP URL path.</p>"""
    tls_encryption: NotRequired["capo_mediaconnect.types.tls_encryption.TlsEncryption"]
    """<p>The TLS encryption settings for the output. When you specify these settings, the output uses RTMPS (RTMP over TLS) to establish a secure, encrypted connection to the destination server.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RtmpPushOutputSettings) -> dict:
    out: dict = {}
    if "application_name" in value:
        out["applicationName"] = value["application_name"]
    if "stream_name" in value:
        out["streamName"] = value["stream_name"]
    if "tls_encryption" in value:
        import capo_mediaconnect.types.tls_encryption

        out["tlsEncryption"] = capo_mediaconnect.types.tls_encryption.serialize_json(
            value["tls_encryption"]
        )
    return out


def deserialize_json(data: dict) -> RtmpPushOutputSettings:
    out: RtmpPushOutputSettings = {}  # type: ignore[typeddict-item]
    if data.get("applicationName") is not None:
        out["application_name"] = data["applicationName"]
    if data.get("streamName") is not None:
        out["stream_name"] = data["streamName"]
    if data.get("tlsEncryption") is not None:
        import capo_mediaconnect.types.tls_encryption

        out["tls_encryption"] = capo_mediaconnect.types.tls_encryption.deserialize_json(
            data["tlsEncryption"]
        )
    return out
