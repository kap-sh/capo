"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#CancelAgreementOutput``."""

from typing_extensions import TypedDict


class CancelAgreementOutput(TypedDict, closed=True):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CancelAgreementOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> CancelAgreementOutput:
    out: CancelAgreementOutput = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CancelAgreementOutput) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> CancelAgreementOutput:
    out: CancelAgreementOutput = {}  # type: ignore[typeddict-item]
    return out
