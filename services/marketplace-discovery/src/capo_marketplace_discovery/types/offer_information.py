"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#OfferInformation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_marketplace_discovery.errors import DeserializationError

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.nullable_string
    import capo_marketplace_discovery.types.offer_id
    import capo_marketplace_discovery.types.seller_information


class OfferInformation(TypedDict, closed=True):
    offer_id: "capo_marketplace_discovery.types.offer_id.OfferId"
    """<p>The unique identifier of the offer.</p>"""
    offer_name: NotRequired[
        "capo_marketplace_discovery.types.nullable_string.NullableString"
    ]
    """<p>The display name of the offer.</p>"""
    seller_of_record: (
        "capo_marketplace_discovery.types.seller_information.SellerInformation"
    )
    """<p>The entity responsible for selling the product under this offer.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OfferInformation) -> dict:
    out: dict = {}
    out["offerId"] = value["offer_id"]
    if "offer_name" in value:
        out["offerName"] = value["offer_name"]
    import capo_marketplace_discovery.types.seller_information

    out["sellerOfRecord"] = (
        capo_marketplace_discovery.types.seller_information.serialize_json(
            value["seller_of_record"]
        )
    )
    return out


def deserialize_json(data: dict) -> OfferInformation:
    out: OfferInformation = {}  # type: ignore[typeddict-item]
    if data.get("offerId") is not None:
        out["offer_id"] = data["offerId"]
    else:
        out["offer_id"] = ""
    if data.get("offerName") is not None:
        out["offer_name"] = data["offerName"]
    if data.get("sellerOfRecord") is not None:
        import capo_marketplace_discovery.types.seller_information

        out["seller_of_record"] = (
            capo_marketplace_discovery.types.seller_information.deserialize_json(
                data["sellerOfRecord"]
            )
        )
    else:
        raise DeserializationError("OfferInformation.seller_of_record required")
    return out
