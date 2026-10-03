"""Generated from Smithy shape ``com.amazonaws.personalizeevents#ActionInteraction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_personalize_events.errors import DeserializationError

if TYPE_CHECKING:
    import capo_personalize_events.types.action_id
    import capo_personalize_events.types.action_impression
    import capo_personalize_events.types.date
    import capo_personalize_events.types.recommendation_id
    import capo_personalize_events.types.string_type
    import capo_personalize_events.types.synthesized_json_action_interaction_properties
    import capo_personalize_events.types.user_id


class ActionInteraction(TypedDict, closed=True):
    action_id: "capo_personalize_events.types.action_id.ActionId"
    """<p>The ID of the action the user interacted with. This corresponds to the <code>ACTION_ID</code> field of the Action interaction schema.</p>"""
    user_id: NotRequired["capo_personalize_events.types.user_id.UserId"]
    """<p>The ID of the user who interacted with the action. This corresponds to the <code>USER_ID</code> field of the Action interaction schema.</p>"""
    session_id: "capo_personalize_events.types.string_type.StringType"
    """<p>The ID associated with the user's visit. Your application generates a unique <code>sessionId</code> when a user first visits your website or uses your application. </p>"""
    timestamp: "capo_personalize_events.types.date.Date"
    """<p>The timestamp for when the action interaction event occurred. Timestamps must be in Unix epoch time format, in seconds.</p>"""
    event_type: "capo_personalize_events.types.string_type.StringType"
    """<p>The type of action interaction event. You can specify <code>Viewed</code>, <code>Taken</code>, and <code>Not Taken</code> event types. For more information about action interaction event type data, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/action-interaction-event-type-data.html">Event type data</a>. </p>"""
    event_id: NotRequired["capo_personalize_events.types.string_type.StringType"]
    """<p>An ID associated with the event. If an event ID is not provided, Amazon Personalize generates a unique ID for the event. An event ID is not used as an input to the model. Amazon Personalize uses the event ID to distinguish unique events. Any subsequent events after the first with the same event ID are not used in model training.</p>"""
    recommendation_id: NotRequired[
        "capo_personalize_events.types.recommendation_id.RecommendationId"
    ]
    """<p>The ID of the list of recommendations that contains the action the user interacted with.</p>"""
    impression: NotRequired[
        "capo_personalize_events.types.action_impression.ActionImpression"
    ]
    """<p>A list of action IDs that represents the sequence of actions you have shown the user. For example, <code>["actionId1", "actionId2", "actionId3"]</code>. Amazon Personalize doesn't use impressions data from action interaction events. Instead, record multiple events for each action and use the <code>Viewed</code> event type. </p>"""
    properties: NotRequired[
        "capo_personalize_events.types.synthesized_json_action_interaction_properties.SynthesizedJsonActionInteractionProperties"
    ]
    """<p>A string map of event-specific data that you might choose to record. For example, if a user takes an action, other than the action ID, you might also send the number of actions taken by the user.</p> <p>Each item in the map consists of a key-value pair. For example,</p> <p> <code>{"numberOfActions": "12"}</code> </p> <p>The keys use camel case names that match the fields in the Action interactions schema. In the above example, the <code>numberOfActions</code> would match the 'NUMBER_OF_ACTIONS' field defined in the Action interactions schema.</p> <p> The following can't be included as a keyword for properties (case insensitive). </p> <ul> <li> <p> userId </p> </li> <li> <p> sessionId </p> </li> <li> <p>eventType</p> </li> <li> <p>timestamp</p> </li> <li> <p>recommendationId</p> </li> <li> <p>impression</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: ActionInteraction) -> dict:
    out: dict = {}
    out["actionId"] = value["action_id"]
    if "user_id" in value:
        out["userId"] = value["user_id"]
    out["sessionId"] = value["session_id"]
    import capo_personalize_events.types.date

    out["timestamp"] = capo_personalize_events.types.date.serialize_json(
        value["timestamp"]
    )
    out["eventType"] = value["event_type"]
    if "event_id" in value:
        out["eventId"] = value["event_id"]
    if "recommendation_id" in value:
        out["recommendationId"] = value["recommendation_id"]
    if "impression" in value:
        import capo_personalize_events.types.action_impression

        out["impression"] = (
            capo_personalize_events.types.action_impression.serialize_json(
                value["impression"]
            )
        )
    if "properties" in value:
        out["properties"] = value["properties"]
    return out


def deserialize_json(data: dict) -> ActionInteraction:
    out: ActionInteraction = {}  # type: ignore[typeddict-item]
    if data.get("actionId") is not None:
        out["action_id"] = data["actionId"]
    else:
        raise DeserializationError("ActionInteraction.action_id required")
    if data.get("userId") is not None:
        out["user_id"] = data["userId"]
    if data.get("sessionId") is not None:
        out["session_id"] = data["sessionId"]
    else:
        raise DeserializationError("ActionInteraction.session_id required")
    if data.get("timestamp") is not None:
        import capo_personalize_events.types.date

        out["timestamp"] = capo_personalize_events.types.date.deserialize_json(
            data["timestamp"]
        )
    else:
        raise DeserializationError("ActionInteraction.timestamp required")
    if data.get("eventType") is not None:
        out["event_type"] = data["eventType"]
    else:
        raise DeserializationError("ActionInteraction.event_type required")
    if data.get("eventId") is not None:
        out["event_id"] = data["eventId"]
    if data.get("recommendationId") is not None:
        out["recommendation_id"] = data["recommendationId"]
    if data.get("impression") is not None:
        import capo_personalize_events.types.action_impression

        out["impression"] = (
            capo_personalize_events.types.action_impression.deserialize_json(
                data["impression"]
            )
        )
    if data.get("properties") is not None:
        out["properties"] = data["properties"]
    return out
