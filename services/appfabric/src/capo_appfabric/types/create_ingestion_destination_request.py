"""Generated from Smithy shape ``com.amazonaws.appfabric#CreateIngestionDestinationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_appfabric.errors import DeserializationError

if TYPE_CHECKING:
    import capo_appfabric.types.destination_configuration
    import capo_appfabric.types.identifier
    import capo_appfabric.types.processing_configuration
    import capo_appfabric.types.tag_list
    import capo_appfabric.types.uuid


class CreateIngestionDestinationRequest(TypedDict, closed=True):
    app_bundle_identifier: "capo_appfabric.types.identifier.Identifier"
    """<p>The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the app bundle to use for the request.</p>"""
    ingestion_identifier: "capo_appfabric.types.identifier.Identifier"
    """<p>The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the ingestion to use for the request.</p>"""
    processing_configuration: (
        "capo_appfabric.types.processing_configuration.ProcessingConfiguration"
    )
    """<p>Contains information about how ingested data is processed.</p>"""
    destination_configuration: (
        "capo_appfabric.types.destination_configuration.DestinationConfiguration"
    )
    """<p>Contains information about the destination of ingested data.</p>"""
    client_token: NotRequired["capo_appfabric.types.uuid.UUID"]
    """<p>Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID type of value</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>ClientToken</code>, but with different parameters, the retry fails with an <code>IdempotentParameterMismatch</code> error.</p>"""
    tags: NotRequired["capo_appfabric.types.tag_list.TagList"]
    """<p>A map of the key-value pairs of the tag or tags to assign to the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateIngestionDestinationRequest) -> dict:
    out: dict = {}
    import capo_appfabric.types.processing_configuration

    out["processingConfiguration"] = (
        capo_appfabric.types.processing_configuration.serialize_json(
            value["processing_configuration"]
        )
    )
    import capo_appfabric.types.destination_configuration

    out["destinationConfiguration"] = (
        capo_appfabric.types.destination_configuration.serialize_json(
            value["destination_configuration"]
        )
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import capo_appfabric.types.tag_list

        out["tags"] = capo_appfabric.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateIngestionDestinationRequest:
    out: CreateIngestionDestinationRequest = {}  # type: ignore[typeddict-item]
    if data.get("processingConfiguration") is not None:
        import capo_appfabric.types.processing_configuration

        out["processing_configuration"] = (
            capo_appfabric.types.processing_configuration.deserialize_json(
                data["processingConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "CreateIngestionDestinationRequest.processing_configuration required"
        )
    if data.get("destinationConfiguration") is not None:
        import capo_appfabric.types.destination_configuration

        out["destination_configuration"] = (
            capo_appfabric.types.destination_configuration.deserialize_json(
                data["destinationConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "CreateIngestionDestinationRequest.destination_configuration required"
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("tags") is not None:
        import capo_appfabric.types.tag_list

        out["tags"] = capo_appfabric.types.tag_list.deserialize_json(data["tags"])
    return out
