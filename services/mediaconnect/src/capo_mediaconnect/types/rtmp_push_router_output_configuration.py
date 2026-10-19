"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RtmpPushRouterOutputConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.tls_encryption


class RtmpPushRouterOutputConfiguration(TypedDict, closed=True):
    destination_address: "str"
    """<p>The IP address or hostname of the destination RTMP server that the router output pushes the stream to. Provide only the server address; specify the application and stream names separately.</p>"""
    destination_port: "int"
    """<p>The TCP port on the destination RTMP server. For RTMP, valid values range from <code>1024</code> to <code>65535</code>. For RTMPS (RTMP over TLS), valid values are <code>443</code> or <code>1024</code> to <code>65535</code>. RTMP typically uses port <code>1935</code>, and RTMPS typically uses port <code>443</code>.</p>"""
    application_name: "str"
    """<p>The name of the RTMP application on the destination server. Together with the stream name, the application name forms the RTMP URL path, in the pattern <code>rtmp://destinationAddress/applicationName/streamName</code>.</p>"""
    stream_name: "str"
    """<p>The name of the RTMP stream that the output publishes to the destination application. The stream name forms the final segment of the RTMP URL path.</p>"""
    tls_encryption: NotRequired["capo_mediaconnect.types.tls_encryption.TlsEncryption"]
    """<p>The TLS encryption settings for the output. When you specify these settings, the output uses RTMPS (RTMP over TLS) to establish a secure, encrypted connection to the destination server.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RtmpPushRouterOutputConfiguration) -> dict:
    out: dict = {}
    out["destinationAddress"] = value["destination_address"]
    out["destinationPort"] = value["destination_port"]
    out["applicationName"] = value["application_name"]
    out["streamName"] = value["stream_name"]
    if "tls_encryption" in value:
        import capo_mediaconnect.types.tls_encryption

        out["tlsEncryption"] = capo_mediaconnect.types.tls_encryption.serialize_json(
            value["tls_encryption"]
        )
    return out


def deserialize_json(data: dict) -> RtmpPushRouterOutputConfiguration:
    out: RtmpPushRouterOutputConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("destinationAddress") is not None:
        out["destination_address"] = data["destinationAddress"]
    else:
        out["destination_address"] = ""
    if data.get("destinationPort") is not None:
        out["destination_port"] = data["destinationPort"]
    else:
        out["destination_port"] = 0
    if data.get("applicationName") is not None:
        out["application_name"] = data["applicationName"]
    else:
        out["application_name"] = ""
    if data.get("streamName") is not None:
        out["stream_name"] = data["streamName"]
    else:
        out["stream_name"] = ""
    if data.get("tlsEncryption") is not None:
        import capo_mediaconnect.types.tls_encryption

        out["tls_encryption"] = capo_mediaconnect.types.tls_encryption.deserialize_json(
            data["tlsEncryption"]
        )
    return out
