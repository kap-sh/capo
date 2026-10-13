"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#DescribeEventSourceResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridgev2.types.description
    import capo_eventbridgev2.types.event_bus_arn
    import capo_eventbridgev2.types.event_source_arn
    import capo_eventbridgev2.types.event_source_configuration
    import capo_eventbridgev2.types.event_source_name
    import capo_eventbridgev2.types.event_source_state
    import capo_eventbridgev2.types.timestamp


class DescribeEventSourceResponse(TypedDict, closed=True):
    event_source_arn: NotRequired[
        "capo_eventbridgev2.types.event_source_arn.EventSourceArn"
    ]
    name: NotRequired["capo_eventbridgev2.types.event_source_name.EventSourceName"]
    event_bus_arn: NotRequired["capo_eventbridgev2.types.event_bus_arn.EventBusArn"]
    configuration: NotRequired[
        "capo_eventbridgev2.types.event_source_configuration.EventSourceConfiguration"
    ]
    description: NotRequired["capo_eventbridgev2.types.description.Description"]
    state: NotRequired["capo_eventbridgev2.types.event_source_state.EventSourceState"]
    revoked: NotRequired["bool"]
    """True when the bus owner has withdrawn this EventSource. Present only when true, so an absent member means the EventSource is not revoked. Revocation is terminal: it never returns to false. Mutating operations on a revoked EventSource fail with InvalidStateException, except DeleteEventSource, which stays available so a revoked EventSource can still be cleaned up."""
    creation_time: NotRequired["capo_eventbridgev2.types.timestamp.Timestamp"]
    """The time the EventSource was created."""
    last_modified_time: NotRequired["capo_eventbridgev2.types.timestamp.Timestamp"]
    """The time the EventSource was last modified."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeEventSourceResponse) -> dict:
    out: dict = {}
    if "event_source_arn" in value:
        out["EventSourceArn"] = value["event_source_arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "event_bus_arn" in value:
        out["EventBusArn"] = value["event_bus_arn"]
    if "configuration" in value:
        import capo_eventbridgev2.types.event_source_configuration

        out["Configuration"] = (
            capo_eventbridgev2.types.event_source_configuration.serialize_cbor(
                value["configuration"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "state" in value:
        import capo_eventbridgev2.types.event_source_state

        out["State"] = capo_eventbridgev2.types.event_source_state.serialize_cbor(
            value["state"]
        )
    if "revoked" in value:
        out["Revoked"] = value["revoked"]
    if "creation_time" in value:
        import capo_eventbridgev2.types.timestamp

        out["CreationTime"] = capo_eventbridgev2.types.timestamp.serialize_cbor(
            value["creation_time"]
        )
    if "last_modified_time" in value:
        import capo_eventbridgev2.types.timestamp

        out["LastModifiedTime"] = capo_eventbridgev2.types.timestamp.serialize_cbor(
            value["last_modified_time"]
        )
    return out


def deserialize_cbor(data: dict) -> DescribeEventSourceResponse:
    out: DescribeEventSourceResponse = {}  # type: ignore[typeddict-item]
    if data.get("EventSourceArn") is not None:
        out["event_source_arn"] = data["EventSourceArn"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("EventBusArn") is not None:
        out["event_bus_arn"] = data["EventBusArn"]
    if data.get("Configuration") is not None:
        import capo_eventbridgev2.types.event_source_configuration

        out["configuration"] = (
            capo_eventbridgev2.types.event_source_configuration.deserialize_cbor(
                data["Configuration"]
            )
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("State") is not None:
        import capo_eventbridgev2.types.event_source_state

        out["state"] = capo_eventbridgev2.types.event_source_state.deserialize_cbor(
            data["State"]
        )
    if data.get("Revoked") is not None:
        out["revoked"] = data["Revoked"]
    if data.get("CreationTime") is not None:
        import capo_eventbridgev2.types.timestamp

        out["creation_time"] = capo_eventbridgev2.types.timestamp.deserialize_cbor(
            data["CreationTime"]
        )
    if data.get("LastModifiedTime") is not None:
        import capo_eventbridgev2.types.timestamp

        out["last_modified_time"] = capo_eventbridgev2.types.timestamp.deserialize_cbor(
            data["LastModifiedTime"]
        )
    return out


def redact_sensitive(value: DescribeEventSourceResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "configuration" in value:
        import capo_eventbridgev2.types.event_source_configuration

        out["configuration"] = (
            capo_eventbridgev2.types.event_source_configuration.redact_sensitive(
                value["configuration"]
            )
        )
    return out
