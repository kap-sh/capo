"""Generated from Smithy shape ``com.amazonaws.comprehend#TargetedSentimentMention``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.float
    import capo_comprehend.types.integer
    import capo_comprehend.types.mention_sentiment
    import capo_comprehend.types.string
    import capo_comprehend.types.targeted_sentiment_entity_type


class TargetedSentimentMention(TypedDict, closed=True):
    score: NotRequired["capo_comprehend.types.float.Float"]
    """<p>Model confidence that the entity is relevant. Value range is zero to one, where one is highest confidence.</p>"""
    group_score: NotRequired["capo_comprehend.types.float.Float"]
    """<p>The confidence that all the entities mentioned in the group relate to the same entity.</p>"""
    text: NotRequired["capo_comprehend.types.string.String"]
    """<p>The text in the document that identifies the entity.</p>"""
    type: NotRequired[
        "capo_comprehend.types.targeted_sentiment_entity_type.TargetedSentimentEntityType"
    ]
    """<p>The type of the entity. Amazon Comprehend supports a variety of <a href="https://docs.aws.amazon.com/comprehend/latest/dg/how-targeted-sentiment.html#how-targeted-sentiment-entities">entity types</a>.</p>"""
    mention_sentiment: NotRequired[
        "capo_comprehend.types.mention_sentiment.MentionSentiment"
    ]
    """<p>Contains the sentiment and sentiment score for the mention.</p>"""
    begin_offset: NotRequired["capo_comprehend.types.integer.Integer"]
    """<p>The offset into the document text where the mention begins.</p>"""
    end_offset: NotRequired["capo_comprehend.types.integer.Integer"]
    """<p>The offset into the document text where the mention ends.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetedSentimentMention) -> dict:
    out: dict = {}
    if "score" in value:
        out["Score"] = (
            "NaN"
            if value["score"] != value["score"]
            else "Infinity"
            if value["score"] == float("inf")
            else "-Infinity"
            if value["score"] == float("-inf")
            else value["score"]
        )
    if "group_score" in value:
        out["GroupScore"] = (
            "NaN"
            if value["group_score"] != value["group_score"]
            else "Infinity"
            if value["group_score"] == float("inf")
            else "-Infinity"
            if value["group_score"] == float("-inf")
            else value["group_score"]
        )
    if "text" in value:
        out["Text"] = value["text"]
    if "type" in value:
        import capo_comprehend.types.targeted_sentiment_entity_type

        out["Type"] = (
            capo_comprehend.types.targeted_sentiment_entity_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    if "mention_sentiment" in value:
        import capo_comprehend.types.mention_sentiment

        out["MentionSentiment"] = (
            capo_comprehend.types.mention_sentiment.serialize_aws_json_1_1(
                value["mention_sentiment"]
            )
        )
    if "begin_offset" in value:
        out["BeginOffset"] = value["begin_offset"]
    if "end_offset" in value:
        out["EndOffset"] = value["end_offset"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TargetedSentimentMention:
    out: TargetedSentimentMention = {}  # type: ignore[typeddict-item]
    if data.get("Score") is not None:
        out["score"] = float(data["Score"])
    if data.get("GroupScore") is not None:
        out["group_score"] = float(data["GroupScore"])
    if data.get("Text") is not None:
        out["text"] = data["Text"]
    if data.get("Type") is not None:
        import capo_comprehend.types.targeted_sentiment_entity_type

        out["type"] = (
            capo_comprehend.types.targeted_sentiment_entity_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    if data.get("MentionSentiment") is not None:
        import capo_comprehend.types.mention_sentiment

        out["mention_sentiment"] = (
            capo_comprehend.types.mention_sentiment.deserialize_aws_json_1_1(
                data["MentionSentiment"]
            )
        )
    if data.get("BeginOffset") is not None:
        out["begin_offset"] = data["BeginOffset"]
    if data.get("EndOffset") is not None:
        out["end_offset"] = data["EndOffset"]
    return out
