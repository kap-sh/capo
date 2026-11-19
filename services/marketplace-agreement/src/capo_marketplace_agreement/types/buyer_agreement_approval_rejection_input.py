"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#BuyerAgreementApprovalRejectionInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.agreement_approval_id
    import capo_marketplace_agreement.types.agreement_approval_note
    import capo_marketplace_agreement.types.approver_outcome_id


class BuyerAgreementApprovalRejectionInput(TypedDict, closed=True):
    agreement_approval_id: (
        "capo_marketplace_agreement.types.agreement_approval_id.AgreementApprovalId"
    )
    """<p>The unique identifier of the agreement approval to reject.</p>"""
    note: (
        "capo_marketplace_agreement.types.agreement_approval_note.AgreementApprovalNote"
    )
    """<p>The reason for the rejection.</p>"""
    approver_outcome_id_to_override: NotRequired[
        "capo_marketplace_agreement.types.approver_outcome_id.ApproverOutcomeId"
    ]
    """<p>The <code>approverOutcomeId</code> of the approver to decide on behalf of. You must be the management account or a delegated administrator of your AWS organization to set this field. Use <code>GetAgreementApproval</code> to retrieve the <code>approverOutcomeId</code> of each approver.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BuyerAgreementApprovalRejectionInput) -> dict:
    out: dict = {}
    out["agreementApprovalId"] = value["agreement_approval_id"]
    out["note"] = value["note"]
    if "approver_outcome_id_to_override" in value:
        out["approverOutcomeIdToOverride"] = value["approver_outcome_id_to_override"]
    return out


def deserialize_aws_json_1_0(data: dict) -> BuyerAgreementApprovalRejectionInput:
    out: BuyerAgreementApprovalRejectionInput = {}  # type: ignore[typeddict-item]
    if data.get("agreementApprovalId") is not None:
        out["agreement_approval_id"] = data["agreementApprovalId"]
    else:
        out["agreement_approval_id"] = ""
    if data.get("note") is not None:
        out["note"] = data["note"]
    else:
        out["note"] = ""
    if data.get("approverOutcomeIdToOverride") is not None:
        out["approver_outcome_id_to_override"] = data["approverOutcomeIdToOverride"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: BuyerAgreementApprovalRejectionInput) -> dict:
    out: dict = {}
    out["agreementApprovalId"] = value["agreement_approval_id"]
    out["note"] = value["note"]
    if "approver_outcome_id_to_override" in value:
        out["approverOutcomeIdToOverride"] = value["approver_outcome_id_to_override"]
    return out


def deserialize_cbor(data: dict) -> BuyerAgreementApprovalRejectionInput:
    out: BuyerAgreementApprovalRejectionInput = {}  # type: ignore[typeddict-item]
    if data.get("agreementApprovalId") is not None:
        out["agreement_approval_id"] = data["agreementApprovalId"]
    else:
        out["agreement_approval_id"] = ""
    if data.get("note") is not None:
        out["note"] = data["note"]
    else:
        out["note"] = ""
    if data.get("approverOutcomeIdToOverride") is not None:
        out["approver_outcome_id_to_override"] = data["approverOutcomeIdToOverride"]
    return out


def redact_sensitive(value: BuyerAgreementApprovalRejectionInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "note" in value:
        out["note"] = "*** Sensitive Data Redacted ***"
    return out
