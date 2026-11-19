"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#AcceptAgreementApprovalOutput``."""

from typing_extensions import TypedDict


class AcceptAgreementApprovalOutput(TypedDict, closed=True):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AcceptAgreementApprovalOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> AcceptAgreementApprovalOutput:
    out: AcceptAgreementApprovalOutput = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AcceptAgreementApprovalOutput) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> AcceptAgreementApprovalOutput:
    out: AcceptAgreementApprovalOutput = {}  # type: ignore[typeddict-item]
    return out
