"""Generated from Smithy shape ``com.amazonaws.appfabric#UpdateIngestionDestinationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_appfabric.types.destination_configuration
    import capo_appfabric.types.identifier


class UpdateIngestionDestinationRequest(TypedDict, closed=True):
    app_bundle_identifier: "capo_appfabric.types.identifier.Identifier"
    """<p>The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the app bundle to use for the request.</p>"""
    ingestion_identifier: "capo_appfabric.types.identifier.Identifier"
    """<p>The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the ingestion to use for the request.</p>"""
    ingestion_destination_identifier: "capo_appfabric.types.identifier.Identifier"
    """<p>The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the ingestion destination to use for the request.</p>"""
    destination_configuration: (
        "capo_appfabric.types.destination_configuration.DestinationConfiguration"
    )
    """<p>Contains information about the destination of ingested data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateIngestionDestinationRequest) -> dict:
    out: dict = {}
    import capo_appfabric.types.destination_configuration

    out["destinationConfiguration"] = (
        capo_appfabric.types.destination_configuration.serialize_json(
            value["destination_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateIngestionDestinationRequest:
    out: UpdateIngestionDestinationRequest = {}  # type: ignore[typeddict-item]
    if data.get("destinationConfiguration") is not None:
        import capo_appfabric.types.destination_configuration

        out["destination_configuration"] = (
            capo_appfabric.types.destination_configuration.deserialize_json(
                data["destinationConfiguration"]
            )
        )
    else:
        out["destination_configuration"] = {"$unknown": {"name": ""}}
    return out
