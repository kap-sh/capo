"""Generated from Smithy shape ``com.amazonaws.comprehend#DetectSentimentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.sentiment_score
    import capo_comprehend.types.sentiment_type


class DetectSentimentResponse(TypedDict, closed=True):
    sentiment: NotRequired["capo_comprehend.types.sentiment_type.SentimentType"]
    """<p>The inferred sentiment that Amazon Comprehend has the highest level of confidence in.</p>"""
    sentiment_score: NotRequired["capo_comprehend.types.sentiment_score.SentimentScore"]
    """<p>An object that lists the sentiments, and their corresponding confidence levels.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DetectSentimentResponse) -> dict:
    out: dict = {}
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


def deserialize_aws_json_1_1(data: dict) -> DetectSentimentResponse:
    out: DetectSentimentResponse = {}  # type: ignore[typeddict-item]
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
def serialize_cbor(value: DetectSentimentResponse) -> dict:
    out: dict = {}
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


def deserialize_cbor(data: dict) -> DetectSentimentResponse:
    out: DetectSentimentResponse = {}  # type: ignore[typeddict-item]
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
