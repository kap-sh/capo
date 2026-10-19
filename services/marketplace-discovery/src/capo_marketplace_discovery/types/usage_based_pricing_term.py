"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#UsageBasedPricingTerm``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.currency_code
    import capo_marketplace_discovery.types.term_id
    import capo_marketplace_discovery.types.term_type
    import capo_marketplace_discovery.types.usage_based_rate_card_list


class UsageBasedPricingTerm(TypedDict, closed=True):
    id: "capo_marketplace_discovery.types.term_id.TermId"
    """<p>The unique identifier of the term.</p>"""
    type: "capo_marketplace_discovery.types.term_type.TermType"
    """<p>The category of the term.</p>"""
    currency_code: "capo_marketplace_discovery.types.currency_code.CurrencyCode"
    """<p>Defines the currency for the prices in this term.</p>"""
    rate_cards: "capo_marketplace_discovery.types.usage_based_rate_card_list.UsageBasedRateCardList"
    """<p>The rate cards containing per-unit rates for usage-based pricing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UsageBasedPricingTerm) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    import capo_marketplace_discovery.types.term_type

    out["type"] = capo_marketplace_discovery.types.term_type.serialize_json(
        value["type"]
    )
    out["currencyCode"] = value["currency_code"]
    import capo_marketplace_discovery.types.usage_based_rate_card_list

    out["rateCards"] = (
        capo_marketplace_discovery.types.usage_based_rate_card_list.serialize_json(
            value["rate_cards"]
        )
    )
    return out


def deserialize_json(data: dict) -> UsageBasedPricingTerm:
    out: UsageBasedPricingTerm = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("type") is not None:
        import capo_marketplace_discovery.types.term_type

        out["type"] = capo_marketplace_discovery.types.term_type.deserialize_json(
            data["type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_marketplace_discovery.types.term_type.TermType", ""
        )
    if data.get("currencyCode") is not None:
        out["currency_code"] = data["currencyCode"]
    else:
        out["currency_code"] = ""
    if data.get("rateCards") is not None:
        import capo_marketplace_discovery.types.usage_based_rate_card_list

        out["rate_cards"] = (
            capo_marketplace_discovery.types.usage_based_rate_card_list.deserialize_json(
                data["rateCards"]
            )
        )
    else:
        out["rate_cards"] = []
    return out
