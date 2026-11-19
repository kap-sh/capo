"""Generated from Smithy shape ``com.amazonaws.comprehend#BatchDetectTargetedSentimentItemResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.integer
    import capo_comprehend.types.list_of_targeted_sentiment_entities


class BatchDetectTargetedSentimentItemResult(TypedDict, closed=True):
    index: NotRequired["capo_comprehend.types.integer.Integer"]
    """<p>The zero-based index of this result in the input list.</p>"""
    entities: NotRequired[
        "capo_comprehend.types.list_of_targeted_sentiment_entities.ListOfTargetedSentimentEntities"
    ]
    """<p>An array of targeted sentiment entities.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchDetectTargetedSentimentItemResult) -> dict:
    out: dict = {}
    if "index" in value:
        out["Index"] = value["index"]
    if "entities" in value:
        import capo_comprehend.types.list_of_targeted_sentiment_entities

        out["Entities"] = (
            capo_comprehend.types.list_of_targeted_sentiment_entities.serialize_aws_json_1_1(
                value["entities"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchDetectTargetedSentimentItemResult:
    out: BatchDetectTargetedSentimentItemResult = {}  # type: ignore[typeddict-item]
    if data.get("Index") is not None:
        out["index"] = data["Index"]
    if data.get("Entities") is not None:
        import capo_comprehend.types.list_of_targeted_sentiment_entities

        out["entities"] = (
            capo_comprehend.types.list_of_targeted_sentiment_entities.deserialize_aws_json_1_1(
                data["Entities"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: BatchDetectTargetedSentimentItemResult) -> dict:
    out: dict = {}
    if "index" in value:
        out["Index"] = value["index"]
    if "entities" in value:
        import capo_comprehend.types.list_of_targeted_sentiment_entities

        out["Entities"] = (
            capo_comprehend.types.list_of_targeted_sentiment_entities.serialize_cbor(
                value["entities"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> BatchDetectTargetedSentimentItemResult:
    out: BatchDetectTargetedSentimentItemResult = {}  # type: ignore[typeddict-item]
    if data.get("Index") is not None:
        out["index"] = data["Index"]
    if data.get("Entities") is not None:
        import capo_comprehend.types.list_of_targeted_sentiment_entities

        out["entities"] = (
            capo_comprehend.types.list_of_targeted_sentiment_entities.deserialize_cbor(
                data["Entities"]
            )
        )
    return out
