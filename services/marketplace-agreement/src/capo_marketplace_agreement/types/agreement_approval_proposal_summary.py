"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#AgreementApprovalProposalSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.agreement_approval_offer_id
    import capo_marketplace_agreement.types.agreement_approval_offer_set_id
    import capo_marketplace_agreement.types.agreement_approval_resources
    import capo_marketplace_agreement.types.offer_visibility_scope


class AgreementApprovalProposalSummary(TypedDict, closed=True):
    offer_id: "capo_marketplace_agreement.types.agreement_approval_offer_id.AgreementApprovalOfferId"
    """<p>The unique identifier of the offer in AWS Marketplace.</p>"""
    offer_set_id: NotRequired[
        "capo_marketplace_agreement.types.agreement_approval_offer_set_id.AgreementApprovalOfferSetId"
    ]
    """<p>A unique identifier for the offer set containing this offer.</p>"""
    resources: NotRequired[
        "capo_marketplace_agreement.types.agreement_approval_resources.AgreementApprovalResources"
    ]
    """<p>The list of resources involved in the agreement.</p>"""
    visibility_scope: (
        "capo_marketplace_agreement.types.offer_visibility_scope.OfferVisibilityScope"
    )
    """<p>The visibility of the offer. Valid values are <code>PUBLIC</code> and <code>PRIVATE</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AgreementApprovalProposalSummary) -> dict:
    out: dict = {}
    out["offerId"] = value["offer_id"]
    if "offer_set_id" in value:
        out["offerSetId"] = value["offer_set_id"]
    if "resources" in value:
        import capo_marketplace_agreement.types.agreement_approval_resources

        out["resources"] = (
            capo_marketplace_agreement.types.agreement_approval_resources.serialize_aws_json_1_0(
                value["resources"]
            )
        )
    import capo_marketplace_agreement.types.offer_visibility_scope

    out["visibilityScope"] = (
        capo_marketplace_agreement.types.offer_visibility_scope.serialize_aws_json_1_0(
            value["visibility_scope"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> AgreementApprovalProposalSummary:
    out: AgreementApprovalProposalSummary = {}  # type: ignore[typeddict-item]
    if data.get("offerId") is not None:
        out["offer_id"] = data["offerId"]
    else:
        out["offer_id"] = ""
    if data.get("offerSetId") is not None:
        out["offer_set_id"] = data["offerSetId"]
    if data.get("resources") is not None:
        import capo_marketplace_agreement.types.agreement_approval_resources

        out["resources"] = (
            capo_marketplace_agreement.types.agreement_approval_resources.deserialize_aws_json_1_0(
                data["resources"]
            )
        )
    if data.get("visibilityScope") is not None:
        import capo_marketplace_agreement.types.offer_visibility_scope

        out["visibility_scope"] = (
            capo_marketplace_agreement.types.offer_visibility_scope.deserialize_aws_json_1_0(
                data["visibilityScope"]
            )
        )
    else:
        import typing

        out["visibility_scope"] = typing.cast(
            "capo_marketplace_agreement.types.offer_visibility_scope.OfferVisibilityScope",
            "",
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AgreementApprovalProposalSummary) -> dict:
    out: dict = {}
    out["offerId"] = value["offer_id"]
    if "offer_set_id" in value:
        out["offerSetId"] = value["offer_set_id"]
    if "resources" in value:
        import capo_marketplace_agreement.types.agreement_approval_resources

        out["resources"] = (
            capo_marketplace_agreement.types.agreement_approval_resources.serialize_cbor(
                value["resources"]
            )
        )
    import capo_marketplace_agreement.types.offer_visibility_scope

    out["visibilityScope"] = (
        capo_marketplace_agreement.types.offer_visibility_scope.serialize_cbor(
            value["visibility_scope"]
        )
    )
    return out


def deserialize_cbor(data: dict) -> AgreementApprovalProposalSummary:
    out: AgreementApprovalProposalSummary = {}  # type: ignore[typeddict-item]
    if data.get("offerId") is not None:
        out["offer_id"] = data["offerId"]
    else:
        out["offer_id"] = ""
    if data.get("offerSetId") is not None:
        out["offer_set_id"] = data["offerSetId"]
    if data.get("resources") is not None:
        import capo_marketplace_agreement.types.agreement_approval_resources

        out["resources"] = (
            capo_marketplace_agreement.types.agreement_approval_resources.deserialize_cbor(
                data["resources"]
            )
        )
    if data.get("visibilityScope") is not None:
        import capo_marketplace_agreement.types.offer_visibility_scope

        out["visibility_scope"] = (
            capo_marketplace_agreement.types.offer_visibility_scope.deserialize_cbor(
                data["visibilityScope"]
            )
        )
    else:
        import typing

        out["visibility_scope"] = typing.cast(
            "capo_marketplace_agreement.types.offer_visibility_scope.OfferVisibilityScope",
            "",
        )
    return out
