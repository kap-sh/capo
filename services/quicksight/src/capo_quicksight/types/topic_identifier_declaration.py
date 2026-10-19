"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicIdentifierDeclaration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.topic_identifier


class TopicIdentifierDeclaration(TypedDict, closed=True):
    identifier: "capo_quicksight.types.topic_identifier.TopicIdentifier"
    """<p>The identifier of the topic, typically the topic's name.</p>"""
    topic_arn: "capo_quicksight.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the topic.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TopicIdentifierDeclaration) -> dict:
    out: dict = {}
    out["Identifier"] = value["identifier"]
    out["TopicArn"] = value["topic_arn"]
    return out


def deserialize_json(data: dict) -> TopicIdentifierDeclaration:
    out: TopicIdentifierDeclaration = {}  # type: ignore[typeddict-item]
    if data.get("Identifier") is not None:
        out["identifier"] = data["Identifier"]
    else:
        out["identifier"] = ""
    if data.get("TopicArn") is not None:
        out["topic_arn"] = data["TopicArn"]
    else:
        out["topic_arn"] = ""
    return out
