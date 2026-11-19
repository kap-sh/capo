"""Generated from Smithy shape ``com.amazonaws.appstream#DisassociateSoftwareFromImageBuilderResult``."""

from typing_extensions import TypedDict


class DisassociateSoftwareFromImageBuilderResult(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisassociateSoftwareFromImageBuilderResult) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DisassociateSoftwareFromImageBuilderResult:
    out: DisassociateSoftwareFromImageBuilderResult = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DisassociateSoftwareFromImageBuilderResult) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DisassociateSoftwareFromImageBuilderResult:
    out: DisassociateSoftwareFromImageBuilderResult = {}  # type: ignore[typeddict-item]
    return out
