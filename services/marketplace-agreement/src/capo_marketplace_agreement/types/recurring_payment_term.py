"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#RecurringPaymentTerm``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.bounded_string
    import capo_marketplace_agreement.types.currency_code
    import capo_marketplace_agreement.types.term_id
    import capo_marketplace_agreement.types.unversioned_term_type


class RecurringPaymentTerm(TypedDict, closed=True):
    type: NotRequired[
        "capo_marketplace_agreement.types.unversioned_term_type.UnversionedTermType"
    ]
    """<p>Type of the term being updated.</p>"""
    id: NotRequired["capo_marketplace_agreement.types.term_id.TermId"]
    """<p>The unique identifier for the term.</p>"""
    currency_code: NotRequired[
        "capo_marketplace_agreement.types.currency_code.CurrencyCode"
    ]
    """<p>Defines the currency for the prices mentioned in this term. </p>"""
    billing_period: NotRequired[
        "capo_marketplace_agreement.types.bounded_string.BoundedString"
    ]
    """<p>Defines the recurrence at which buyers are charged.</p>"""
    price: NotRequired["capo_marketplace_agreement.types.bounded_string.BoundedString"]
    """<p>Amount charged to the buyer every billing period.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RecurringPaymentTerm) -> dict:
    out: dict = {}
    if "type" in value:
        out["type"] = value["type"]
    if "id" in value:
        out["id"] = value["id"]
    if "currency_code" in value:
        out["currencyCode"] = value["currency_code"]
    if "billing_period" in value:
        out["billingPeriod"] = value["billing_period"]
    if "price" in value:
        out["price"] = value["price"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RecurringPaymentTerm:
    out: RecurringPaymentTerm = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        out["type"] = data["type"]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("currencyCode") is not None:
        out["currency_code"] = data["currencyCode"]
    if data.get("billingPeriod") is not None:
        out["billing_period"] = data["billingPeriod"]
    if data.get("price") is not None:
        out["price"] = data["price"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RecurringPaymentTerm) -> dict:
    out: dict = {}
    if "type" in value:
        out["type"] = value["type"]
    if "id" in value:
        out["id"] = value["id"]
    if "currency_code" in value:
        out["currencyCode"] = value["currency_code"]
    if "billing_period" in value:
        out["billingPeriod"] = value["billing_period"]
    if "price" in value:
        out["price"] = value["price"]
    return out


def deserialize_cbor(data: dict) -> RecurringPaymentTerm:
    out: RecurringPaymentTerm = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        out["type"] = data["type"]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("currencyCode") is not None:
        out["currency_code"] = data["currencyCode"]
    if data.get("billingPeriod") is not None:
        out["billing_period"] = data["billingPeriod"]
    if data.get("price") is not None:
        out["price"] = data["price"]
    return out
