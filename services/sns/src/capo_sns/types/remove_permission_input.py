"""Generated from Smithy shape ``com.amazonaws.sns#RemovePermissionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_sns._protocol.xml import Element

if TYPE_CHECKING:
    import capo_sns.types.label
    import capo_sns.types.topic_arn


class RemovePermissionInput(TypedDict, closed=True):
    topic_arn: "capo_sns.types.topic_arn.topicARN"
    """<p>The ARN of the topic whose access control policy you wish to modify.</p>"""
    label: "capo_sns.types.label.label"
    """<p>The unique label of the statement you want to remove.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RemovePermissionInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}TopicArn", str(value["topic_arn"])))
    pairs.append((f"{key_prefix}Label", str(value["label"])))


def deserialize_query(el: Element) -> RemovePermissionInput:
    out: RemovePermissionInput = {}  # type: ignore[typeddict-item]
    child_topic_arn = el.find("TopicArn")
    if child_topic_arn is not None:
        out["topic_arn"] = str(child_topic_arn.text or "")
    else:
        out["topic_arn"] = ""
    child_label = el.find("Label")
    if child_label is not None:
        out["label"] = str(child_label.text or "")
    else:
        out["label"] = ""
    return out
