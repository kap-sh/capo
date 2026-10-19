"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#GetOfferOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_marketplace_discovery.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_marketplace_discovery.types.agreement_resource_id
    import capo_marketplace_discovery.types.catalog
    import capo_marketplace_discovery.types.locale
    import capo_marketplace_discovery.types.nullable_string
    import capo_marketplace_discovery.types.offer_associated_entity_list
    import capo_marketplace_discovery.types.offer_id
    import capo_marketplace_discovery.types.pricing_model
    import capo_marketplace_discovery.types.purchase_option_badge_list
    import capo_marketplace_discovery.types.seller_information


class GetOfferOutput(TypedDict, closed=True):
    locale: NotRequired["capo_marketplace_discovery.types.locale.Locale"]
    """<p>The locale of the returned content. Indicates whether the response contains content in the requested locale, or fell back to the default locale. See <code>Locale</code> for details.</p>"""
    offer_id: "capo_marketplace_discovery.types.offer_id.OfferId"
    """<p>The unique identifier of the offer.</p>"""
    catalog: "capo_marketplace_discovery.types.catalog.Catalog"
    """<p>The name of the catalog that the offer belongs to.</p>"""
    offer_name: NotRequired[
        "capo_marketplace_discovery.types.nullable_string.NullableString"
    ]
    """<p>The display name of the offer. This is free-form text provided by the seller.</p>"""
    expiration_time: NotRequired["datetime.datetime"]
    """<p>The date and time until when the offer can be procured. This value is null for offers that never expire.</p>"""
    available_from_time: NotRequired["datetime.datetime"]
    """<p>The date and time when the offer became available to the buyer.</p>"""
    seller_of_record: (
        "capo_marketplace_discovery.types.seller_information.SellerInformation"
    )
    """<p>The entity responsible for selling the product under this offer.</p>"""
    associated_entities: "capo_marketplace_discovery.types.offer_associated_entity_list.OfferAssociatedEntityList"
    """<p>The products and offer sets associated with this offer.</p>"""
    agreement_proposal_id: (
        "capo_marketplace_discovery.types.agreement_resource_id.AgreementResourceId"
    )
    """<p>An encoded string to be passed by the acceptor of the terms when creating an agreement.</p>"""
    replacement_agreement_id: NotRequired[
        "capo_marketplace_discovery.types.agreement_resource_id.AgreementResourceId"
    ]
    """<p>The identifier of the existing agreement that this offer would replace. Enables agreement-based offer functionality.</p>"""
    pricing_model: "capo_marketplace_discovery.types.pricing_model.PricingModel"
    """<p>The pricing model that determines how buyers are charged, such as usage-based, contract, BYOL, or free.</p>"""
    badges: "capo_marketplace_discovery.types.purchase_option_badge_list.PurchaseOptionBadgeList"
    """<p>Badges indicating special attributes of the offer, such as private pricing, future dated, or replacement offer.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetOfferOutput) -> dict:
    out: dict = {}
    if "locale" in value:
        out["locale"] = value["locale"]
    out["offerId"] = value["offer_id"]
    out["catalog"] = value["catalog"]
    if "offer_name" in value:
        out["offerName"] = value["offer_name"]
    if "expiration_time" in value:
        import capo_marketplace_discovery.types._prelude.timestamp

        out["expirationTime"] = (
            capo_marketplace_discovery.types._prelude.timestamp.serialize_json(
                value["expiration_time"]
            )
        )
    if "available_from_time" in value:
        import capo_marketplace_discovery.types._prelude.timestamp

        out["availableFromTime"] = (
            capo_marketplace_discovery.types._prelude.timestamp.serialize_json(
                value["available_from_time"]
            )
        )
    import capo_marketplace_discovery.types.seller_information

    out["sellerOfRecord"] = (
        capo_marketplace_discovery.types.seller_information.serialize_json(
            value["seller_of_record"]
        )
    )
    import capo_marketplace_discovery.types.offer_associated_entity_list

    out["associatedEntities"] = (
        capo_marketplace_discovery.types.offer_associated_entity_list.serialize_json(
            value["associated_entities"]
        )
    )
    out["agreementProposalId"] = value["agreement_proposal_id"]
    if "replacement_agreement_id" in value:
        out["replacementAgreementId"] = value["replacement_agreement_id"]
    import capo_marketplace_discovery.types.pricing_model

    out["pricingModel"] = capo_marketplace_discovery.types.pricing_model.serialize_json(
        value["pricing_model"]
    )
    import capo_marketplace_discovery.types.purchase_option_badge_list

    out["badges"] = (
        capo_marketplace_discovery.types.purchase_option_badge_list.serialize_json(
            value["badges"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetOfferOutput:
    out: GetOfferOutput = {}  # type: ignore[typeddict-item]
    if data.get("locale") is not None:
        out["locale"] = data["locale"]
    if data.get("offerId") is not None:
        out["offer_id"] = data["offerId"]
    else:
        out["offer_id"] = ""
    if data.get("catalog") is not None:
        out["catalog"] = data["catalog"]
    else:
        out["catalog"] = ""
    if data.get("offerName") is not None:
        out["offer_name"] = data["offerName"]
    if data.get("expirationTime") is not None:
        import capo_marketplace_discovery.types._prelude.timestamp

        out["expiration_time"] = (
            capo_marketplace_discovery.types._prelude.timestamp.deserialize_json(
                data["expirationTime"]
            )
        )
    if data.get("availableFromTime") is not None:
        import capo_marketplace_discovery.types._prelude.timestamp

        out["available_from_time"] = (
            capo_marketplace_discovery.types._prelude.timestamp.deserialize_json(
                data["availableFromTime"]
            )
        )
    if data.get("sellerOfRecord") is not None:
        import capo_marketplace_discovery.types.seller_information

        out["seller_of_record"] = (
            capo_marketplace_discovery.types.seller_information.deserialize_json(
                data["sellerOfRecord"]
            )
        )
    else:
        raise DeserializationError("GetOfferOutput.seller_of_record required")
    if data.get("associatedEntities") is not None:
        import capo_marketplace_discovery.types.offer_associated_entity_list

        out["associated_entities"] = (
            capo_marketplace_discovery.types.offer_associated_entity_list.deserialize_json(
                data["associatedEntities"]
            )
        )
    else:
        out["associated_entities"] = []
    if data.get("agreementProposalId") is not None:
        out["agreement_proposal_id"] = data["agreementProposalId"]
    else:
        out["agreement_proposal_id"] = ""
    if data.get("replacementAgreementId") is not None:
        out["replacement_agreement_id"] = data["replacementAgreementId"]
    if data.get("pricingModel") is not None:
        import capo_marketplace_discovery.types.pricing_model

        out["pricing_model"] = (
            capo_marketplace_discovery.types.pricing_model.deserialize_json(
                data["pricingModel"]
            )
        )
    else:
        raise DeserializationError("GetOfferOutput.pricing_model required")
    if data.get("badges") is not None:
        import capo_marketplace_discovery.types.purchase_option_badge_list

        out["badges"] = (
            capo_marketplace_discovery.types.purchase_option_badge_list.deserialize_json(
                data["badges"]
            )
        )
    else:
        out["badges"] = []
    return out
