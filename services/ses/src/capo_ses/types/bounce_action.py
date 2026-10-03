"""Generated from Smithy shape ``com.amazonaws.ses#BounceAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ses._protocol.xml import Element
from capo_ses.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ses.types.address
    import capo_ses.types.amazon_resource_name
    import capo_ses.types.bounce_message
    import capo_ses.types.bounce_smtp_reply_code
    import capo_ses.types.bounce_status_code


class BounceAction(TypedDict, closed=True):
    topic_arn: NotRequired["capo_ses.types.amazon_resource_name.AmazonResourceName"]
    """<p>The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the bounce action is taken. You can find the ARN of a topic by using the <a href="https://docs.aws.amazon.com/sns/latest/api/API_ListTopics.html">ListTopics</a> operation in Amazon SNS.</p> <p>For more information about Amazon SNS topics, see the <a href="https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html">Amazon SNS Developer Guide</a>.</p>"""
    smtp_reply_code: "capo_ses.types.bounce_smtp_reply_code.BounceSmtpReplyCode"
    """<p>The SMTP reply code, as defined by <a href="https://tools.ietf.org/html/rfc5321">RFC 5321</a>.</p>"""
    status_code: NotRequired["capo_ses.types.bounce_status_code.BounceStatusCode"]
    """<p>The SMTP enhanced status code, as defined by <a href="https://tools.ietf.org/html/rfc3463">RFC 3463</a>.</p>"""
    message: "capo_ses.types.bounce_message.BounceMessage"
    """<p>Human-readable text to include in the bounce message.</p>"""
    sender: "capo_ses.types.address.Address"
    """<p>The email address of the sender of the bounced email. This is the address from which the bounce message is sent.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: BounceAction, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "topic_arn" in value:
        pairs.append((f"{key_prefix}TopicArn", str(value["topic_arn"])))
    pairs.append((f"{key_prefix}SmtpReplyCode", str(value["smtp_reply_code"])))
    if "status_code" in value:
        pairs.append((f"{key_prefix}StatusCode", str(value["status_code"])))
    pairs.append((f"{key_prefix}Message", str(value["message"])))
    pairs.append((f"{key_prefix}Sender", str(value["sender"])))


def deserialize_query(el: Element) -> BounceAction:
    out: BounceAction = {}  # type: ignore[typeddict-item]
    child_topic_arn = el.find("TopicArn")
    if child_topic_arn is not None:
        out["topic_arn"] = str(child_topic_arn.text or "")
    child_smtp_reply_code = el.find("SmtpReplyCode")
    if child_smtp_reply_code is not None:
        out["smtp_reply_code"] = str(child_smtp_reply_code.text or "")
    else:
        raise DeserializationError("BounceAction.smtp_reply_code required")
    child_status_code = el.find("StatusCode")
    if child_status_code is not None:
        out["status_code"] = str(child_status_code.text or "")
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    else:
        raise DeserializationError("BounceAction.message required")
    child_sender = el.find("Sender")
    if child_sender is not None:
        out["sender"] = str(child_sender.text or "")
    else:
        raise DeserializationError("BounceAction.sender required")
    return out
