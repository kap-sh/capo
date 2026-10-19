"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#ListFulfillmentOptionsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_marketplace_discovery.errors import DeserializationError

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.locale
    import capo_marketplace_discovery.types.next_token
    import capo_marketplace_discovery.types.product_id


class ListFulfillmentOptionsInput(TypedDict, closed=True):
    locale: NotRequired["capo_marketplace_discovery.types.locale.Locale"]
    """<p>A BCP 47 language tag or comma-separated priority list specifying the preferred locale for response content. See <code>Locale</code> for supported values, constraints, fallback behavior, and the default locale. If omitted, the service returns content in the default locale.</p>"""
    product_id: "capo_marketplace_discovery.types.product_id.ProductId"
    """<p>The unique identifier of the product for which to list fulfillment options.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of results that are returned per call. You can use <code>nextToken</code> to get more results.</p>"""
    next_token: NotRequired["capo_marketplace_discovery.types.next_token.NextToken"]
    """<p>If <code>nextToken</code> is returned, there are more results available. Make the call again using the returned token to retrieve the next page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFulfillmentOptionsInput) -> dict:
    out: dict = {}
    if "locale" in value:
        out["locale"] = value["locale"]
    out["productId"] = value["product_id"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListFulfillmentOptionsInput:
    out: ListFulfillmentOptionsInput = {}  # type: ignore[typeddict-item]
    if data.get("locale") is not None:
        out["locale"] = data["locale"]
    if data.get("productId") is not None:
        out["product_id"] = data["productId"]
    else:
        raise DeserializationError("ListFulfillmentOptionsInput.product_id required")
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
