"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#AcceptAgreementApprovalInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.buyer_agreement_approval_approver_input


class AcceptAgreementApprovalInput(TypedDict, closed=True):
    buyer_agreement_approval_approver_input: NotRequired[
        "capo_marketplace_agreement.types.buyer_agreement_approval_approver_input.BuyerAgreementApprovalApproverInput"
    ]
    """<p>The approval decision for an agreement approval that the buyer's organization requires.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AcceptAgreementApprovalInput) -> dict:
    out: dict = {}
    if "buyer_agreement_approval_approver_input" in value:
        import capo_marketplace_agreement.types.buyer_agreement_approval_approver_input

        out["buyerAgreementApprovalApproverInput"] = (
            capo_marketplace_agreement.types.buyer_agreement_approval_approver_input.serialize_aws_json_1_0(
                value["buyer_agreement_approval_approver_input"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> AcceptAgreementApprovalInput:
    out: AcceptAgreementApprovalInput = {}  # type: ignore[typeddict-item]
    if data.get("buyerAgreementApprovalApproverInput") is not None:
        import capo_marketplace_agreement.types.buyer_agreement_approval_approver_input

        out["buyer_agreement_approval_approver_input"] = (
            capo_marketplace_agreement.types.buyer_agreement_approval_approver_input.deserialize_aws_json_1_0(
                data["buyerAgreementApprovalApproverInput"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AcceptAgreementApprovalInput) -> dict:
    out: dict = {}
    if "buyer_agreement_approval_approver_input" in value:
        import capo_marketplace_agreement.types.buyer_agreement_approval_approver_input

        out["buyerAgreementApprovalApproverInput"] = (
            capo_marketplace_agreement.types.buyer_agreement_approval_approver_input.serialize_cbor(
                value["buyer_agreement_approval_approver_input"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> AcceptAgreementApprovalInput:
    out: AcceptAgreementApprovalInput = {}  # type: ignore[typeddict-item]
    if data.get("buyerAgreementApprovalApproverInput") is not None:
        import capo_marketplace_agreement.types.buyer_agreement_approval_approver_input

        out["buyer_agreement_approval_approver_input"] = (
            capo_marketplace_agreement.types.buyer_agreement_approval_approver_input.deserialize_cbor(
                data["buyerAgreementApprovalApproverInput"]
            )
        )
    return out


def redact_sensitive(value: AcceptAgreementApprovalInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "buyer_agreement_approval_approver_input" in value:
        import capo_marketplace_agreement.types.buyer_agreement_approval_approver_input

        out["buyer_agreement_approval_approver_input"] = (
            capo_marketplace_agreement.types.buyer_agreement_approval_approver_input.redact_sensitive(
                value["buyer_agreement_approval_approver_input"]
            )
        )
    return out
