"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#GetListingInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.listing_id
    import capo_marketplace_discovery.types.locale


class GetListingInput(TypedDict, closed=True):
    locale: NotRequired["capo_marketplace_discovery.types.locale.Locale"]
    """<p>A BCP 47 language tag or comma-separated priority list specifying the preferred locale for response content. See <code>Locale</code> for supported values, constraints, fallback behavior, and the default locale. If omitted, the service returns content in the default locale.</p>"""
    listing_id: "capo_marketplace_discovery.types.listing_id.ListingId"
    """<p>The unique identifier of the listing to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetListingInput) -> dict:
    out: dict = {}
    if "locale" in value:
        out["locale"] = value["locale"]
    out["listingId"] = value["listing_id"]
    return out


def deserialize_json(data: dict) -> GetListingInput:
    out: GetListingInput = {}  # type: ignore[typeddict-item]
    if data.get("locale") is not None:
        out["locale"] = data["locale"]
    if data.get("listingId") is not None:
        out["listing_id"] = data["listingId"]
    else:
        out["listing_id"] = ""
    return out
