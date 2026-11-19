"""Generated from Smithy shape ``com.amazonaws.health#EventDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_health.types.event
    import capo_health.types.event_description
    import capo_health.types.event_metadata


class EventDetails(TypedDict, closed=True):
    event: NotRequired["capo_health.types.event.Event"]
    """<p>Summary information about the event.</p>"""
    event_description: NotRequired[
        "capo_health.types.event_description.EventDescription"
    ]
    """<p>The most recent description of the event.</p>"""
    event_metadata: NotRequired["capo_health.types.event_metadata.eventMetadata"]
    """<p>Additional metadata about the event.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventDetails) -> dict:
    out: dict = {}
    if "event" in value:
        import capo_health.types.event

        out["event"] = capo_health.types.event.serialize_aws_json_1_1(value["event"])
    if "event_description" in value:
        import capo_health.types.event_description

        out["eventDescription"] = (
            capo_health.types.event_description.serialize_aws_json_1_1(
                value["event_description"]
            )
        )
    if "event_metadata" in value:
        import capo_health.types.event_metadata

        out["eventMetadata"] = capo_health.types.event_metadata.serialize_aws_json_1_1(
            value["event_metadata"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EventDetails:
    out: EventDetails = {}  # type: ignore[typeddict-item]
    if data.get("event") is not None:
        import capo_health.types.event

        out["event"] = capo_health.types.event.deserialize_aws_json_1_1(data["event"])
    if data.get("eventDescription") is not None:
        import capo_health.types.event_description

        out["event_description"] = (
            capo_health.types.event_description.deserialize_aws_json_1_1(
                data["eventDescription"]
            )
        )
    if data.get("eventMetadata") is not None:
        import capo_health.types.event_metadata

        out["event_metadata"] = (
            capo_health.types.event_metadata.deserialize_aws_json_1_1(
                data["eventMetadata"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EventDetails) -> dict:
    out: dict = {}
    if "event" in value:
        import capo_health.types.event

        out["event"] = capo_health.types.event.serialize_cbor(value["event"])
    if "event_description" in value:
        import capo_health.types.event_description

        out["eventDescription"] = capo_health.types.event_description.serialize_cbor(
            value["event_description"]
        )
    if "event_metadata" in value:
        import capo_health.types.event_metadata

        out["eventMetadata"] = capo_health.types.event_metadata.serialize_cbor(
            value["event_metadata"]
        )
    return out


def deserialize_cbor(data: dict) -> EventDetails:
    out: EventDetails = {}  # type: ignore[typeddict-item]
    if data.get("event") is not None:
        import capo_health.types.event

        out["event"] = capo_health.types.event.deserialize_cbor(data["event"])
    if data.get("eventDescription") is not None:
        import capo_health.types.event_description

        out["event_description"] = capo_health.types.event_description.deserialize_cbor(
            data["eventDescription"]
        )
    if data.get("eventMetadata") is not None:
        import capo_health.types.event_metadata

        out["event_metadata"] = capo_health.types.event_metadata.deserialize_cbor(
            data["eventMetadata"]
        )
    return out
