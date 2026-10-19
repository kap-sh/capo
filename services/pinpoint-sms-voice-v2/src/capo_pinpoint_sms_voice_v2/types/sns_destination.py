"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#SnsDestination``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.sns_topic_arn


class SnsDestination(TypedDict, closed=True):
    topic_arn: "capo_pinpoint_sms_voice_v2.types.sns_topic_arn.SnsTopicArn"
    """<p>The Amazon Resource Name (ARN) of the Amazon SNS topic that you want to publish events to.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SnsDestination) -> dict:
    out: dict = {}
    out["TopicArn"] = value["topic_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> SnsDestination:
    out: SnsDestination = {}  # type: ignore[typeddict-item]
    if data.get("TopicArn") is not None:
        out["topic_arn"] = data["TopicArn"]
    else:
        out["topic_arn"] = ""
    return out
