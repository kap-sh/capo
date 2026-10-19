"""Generated from Smithy shape ``com.amazonaws.customerprofiles#EventStreamSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.destination_summary
    import capo_customer_profiles.types.event_stream_state
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.string1_to255
    import capo_customer_profiles.types.tag_map
    import capo_customer_profiles.types.timestamp


class EventStreamSummary(TypedDict, closed=True):
    domain_name: "capo_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    event_stream_name: "capo_customer_profiles.types.name.name"
    """<p>The name of the event stream.</p>"""
    event_stream_arn: "capo_customer_profiles.types.string1_to255.string1To255"
    """<p>A unique identifier for the event stream.</p>"""
    state: "capo_customer_profiles.types.event_stream_state.EventStreamState"
    """<p>The operational state of destination stream for export.</p>"""
    stopped_since: NotRequired["capo_customer_profiles.types.timestamp.timestamp"]
    """<p>The timestamp when the <code>State</code> changed to <code>STOPPED</code>.</p>"""
    destination_summary: NotRequired[
        "capo_customer_profiles.types.destination_summary.DestinationSummary"
    ]
    """<p>Summary information about the Kinesis data stream.</p>"""
    tags: NotRequired["capo_customer_profiles.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EventStreamSummary) -> dict:
    out: dict = {}
    out["DomainName"] = value["domain_name"]
    out["EventStreamName"] = value["event_stream_name"]
    out["EventStreamArn"] = value["event_stream_arn"]
    import capo_customer_profiles.types.event_stream_state

    out["State"] = capo_customer_profiles.types.event_stream_state.serialize_json(
        value["state"]
    )
    if "stopped_since" in value:
        import capo_customer_profiles.types.timestamp

        out["StoppedSince"] = capo_customer_profiles.types.timestamp.serialize_json(
            value["stopped_since"]
        )
    if "destination_summary" in value:
        import capo_customer_profiles.types.destination_summary

        out["DestinationSummary"] = (
            capo_customer_profiles.types.destination_summary.serialize_json(
                value["destination_summary"]
            )
        )
    if "tags" in value:
        import capo_customer_profiles.types.tag_map

        out["Tags"] = capo_customer_profiles.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> EventStreamSummary:
    out: EventStreamSummary = {}  # type: ignore[typeddict-item]
    if data.get("DomainName") is not None:
        out["domain_name"] = data["DomainName"]
    else:
        out["domain_name"] = ""
    if data.get("EventStreamName") is not None:
        out["event_stream_name"] = data["EventStreamName"]
    else:
        out["event_stream_name"] = ""
    if data.get("EventStreamArn") is not None:
        out["event_stream_arn"] = data["EventStreamArn"]
    else:
        out["event_stream_arn"] = ""
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
    if data.get("DestinationSummary") is not None:
        import capo_customer_profiles.types.destination_summary

        out["destination_summary"] = (
            capo_customer_profiles.types.destination_summary.deserialize_json(
                data["DestinationSummary"]
            )
        )
    if data.get("Tags") is not None:
        import capo_customer_profiles.types.tag_map

        out["tags"] = capo_customer_profiles.types.tag_map.deserialize_json(
            data["Tags"]
        )
    return out
