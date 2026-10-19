"""Generated from Smithy shape ``com.amazonaws.sns#ListSubscriptionsByTopicInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sns._protocol.xml import Element

if TYPE_CHECKING:
    import capo_sns.types.next_token
    import capo_sns.types.topic_arn


class ListSubscriptionsByTopicInput(TypedDict, closed=True):
    topic_arn: "capo_sns.types.topic_arn.topicARN"
    """<p>The ARN of the topic for which you wish to find subscriptions.</p>"""
    next_token: NotRequired["capo_sns.types.next_token.nextToken"]
    """<p>Token returned by the previous <code>ListSubscriptionsByTopic</code> request.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListSubscriptionsByTopicInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}TopicArn", str(value["topic_arn"])))
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> ListSubscriptionsByTopicInput:
    out: ListSubscriptionsByTopicInput = {}  # type: ignore[typeddict-item]
    child_topic_arn = el.find("TopicArn")
    if child_topic_arn is not None:
        out["topic_arn"] = str(child_topic_arn.text or "")
    else:
        out["topic_arn"] = ""
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
