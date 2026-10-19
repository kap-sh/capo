"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#GetOfferSetInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.locale
    import capo_marketplace_discovery.types.offer_set_id


class GetOfferSetInput(TypedDict, closed=True):
    locale: NotRequired["capo_marketplace_discovery.types.locale.Locale"]
    """<p>A BCP 47 language tag or comma-separated priority list specifying the preferred locale for response content. See <code>Locale</code> for supported values, constraints, fallback behavior, and the default locale. If omitted, the service returns content in the default locale.</p>"""
    offer_set_id: "capo_marketplace_discovery.types.offer_set_id.OfferSetId"
    """<p>The unique identifier of the offer set to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetOfferSetInput) -> dict:
    out: dict = {}
    if "locale" in value:
        out["locale"] = value["locale"]
    out["offerSetId"] = value["offer_set_id"]
    return out


def deserialize_json(data: dict) -> GetOfferSetInput:
    out: GetOfferSetInput = {}  # type: ignore[typeddict-item]
    if data.get("locale") is not None:
        out["locale"] = data["locale"]
    if data.get("offerSetId") is not None:
        out["offer_set_id"] = data["offerSetId"]
    else:
        out["offer_set_id"] = ""
    return out
