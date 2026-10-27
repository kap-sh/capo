"""Generated from Smithy shape ``com.amazonaws.mediaconnect#SrtListenerStandardSourceEndpointConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.endpoint_encryption_secret_configuration


class SrtListenerStandardSourceEndpointConfiguration(TypedDict, closed=True):
    source_listener_port: "int"
    """<p>The port that the source endpoint listens on for incoming connections. The valid range is 1024 to 65535.</p>"""
    source_address: "str"
    """<p>The IP address that the source endpoint listens on for incoming connections.</p>"""
    minimum_latency_milliseconds: "int"
    """<p>The minimum latency, in milliseconds, for the SRT connection. The valid range is 10 to 10000.</p>"""
    stream_id: NotRequired["str"]
    """<p>The stream ID that identifies the content for the SRT connection.</p>"""
    encryption_passphrase: NotRequired[
        "capo_mediaconnect.types.endpoint_encryption_secret_configuration.EndpointEncryptionSecretConfiguration"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: SrtListenerStandardSourceEndpointConfiguration) -> dict:
    out: dict = {}
    out["sourceListenerPort"] = value["source_listener_port"]
    out["sourceAddress"] = value["source_address"]
    out["minimumLatencyMilliseconds"] = value["minimum_latency_milliseconds"]
    if "stream_id" in value:
        out["streamId"] = value["stream_id"]
    if "encryption_passphrase" in value:
        import capo_mediaconnect.types.endpoint_encryption_secret_configuration

        out["encryptionPassphrase"] = (
            capo_mediaconnect.types.endpoint_encryption_secret_configuration.serialize_json(
                value["encryption_passphrase"]
            )
        )
    return out


def deserialize_json(data: dict) -> SrtListenerStandardSourceEndpointConfiguration:
    out: SrtListenerStandardSourceEndpointConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("sourceListenerPort") is not None:
        out["source_listener_port"] = data["sourceListenerPort"]
    else:
        out["source_listener_port"] = 0
    if data.get("sourceAddress") is not None:
        out["source_address"] = data["sourceAddress"]
    else:
        out["source_address"] = ""
    if data.get("minimumLatencyMilliseconds") is not None:
        out["minimum_latency_milliseconds"] = data["minimumLatencyMilliseconds"]
    else:
        out["minimum_latency_milliseconds"] = 0
    if data.get("streamId") is not None:
        out["stream_id"] = data["streamId"]
    if data.get("encryptionPassphrase") is not None:
        import capo_mediaconnect.types.endpoint_encryption_secret_configuration

        out["encryption_passphrase"] = (
            capo_mediaconnect.types.endpoint_encryption_secret_configuration.deserialize_json(
                data["encryptionPassphrase"]
            )
        )
    return out
