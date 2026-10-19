"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#PutRawEventsRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridgev2.types.deduplication_configuration
    import capo_eventbridgev2.types.event_bus_arn
    import capo_eventbridgev2.types.put_raw_events_request_entry_list
    import capo_eventbridgev2.types.schema_registry_configuration


class PutRawEventsRequest(TypedDict, closed=True):
    event_bus_arn: "capo_eventbridgev2.types.event_bus_arn.EventBusArn"
    entries: "capo_eventbridgev2.types.put_raw_events_request_entry_list.PutRawEventsRequestEntryList"
    schema_registry_configuration: NotRequired[
        "capo_eventbridgev2.types.schema_registry_configuration.SchemaRegistryConfiguration"
    ]
    """Schema-registry settings for encoding open-format (Avro/Protobuf) events. Required for open-format entries; ignored for JSON entries. The registry is read with the caller's credentials, so the caller needs read access to the registry it references."""
    deduplication_configuration: NotRequired[
        "capo_eventbridgev2.types.deduplication_configuration.DeduplicationConfiguration"
    ]
    """Request-level deduplication settings, applied to every entry in the batch."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PutRawEventsRequest) -> dict:
    out: dict = {}
    out["EventBusArn"] = value["event_bus_arn"]
    import capo_eventbridgev2.types.put_raw_events_request_entry_list

    out["Entries"] = (
        capo_eventbridgev2.types.put_raw_events_request_entry_list.serialize_cbor(
            value["entries"]
        )
    )
    if "schema_registry_configuration" in value:
        import capo_eventbridgev2.types.schema_registry_configuration

        out["SchemaRegistryConfiguration"] = (
            capo_eventbridgev2.types.schema_registry_configuration.serialize_cbor(
                value["schema_registry_configuration"]
            )
        )
    if "deduplication_configuration" in value:
        import capo_eventbridgev2.types.deduplication_configuration

        out["DeduplicationConfiguration"] = (
            capo_eventbridgev2.types.deduplication_configuration.serialize_cbor(
                value["deduplication_configuration"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> PutRawEventsRequest:
    out: PutRawEventsRequest = {}  # type: ignore[typeddict-item]
    if data.get("EventBusArn") is not None:
        out["event_bus_arn"] = data["EventBusArn"]
    else:
        out["event_bus_arn"] = ""
    if data.get("Entries") is not None:
        import capo_eventbridgev2.types.put_raw_events_request_entry_list

        out["entries"] = (
            capo_eventbridgev2.types.put_raw_events_request_entry_list.deserialize_cbor(
                data["Entries"]
            )
        )
    else:
        out["entries"] = []
    if data.get("SchemaRegistryConfiguration") is not None:
        import capo_eventbridgev2.types.schema_registry_configuration

        out["schema_registry_configuration"] = (
            capo_eventbridgev2.types.schema_registry_configuration.deserialize_cbor(
                data["SchemaRegistryConfiguration"]
            )
        )
    if data.get("DeduplicationConfiguration") is not None:
        import capo_eventbridgev2.types.deduplication_configuration

        out["deduplication_configuration"] = (
            capo_eventbridgev2.types.deduplication_configuration.deserialize_cbor(
                data["DeduplicationConfiguration"]
            )
        )
    return out


def redact_sensitive(value: PutRawEventsRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "entries" in value:
        import capo_eventbridgev2.types.put_raw_events_request_entry_list

        out["entries"] = (
            capo_eventbridgev2.types.put_raw_events_request_entry_list.redact_sensitive(
                value["entries"]
            )
        )
    return out
