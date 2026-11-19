"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#RejectAgreementApprovalInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.buyer_agreement_approval_rejection_input


class RejectAgreementApprovalInput(TypedDict, closed=True):
    buyer_agreement_approval_rejection_input: NotRequired[
        "capo_marketplace_agreement.types.buyer_agreement_approval_rejection_input.BuyerAgreementApprovalRejectionInput"
    ]
    """<p>The rejection decision for an agreement approval that the buyer's organization requires.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RejectAgreementApprovalInput) -> dict:
    out: dict = {}
    if "buyer_agreement_approval_rejection_input" in value:
        import capo_marketplace_agreement.types.buyer_agreement_approval_rejection_input

        out["buyerAgreementApprovalRejectionInput"] = (
            capo_marketplace_agreement.types.buyer_agreement_approval_rejection_input.serialize_aws_json_1_0(
                value["buyer_agreement_approval_rejection_input"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> RejectAgreementApprovalInput:
    out: RejectAgreementApprovalInput = {}  # type: ignore[typeddict-item]
    if data.get("buyerAgreementApprovalRejectionInput") is not None:
        import capo_marketplace_agreement.types.buyer_agreement_approval_rejection_input

        out["buyer_agreement_approval_rejection_input"] = (
            capo_marketplace_agreement.types.buyer_agreement_approval_rejection_input.deserialize_aws_json_1_0(
                data["buyerAgreementApprovalRejectionInput"]
            )
        )
    return out


def redact_sensitive(value: RejectAgreementApprovalInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "buyer_agreement_approval_rejection_input" in value:
        import capo_marketplace_agreement.types.buyer_agreement_approval_rejection_input

        out["buyer_agreement_approval_rejection_input"] = (
            capo_marketplace_agreement.types.buyer_agreement_approval_rejection_input.redact_sensitive(
                value["buyer_agreement_approval_rejection_input"]
            )
        )
    return out
