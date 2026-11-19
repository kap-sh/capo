"""Generated from Smithy shape ``com.amazonaws.comprehend#DetectTargetedSentimentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.list_of_targeted_sentiment_entities


class DetectTargetedSentimentResponse(TypedDict, closed=True):
    entities: NotRequired[
        "capo_comprehend.types.list_of_targeted_sentiment_entities.ListOfTargetedSentimentEntities"
    ]
    """<p>Targeted sentiment analysis for each of the entities identified in the input text.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DetectTargetedSentimentResponse) -> dict:
    out: dict = {}
    if "entities" in value:
        import capo_comprehend.types.list_of_targeted_sentiment_entities

        out["Entities"] = (
            capo_comprehend.types.list_of_targeted_sentiment_entities.serialize_aws_json_1_1(
                value["entities"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DetectTargetedSentimentResponse:
    out: DetectTargetedSentimentResponse = {}  # type: ignore[typeddict-item]
    if data.get("Entities") is not None:
        import capo_comprehend.types.list_of_targeted_sentiment_entities

        out["entities"] = (
            capo_comprehend.types.list_of_targeted_sentiment_entities.deserialize_aws_json_1_1(
                data["Entities"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DetectTargetedSentimentResponse) -> dict:
    out: dict = {}
    if "entities" in value:
        import capo_comprehend.types.list_of_targeted_sentiment_entities

        out["Entities"] = (
            capo_comprehend.types.list_of_targeted_sentiment_entities.serialize_cbor(
                value["entities"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> DetectTargetedSentimentResponse:
    out: DetectTargetedSentimentResponse = {}  # type: ignore[typeddict-item]
    if data.get("Entities") is not None:
        import capo_comprehend.types.list_of_targeted_sentiment_entities

        out["entities"] = (
            capo_comprehend.types.list_of_targeted_sentiment_entities.deserialize_cbor(
                data["Entities"]
            )
        )
    return out
