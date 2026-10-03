"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#PutRawEventsRequestEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_eventbridgev2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_eventbridgev2.types.event_data
    import capo_eventbridgev2.types.event_metadata_map
    import capo_eventbridgev2.types.put_raw_events_system_metadata


class PutRawEventsRequestEntry(TypedDict, closed=True):
    data: "capo_eventbridgev2.types.event_data.EventData"
    """The event data as a base64-encoded blob. Supports binary formats."""
    metadata: NotRequired[
        "capo_eventbridgev2.types.event_metadata_map.EventMetadataMap"
    ]
    """Metadata key-value pairs you define. Keys must be 1-128 characters and must not contain "/"."""
    system_metadata: "capo_eventbridgev2.types.put_raw_events_system_metadata.PutRawEventsSystemMetadata"
    """Structured system metadata with defined properties."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PutRawEventsRequestEntry) -> dict:
    out: dict = {}
    import capo_eventbridgev2.types.event_data

    out["Data"] = capo_eventbridgev2.types.event_data.serialize_cbor(value["data"])
    if "metadata" in value:
        import capo_eventbridgev2.types.event_metadata_map

        out["Metadata"] = capo_eventbridgev2.types.event_metadata_map.serialize_cbor(
            value["metadata"]
        )
    import capo_eventbridgev2.types.put_raw_events_system_metadata

    out["SystemMetadata"] = (
        capo_eventbridgev2.types.put_raw_events_system_metadata.serialize_cbor(
            value["system_metadata"]
        )
    )
    return out


def deserialize_cbor(data: dict) -> PutRawEventsRequestEntry:
    out: PutRawEventsRequestEntry = {}  # type: ignore[typeddict-item]
    if data.get("Data") is not None:
        import capo_eventbridgev2.types.event_data

        out["data"] = capo_eventbridgev2.types.event_data.deserialize_cbor(data["Data"])
    else:
        raise DeserializationError("PutRawEventsRequestEntry.data required")
    if data.get("Metadata") is not None:
        import capo_eventbridgev2.types.event_metadata_map

        out["metadata"] = capo_eventbridgev2.types.event_metadata_map.deserialize_cbor(
            data["Metadata"]
        )
    if data.get("SystemMetadata") is not None:
        import capo_eventbridgev2.types.put_raw_events_system_metadata

        out["system_metadata"] = (
            capo_eventbridgev2.types.put_raw_events_system_metadata.deserialize_cbor(
                data["SystemMetadata"]
            )
        )
    else:
        raise DeserializationError("PutRawEventsRequestEntry.system_metadata required")
    return out
