"""Generated from Smithy shape ``com.amazonaws.customerprofiles#GetEventStreamResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import capo_customer_profiles.types.event_stream_destination_details
    import capo_customer_profiles.types.event_stream_state
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.string1_to255
    import capo_customer_profiles.types.tag_map
    import capo_customer_profiles.types.timestamp


class GetEventStreamResponse(TypedDict, closed=True):
    domain_name: "capo_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    event_stream_arn: "capo_customer_profiles.types.string1_to255.string1To255"
    """<p>A unique identifier for the event stream.</p>"""
    created_at: "capo_customer_profiles.types.timestamp.timestamp"
    """<p>The timestamp of when the export was created.</p>"""
    state: "capo_customer_profiles.types.event_stream_state.EventStreamState"
    """<p>The operational state of destination stream for export.</p>"""
    stopped_since: NotRequired["capo_customer_profiles.types.timestamp.timestamp"]
    """<p>The timestamp when the <code>State</code> changed to <code>STOPPED</code>.</p>"""
    destination_details: "capo_customer_profiles.types.event_stream_destination_details.EventStreamDestinationDetails"
    """<p>Details regarding the Kinesis stream.</p>"""
    tags: NotRequired["capo_customer_profiles.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEventStreamResponse) -> dict:
    out: dict = {}
    out["DomainName"] = value["domain_name"]
    out["EventStreamArn"] = value["event_stream_arn"]
    import capo_customer_profiles.types.timestamp

    out["CreatedAt"] = capo_customer_profiles.types.timestamp.serialize_json(
        value["created_at"]
    )
    import capo_customer_profiles.types.event_stream_state

    out["State"] = capo_customer_profiles.types.event_stream_state.serialize_json(
        value["state"]
    )
    if "stopped_since" in value:
        import capo_customer_profiles.types.timestamp

        out["StoppedSince"] = capo_customer_profiles.types.timestamp.serialize_json(
            value["stopped_since"]
        )
    import capo_customer_profiles.types.event_stream_destination_details

    out["DestinationDetails"] = (
        capo_customer_profiles.types.event_stream_destination_details.serialize_json(
            value["destination_details"]
        )
    )
    if "tags" in value:
        import capo_customer_profiles.types.tag_map

        out["Tags"] = capo_customer_profiles.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> GetEventStreamResponse:
    out: GetEventStreamResponse = {}  # type: ignore[typeddict-item]
    if data.get("DomainName") is not None:
        out["domain_name"] = data["DomainName"]
    else:
        out["domain_name"] = ""
    if data.get("EventStreamArn") is not None:
        out["event_stream_arn"] = data["EventStreamArn"]
    else:
        out["event_stream_arn"] = ""
    if data.get("CreatedAt") is not None:
        import capo_customer_profiles.types.timestamp

        out["created_at"] = capo_customer_profiles.types.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("State") is not None:
        import capo_customer_profiles.types.event_stream_state

        out["state"] = capo_customer_profiles.types.event_stream_state.deserialize_json(
            data["State"]
        )
    else:
        import typing

        out["state"] = typing.cast(
            "capo_customer_profiles.types.event_stream_state.EventStreamState", ""
        )
    if data.get("StoppedSince") is not None:
        import capo_customer_profiles.types.timestamp

        out["stopped_since"] = capo_customer_profiles.types.timestamp.deserialize_json(
            data["StoppedSince"]
        )
    if data.get("DestinationDetails") is not None:
        import capo_customer_profiles.types.event_stream_destination_details

        out["destination_details"] = (
            capo_customer_profiles.types.event_stream_destination_details.deserialize_json(
                data["DestinationDetails"]
            )
        )
    else:
        raise DeserializationError(
            "GetEventStreamResponse.destination_details required"
        )
    if data.get("Tags") is not None:
        import capo_customer_profiles.types.tag_map

        out["tags"] = capo_customer_profiles.types.tag_map.deserialize_json(
            data["Tags"]
        )
    return out
