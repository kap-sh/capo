"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#GetProductInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.locale
    import capo_marketplace_discovery.types.product_id


class GetProductInput(TypedDict, closed=True):
    locale: NotRequired["capo_marketplace_discovery.types.locale.Locale"]
    """<p>A BCP 47 language tag or comma-separated priority list specifying the preferred locale for response content. See <code>Locale</code> for supported values, constraints, fallback behavior, and the default locale. If omitted, the service returns content in the default locale.</p>"""
    product_id: "capo_marketplace_discovery.types.product_id.ProductId"
    """<p>The unique identifier of the product to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetProductInput) -> dict:
    out: dict = {}
    if "locale" in value:
        out["locale"] = value["locale"]
    out["productId"] = value["product_id"]
    return out


def deserialize_json(data: dict) -> GetProductInput:
    out: GetProductInput = {}  # type: ignore[typeddict-item]
    if data.get("locale") is not None:
        out["locale"] = data["locale"]
    if data.get("productId") is not None:
        out["product_id"] = data["productId"]
    else:
        out["product_id"] = ""
    return out
