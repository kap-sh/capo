"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#GetOfferSetOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_marketplace_discovery.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_marketplace_discovery.types.catalog
    import capo_marketplace_discovery.types.locale
    import capo_marketplace_discovery.types.non_empty_string
    import capo_marketplace_discovery.types.nullable_string
    import capo_marketplace_discovery.types.offer_set_associated_entity_list
    import capo_marketplace_discovery.types.offer_set_id
    import capo_marketplace_discovery.types.purchase_option_badge_list
    import capo_marketplace_discovery.types.seller_information


class GetOfferSetOutput(TypedDict, closed=True):
    locale: NotRequired["capo_marketplace_discovery.types.locale.Locale"]
    """<p>The locale of the returned content. Indicates whether the response contains content in the requested locale, or fell back to the default locale. See <code>Locale</code> for details.</p>"""
    offer_set_id: "capo_marketplace_discovery.types.offer_set_id.OfferSetId"
    """<p>The unique identifier of the offer set.</p>"""
    catalog: "capo_marketplace_discovery.types.catalog.Catalog"
    """<p>The name of the catalog that the offer set belongs to.</p>"""
    offer_set_name: NotRequired[
        "capo_marketplace_discovery.types.non_empty_string.NonEmptyString"
    ]
    """<p>The display name of the offer set.</p>"""
    available_from_time: NotRequired["datetime.datetime"]
    """<p>The date and time when the offer set became available to the buyer.</p>"""
    expiration_time: NotRequired["datetime.datetime"]
    """<p>The date and time when the offer set expires and is no longer available for procurement.</p>"""
    buyer_notes: NotRequired[
        "capo_marketplace_discovery.types.nullable_string.NullableString"
    ]
    """<p>Detailed information about the offer set that helps buyers understand its purpose and contents.</p>"""
    seller_of_record: (
        "capo_marketplace_discovery.types.seller_information.SellerInformation"
    )
    """<p>The entity responsible for selling the products under this offer set.</p>"""
    badges: "capo_marketplace_discovery.types.purchase_option_badge_list.PurchaseOptionBadgeList"
    """<p>Badges indicating special attributes of the offer set, such as private pricing or future dated.</p>"""
    associated_entities: "capo_marketplace_discovery.types.offer_set_associated_entity_list.OfferSetAssociatedEntityList"
    """<p>The products and offers included in this offer set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetOfferSetOutput) -> dict:
    out: dict = {}
    if "locale" in value:
        out["locale"] = value["locale"]
    out["offerSetId"] = value["offer_set_id"]
    out["catalog"] = value["catalog"]
    if "offer_set_name" in value:
        out["offerSetName"] = value["offer_set_name"]
    if "available_from_time" in value:
        import capo_marketplace_discovery.types._prelude.timestamp

        out["availableFromTime"] = (
            capo_marketplace_discovery.types._prelude.timestamp.serialize_json(
                value["available_from_time"]
            )
        )
    if "expiration_time" in value:
        import capo_marketplace_discovery.types._prelude.timestamp

        out["expirationTime"] = (
            capo_marketplace_discovery.types._prelude.timestamp.serialize_json(
                value["expiration_time"]
            )
        )
    if "buyer_notes" in value:
        out["buyerNotes"] = value["buyer_notes"]
    import capo_marketplace_discovery.types.seller_information

    out["sellerOfRecord"] = (
        capo_marketplace_discovery.types.seller_information.serialize_json(
            value["seller_of_record"]
        )
    )
    import capo_marketplace_discovery.types.purchase_option_badge_list

    out["badges"] = (
        capo_marketplace_discovery.types.purchase_option_badge_list.serialize_json(
            value["badges"]
        )
    )
    import capo_marketplace_discovery.types.offer_set_associated_entity_list

    out["associatedEntities"] = (
        capo_marketplace_discovery.types.offer_set_associated_entity_list.serialize_json(
            value["associated_entities"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetOfferSetOutput:
    out: GetOfferSetOutput = {}  # type: ignore[typeddict-item]
    if data.get("locale") is not None:
        out["locale"] = data["locale"]
    if data.get("offerSetId") is not None:
        out["offer_set_id"] = data["offerSetId"]
    else:
        out["offer_set_id"] = ""
    if data.get("catalog") is not None:
        out["catalog"] = data["catalog"]
    else:
        out["catalog"] = ""
    if data.get("offerSetName") is not None:
        out["offer_set_name"] = data["offerSetName"]
    if data.get("availableFromTime") is not None:
        import capo_marketplace_discovery.types._prelude.timestamp

        out["available_from_time"] = (
            capo_marketplace_discovery.types._prelude.timestamp.deserialize_json(
                data["availableFromTime"]
            )
        )
    if data.get("expirationTime") is not None:
        import capo_marketplace_discovery.types._prelude.timestamp

        out["expiration_time"] = (
            capo_marketplace_discovery.types._prelude.timestamp.deserialize_json(
                data["expirationTime"]
            )
        )
    if data.get("buyerNotes") is not None:
        out["buyer_notes"] = data["buyerNotes"]
    if data.get("sellerOfRecord") is not None:
        import capo_marketplace_discovery.types.seller_information

        out["seller_of_record"] = (
            capo_marketplace_discovery.types.seller_information.deserialize_json(
                data["sellerOfRecord"]
            )
        )
    else:
        raise DeserializationError("GetOfferSetOutput.seller_of_record required")
    if data.get("badges") is not None:
        import capo_marketplace_discovery.types.purchase_option_badge_list

        out["badges"] = (
            capo_marketplace_discovery.types.purchase_option_badge_list.deserialize_json(
                data["badges"]
            )
        )
    else:
        out["badges"] = []
    if data.get("associatedEntities") is not None:
        import capo_marketplace_discovery.types.offer_set_associated_entity_list

        out["associated_entities"] = (
            capo_marketplace_discovery.types.offer_set_associated_entity_list.deserialize_json(
                data["associatedEntities"]
            )
        )
    else:
        out["associated_entities"] = []
    return out
