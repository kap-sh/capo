"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#ProposalSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.offer_id
    import capo_marketplace_agreement.types.offer_set_id
    import capo_marketplace_agreement.types.resources


class ProposalSummary(TypedDict, closed=True):
    resources: NotRequired["capo_marketplace_agreement.types.resources.Resources"]
    """<p>The list of resources involved in the agreement.</p>"""
    offer_id: NotRequired["capo_marketplace_agreement.types.offer_id.OfferId"]
    """<p>The unique identifier of the offer in AWS Marketplace.</p>"""
    offer_set_id: NotRequired[
        "capo_marketplace_agreement.types.offer_set_id.OfferSetId"
    ]
    """<p>A unique identifier for the offer set containing this offer. All agreements created from offers in this set include this identifier as context.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProposalSummary) -> dict:
    out: dict = {}
    if "resources" in value:
        import capo_marketplace_agreement.types.resources

        out["resources"] = (
            capo_marketplace_agreement.types.resources.serialize_aws_json_1_0(
                value["resources"]
            )
        )
    if "offer_id" in value:
        out["offerId"] = value["offer_id"]
    if "offer_set_id" in value:
        out["offerSetId"] = value["offer_set_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ProposalSummary:
    out: ProposalSummary = {}  # type: ignore[typeddict-item]
    if data.get("resources") is not None:
        import capo_marketplace_agreement.types.resources

        out["resources"] = (
            capo_marketplace_agreement.types.resources.deserialize_aws_json_1_0(
                data["resources"]
            )
        )
    if data.get("offerId") is not None:
        out["offer_id"] = data["offerId"]
    if data.get("offerSetId") is not None:
        out["offer_set_id"] = data["offerSetId"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ProposalSummary) -> dict:
    out: dict = {}
    if "resources" in value:
        import capo_marketplace_agreement.types.resources

        out["resources"] = capo_marketplace_agreement.types.resources.serialize_cbor(
            value["resources"]
        )
    if "offer_id" in value:
        out["offerId"] = value["offer_id"]
    if "offer_set_id" in value:
        out["offerSetId"] = value["offer_set_id"]
    return out


def deserialize_cbor(data: dict) -> ProposalSummary:
    out: ProposalSummary = {}  # type: ignore[typeddict-item]
    if data.get("resources") is not None:
        import capo_marketplace_agreement.types.resources

        out["resources"] = capo_marketplace_agreement.types.resources.deserialize_cbor(
            data["resources"]
        )
    if data.get("offerId") is not None:
        out["offer_id"] = data["offerId"]
    if data.get("offerSetId") is not None:
        out["offer_set_id"] = data["offerSetId"]
    return out
