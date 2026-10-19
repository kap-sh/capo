"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#PurchaseOptionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_marketplace_discovery.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_marketplace_discovery.types.catalog
    import capo_marketplace_discovery.types.non_empty_string
    import capo_marketplace_discovery.types.purchase_option_associated_entity_list
    import capo_marketplace_discovery.types.purchase_option_badge_list
    import capo_marketplace_discovery.types.purchase_option_type
    import capo_marketplace_discovery.types.seller_information


class PurchaseOptionSummary(TypedDict, closed=True):
    purchase_option_id: (
        "capo_marketplace_discovery.types.non_empty_string.NonEmptyString"
    )
    """<p>The unique identifier of the purchase option.</p>"""
    catalog: "capo_marketplace_discovery.types.catalog.Catalog"
    """<p>The name of the catalog that the purchase option belongs to.</p>"""
    purchase_option_type: (
        "capo_marketplace_discovery.types.purchase_option_type.PurchaseOptionType"
    )
    """<p>The type of purchase option. Values are <code>OFFER</code> for a single-product offer or <code>OFFERSET</code> for a bundled offer set.</p>"""
    purchase_option_name: NotRequired[
        "capo_marketplace_discovery.types.non_empty_string.NonEmptyString"
    ]
    """<p>The display name of the purchase option.</p>"""
    available_from_time: NotRequired["datetime.datetime"]
    """<p>The date and time when the purchase option became available to the buyer.</p>"""
    expiration_time: NotRequired["datetime.datetime"]
    """<p>The date and time when the purchase option expires and is no longer available for procurement.</p>"""
    seller_of_record: (
        "capo_marketplace_discovery.types.seller_information.SellerInformation"
    )
    """<p>The entity responsible for selling the product under this purchase option.</p>"""
    badges: NotRequired[
        "capo_marketplace_discovery.types.purchase_option_badge_list.PurchaseOptionBadgeList"
    ]
    """<p>Badges indicating special attributes of the purchase option, such as private pricing or future dated.</p>"""
    associated_entities: "capo_marketplace_discovery.types.purchase_option_associated_entity_list.PurchaseOptionAssociatedEntityList"
    """<p>The products, offers, and offer sets associated with this purchase option.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PurchaseOptionSummary) -> dict:
    out: dict = {}
    out["purchaseOptionId"] = value["purchase_option_id"]
    out["catalog"] = value["catalog"]
    import capo_marketplace_discovery.types.purchase_option_type

    out["purchaseOptionType"] = (
        capo_marketplace_discovery.types.purchase_option_type.serialize_json(
            value["purchase_option_type"]
        )
    )
    if "purchase_option_name" in value:
        out["purchaseOptionName"] = value["purchase_option_name"]
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
    import capo_marketplace_discovery.types.seller_information

    out["sellerOfRecord"] = (
        capo_marketplace_discovery.types.seller_information.serialize_json(
            value["seller_of_record"]
        )
    )
    if "badges" in value:
        import capo_marketplace_discovery.types.purchase_option_badge_list

        out["badges"] = (
            capo_marketplace_discovery.types.purchase_option_badge_list.serialize_json(
                value["badges"]
            )
        )
    import capo_marketplace_discovery.types.purchase_option_associated_entity_list

    out["associatedEntities"] = (
        capo_marketplace_discovery.types.purchase_option_associated_entity_list.serialize_json(
            value["associated_entities"]
        )
    )
    return out


def deserialize_json(data: dict) -> PurchaseOptionSummary:
    out: PurchaseOptionSummary = {}  # type: ignore[typeddict-item]
    if data.get("purchaseOptionId") is not None:
        out["purchase_option_id"] = data["purchaseOptionId"]
    else:
        out["purchase_option_id"] = ""
    if data.get("catalog") is not None:
        out["catalog"] = data["catalog"]
    else:
        out["catalog"] = ""
    if data.get("purchaseOptionType") is not None:
        import capo_marketplace_discovery.types.purchase_option_type

        out["purchase_option_type"] = (
            capo_marketplace_discovery.types.purchase_option_type.deserialize_json(
                data["purchaseOptionType"]
            )
        )
    else:
        import typing

        out["purchase_option_type"] = typing.cast(
            "capo_marketplace_discovery.types.purchase_option_type.PurchaseOptionType",
            "",
        )
    if data.get("purchaseOptionName") is not None:
        out["purchase_option_name"] = data["purchaseOptionName"]
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
    if data.get("sellerOfRecord") is not None:
        import capo_marketplace_discovery.types.seller_information

        out["seller_of_record"] = (
            capo_marketplace_discovery.types.seller_information.deserialize_json(
                data["sellerOfRecord"]
            )
        )
    else:
        raise DeserializationError("PurchaseOptionSummary.seller_of_record required")
    if data.get("badges") is not None:
        import capo_marketplace_discovery.types.purchase_option_badge_list

        out["badges"] = (
            capo_marketplace_discovery.types.purchase_option_badge_list.deserialize_json(
                data["badges"]
            )
        )
    if data.get("associatedEntities") is not None:
        import capo_marketplace_discovery.types.purchase_option_associated_entity_list

        out["associated_entities"] = (
            capo_marketplace_discovery.types.purchase_option_associated_entity_list.deserialize_json(
                data["associatedEntities"]
            )
        )
    else:
        out["associated_entities"] = []
    return out
