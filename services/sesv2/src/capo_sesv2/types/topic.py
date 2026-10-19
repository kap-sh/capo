"""Generated from Smithy shape ``com.amazonaws.sesv2#Topic``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.description
    import capo_sesv2.types.display_name
    import capo_sesv2.types.subscription_status
    import capo_sesv2.types.topic_name


class Topic(TypedDict, closed=True):
    topic_name: "capo_sesv2.types.topic_name.TopicName"
    """<p>The name of the topic.</p>"""
    display_name: "capo_sesv2.types.display_name.DisplayName"
    """<p>The name of the topic the contact will see.</p>"""
    description: NotRequired["capo_sesv2.types.description.Description"]
    """<p>A description of what the topic is about, which the contact will see.</p>"""
    default_subscription_status: (
        "capo_sesv2.types.subscription_status.SubscriptionStatus"
    )
    """<p>The default subscription status to be applied to a contact if the contact has not noted their preference for subscribing to a topic.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Topic) -> dict:
    out: dict = {}
    out["TopicName"] = value["topic_name"]
    out["DisplayName"] = value["display_name"]
    if "description" in value:
        out["Description"] = value["description"]
    import capo_sesv2.types.subscription_status

    out["DefaultSubscriptionStatus"] = (
        capo_sesv2.types.subscription_status.serialize_json(
            value["default_subscription_status"]
        )
    )
    return out


def deserialize_json(data: dict) -> Topic:
    out: Topic = {}  # type: ignore[typeddict-item]
    if data.get("TopicName") is not None:
        out["topic_name"] = data["TopicName"]
    else:
        out["topic_name"] = ""
    if data.get("DisplayName") is not None:
        out["display_name"] = data["DisplayName"]
    else:
        out["display_name"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("DefaultSubscriptionStatus") is not None:
        import capo_sesv2.types.subscription_status

        out["default_subscription_status"] = (
            capo_sesv2.types.subscription_status.deserialize_json(
                data["DefaultSubscriptionStatus"]
            )
        )
    else:
        import typing

        out["default_subscription_status"] = typing.cast(
            "capo_sesv2.types.subscription_status.SubscriptionStatus", ""
        )
    return out
