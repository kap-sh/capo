"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#PutEventsRequestEntry``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_eventbridgev2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_eventbridgev2.types.detail_type
    import capo_eventbridgev2.types.event_detail
    import capo_eventbridgev2.types.put_events_resource_list
    import capo_eventbridgev2.types.put_events_system_metadata
    import capo_eventbridgev2.types.source
    import capo_eventbridgev2.types.timestamp


class PutEventsRequestEntry(TypedDict, closed=True):
    source: "capo_eventbridgev2.types.source.Source"
    """The source of the event. The `aws.` value prefix is service-reserved and cannot be used as a value."""
    detail_type: "capo_eventbridgev2.types.detail_type.DetailType"
    detail: NotRequired["capo_eventbridgev2.types.event_detail.EventDetail"]
    """The event payload, as a valid JSON string."""
    resources: NotRequired[
        "capo_eventbridgev2.types.put_events_resource_list.PutEventsResourceList"
    ]
    """ARNs of resources the event concerns. Included in the event delivered to subscribers."""
    time: NotRequired["capo_eventbridgev2.types.timestamp.Timestamp"]
    """The time the event occurred. Defaults to the time the service receives the event when omitted."""
    system_metadata: NotRequired[
        "capo_eventbridgev2.types.put_events_system_metadata.PutEventsSystemMetadata"
    ]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PutEventsRequestEntry) -> dict:
    out: dict = {}
    out["Source"] = value["source"]
    out["DetailType"] = value["detail_type"]
    if "detail" in value:
        out["Detail"] = value["detail"]
    if "resources" in value:
        import capo_eventbridgev2.types.put_events_resource_list

        out["Resources"] = (
            capo_eventbridgev2.types.put_events_resource_list.serialize_cbor(
                value["resources"]
            )
        )
    if "time" in value:
        import capo_eventbridgev2.types.timestamp

        out["Time"] = capo_eventbridgev2.types.timestamp.serialize_cbor(value["time"])
    if "system_metadata" in value:
        import capo_eventbridgev2.types.put_events_system_metadata

        out["SystemMetadata"] = (
            capo_eventbridgev2.types.put_events_system_metadata.serialize_cbor(
                value["system_metadata"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> PutEventsRequestEntry:
    out: PutEventsRequestEntry = {}  # type: ignore[typeddict-item]
    if data.get("Source") is not None:
        out["source"] = data["Source"]
    else:
        raise DeserializationError("PutEventsRequestEntry.source required")
    if data.get("DetailType") is not None:
        out["detail_type"] = data["DetailType"]
    else:
        raise DeserializationError("PutEventsRequestEntry.detail_type required")
    if data.get("Detail") is not None:
        out["detail"] = data["Detail"]
    if data.get("Resources") is not None:
        import capo_eventbridgev2.types.put_events_resource_list

        out["resources"] = (
            capo_eventbridgev2.types.put_events_resource_list.deserialize_cbor(
                data["Resources"]
            )
        )
    if data.get("Time") is not None:
        import capo_eventbridgev2.types.timestamp

        out["time"] = capo_eventbridgev2.types.timestamp.deserialize_cbor(data["Time"])
    if data.get("SystemMetadata") is not None:
        import capo_eventbridgev2.types.put_events_system_metadata

        out["system_metadata"] = (
            capo_eventbridgev2.types.put_events_system_metadata.deserialize_cbor(
                data["SystemMetadata"]
            )
        )
    return out


def redact_sensitive(value: PutEventsRequestEntry) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "detail" in value:
        out["detail"] = "*** Sensitive Data Redacted ***"
    return out
