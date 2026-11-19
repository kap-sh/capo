"""Generated from Smithy shape ``com.amazonaws.comprehend#ListOfTargetedSentimentEntities``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_comprehend.types.targeted_sentiment_entity

ListOfTargetedSentimentEntities: TypeAlias = list[
    "capo_comprehend.types.targeted_sentiment_entity.TargetedSentimentEntity"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListOfTargetedSentimentEntities) -> list:
    import capo_comprehend.types.targeted_sentiment_entity

    out: list = []
    for item in value:
        out.append(
            capo_comprehend.types.targeted_sentiment_entity.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ListOfTargetedSentimentEntities:
    import capo_comprehend.types.targeted_sentiment_entity

    out: ListOfTargetedSentimentEntities = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_comprehend.types.targeted_sentiment_entity.deserialize_aws_json_1_1(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListOfTargetedSentimentEntities) -> list:
    import capo_comprehend.types.targeted_sentiment_entity

    out: list = []
    for item in value:
        out.append(capo_comprehend.types.targeted_sentiment_entity.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ListOfTargetedSentimentEntities:
    import capo_comprehend.types.targeted_sentiment_entity

    out: ListOfTargetedSentimentEntities = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_comprehend.types.targeted_sentiment_entity.deserialize_cbor(item)
        )
    return out
