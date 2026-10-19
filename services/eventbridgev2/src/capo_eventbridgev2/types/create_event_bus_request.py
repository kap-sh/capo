"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#CreateEventBusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridgev2.types.client_token
    import capo_eventbridgev2.types.description
    import capo_eventbridgev2.types.encryption_configuration
    import capo_eventbridgev2.types.event_bus_name
    import capo_eventbridgev2.types.storage_configuration
    import capo_eventbridgev2.types.tag_map


class CreateEventBusRequest(TypedDict, closed=True):
    name: "capo_eventbridgev2.types.event_bus_name.EventBusName"
    description: NotRequired["capo_eventbridgev2.types.description.Description"]
    encryption_configuration: NotRequired[
        "capo_eventbridgev2.types.encryption_configuration.EncryptionConfiguration"
    ]
    storage_configuration: NotRequired[
        "capo_eventbridgev2.types.storage_configuration.StorageConfiguration"
    ]
    tags: NotRequired["capo_eventbridgev2.types.tag_map.TagMap"]
    client_token: NotRequired["capo_eventbridgev2.types.client_token.ClientToken"]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateEventBusRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
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
    if "tags" in value:
        import capo_eventbridgev2.types.tag_map

        out["Tags"] = capo_eventbridgev2.types.tag_map.serialize_cbor(value["tags"])
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_cbor(data: dict) -> CreateEventBusRequest:
    out: CreateEventBusRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
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
    if data.get("Tags") is not None:
        import capo_eventbridgev2.types.tag_map

        out["tags"] = capo_eventbridgev2.types.tag_map.deserialize_cbor(data["Tags"])
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out
