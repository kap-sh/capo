"""Generated from Smithy shape ``com.amazonaws.mediaconnect#StandardDestinationEndpointConnectionDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.endpoint_encryption_configuration
    import capo_mediaconnect.types.endpoint_encryption_type
    import capo_mediaconnect.types.source_endpoint_type


class StandardDestinationEndpointConnectionDetails(TypedDict, closed=True):
    source_ip_address: NotRequired["str"]
    """<p>The IP address of the source that is connected to the destination endpoint.</p>"""
    source_listener_port: NotRequired["int"]
    """<p>The port on which the source listens for the connection.</p>"""
    source_encryption_type: NotRequired[
        "capo_mediaconnect.types.endpoint_encryption_type.EndpointEncryptionType"
    ]
    """<p>The type of encryption that the source uses for the connection.</p>"""
    source_encryption_configuration: NotRequired[
        "capo_mediaconnect.types.endpoint_encryption_configuration.EndpointEncryptionConfiguration"
    ]
    source_endpoint_type: NotRequired[
        "capo_mediaconnect.types.source_endpoint_type.SourceEndpointType"
    ]
    """<p>The type of the connected source endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StandardDestinationEndpointConnectionDetails) -> dict:
    out: dict = {}
    if "source_ip_address" in value:
        out["sourceIpAddress"] = value["source_ip_address"]
    if "source_listener_port" in value:
        out["sourceListenerPort"] = value["source_listener_port"]
    if "source_encryption_type" in value:
        import capo_mediaconnect.types.endpoint_encryption_type

        out["sourceEncryptionType"] = (
            capo_mediaconnect.types.endpoint_encryption_type.serialize_json(
                value["source_encryption_type"]
            )
        )
    if "source_encryption_configuration" in value:
        import capo_mediaconnect.types.endpoint_encryption_configuration

        out["sourceEncryptionConfiguration"] = (
            capo_mediaconnect.types.endpoint_encryption_configuration.serialize_json(
                value["source_encryption_configuration"]
            )
        )
    if "source_endpoint_type" in value:
        import capo_mediaconnect.types.source_endpoint_type

        out["sourceEndpointType"] = (
            capo_mediaconnect.types.source_endpoint_type.serialize_json(
                value["source_endpoint_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> StandardDestinationEndpointConnectionDetails:
    out: StandardDestinationEndpointConnectionDetails = {}  # type: ignore[typeddict-item]
    if data.get("sourceIpAddress") is not None:
        out["source_ip_address"] = data["sourceIpAddress"]
    if data.get("sourceListenerPort") is not None:
        out["source_listener_port"] = data["sourceListenerPort"]
    if data.get("sourceEncryptionType") is not None:
        import capo_mediaconnect.types.endpoint_encryption_type

        out["source_encryption_type"] = (
            capo_mediaconnect.types.endpoint_encryption_type.deserialize_json(
                data["sourceEncryptionType"]
            )
        )
    if data.get("sourceEncryptionConfiguration") is not None:
        import capo_mediaconnect.types.endpoint_encryption_configuration

        out["source_encryption_configuration"] = (
            capo_mediaconnect.types.endpoint_encryption_configuration.deserialize_json(
                data["sourceEncryptionConfiguration"]
            )
        )
    if data.get("sourceEndpointType") is not None:
        import capo_mediaconnect.types.source_endpoint_type

        out["source_endpoint_type"] = (
            capo_mediaconnect.types.source_endpoint_type.deserialize_json(
                data["sourceEndpointType"]
            )
        )
    return out
