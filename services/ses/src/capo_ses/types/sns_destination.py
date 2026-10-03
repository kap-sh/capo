"""Generated from Smithy shape ``com.amazonaws.ses#SNSDestination``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ses._protocol.xml import Element
from capo_ses.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ses.types.amazon_resource_name


class SNSDestination(TypedDict, closed=True):
    topic_arn: "capo_ses.types.amazon_resource_name.AmazonResourceName"
    """<p>The ARN of the Amazon SNS topic for email sending events. You can find the ARN of a topic by using the <a href="https://docs.aws.amazon.com/sns/latest/api/API_ListTopics.html">ListTopics</a> Amazon SNS operation.</p> <p>For more information about Amazon SNS topics, see the <a href="https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html">Amazon SNS Developer Guide</a>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SNSDestination, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}TopicARN", str(value["topic_arn"])))


def deserialize_query(el: Element) -> SNSDestination:
    out: SNSDestination = {}  # type: ignore[typeddict-item]
    child_topic_arn = el.find("TopicARN")
    if child_topic_arn is not None:
        out["topic_arn"] = str(child_topic_arn.text or "")
    else:
        raise DeserializationError("SNSDestination.topic_arn required")
    return out
