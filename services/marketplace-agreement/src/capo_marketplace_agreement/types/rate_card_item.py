"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#RateCardItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.bounded_string


class RateCardItem(TypedDict, closed=True):
    dimension_key: NotRequired[
        "capo_marketplace_agreement.types.bounded_string.BoundedString"
    ]
    """<p>Dimension for which the given entitlement applies. Dimensions represent categories of capacity in a product and are specified when the product is listed in AWS Marketplace.</p>"""
    price: NotRequired["capo_marketplace_agreement.types.bounded_string.BoundedString"]
    """<p>Per unit price for the product dimension that's used for calculating the amount to be charged.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RateCardItem) -> dict:
    out: dict = {}
    if "dimension_key" in value:
        out["dimensionKey"] = value["dimension_key"]
    if "price" in value:
        out["price"] = value["price"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RateCardItem:
    out: RateCardItem = {}  # type: ignore[typeddict-item]
    if data.get("dimensionKey") is not None:
        out["dimension_key"] = data["dimensionKey"]
    if data.get("price") is not None:
        out["price"] = data["price"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RateCardItem) -> dict:
    out: dict = {}
    if "dimension_key" in value:
        out["dimensionKey"] = value["dimension_key"]
    if "price" in value:
        out["price"] = value["price"]
    return out


def deserialize_cbor(data: dict) -> RateCardItem:
    out: RateCardItem = {}  # type: ignore[typeddict-item]
    if data.get("dimensionKey") is not None:
        out["dimension_key"] = data["dimensionKey"]
    if data.get("price") is not None:
        out["price"] = data["price"]
    return out
