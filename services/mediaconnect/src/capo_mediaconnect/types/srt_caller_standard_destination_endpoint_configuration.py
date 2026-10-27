"""Generated from Smithy shape ``com.amazonaws.mediaconnect#SrtCallerStandardDestinationEndpointConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.endpoint_encryption_secret_configuration


class SrtCallerStandardDestinationEndpointConfiguration(TypedDict, closed=True):
    source_listener_port: "int"
    """<p>The port on which the source listens for the connection. The valid range is 3000 to 30000.</p>"""
    minimum_latency_milliseconds: "int"
    """<p>The minimum latency, in milliseconds, for the SRT connection. The valid range is 10 to 10000.</p>"""
    encryption_passphrase: NotRequired[
        "capo_mediaconnect.types.endpoint_encryption_secret_configuration.EndpointEncryptionSecretConfiguration"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: SrtCallerStandardDestinationEndpointConfiguration) -> dict:
    out: dict = {}
    out["sourceListenerPort"] = value["source_listener_port"]
    out["minimumLatencyMilliseconds"] = value["minimum_latency_milliseconds"]
    if "encryption_passphrase" in value:
        import capo_mediaconnect.types.endpoint_encryption_secret_configuration

        out["encryptionPassphrase"] = (
            capo_mediaconnect.types.endpoint_encryption_secret_configuration.serialize_json(
                value["encryption_passphrase"]
            )
        )
    return out


def deserialize_json(data: dict) -> SrtCallerStandardDestinationEndpointConfiguration:
    out: SrtCallerStandardDestinationEndpointConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("sourceListenerPort") is not None:
        out["source_listener_port"] = data["sourceListenerPort"]
    else:
        out["source_listener_port"] = 0
    if data.get("minimumLatencyMilliseconds") is not None:
        out["minimum_latency_milliseconds"] = data["minimumLatencyMilliseconds"]
    else:
        out["minimum_latency_milliseconds"] = 0
    if data.get("encryptionPassphrase") is not None:
        import capo_mediaconnect.types.endpoint_encryption_secret_configuration

        out["encryption_passphrase"] = (
            capo_mediaconnect.types.endpoint_encryption_secret_configuration.deserialize_json(
                data["encryptionPassphrase"]
            )
        )
    return out
