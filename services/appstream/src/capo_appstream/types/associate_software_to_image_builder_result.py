"""Generated from Smithy shape ``com.amazonaws.appstream#AssociateSoftwareToImageBuilderResult``."""

from typing_extensions import TypedDict


class AssociateSoftwareToImageBuilderResult(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociateSoftwareToImageBuilderResult) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociateSoftwareToImageBuilderResult:
    out: AssociateSoftwareToImageBuilderResult = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AssociateSoftwareToImageBuilderResult) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> AssociateSoftwareToImageBuilderResult:
    out: AssociateSoftwareToImageBuilderResult = {}  # type: ignore[typeddict-item]
    return out
