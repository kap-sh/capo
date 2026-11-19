"""Generated from Smithy shape ``com.amazonaws.codebuild#ListCuratedEnvironmentImagesInput``."""

from typing_extensions import TypedDict


class ListCuratedEnvironmentImagesInput(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListCuratedEnvironmentImagesInput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> ListCuratedEnvironmentImagesInput:
    out: ListCuratedEnvironmentImagesInput = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListCuratedEnvironmentImagesInput) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> ListCuratedEnvironmentImagesInput:
    out: ListCuratedEnvironmentImagesInput = {}  # type: ignore[typeddict-item]
    return out
