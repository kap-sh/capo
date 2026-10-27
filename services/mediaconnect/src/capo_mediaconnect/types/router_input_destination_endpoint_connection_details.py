"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterInputDestinationEndpointConnectionDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.endpoint_encryption_configuration
    import capo_mediaconnect.types.endpoint_encryption_type
    import capo_mediaconnect.types.source_endpoint_type


class RouterInputDestinationEndpointConnectionDetails(TypedDict, closed=True):
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
def serialize_json(value: RouterInputDestinationEndpointConnectionDetails) -> dict:
    out: dict = {}
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


def deserialize_json(data: dict) -> RouterInputDestinationEndpointConnectionDetails:
    out: RouterInputDestinationEndpointConnectionDetails = {}  # type: ignore[typeddict-item]
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
