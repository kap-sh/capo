"""Generated from Smithy shape ``com.amazonaws.comprehend#ListOfDetectSentimentResult``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_comprehend.types.batch_detect_sentiment_item_result

ListOfDetectSentimentResult: TypeAlias = list[
    "capo_comprehend.types.batch_detect_sentiment_item_result.BatchDetectSentimentItemResult"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListOfDetectSentimentResult) -> list:
    import capo_comprehend.types.batch_detect_sentiment_item_result

    out: list = []
    for item in value:
        out.append(
            capo_comprehend.types.batch_detect_sentiment_item_result.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ListOfDetectSentimentResult:
    import capo_comprehend.types.batch_detect_sentiment_item_result

    out: ListOfDetectSentimentResult = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_comprehend.types.batch_detect_sentiment_item_result.deserialize_aws_json_1_1(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListOfDetectSentimentResult) -> list:
    import capo_comprehend.types.batch_detect_sentiment_item_result

    out: list = []
    for item in value:
        out.append(
            capo_comprehend.types.batch_detect_sentiment_item_result.serialize_cbor(
                item
            )
        )
    return out


def deserialize_cbor(data: list) -> ListOfDetectSentimentResult:
    import capo_comprehend.types.batch_detect_sentiment_item_result

    out: ListOfDetectSentimentResult = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_comprehend.types.batch_detect_sentiment_item_result.deserialize_cbor(
                item
            )
        )
    return out
