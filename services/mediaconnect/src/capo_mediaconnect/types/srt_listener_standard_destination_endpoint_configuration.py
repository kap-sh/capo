"""Generated from Smithy shape ``com.amazonaws.mediaconnect#SrtListenerStandardDestinationEndpointConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.endpoint_encryption_secret_configuration


class SrtListenerStandardDestinationEndpointConfiguration(TypedDict, closed=True):
    destination_address: "str"
    """<p>The IP address on which the destination endpoint listens for incoming connections.</p>"""
    destination_ingest_port: "int"
    """<p>The port on which the destination endpoint listens for incoming connections. The valid range is 0 to 65531.</p>"""
    minimum_latency_milliseconds: "int"
    """<p>The minimum latency, in milliseconds, for the SRT connection. The valid range is 10 to 10000.</p>"""
    stream_id: NotRequired["str"]
    """<p>The stream ID that identifies the content for the SRT connection.</p>"""
    encryption_passphrase: NotRequired[
        "capo_mediaconnect.types.endpoint_encryption_secret_configuration.EndpointEncryptionSecretConfiguration"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: SrtListenerStandardDestinationEndpointConfiguration) -> dict:
    out: dict = {}
    out["destinationAddress"] = value["destination_address"]
    out["destinationIngestPort"] = value["destination_ingest_port"]
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


def deserialize_json(data: dict) -> SrtListenerStandardDestinationEndpointConfiguration:
    out: SrtListenerStandardDestinationEndpointConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("destinationAddress") is not None:
        out["destination_address"] = data["destinationAddress"]
    else:
        out["destination_address"] = ""
    if data.get("destinationIngestPort") is not None:
        out["destination_ingest_port"] = data["destinationIngestPort"]
    else:
        out["destination_ingest_port"] = 0
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
