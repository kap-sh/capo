"""Generated from Smithy shape ``com.amazonaws.pinpointemail#SnsDestination``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_pinpoint_email.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pinpoint_email.types.amazon_resource_name


class SnsDestination(TypedDict, closed=True):
    topic_arn: "capo_pinpoint_email.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Name (ARN) of the Amazon SNS topic that you want to publish email events to. For more information about Amazon SNS topics, see the <a href="https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html">Amazon SNS Developer Guide</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SnsDestination) -> dict:
    out: dict = {}
    out["TopicArn"] = value["topic_arn"]
    return out


def deserialize_json(data: dict) -> SnsDestination:
    out: SnsDestination = {}  # type: ignore[typeddict-item]
    if data.get("TopicArn") is not None:
        out["topic_arn"] = data["TopicArn"]
    else:
        raise DeserializationError("SnsDestination.topic_arn required")
    return out
