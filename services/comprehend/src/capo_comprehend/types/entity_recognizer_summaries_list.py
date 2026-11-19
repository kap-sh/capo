"""Generated from Smithy shape ``com.amazonaws.comprehend#EntityRecognizerSummariesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_comprehend.types.entity_recognizer_summary

EntityRecognizerSummariesList: TypeAlias = list[
    "capo_comprehend.types.entity_recognizer_summary.EntityRecognizerSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntityRecognizerSummariesList) -> list:
    import capo_comprehend.types.entity_recognizer_summary

    out: list = []
    for item in value:
        out.append(
            capo_comprehend.types.entity_recognizer_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> EntityRecognizerSummariesList:
    import capo_comprehend.types.entity_recognizer_summary

    out: EntityRecognizerSummariesList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_comprehend.types.entity_recognizer_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EntityRecognizerSummariesList) -> list:
    import capo_comprehend.types.entity_recognizer_summary

    out: list = []
    for item in value:
        out.append(capo_comprehend.types.entity_recognizer_summary.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> EntityRecognizerSummariesList:
    import capo_comprehend.types.entity_recognizer_summary

    out: EntityRecognizerSummariesList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_comprehend.types.entity_recognizer_summary.deserialize_cbor(item)
        )
    return out
