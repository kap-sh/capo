"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#UpdateEventSourceRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridgev2.types.description
    import capo_eventbridgev2.types.event_source_arn
    import capo_eventbridgev2.types.event_source_configuration


class UpdateEventSourceRequest(TypedDict, closed=True):
    event_source_arn: "capo_eventbridgev2.types.event_source_arn.EventSourceArn"
    configuration: NotRequired[
        "capo_eventbridgev2.types.event_source_configuration.EventSourceConfiguration"
    ]
    description: NotRequired["capo_eventbridgev2.types.description.Description"]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateEventSourceRequest) -> dict:
    out: dict = {}
    out["EventSourceArn"] = value["event_source_arn"]
    if "configuration" in value:
        import capo_eventbridgev2.types.event_source_configuration

        out["Configuration"] = (
            capo_eventbridgev2.types.event_source_configuration.serialize_cbor(
                value["configuration"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_cbor(data: dict) -> UpdateEventSourceRequest:
    out: UpdateEventSourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("EventSourceArn") is not None:
        out["event_source_arn"] = data["EventSourceArn"]
    else:
        out["event_source_arn"] = ""
    if data.get("Configuration") is not None:
        import capo_eventbridgev2.types.event_source_configuration

        out["configuration"] = (
            capo_eventbridgev2.types.event_source_configuration.deserialize_cbor(
                data["Configuration"]
            )
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    return out


def redact_sensitive(value: UpdateEventSourceRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "configuration" in value:
        import capo_eventbridgev2.types.event_source_configuration

        out["configuration"] = (
            capo_eventbridgev2.types.event_source_configuration.redact_sensitive(
                value["configuration"]
            )
        )
    return out
