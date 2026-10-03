"""Generated from Smithy shape ``com.amazonaws.comprehend#TargetedSentimentEntity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.list_of_descriptive_mention_indices
    import capo_comprehend.types.list_of_mentions


class TargetedSentimentEntity(TypedDict, closed=True):
    descriptive_mention_index: NotRequired[
        "capo_comprehend.types.list_of_descriptive_mention_indices.ListOfDescriptiveMentionIndices"
    ]
    """<p>One or more index into the Mentions array that provides the best name for the entity group.</p>"""
    mentions: NotRequired["capo_comprehend.types.list_of_mentions.ListOfMentions"]
    """<p>An array of mentions of the entity in the document. The array represents a co-reference group. See <a href="https://docs.aws.amazon.com/comprehend/latest/dg/how-targeted-sentiment.html#how-targeted-sentiment-values"> Co-reference group</a> for an example. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetedSentimentEntity) -> dict:
    out: dict = {}
    if "descriptive_mention_index" in value:
        import capo_comprehend.types.list_of_descriptive_mention_indices

        out["DescriptiveMentionIndex"] = (
            capo_comprehend.types.list_of_descriptive_mention_indices.serialize_aws_json_1_1(
                value["descriptive_mention_index"]
            )
        )
    if "mentions" in value:
        import capo_comprehend.types.list_of_mentions

        out["Mentions"] = capo_comprehend.types.list_of_mentions.serialize_aws_json_1_1(
            value["mentions"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TargetedSentimentEntity:
    out: TargetedSentimentEntity = {}  # type: ignore[typeddict-item]
    if data.get("DescriptiveMentionIndex") is not None:
        import capo_comprehend.types.list_of_descriptive_mention_indices

        out["descriptive_mention_index"] = (
            capo_comprehend.types.list_of_descriptive_mention_indices.deserialize_aws_json_1_1(
                data["DescriptiveMentionIndex"]
            )
        )
    if data.get("Mentions") is not None:
        import capo_comprehend.types.list_of_mentions

        out["mentions"] = (
            capo_comprehend.types.list_of_mentions.deserialize_aws_json_1_1(
                data["Mentions"]
            )
        )
    return out
