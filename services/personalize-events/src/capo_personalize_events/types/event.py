"""Generated from Smithy shape ``com.amazonaws.personalizeevents#Event``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_personalize_events.errors import DeserializationError

if TYPE_CHECKING:
    import capo_personalize_events.types.date
    import capo_personalize_events.types.float_type
    import capo_personalize_events.types.impression
    import capo_personalize_events.types.item_id
    import capo_personalize_events.types.metric_attribution
    import capo_personalize_events.types.recommendation_id
    import capo_personalize_events.types.string_type
    import capo_personalize_events.types.synthesized_json_event_properties_json


class Event(TypedDict, closed=True):
    event_id: NotRequired["capo_personalize_events.types.string_type.StringType"]
    """<p>An ID associated with the event. If an event ID is not provided, Amazon Personalize generates a unique ID for the event. An event ID is not used as an input to the model. Amazon Personalize uses the event ID to distinguish unique events. Any subsequent events after the first with the same event ID are not used in model training.</p>"""
    event_type: "capo_personalize_events.types.string_type.StringType"
    """<p>The type of event, such as click or download. This property corresponds to the <code>EVENT_TYPE</code> field of your Item interactions dataset's schema and depends on the types of events you are tracking.</p>"""
    event_value: NotRequired["capo_personalize_events.types.float_type.FloatType"]
    """<p>The event value that corresponds to the <code>EVENT_VALUE</code> field of the Item interactions schema.</p>"""
    item_id: NotRequired["capo_personalize_events.types.item_id.ItemId"]
    """<p>The item ID key that corresponds to the <code>ITEM_ID</code> field of the Item interactions dataset's schema.</p>"""
    properties: NotRequired[
        "capo_personalize_events.types.synthesized_json_event_properties_json.SynthesizedJsonEventPropertiesJSON"
    ]
    """<p>A string map of event-specific data that you might choose to record. For example, if a user rates a movie on your site, other than movie ID (<code>itemId</code>) and rating (<code>eventValue</code>) , you might also send the number of movie ratings made by the user.</p> <p>Each item in the map consists of a key-value pair. For example,</p> <p> <code>{"numberOfRatings": "12"}</code> </p> <p>The keys use camel case names that match the fields in the Item interactions dataset's schema. In the above example, the <code>numberOfRatings</code> would match the 'NUMBER_OF_RATINGS' field defined in the Item interactions dataset's schema.</p> <p> The following can't be included as a keyword for properties (case insensitive). </p> <ul> <li> <p> userId </p> </li> <li> <p> sessionId </p> </li> <li> <p>eventType</p> </li> <li> <p>timestamp</p> </li> <li> <p>recommendationId</p> </li> <li> <p>impression</p> </li> </ul>"""
    sent_at: "capo_personalize_events.types.date.Date"
    """<p>The timestamp (in Unix time) on the client side when the event occurred.</p>"""
    recommendation_id: NotRequired[
        "capo_personalize_events.types.recommendation_id.RecommendationId"
    ]
    """<p>The ID of the list of recommendations that contains the item the user interacted with. Provide a <code>recommendationId</code> to have Amazon Personalize implicitly record the recommendations you show your user as impressions data. Or provide a <code>recommendationId</code> if you use a metric attribution to measure the impact of recommendations. </p> <p> For more information on recording impressions data, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/recording-events.html#putevents-including-impressions-data">Recording impressions data</a>. For more information on creating a metric attribution see <a href="https://docs.aws.amazon.com/personalize/latest/dg/measuring-recommendation-impact.html">Measuring impact of recommendations</a>. </p>"""
    impression: NotRequired["capo_personalize_events.types.impression.Impression"]
    """<p>A list of item IDs that represents the sequence of items you have shown the user. For example, <code>["itemId1", "itemId2", "itemId3"]</code>. Provide a list of items to manually record impressions data for an event. For more information on recording impressions data, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/recording-events.html#putevents-including-impressions-data">Recording impressions data</a>. </p>"""
    metric_attribution: NotRequired[
        "capo_personalize_events.types.metric_attribution.MetricAttribution"
    ]
    """<p>Contains information about the metric attribution associated with an event. For more information about metric attributions, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/measuring-recommendation-impact.html">Measuring impact of recommendations</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Event) -> dict:
    out: dict = {}
    if "event_id" in value:
        out["eventId"] = value["event_id"]
    out["eventType"] = value["event_type"]
    if "event_value" in value:
        out["eventValue"] = (
            "NaN"
            if value["event_value"] != value["event_value"]
            else "Infinity"
            if value["event_value"] == float("inf")
            else "-Infinity"
            if value["event_value"] == float("-inf")
            else value["event_value"]
        )
    if "item_id" in value:
        out["itemId"] = value["item_id"]
    if "properties" in value:
        out["properties"] = value["properties"]
    import capo_personalize_events.types.date

    out["sentAt"] = capo_personalize_events.types.date.serialize_json(value["sent_at"])
    if "recommendation_id" in value:
        out["recommendationId"] = value["recommendation_id"]
    if "impression" in value:
        import capo_personalize_events.types.impression

        out["impression"] = capo_personalize_events.types.impression.serialize_json(
            value["impression"]
        )
    if "metric_attribution" in value:
        import capo_personalize_events.types.metric_attribution

        out["metricAttribution"] = (
            capo_personalize_events.types.metric_attribution.serialize_json(
                value["metric_attribution"]
            )
        )
    return out


def deserialize_json(data: dict) -> Event:
    out: Event = {}  # type: ignore[typeddict-item]
    if data.get("eventId") is not None:
        out["event_id"] = data["eventId"]
    if data.get("eventType") is not None:
        out["event_type"] = data["eventType"]
    else:
        raise DeserializationError("Event.event_type required")
    if data.get("eventValue") is not None:
        out["event_value"] = float(data["eventValue"])
    if data.get("itemId") is not None:
        out["item_id"] = data["itemId"]
    if data.get("properties") is not None:
        out["properties"] = data["properties"]
    if data.get("sentAt") is not None:
        import capo_personalize_events.types.date

        out["sent_at"] = capo_personalize_events.types.date.deserialize_json(
            data["sentAt"]
        )
    else:
        raise DeserializationError("Event.sent_at required")
    if data.get("recommendationId") is not None:
        out["recommendation_id"] = data["recommendationId"]
    if data.get("impression") is not None:
        import capo_personalize_events.types.impression

        out["impression"] = capo_personalize_events.types.impression.deserialize_json(
            data["impression"]
        )
    if data.get("metricAttribution") is not None:
        import capo_personalize_events.types.metric_attribution

        out["metric_attribution"] = (
            capo_personalize_events.types.metric_attribution.deserialize_json(
                data["metricAttribution"]
            )
        )
    return out
