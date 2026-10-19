"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#SchemaRegistryConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridgev2.types.confluent_public_registry_configuration
    import capo_eventbridgev2.types.schema_registry_uri


class SchemaRegistryConfiguration(TypedDict, closed=True):
    registry_uri: "capo_eventbridgev2.types.schema_registry_uri.SchemaRegistryUri"
    """Glue Schema Registry ARN, or Confluent Cloud HTTPS URL."""
    confluent_public_registry_configuration: NotRequired[
        "capo_eventbridgev2.types.confluent_public_registry_configuration.ConfluentPublicRegistryConfiguration"
    ]
    """Required when RegistryUri is an HTTPS URL. Provides Connection-based auth for Confluent Cloud."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SchemaRegistryConfiguration) -> dict:
    out: dict = {}
    out["RegistryUri"] = value["registry_uri"]
    if "confluent_public_registry_configuration" in value:
        import capo_eventbridgev2.types.confluent_public_registry_configuration

        out["ConfluentPublicRegistryConfiguration"] = (
            capo_eventbridgev2.types.confluent_public_registry_configuration.serialize_cbor(
                value["confluent_public_registry_configuration"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> SchemaRegistryConfiguration:
    out: SchemaRegistryConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("RegistryUri") is not None:
        out["registry_uri"] = data["RegistryUri"]
    else:
        out["registry_uri"] = ""
    if data.get("ConfluentPublicRegistryConfiguration") is not None:
        import capo_eventbridgev2.types.confluent_public_registry_configuration

        out["confluent_public_registry_configuration"] = (
            capo_eventbridgev2.types.confluent_public_registry_configuration.deserialize_cbor(
                data["ConfluentPublicRegistryConfiguration"]
            )
        )
    return out
