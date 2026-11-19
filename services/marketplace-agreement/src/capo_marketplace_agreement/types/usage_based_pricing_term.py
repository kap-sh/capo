"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#UsageBasedPricingTerm``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.currency_code
    import capo_marketplace_agreement.types.term_id
    import capo_marketplace_agreement.types.unversioned_term_type
    import capo_marketplace_agreement.types.usage_based_rate_card_list


class UsageBasedPricingTerm(TypedDict, closed=True):
    type: NotRequired[
        "capo_marketplace_agreement.types.unversioned_term_type.UnversionedTermType"
    ]
    """<p>Category of the term.</p>"""
    id: NotRequired["capo_marketplace_agreement.types.term_id.TermId"]
    """<p>The unique identifier for the term.</p>"""
    currency_code: NotRequired[
        "capo_marketplace_agreement.types.currency_code.CurrencyCode"
    ]
    """<p>Defines the currency for the prices mentioned in the term. </p>"""
    rate_cards: NotRequired[
        "capo_marketplace_agreement.types.usage_based_rate_card_list.UsageBasedRateCardList"
    ]
    """<p>List of rate cards.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UsageBasedPricingTerm) -> dict:
    out: dict = {}
    if "type" in value:
        out["type"] = value["type"]
    if "id" in value:
        out["id"] = value["id"]
    if "currency_code" in value:
        out["currencyCode"] = value["currency_code"]
    if "rate_cards" in value:
        import capo_marketplace_agreement.types.usage_based_rate_card_list

        out["rateCards"] = (
            capo_marketplace_agreement.types.usage_based_rate_card_list.serialize_aws_json_1_0(
                value["rate_cards"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UsageBasedPricingTerm:
    out: UsageBasedPricingTerm = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        out["type"] = data["type"]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("currencyCode") is not None:
        out["currency_code"] = data["currencyCode"]
    if data.get("rateCards") is not None:
        import capo_marketplace_agreement.types.usage_based_rate_card_list

        out["rate_cards"] = (
            capo_marketplace_agreement.types.usage_based_rate_card_list.deserialize_aws_json_1_0(
                data["rateCards"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UsageBasedPricingTerm) -> dict:
    out: dict = {}
    if "type" in value:
        out["type"] = value["type"]
    if "id" in value:
        out["id"] = value["id"]
    if "currency_code" in value:
        out["currencyCode"] = value["currency_code"]
    if "rate_cards" in value:
        import capo_marketplace_agreement.types.usage_based_rate_card_list

        out["rateCards"] = (
            capo_marketplace_agreement.types.usage_based_rate_card_list.serialize_cbor(
                value["rate_cards"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> UsageBasedPricingTerm:
    out: UsageBasedPricingTerm = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        out["type"] = data["type"]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("currencyCode") is not None:
        out["currency_code"] = data["currencyCode"]
    if data.get("rateCards") is not None:
        import capo_marketplace_agreement.types.usage_based_rate_card_list

        out["rate_cards"] = (
            capo_marketplace_agreement.types.usage_based_rate_card_list.deserialize_cbor(
                data["rateCards"]
            )
        )
    return out
