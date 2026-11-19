"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#RejectAgreementApprovalOutput``."""

from typing_extensions import TypedDict


class RejectAgreementApprovalOutput(TypedDict, closed=True):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RejectAgreementApprovalOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> RejectAgreementApprovalOutput:
    out: RejectAgreementApprovalOutput = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RejectAgreementApprovalOutput) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> RejectAgreementApprovalOutput:
    out: RejectAgreementApprovalOutput = {}  # type: ignore[typeddict-item]
    return out
