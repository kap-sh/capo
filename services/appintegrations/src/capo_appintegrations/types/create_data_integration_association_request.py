"""Generated from Smithy shape ``com.amazonaws.appintegrations#CreateDataIntegrationAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appintegrations.types.client_association_metadata
    import capo_appintegrations.types.client_id
    import capo_appintegrations.types.destination_uri
    import capo_appintegrations.types.execution_configuration
    import capo_appintegrations.types.idempotency_token
    import capo_appintegrations.types.identifier
    import capo_appintegrations.types.object_configuration


class CreateDataIntegrationAssociationRequest(TypedDict, closed=True):
    data_integration_identifier: "capo_appintegrations.types.identifier.Identifier"
    """<p>A unique identifier for the DataIntegration.</p>"""
    client_id: NotRequired["capo_appintegrations.types.client_id.ClientId"]
    """<p>The identifier for the client that is associated with the DataIntegration association.</p>"""
    object_configuration: NotRequired[
        "capo_appintegrations.types.object_configuration.ObjectConfiguration"
    ]
    destination_uri: NotRequired[
        "capo_appintegrations.types.destination_uri.DestinationURI"
    ]
    """<p>The URI of the data destination.</p>"""
    client_association_metadata: NotRequired[
        "capo_appintegrations.types.client_association_metadata.ClientAssociationMetadata"
    ]
    """<p>The mapping of metadata to be extracted from the data.</p>"""
    client_token: NotRequired[
        "capo_appintegrations.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>"""
    execution_configuration: NotRequired[
        "capo_appintegrations.types.execution_configuration.ExecutionConfiguration"
    ]
    """<p>The configuration for how the files should be pulled from the source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDataIntegrationAssociationRequest) -> dict:
    out: dict = {}
    if "client_id" in value:
        out["ClientId"] = value["client_id"]
    if "object_configuration" in value:
        import capo_appintegrations.types.object_configuration

        out["ObjectConfiguration"] = (
            capo_appintegrations.types.object_configuration.serialize_json(
                value["object_configuration"]
            )
        )
    if "destination_uri" in value:
        out["DestinationURI"] = value["destination_uri"]
    if "client_association_metadata" in value:
        import capo_appintegrations.types.client_association_metadata

        out["ClientAssociationMetadata"] = (
            capo_appintegrations.types.client_association_metadata.serialize_json(
                value["client_association_metadata"]
            )
        )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "execution_configuration" in value:
        import capo_appintegrations.types.execution_configuration

        out["ExecutionConfiguration"] = (
            capo_appintegrations.types.execution_configuration.serialize_json(
                value["execution_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateDataIntegrationAssociationRequest:
    out: CreateDataIntegrationAssociationRequest = {}  # type: ignore[typeddict-item]
    if data.get("ClientId") is not None:
        out["client_id"] = data["ClientId"]
    if data.get("ObjectConfiguration") is not None:
        import capo_appintegrations.types.object_configuration

        out["object_configuration"] = (
            capo_appintegrations.types.object_configuration.deserialize_json(
                data["ObjectConfiguration"]
            )
        )
    if data.get("DestinationURI") is not None:
        out["destination_uri"] = data["DestinationURI"]
    if data.get("ClientAssociationMetadata") is not None:
        import capo_appintegrations.types.client_association_metadata

        out["client_association_metadata"] = (
            capo_appintegrations.types.client_association_metadata.deserialize_json(
                data["ClientAssociationMetadata"]
            )
        )
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("ExecutionConfiguration") is not None:
        import capo_appintegrations.types.execution_configuration

        out["execution_configuration"] = (
            capo_appintegrations.types.execution_configuration.deserialize_json(
                data["ExecutionConfiguration"]
            )
        )
    return out
