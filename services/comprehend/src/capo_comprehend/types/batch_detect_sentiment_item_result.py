"""Generated from Smithy shape ``com.amazonaws.comprehend#BatchDetectSentimentItemResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.integer
    import capo_comprehend.types.sentiment_score
    import capo_comprehend.types.sentiment_type


class BatchDetectSentimentItemResult(TypedDict, closed=True):
    index: NotRequired["capo_comprehend.types.integer.Integer"]
    """<p>The zero-based index of the document in the input list.</p>"""
    sentiment: NotRequired["capo_comprehend.types.sentiment_type.SentimentType"]
    """<p>The sentiment detected in the document.</p>"""
    sentiment_score: NotRequired["capo_comprehend.types.sentiment_score.SentimentScore"]
    """<p>The level of confidence that Amazon Comprehend has in the accuracy of its sentiment detection.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchDetectSentimentItemResult) -> dict:
    out: dict = {}
    if "index" in value:
        out["Index"] = value["index"]
    if "sentiment" in value:
        import capo_comprehend.types.sentiment_type

        out["Sentiment"] = capo_comprehend.types.sentiment_type.serialize_aws_json_1_1(
            value["sentiment"]
        )
    if "sentiment_score" in value:
        import capo_comprehend.types.sentiment_score

        out["SentimentScore"] = (
            capo_comprehend.types.sentiment_score.serialize_aws_json_1_1(
                value["sentiment_score"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchDetectSentimentItemResult:
    out: BatchDetectSentimentItemResult = {}  # type: ignore[typeddict-item]
    if data.get("Index") is not None:
        out["index"] = data["Index"]
    if data.get("Sentiment") is not None:
        import capo_comprehend.types.sentiment_type

        out["sentiment"] = (
            capo_comprehend.types.sentiment_type.deserialize_aws_json_1_1(
                data["Sentiment"]
            )
        )
    if data.get("SentimentScore") is not None:
        import capo_comprehend.types.sentiment_score

        out["sentiment_score"] = (
            capo_comprehend.types.sentiment_score.deserialize_aws_json_1_1(
                data["SentimentScore"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: BatchDetectSentimentItemResult) -> dict:
    out: dict = {}
    if "index" in value:
        out["Index"] = value["index"]
    if "sentiment" in value:
        import capo_comprehend.types.sentiment_type

        out["Sentiment"] = capo_comprehend.types.sentiment_type.serialize_cbor(
            value["sentiment"]
        )
    if "sentiment_score" in value:
        import capo_comprehend.types.sentiment_score

        out["SentimentScore"] = capo_comprehend.types.sentiment_score.serialize_cbor(
            value["sentiment_score"]
        )
    return out


def deserialize_cbor(data: dict) -> BatchDetectSentimentItemResult:
    out: BatchDetectSentimentItemResult = {}  # type: ignore[typeddict-item]
    if data.get("Index") is not None:
        out["index"] = data["Index"]
    if data.get("Sentiment") is not None:
        import capo_comprehend.types.sentiment_type

        out["sentiment"] = capo_comprehend.types.sentiment_type.deserialize_cbor(
            data["Sentiment"]
        )
    if data.get("SentimentScore") is not None:
        import capo_comprehend.types.sentiment_score

        out["sentiment_score"] = capo_comprehend.types.sentiment_score.deserialize_cbor(
            data["SentimentScore"]
        )
    return out
