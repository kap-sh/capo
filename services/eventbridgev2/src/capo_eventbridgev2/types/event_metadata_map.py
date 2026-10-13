"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#EventMetadataMap``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_eventbridgev2.types.event_metadata_key
    import capo_eventbridgev2.types.event_metadata_value

EventMetadataMap: TypeAlias = dict[
    "capo_eventbridgev2.types.event_metadata_key.EventMetadataKey",
    "capo_eventbridgev2.types.event_metadata_value.EventMetadataValue",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(input_to_serialize: EventMetadataMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_cbor(data: dict) -> EventMetadataMap:
    out: EventMetadataMap = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out


def redact_sensitive(value: EventMetadataMap) -> dict[str, Any]:
    return dict.fromkeys(value, "*** Sensitive Data Redacted ***")
