"""Generated from Smithy shape ``com.amazonaws.textract#ContentClassifier``."""

from typing import Literal, TypeAlias, cast

ContentClassifier: TypeAlias = Literal[
    "FreeOfPersonallyIdentifiableInformation",
    "FreeOfAdultContent",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContentClassifier) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ContentClassifier:
    return cast(ContentClassifier, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ContentClassifier) -> str:
    return value


def deserialize_cbor(data: str) -> ContentClassifier:
    return cast(ContentClassifier, data)
