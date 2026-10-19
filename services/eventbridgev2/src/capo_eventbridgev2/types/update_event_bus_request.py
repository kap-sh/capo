"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#UpdateEventBusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridgev2.types.description
    import capo_eventbridgev2.types.encryption_configuration
    import capo_eventbridgev2.types.event_bus_arn
    import capo_eventbridgev2.types.storage_configuration


class UpdateEventBusRequest(TypedDict, closed=True):
    event_bus_arn: "capo_eventbridgev2.types.event_bus_arn.EventBusArn"
    description: NotRequired["capo_eventbridgev2.types.description.Description"]
    encryption_configuration: NotRequired[
        "capo_eventbridgev2.types.encryption_configuration.EncryptionConfiguration"
    ]
    storage_configuration: NotRequired[
        "capo_eventbridgev2.types.storage_configuration.StorageConfiguration"
    ]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateEventBusRequest) -> dict:
    out: dict = {}
    out["EventBusArn"] = value["event_bus_arn"]
    if "description" in value:
        out["Description"] = value["description"]
    if "encryption_configuration" in value:
        import capo_eventbridgev2.types.encryption_configuration

        out["EncryptionConfiguration"] = (
            capo_eventbridgev2.types.encryption_configuration.serialize_cbor(
                value["encryption_configuration"]
            )
        )
    if "storage_configuration" in value:
        import capo_eventbridgev2.types.storage_configuration

        out["StorageConfiguration"] = (
            capo_eventbridgev2.types.storage_configuration.serialize_cbor(
                value["storage_configuration"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> UpdateEventBusRequest:
    out: UpdateEventBusRequest = {}  # type: ignore[typeddict-item]
    if data.get("EventBusArn") is not None:
        out["event_bus_arn"] = data["EventBusArn"]
    else:
        out["event_bus_arn"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("EncryptionConfiguration") is not None:
        import capo_eventbridgev2.types.encryption_configuration

        out["encryption_configuration"] = (
            capo_eventbridgev2.types.encryption_configuration.deserialize_cbor(
                data["EncryptionConfiguration"]
            )
        )
    if data.get("StorageConfiguration") is not None:
        import capo_eventbridgev2.types.storage_configuration

        out["storage_configuration"] = (
            capo_eventbridgev2.types.storage_configuration.deserialize_cbor(
                data["StorageConfiguration"]
            )
        )
    return out
