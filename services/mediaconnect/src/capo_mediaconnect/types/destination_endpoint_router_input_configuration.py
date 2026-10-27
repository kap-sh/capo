"""Generated from Smithy shape ``com.amazonaws.mediaconnect#DestinationEndpointRouterInputConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.endpoint_encryption_configuration
    import capo_mediaconnect.types.endpoint_encryption_type
    import capo_mediaconnect.types.endpoint_lifecycle


class DestinationEndpointRouterInputConfiguration(TypedDict, closed=True):
    endpoint_lifecycle_management: (
        "capo_mediaconnect.types.endpoint_lifecycle.EndpointLifecycle"
    )
    """<p>The entity that manages the lifecycle of the associated destination endpoint. Valid values include the following:</p> <ul> <li> <p> <code>MANAGED</code> – MediaConnect manages the lifecycle of the associated destination endpoint.</p> </li> <li> <p> <code>UNMANAGED</code> – You manage the lifecycle of the associated destination endpoint.</p> </li> </ul>"""
    source_transit_decryption_type: NotRequired[
        "capo_mediaconnect.types.endpoint_encryption_type.EndpointEncryptionType"
    ]
    """<p>The type of transit decryption applied to the source content that this router input receives. Valid values include the following:</p> <ul> <li> <p> <code>SECRETS_MANAGER</code> – The decryption key or passphrase is stored in Secrets Manager.</p> </li> <li> <p> <code>AUTOMATIC</code> – MediaConnect determines the decryption key when the endpoint connects.</p> </li> </ul>"""
    source_transit_decryption: "capo_mediaconnect.types.endpoint_encryption_configuration.EndpointEncryptionConfiguration"


# --- restJson1 ser/de ---
def serialize_json(value: DestinationEndpointRouterInputConfiguration) -> dict:
    out: dict = {}
    import capo_mediaconnect.types.endpoint_lifecycle

    out["endpointLifecycleManagement"] = (
        capo_mediaconnect.types.endpoint_lifecycle.serialize_json(
            value["endpoint_lifecycle_management"]
        )
    )
    if "source_transit_decryption_type" in value:
        import capo_mediaconnect.types.endpoint_encryption_type

        out["sourceTransitDecryptionType"] = (
            capo_mediaconnect.types.endpoint_encryption_type.serialize_json(
                value["source_transit_decryption_type"]
            )
        )
    import capo_mediaconnect.types.endpoint_encryption_configuration

    out["sourceTransitDecryption"] = (
        capo_mediaconnect.types.endpoint_encryption_configuration.serialize_json(
            value["source_transit_decryption"]
        )
    )
    return out


def deserialize_json(data: dict) -> DestinationEndpointRouterInputConfiguration:
    out: DestinationEndpointRouterInputConfiguration = {}  # type: ignore[typeddict-item]
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
    if data.get("sourceTransitDecryptionType") is not None:
        import capo_mediaconnect.types.endpoint_encryption_type

        out["source_transit_decryption_type"] = (
            capo_mediaconnect.types.endpoint_encryption_type.deserialize_json(
                data["sourceTransitDecryptionType"]
            )
        )
    if data.get("sourceTransitDecryption") is not None:
        import capo_mediaconnect.types.endpoint_encryption_configuration

        out["source_transit_decryption"] = (
            capo_mediaconnect.types.endpoint_encryption_configuration.deserialize_json(
                data["sourceTransitDecryption"]
            )
        )
    else:
        out["source_transit_decryption"] = {"$unknown": {"name": ""}}
    return out
