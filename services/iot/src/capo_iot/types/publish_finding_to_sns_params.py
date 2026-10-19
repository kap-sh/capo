"""Generated from Smithy shape ``com.amazonaws.iot#PublishFindingToSnsParams``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot.types.sns_topic_arn


class PublishFindingToSnsParams(TypedDict, closed=True):
    topic_arn: "capo_iot.types.sns_topic_arn.SnsTopicArn"
    """<p>The ARN of the topic to which you want to publish the findings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PublishFindingToSnsParams) -> dict:
    out: dict = {}
    out["topicArn"] = value["topic_arn"]
    return out


def deserialize_json(data: dict) -> PublishFindingToSnsParams:
    out: PublishFindingToSnsParams = {}  # type: ignore[typeddict-item]
    if data.get("topicArn") is not None:
        out["topic_arn"] = data["topicArn"]
    else:
        out["topic_arn"] = ""
    return out
