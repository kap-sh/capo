"""Generated from Smithy shape ``com.amazonaws.mediaconnect#SourceEndpointRouterOutputConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.endpoint_encryption_configuration
    import capo_mediaconnect.types.endpoint_encryption_type
    import capo_mediaconnect.types.endpoint_lifecycle


class SourceEndpointRouterOutputConfiguration(TypedDict, closed=True):
    endpoint_lifecycle_management: (
        "capo_mediaconnect.types.endpoint_lifecycle.EndpointLifecycle"
    )
    """<p>The entity that manages the lifecycle of the associated source endpoint. Valid values include the following:</p> <ul> <li> <p> <code>MANAGED</code> – MediaConnect manages the lifecycle of the associated source endpoint.</p> </li> <li> <p> <code>UNMANAGED</code> – You manage the lifecycle of the associated source endpoint.</p> </li> </ul>"""
    destination_transit_encryption_type: NotRequired[
        "capo_mediaconnect.types.endpoint_encryption_type.EndpointEncryptionType"
    ]
    """<p>The type of transit encryption applied to the destination content that this router output sends. Valid values include the following:</p> <ul> <li> <p> <code>SECRETS_MANAGER</code> – The encryption key or passphrase is stored in Secrets Manager.</p> </li> <li> <p> <code>AUTOMATIC</code> – MediaConnect determines the encryption key when the endpoint connects.</p> </li> </ul>"""
    destination_transit_encryption: "capo_mediaconnect.types.endpoint_encryption_configuration.EndpointEncryptionConfiguration"


# --- restJson1 ser/de ---
def serialize_json(value: SourceEndpointRouterOutputConfiguration) -> dict:
    out: dict = {}
    import capo_mediaconnect.types.endpoint_lifecycle

    out["endpointLifecycleManagement"] = (
        capo_mediaconnect.types.endpoint_lifecycle.serialize_json(
            value["endpoint_lifecycle_management"]
        )
    )
    if "destination_transit_encryption_type" in value:
        import capo_mediaconnect.types.endpoint_encryption_type

        out["destinationTransitEncryptionType"] = (
            capo_mediaconnect.types.endpoint_encryption_type.serialize_json(
                value["destination_transit_encryption_type"]
            )
        )
    import capo_mediaconnect.types.endpoint_encryption_configuration

    out["destinationTransitEncryption"] = (
        capo_mediaconnect.types.endpoint_encryption_configuration.serialize_json(
            value["destination_transit_encryption"]
        )
    )
    return out


def deserialize_json(data: dict) -> SourceEndpointRouterOutputConfiguration:
    out: SourceEndpointRouterOutputConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("endpointLifecycleManagement") is not None:
        import capo_mediaconnect.types.endpoint_lifecycle

        out["endpoint_lifecycle_management"] = (
            capo_mediaconnect.types.endpoint_lifecycle.deserialize_json(
                data["endpointLifecycleManagement"]
            )
        )
    else:
        import typing

        out["endpoint_lifecycle_management"] = typing.cast(
            "capo_mediaconnect.types.endpoint_lifecycle.EndpointLifecycle", ""
        )
    if data.get("destinationTransitEncryptionType") is not None:
        import capo_mediaconnect.types.endpoint_encryption_type

        out["destination_transit_encryption_type"] = (
            capo_mediaconnect.types.endpoint_encryption_type.deserialize_json(
                data["destinationTransitEncryptionType"]
            )
        )
    if data.get("destinationTransitEncryption") is not None:
        import capo_mediaconnect.types.endpoint_encryption_configuration

        out["destination_transit_encryption"] = (
            capo_mediaconnect.types.endpoint_encryption_configuration.deserialize_json(
                data["destinationTransitEncryption"]
            )
        )
    else:
        out["destination_transit_encryption"] = {"$unknown": {"name": ""}}
    return out
