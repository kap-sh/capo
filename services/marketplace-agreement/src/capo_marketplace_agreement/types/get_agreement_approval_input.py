"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#GetAgreementApprovalInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.agreement_approval_id


class GetAgreementApprovalInput(TypedDict, closed=True):
    agreement_approval_id: (
        "capo_marketplace_agreement.types.agreement_approval_id.AgreementApprovalId"
    )
    """<p>The unique identifier of the agreement approval to retrieve.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetAgreementApprovalInput) -> dict:
    out: dict = {}
    out["agreementApprovalId"] = value["agreement_approval_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetAgreementApprovalInput:
    out: GetAgreementApprovalInput = {}  # type: ignore[typeddict-item]
    if data.get("agreementApprovalId") is not None:
        out["agreement_approval_id"] = data["agreementApprovalId"]
    else:
        out["agreement_approval_id"] = ""
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetAgreementApprovalInput) -> dict:
    out: dict = {}
    out["agreementApprovalId"] = value["agreement_approval_id"]
    return out


def deserialize_cbor(data: dict) -> GetAgreementApprovalInput:
    out: GetAgreementApprovalInput = {}  # type: ignore[typeddict-item]
    if data.get("agreementApprovalId") is not None:
        out["agreement_approval_id"] = data["agreementApprovalId"]
    else:
        out["agreement_approval_id"] = ""
    return out
