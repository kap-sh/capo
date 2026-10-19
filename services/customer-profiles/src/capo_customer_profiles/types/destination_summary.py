"""Generated from Smithy shape ``com.amazonaws.customerprofiles#DestinationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.event_stream_destination_status
    import capo_customer_profiles.types.string1_to255
    import capo_customer_profiles.types.timestamp


class DestinationSummary(TypedDict, closed=True):
    uri: "capo_customer_profiles.types.string1_to255.string1To255"
    """<p>The StreamARN of the destination to deliver profile events to. For example, arn:aws:kinesis:region:account-id:stream/stream-name.</p>"""
    status: "capo_customer_profiles.types.event_stream_destination_status.EventStreamDestinationStatus"
    """<p>The status of enabling the Kinesis stream as a destination for export.</p>"""
    unhealthy_since: NotRequired["capo_customer_profiles.types.timestamp.timestamp"]
    """<p>The timestamp when the status last changed to <code>UNHEALHY</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DestinationSummary) -> dict:
    out: dict = {}
    out["Uri"] = value["uri"]
    import capo_customer_profiles.types.event_stream_destination_status

    out["Status"] = (
        capo_customer_profiles.types.event_stream_destination_status.serialize_json(
            value["status"]
        )
    )
    if "unhealthy_since" in value:
        import capo_customer_profiles.types.timestamp

        out["UnhealthySince"] = capo_customer_profiles.types.timestamp.serialize_json(
            value["unhealthy_since"]
        )
    return out


def deserialize_json(data: dict) -> DestinationSummary:
    out: DestinationSummary = {}  # type: ignore[typeddict-item]
    if data.get("Uri") is not None:
        out["uri"] = data["Uri"]
    else:
        out["uri"] = ""
    if data.get("Status") is not None:
        import capo_customer_profiles.types.event_stream_destination_status

        out["status"] = (
            capo_customer_profiles.types.event_stream_destination_status.deserialize_json(
                data["Status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_customer_profiles.types.event_stream_destination_status.EventStreamDestinationStatus",
            "",
        )
    if data.get("UnhealthySince") is not None:
        import capo_customer_profiles.types.timestamp

        out["unhealthy_since"] = (
            capo_customer_profiles.types.timestamp.deserialize_json(
                data["UnhealthySince"]
            )
        )
    return out
