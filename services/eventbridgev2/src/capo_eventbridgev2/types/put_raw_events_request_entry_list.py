"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#PutRawEventsRequestEntryList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_eventbridgev2.types.put_raw_events_request_entry

PutRawEventsRequestEntryList: TypeAlias = list[
    "capo_eventbridgev2.types.put_raw_events_request_entry.PutRawEventsRequestEntry"
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PutRawEventsRequestEntryList) -> list:
    import capo_eventbridgev2.types.put_raw_events_request_entry

    out: list = []
    for item in value:
        out.append(
            capo_eventbridgev2.types.put_raw_events_request_entry.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> PutRawEventsRequestEntryList:
    import capo_eventbridgev2.types.put_raw_events_request_entry

    out: PutRawEventsRequestEntryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_eventbridgev2.types.put_raw_events_request_entry.deserialize_cbor(item)
        )
    return out


def redact_sensitive(value: PutRawEventsRequestEntryList) -> list[Any]:
    import capo_eventbridgev2.types.put_raw_events_request_entry

    return [
        capo_eventbridgev2.types.put_raw_events_request_entry.redact_sensitive(item)
        for item in value
    ]
