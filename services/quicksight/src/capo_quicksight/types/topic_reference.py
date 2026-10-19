"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicReference``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.topic_identifier


class TopicReference(TypedDict, closed=True):
    topic_placeholder: "capo_quicksight.types.topic_identifier.TopicIdentifier"
    """<p>Topic placeholder.</p>"""
    topic_arn: "capo_quicksight.types.arn.Arn"
    """<p>Topic Amazon Resource Name (ARN).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TopicReference) -> dict:
    out: dict = {}
    out["TopicPlaceholder"] = value["topic_placeholder"]
    out["TopicArn"] = value["topic_arn"]
    return out


def deserialize_json(data: dict) -> TopicReference:
    out: TopicReference = {}  # type: ignore[typeddict-item]
    if data.get("TopicPlaceholder") is not None:
        out["topic_placeholder"] = data["TopicPlaceholder"]
    else:
        out["topic_placeholder"] = ""
    if data.get("TopicArn") is not None:
        out["topic_arn"] = data["TopicArn"]
    else:
        out["topic_arn"] = ""
    return out
