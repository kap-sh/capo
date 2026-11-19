"""Generated from Smithy shape ``com.amazonaws.textract#ContentClassifiers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_textract.types.content_classifier

ContentClassifiers: TypeAlias = list[
    "capo_textract.types.content_classifier.ContentClassifier"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContentClassifiers) -> list:
    import capo_textract.types.content_classifier

    out: list = []
    for item in value:
        out.append(capo_textract.types.content_classifier.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ContentClassifiers:
    import capo_textract.types.content_classifier

    out: ContentClassifiers = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_textract.types.content_classifier.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ContentClassifiers) -> list:
    import capo_textract.types.content_classifier

    out: list = []
    for item in value:
        out.append(capo_textract.types.content_classifier.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ContentClassifiers:
    import capo_textract.types.content_classifier

    out: ContentClassifiers = []
    for item in data:
        if item is None:
            continue
        out.append(capo_textract.types.content_classifier.deserialize_cbor(item))
    return out
