"""Generated from Smithy shape ``com.amazonaws.sns#GetTopicAttributesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_sns._protocol.xml import Element

if TYPE_CHECKING:
    import capo_sns.types.topic_arn


class GetTopicAttributesInput(TypedDict, closed=True):
    topic_arn: "capo_sns.types.topic_arn.topicARN"
    """<p>The ARN of the topic whose properties you want to get.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetTopicAttributesInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}TopicArn", str(value["topic_arn"])))


def deserialize_query(el: Element) -> GetTopicAttributesInput:
    out: GetTopicAttributesInput = {}  # type: ignore[typeddict-item]
    child_topic_arn = el.find("TopicArn")
    if child_topic_arn is not None:
        out["topic_arn"] = str(child_topic_arn.text or "")
    else:
        out["topic_arn"] = ""
    return out
