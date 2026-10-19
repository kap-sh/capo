"""Generated from Smithy shape ``com.amazonaws.sesv2#TopicPreference``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.subscription_status
    import capo_sesv2.types.topic_name


class TopicPreference(TypedDict, closed=True):
    topic_name: "capo_sesv2.types.topic_name.TopicName"
    """<p>The name of the topic.</p>"""
    subscription_status: "capo_sesv2.types.subscription_status.SubscriptionStatus"
    """<p>The contact's subscription status to a topic which is either <code>OPT_IN</code> or <code>OPT_OUT</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TopicPreference) -> dict:
    out: dict = {}
    out["TopicName"] = value["topic_name"]
    import capo_sesv2.types.subscription_status

    out["SubscriptionStatus"] = capo_sesv2.types.subscription_status.serialize_json(
        value["subscription_status"]
    )
    return out


def deserialize_json(data: dict) -> TopicPreference:
    out: TopicPreference = {}  # type: ignore[typeddict-item]
    if data.get("TopicName") is not None:
        out["topic_name"] = data["TopicName"]
    else:
        out["topic_name"] = ""
    if data.get("SubscriptionStatus") is not None:
        import capo_sesv2.types.subscription_status

        out["subscription_status"] = (
            capo_sesv2.types.subscription_status.deserialize_json(
                data["SubscriptionStatus"]
            )
        )
    else:
        import typing

        out["subscription_status"] = typing.cast(
            "capo_sesv2.types.subscription_status.SubscriptionStatus", ""
        )
    return out
