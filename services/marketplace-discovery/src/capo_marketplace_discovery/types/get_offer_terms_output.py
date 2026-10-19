"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#GetOfferTermsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.locale
    import capo_marketplace_discovery.types.next_token
    import capo_marketplace_discovery.types.offer_terms_list


class GetOfferTermsOutput(TypedDict, closed=True):
    locale: NotRequired["capo_marketplace_discovery.types.locale.Locale"]
    """<p>The locale of the returned content. Indicates whether the response contains content in the requested locale, or fell back to the default locale. See <code>Locale</code> for details.</p>"""
    offer_terms: "capo_marketplace_discovery.types.offer_terms_list.OfferTermsList"
    """<p>The terms attached to the offer. Each element contains exactly one term type.</p>"""
    next_token: NotRequired["capo_marketplace_discovery.types.next_token.NextToken"]
    """<p>If <code>nextToken</code> is returned, there are more results available. Make the call again using the returned token to retrieve the next page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetOfferTermsOutput) -> dict:
    out: dict = {}
    if "locale" in value:
        out["locale"] = value["locale"]
    import capo_marketplace_discovery.types.offer_terms_list

    out["offerTerms"] = (
        capo_marketplace_discovery.types.offer_terms_list.serialize_json(
            value["offer_terms"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetOfferTermsOutput:
    out: GetOfferTermsOutput = {}  # type: ignore[typeddict-item]
    if data.get("locale") is not None:
        out["locale"] = data["locale"]
    if data.get("offerTerms") is not None:
        import capo_marketplace_discovery.types.offer_terms_list

        out["offer_terms"] = (
            capo_marketplace_discovery.types.offer_terms_list.deserialize_json(
                data["offerTerms"]
            )
        )
    else:
        out["offer_terms"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
