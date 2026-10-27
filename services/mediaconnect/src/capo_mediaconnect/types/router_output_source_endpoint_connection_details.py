"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterOutputSourceEndpointConnectionDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.destination_endpoint_type
    import capo_mediaconnect.types.endpoint_encryption_configuration
    import capo_mediaconnect.types.endpoint_encryption_type


class RouterOutputSourceEndpointConnectionDetails(TypedDict, closed=True):
    destination_decryption_type: NotRequired[
        "capo_mediaconnect.types.endpoint_encryption_type.EndpointEncryptionType"
    ]
    """<p>The type of decryption that the destination uses for the connection.</p>"""
    destination_decryption_configuration: NotRequired[
        "capo_mediaconnect.types.endpoint_encryption_configuration.EndpointEncryptionConfiguration"
    ]
    destination_endpoint_type: NotRequired[
        "capo_mediaconnect.types.destination_endpoint_type.DestinationEndpointType"
    ]
    """<p>The type of the connected destination endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouterOutputSourceEndpointConnectionDetails) -> dict:
    out: dict = {}
    if "destination_decryption_type" in value:
        import capo_mediaconnect.types.endpoint_encryption_type

        out["destinationDecryptionType"] = (
            capo_mediaconnect.types.endpoint_encryption_type.serialize_json(
                value["destination_decryption_type"]
            )
        )
    if "destination_decryption_configuration" in value:
        import capo_mediaconnect.types.endpoint_encryption_configuration

        out["destinationDecryptionConfiguration"] = (
            capo_mediaconnect.types.endpoint_encryption_configuration.serialize_json(
                value["destination_decryption_configuration"]
            )
        )
    if "destination_endpoint_type" in value:
        import capo_mediaconnect.types.destination_endpoint_type

        out["destinationEndpointType"] = (
            capo_mediaconnect.types.destination_endpoint_type.serialize_json(
                value["destination_endpoint_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> RouterOutputSourceEndpointConnectionDetails:
    out: RouterOutputSourceEndpointConnectionDetails = {}  # type: ignore[typeddict-item]
    if data.get("destinationDecryptionType") is not None:
        import capo_mediaconnect.types.endpoint_encryption_type

        out["destination_decryption_type"] = (
            capo_mediaconnect.types.endpoint_encryption_type.deserialize_json(
                data["destinationDecryptionType"]
            )
        )
    if data.get("destinationDecryptionConfiguration") is not None:
        import capo_mediaconnect.types.endpoint_encryption_configuration

        out["destination_decryption_configuration"] = (
            capo_mediaconnect.types.endpoint_encryption_configuration.deserialize_json(
                data["destinationDecryptionConfiguration"]
            )
        )
    if data.get("destinationEndpointType") is not None:
        import capo_mediaconnect.types.destination_endpoint_type

        out["destination_endpoint_type"] = (
            capo_mediaconnect.types.destination_endpoint_type.deserialize_json(
                data["destinationEndpointType"]
            )
        )
    return out
