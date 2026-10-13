"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#PutEventsRequestEntryList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_eventbridgev2.types.put_events_request_entry

PutEventsRequestEntryList: TypeAlias = list[
    "capo_eventbridgev2.types.put_events_request_entry.PutEventsRequestEntry"
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PutEventsRequestEntryList) -> list:
    import capo_eventbridgev2.types.put_events_request_entry

    out: list = []
    for item in value:
        out.append(
            capo_eventbridgev2.types.put_events_request_entry.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> PutEventsRequestEntryList:
    import capo_eventbridgev2.types.put_events_request_entry

    out: PutEventsRequestEntryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_eventbridgev2.types.put_events_request_entry.deserialize_cbor(item)
        )
    return out


def redact_sensitive(value: PutEventsRequestEntryList) -> list[Any]:
    import capo_eventbridgev2.types.put_events_request_entry

    return [
        capo_eventbridgev2.types.put_events_request_entry.redact_sensitive(item)
        for item in value
    ]
