"""Generated from Smithy shape ``com.amazonaws.pinpoint#EventDimensions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.map_of_attribute_dimension
    import capo_pinpoint.types.map_of_metric_dimension
    import capo_pinpoint.types.set_dimension


class EventDimensions(TypedDict, closed=True):
    attributes: NotRequired[
        "capo_pinpoint.types.map_of_attribute_dimension.MapOfAttributeDimension"
    ]
    """<p>One or more custom attributes that your application reports to Amazon Pinpoint. You can use these attributes as selection criteria when you create an event filter.</p>"""
    event_type: NotRequired["capo_pinpoint.types.set_dimension.SetDimension"]
    """<p>The name of the event that causes the campaign to be sent or the journey activity to be performed. This can be a standard event that Amazon Pinpoint generates, such as _email.delivered. For campaigns, this can also be a custom event that's specific to your application. For information about standard events, see <a href="https://docs.aws.amazon.com/pinpoint/latest/developerguide/event-streams.html">Streaming Amazon Pinpoint Events</a> in the <i>Amazon Pinpoint Developer Guide</i>.</p>"""
    metrics: NotRequired[
        "capo_pinpoint.types.map_of_metric_dimension.MapOfMetricDimension"
    ]
    """<p>One or more custom metrics that your application reports to Amazon Pinpoint. You can use these metrics as selection criteria when you create an event filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EventDimensions) -> dict:
    out: dict = {}
    if "attributes" in value:
        import capo_pinpoint.types.map_of_attribute_dimension

        out["Attributes"] = (
            capo_pinpoint.types.map_of_attribute_dimension.serialize_json(
                value["attributes"]
            )
        )
    if "event_type" in value:
        import capo_pinpoint.types.set_dimension

        out["EventType"] = capo_pinpoint.types.set_dimension.serialize_json(
            value["event_type"]
        )
    if "metrics" in value:
        import capo_pinpoint.types.map_of_metric_dimension

        out["Metrics"] = capo_pinpoint.types.map_of_metric_dimension.serialize_json(
            value["metrics"]
        )
    return out


def deserialize_json(data: dict) -> EventDimensions:
    out: EventDimensions = {}  # type: ignore[typeddict-item]
    if data.get("Attributes") is not None:
        import capo_pinpoint.types.map_of_attribute_dimension

        out["attributes"] = (
            capo_pinpoint.types.map_of_attribute_dimension.deserialize_json(
                data["Attributes"]
            )
        )
    if data.get("EventType") is not None:
        import capo_pinpoint.types.set_dimension

        out["event_type"] = capo_pinpoint.types.set_dimension.deserialize_json(
            data["EventType"]
        )
    if data.get("Metrics") is not None:
        import capo_pinpoint.types.map_of_metric_dimension

        out["metrics"] = capo_pinpoint.types.map_of_metric_dimension.deserialize_json(
            data["Metrics"]
        )
    return out
