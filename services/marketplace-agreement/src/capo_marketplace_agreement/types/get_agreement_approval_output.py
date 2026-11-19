"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#GetAgreementApprovalOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.buyer_agreement_approval


class GetAgreementApprovalOutput(TypedDict, closed=True):
    buyer_agreement_approval: NotRequired[
        "capo_marketplace_agreement.types.buyer_agreement_approval.BuyerAgreementApproval"
    ]
    """<p>The details of the agreement approval, when it is a <code>BUYER_AGREEMENT_APPROVAL</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetAgreementApprovalOutput) -> dict:
    out: dict = {}
    if "buyer_agreement_approval" in value:
        import capo_marketplace_agreement.types.buyer_agreement_approval

        out["buyerAgreementApproval"] = (
            capo_marketplace_agreement.types.buyer_agreement_approval.serialize_aws_json_1_0(
                value["buyer_agreement_approval"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetAgreementApprovalOutput:
    out: GetAgreementApprovalOutput = {}  # type: ignore[typeddict-item]
    if data.get("buyerAgreementApproval") is not None:
        import capo_marketplace_agreement.types.buyer_agreement_approval

        out["buyer_agreement_approval"] = (
            capo_marketplace_agreement.types.buyer_agreement_approval.deserialize_aws_json_1_0(
                data["buyerAgreementApproval"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetAgreementApprovalOutput) -> dict:
    out: dict = {}
    if "buyer_agreement_approval" in value:
        import capo_marketplace_agreement.types.buyer_agreement_approval

        out["buyerAgreementApproval"] = (
            capo_marketplace_agreement.types.buyer_agreement_approval.serialize_cbor(
                value["buyer_agreement_approval"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> GetAgreementApprovalOutput:
    out: GetAgreementApprovalOutput = {}  # type: ignore[typeddict-item]
    if data.get("buyerAgreementApproval") is not None:
        import capo_marketplace_agreement.types.buyer_agreement_approval

        out["buyer_agreement_approval"] = (
            capo_marketplace_agreement.types.buyer_agreement_approval.deserialize_cbor(
                data["buyerAgreementApproval"]
            )
        )
    return out


def redact_sensitive(value: GetAgreementApprovalOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "buyer_agreement_approval" in value:
        import capo_marketplace_agreement.types.buyer_agreement_approval

        out["buyer_agreement_approval"] = (
            capo_marketplace_agreement.types.buyer_agreement_approval.redact_sensitive(
                value["buyer_agreement_approval"]
            )
        )
    return out
