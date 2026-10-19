"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#ProductInformation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_marketplace_discovery.errors import DeserializationError

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.non_empty_string
    import capo_marketplace_discovery.types.product_id
    import capo_marketplace_discovery.types.seller_information


class ProductInformation(TypedDict, closed=True):
    product_id: "capo_marketplace_discovery.types.product_id.ProductId"
    """<p>The unique identifier of the product.</p>"""
    product_name: "capo_marketplace_discovery.types.non_empty_string.NonEmptyString"
    """<p>The human-readable display name of the product.</p>"""
    manufacturer: (
        "capo_marketplace_discovery.types.seller_information.SellerInformation"
    )
    """<p>The entity who manufactured the product.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProductInformation) -> dict:
    out: dict = {}
    out["productId"] = value["product_id"]
    out["productName"] = value["product_name"]
    import capo_marketplace_discovery.types.seller_information

    out["manufacturer"] = (
        capo_marketplace_discovery.types.seller_information.serialize_json(
            value["manufacturer"]
        )
    )
    return out


def deserialize_json(data: dict) -> ProductInformation:
    out: ProductInformation = {}  # type: ignore[typeddict-item]
    if data.get("productId") is not None:
        out["product_id"] = data["productId"]
    else:
        out["product_id"] = ""
    if data.get("productName") is not None:
        out["product_name"] = data["productName"]
    else:
        out["product_name"] = ""
    if data.get("manufacturer") is not None:
        import capo_marketplace_discovery.types.seller_information

        out["manufacturer"] = (
            capo_marketplace_discovery.types.seller_information.deserialize_json(
                data["manufacturer"]
            )
        )
    else:
        raise DeserializationError("ProductInformation.manufacturer required")
    return out
