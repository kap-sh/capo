"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#GetOfferInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.locale
    import capo_marketplace_discovery.types.offer_id


class GetOfferInput(TypedDict, closed=True):
    locale: NotRequired["capo_marketplace_discovery.types.locale.Locale"]
    """<p>A BCP 47 language tag or comma-separated priority list specifying the preferred locale for response content. See <code>Locale</code> for supported values, constraints, fallback behavior, and the default locale. If omitted, the service returns content in the default locale.</p>"""
    offer_id: "capo_marketplace_discovery.types.offer_id.OfferId"
    """<p>The unique identifier of the offer to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetOfferInput) -> dict:
    out: dict = {}
    if "locale" in value:
        out["locale"] = value["locale"]
    out["offerId"] = value["offer_id"]
    return out


def deserialize_json(data: dict) -> GetOfferInput:
    out: GetOfferInput = {}  # type: ignore[typeddict-item]
    if data.get("locale") is not None:
        out["locale"] = data["locale"]
    if data.get("offerId") is not None:
        out["offer_id"] = data["offerId"]
    else:
        out["offer_id"] = ""
    return out
