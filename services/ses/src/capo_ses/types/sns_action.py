"""Generated from Smithy shape ``com.amazonaws.ses#SNSAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ses._protocol.xml import Element
from capo_ses.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ses.types.amazon_resource_name
    import capo_ses.types.sns_action_encoding


class SNSAction(TypedDict, closed=True):
    topic_arn: "capo_ses.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Name (ARN) of the Amazon SNS topic to notify. You can find the ARN of a topic by using the <a href="https://docs.aws.amazon.com/sns/latest/api/API_ListTopics.html">ListTopics</a> operation in Amazon SNS.</p> <p>For more information about Amazon SNS topics, see the <a href="https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html">Amazon SNS Developer Guide</a>.</p>"""
    encoding: NotRequired["capo_ses.types.sns_action_encoding.SNSActionEncoding"]
    """<p>The encoding to use for the email within the Amazon SNS notification. UTF-8 is easier to use, but may not preserve all special characters when a message was encoded with a different encoding format. Base64 preserves all special characters. The default value is UTF-8.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SNSAction, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}TopicArn", str(value["topic_arn"])))
    if "encoding" in value:
        import capo_ses.types.sns_action_encoding

        capo_ses.types.sns_action_encoding.serialize_query(
            value["encoding"], pairs, f"{key_prefix}Encoding"
        )


def deserialize_query(el: Element) -> SNSAction:
    out: SNSAction = {}  # type: ignore[typeddict-item]
    child_topic_arn = el.find("TopicArn")
    if child_topic_arn is not None:
        out["topic_arn"] = str(child_topic_arn.text or "")
    else:
        raise DeserializationError("SNSAction.topic_arn required")
    child_encoding = el.find("Encoding")
    if child_encoding is not None:
        import capo_ses.types.sns_action_encoding

        out["encoding"] = capo_ses.types.sns_action_encoding.deserialize_query(
            child_encoding
        )
    return out
