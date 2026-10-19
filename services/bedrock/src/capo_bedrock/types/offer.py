"""Generated from Smithy shape ``com.amazonaws.bedrock#Offer``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.offer_id
    import capo_bedrock.types.offer_token
    import capo_bedrock.types.term_details


class Offer(TypedDict, closed=True):
    offer_id: NotRequired["capo_bedrock.types.offer_id.OfferId"]
    """<p>Offer Id for a model offer.</p>"""
    offer_token: "capo_bedrock.types.offer_token.OfferToken"
    """<p>Offer token.</p>"""
    term_details: "capo_bedrock.types.term_details.TermDetails"
    """<p>Details about the terms of the offer.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Offer) -> dict:
    out: dict = {}
    if "offer_id" in value:
        out["offerId"] = value["offer_id"]
    out["offerToken"] = value["offer_token"]
    import capo_bedrock.types.term_details

    out["termDetails"] = capo_bedrock.types.term_details.serialize_json(
        value["term_details"]
    )
    return out


def deserialize_json(data: dict) -> Offer:
    out: Offer = {}  # type: ignore[typeddict-item]
    if data.get("offerId") is not None:
        out["offer_id"] = data["offerId"]
    if data.get("offerToken") is not None:
        out["offer_token"] = data["offerToken"]
    else:
        out["offer_token"] = ""
    if data.get("termDetails") is not None:
        import capo_bedrock.types.term_details

        out["term_details"] = capo_bedrock.types.term_details.deserialize_json(
            data["termDetails"]
        )
    else:
        raise DeserializationError("Offer.term_details required")
    return out
