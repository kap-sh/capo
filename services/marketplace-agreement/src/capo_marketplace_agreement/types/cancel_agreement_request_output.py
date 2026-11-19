"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#CancelAgreementRequestOutput``."""

from typing_extensions import TypedDict


class CancelAgreementRequestOutput(TypedDict, closed=True):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CancelAgreementRequestOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> CancelAgreementRequestOutput:
    out: CancelAgreementRequestOutput = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CancelAgreementRequestOutput) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> CancelAgreementRequestOutput:
    out: CancelAgreementRequestOutput = {}  # type: ignore[typeddict-item]
    return out
