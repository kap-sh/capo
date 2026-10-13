"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#PutEventsRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_eventbridgev2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_eventbridgev2.types.deduplication_configuration
    import capo_eventbridgev2.types.event_bus_arn
    import capo_eventbridgev2.types.put_events_request_entry_list


class PutEventsRequest(TypedDict, closed=True):
    event_bus_arn: "capo_eventbridgev2.types.event_bus_arn.EventBusArn"
    entries: "capo_eventbridgev2.types.put_events_request_entry_list.PutEventsRequestEntryList"
    deduplication_configuration: NotRequired[
        "capo_eventbridgev2.types.deduplication_configuration.DeduplicationConfiguration"
    ]
    """Request-level deduplication settings, applied to every entry in the batch."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PutEventsRequest) -> dict:
    out: dict = {}
    out["EventBusArn"] = value["event_bus_arn"]
    import capo_eventbridgev2.types.put_events_request_entry_list

    out["Entries"] = (
        capo_eventbridgev2.types.put_events_request_entry_list.serialize_cbor(
            value["entries"]
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


def deserialize_cbor(data: dict) -> PutEventsRequest:
    out: PutEventsRequest = {}  # type: ignore[typeddict-item]
    if data.get("EventBusArn") is not None:
        out["event_bus_arn"] = data["EventBusArn"]
    else:
        raise DeserializationError("PutEventsRequest.event_bus_arn required")
    if data.get("Entries") is not None:
        import capo_eventbridgev2.types.put_events_request_entry_list

        out["entries"] = (
            capo_eventbridgev2.types.put_events_request_entry_list.deserialize_cbor(
                data["Entries"]
            )
        )
    else:
        raise DeserializationError("PutEventsRequest.entries required")
    if data.get("DeduplicationConfiguration") is not None:
        import capo_eventbridgev2.types.deduplication_configuration

        out["deduplication_configuration"] = (
            capo_eventbridgev2.types.deduplication_configuration.deserialize_cbor(
                data["DeduplicationConfiguration"]
            )
        )
    return out


def redact_sensitive(value: PutEventsRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "entries" in value:
        import capo_eventbridgev2.types.put_events_request_entry_list

        out["entries"] = (
            capo_eventbridgev2.types.put_events_request_entry_list.redact_sensitive(
                value["entries"]
            )
        )
    return out
