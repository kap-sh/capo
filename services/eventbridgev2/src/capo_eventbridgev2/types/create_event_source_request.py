"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#CreateEventSourceRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_eventbridgev2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_eventbridgev2.types.client_token
    import capo_eventbridgev2.types.description
    import capo_eventbridgev2.types.event_bus_arn
    import capo_eventbridgev2.types.event_source_configuration
    import capo_eventbridgev2.types.event_source_name
    import capo_eventbridgev2.types.tag_map


class CreateEventSourceRequest(TypedDict, closed=True):
    name: "capo_eventbridgev2.types.event_source_name.EventSourceName"
    event_bus_arn: "capo_eventbridgev2.types.event_bus_arn.EventBusArn"
    configuration: (
        "capo_eventbridgev2.types.event_source_configuration.EventSourceConfiguration"
    )
    description: NotRequired["capo_eventbridgev2.types.description.Description"]
    tags: NotRequired["capo_eventbridgev2.types.tag_map.TagMap"]
    client_token: NotRequired["capo_eventbridgev2.types.client_token.ClientToken"]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateEventSourceRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["EventBusArn"] = value["event_bus_arn"]
    import capo_eventbridgev2.types.event_source_configuration

    out["Configuration"] = (
        capo_eventbridgev2.types.event_source_configuration.serialize_cbor(
            value["configuration"]
        )
    )
    if "description" in value:
        out["Description"] = value["description"]
    if "tags" in value:
        import capo_eventbridgev2.types.tag_map

        out["Tags"] = capo_eventbridgev2.types.tag_map.serialize_cbor(value["tags"])
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_cbor(data: dict) -> CreateEventSourceRequest:
    out: CreateEventSourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateEventSourceRequest.name required")
    if data.get("EventBusArn") is not None:
        out["event_bus_arn"] = data["EventBusArn"]
    else:
        raise DeserializationError("CreateEventSourceRequest.event_bus_arn required")
    if data.get("Configuration") is not None:
        import capo_eventbridgev2.types.event_source_configuration

        out["configuration"] = (
            capo_eventbridgev2.types.event_source_configuration.deserialize_cbor(
                data["Configuration"]
            )
        )
    else:
        raise DeserializationError("CreateEventSourceRequest.configuration required")
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Tags") is not None:
        import capo_eventbridgev2.types.tag_map

        out["tags"] = capo_eventbridgev2.types.tag_map.deserialize_cbor(data["Tags"])
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out


def redact_sensitive(value: CreateEventSourceRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "configuration" in value:
        import capo_eventbridgev2.types.event_source_configuration

        out["configuration"] = (
            capo_eventbridgev2.types.event_source_configuration.redact_sensitive(
                value["configuration"]
            )
        )
    return out
