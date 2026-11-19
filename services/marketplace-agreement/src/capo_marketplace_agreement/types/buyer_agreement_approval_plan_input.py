"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#BuyerAgreementApprovalPlanInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.agreement_approval_note
    import capo_marketplace_agreement.types.agreement_approval_plan_reference


class BuyerAgreementApprovalPlanInput(TypedDict, closed=True):
    plan_reference: "capo_marketplace_agreement.types.agreement_approval_plan_reference.AgreementApprovalPlanReference"
    """<p>The identifier of the approval plan. Use <code>GetAgreementRequestApprovalPlans</code> to retrieve the approval plans of the agreement request.</p>"""
    requester_note: NotRequired[
        "capo_marketplace_agreement.types.agreement_approval_note.AgreementApprovalNote"
    ]
    """<p>An optional note for the approvers, such as the business reason for the purchase (1-1000 characters).</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BuyerAgreementApprovalPlanInput) -> dict:
    out: dict = {}
    out["planReference"] = value["plan_reference"]
    if "requester_note" in value:
        out["requesterNote"] = value["requester_note"]
    return out


def deserialize_aws_json_1_0(data: dict) -> BuyerAgreementApprovalPlanInput:
    out: BuyerAgreementApprovalPlanInput = {}  # type: ignore[typeddict-item]
    if data.get("planReference") is not None:
        out["plan_reference"] = data["planReference"]
    else:
        out["plan_reference"] = ""
    if data.get("requesterNote") is not None:
        out["requester_note"] = data["requesterNote"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: BuyerAgreementApprovalPlanInput) -> dict:
    out: dict = {}
    out["planReference"] = value["plan_reference"]
    if "requester_note" in value:
        out["requesterNote"] = value["requester_note"]
    return out


def deserialize_cbor(data: dict) -> BuyerAgreementApprovalPlanInput:
    out: BuyerAgreementApprovalPlanInput = {}  # type: ignore[typeddict-item]
    if data.get("planReference") is not None:
        out["plan_reference"] = data["planReference"]
    else:
        out["plan_reference"] = ""
    if data.get("requesterNote") is not None:
        out["requester_note"] = data["requesterNote"]
    return out


def redact_sensitive(value: BuyerAgreementApprovalPlanInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "requester_note" in value:
        out["requester_note"] = "*** Sensitive Data Redacted ***"
    return out
