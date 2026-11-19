"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#FixedUpfrontPricingTerm``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.bounded_string
    import capo_marketplace_agreement.types.currency_code
    import capo_marketplace_agreement.types.grant_list
    import capo_marketplace_agreement.types.term_id
    import capo_marketplace_agreement.types.unversioned_term_type


class FixedUpfrontPricingTerm(TypedDict, closed=True):
    type: NotRequired[
        "capo_marketplace_agreement.types.unversioned_term_type.UnversionedTermType"
    ]
    """<p>Category of the term being updated.</p>"""
    id: NotRequired["capo_marketplace_agreement.types.term_id.TermId"]
    """<p>The unique identifier for the term.</p>"""
    currency_code: NotRequired[
        "capo_marketplace_agreement.types.currency_code.CurrencyCode"
    ]
    """<p>Defines the currency for the prices mentioned in this term. </p>"""
    duration: NotRequired[
        "capo_marketplace_agreement.types.bounded_string.BoundedString"
    ]
    """<p>Contract duration for the terms.</p>"""
    price: NotRequired["capo_marketplace_agreement.types.bounded_string.BoundedString"]
    """<p>Fixed amount to be charged to the customer when this term is accepted.</p>"""
    grants: NotRequired["capo_marketplace_agreement.types.grant_list.GrantList"]
    """<p>Entitlements granted to the acceptor of fixed upfront as part of agreement execution.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FixedUpfrontPricingTerm) -> dict:
    out: dict = {}
    if "type" in value:
        out["type"] = value["type"]
    if "id" in value:
        out["id"] = value["id"]
    if "currency_code" in value:
        out["currencyCode"] = value["currency_code"]
    if "duration" in value:
        out["duration"] = value["duration"]
    if "price" in value:
        out["price"] = value["price"]
    if "grants" in value:
        import capo_marketplace_agreement.types.grant_list

        out["grants"] = (
            capo_marketplace_agreement.types.grant_list.serialize_aws_json_1_0(
                value["grants"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> FixedUpfrontPricingTerm:
    out: FixedUpfrontPricingTerm = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        out["type"] = data["type"]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("currencyCode") is not None:
        out["currency_code"] = data["currencyCode"]
    if data.get("duration") is not None:
        out["duration"] = data["duration"]
    if data.get("price") is not None:
        out["price"] = data["price"]
    if data.get("grants") is not None:
        import capo_marketplace_agreement.types.grant_list

        out["grants"] = (
            capo_marketplace_agreement.types.grant_list.deserialize_aws_json_1_0(
                data["grants"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: FixedUpfrontPricingTerm) -> dict:
    out: dict = {}
    if "type" in value:
        out["type"] = value["type"]
    if "id" in value:
        out["id"] = value["id"]
    if "currency_code" in value:
        out["currencyCode"] = value["currency_code"]
    if "duration" in value:
        out["duration"] = value["duration"]
    if "price" in value:
        out["price"] = value["price"]
    if "grants" in value:
        import capo_marketplace_agreement.types.grant_list

        out["grants"] = capo_marketplace_agreement.types.grant_list.serialize_cbor(
            value["grants"]
        )
    return out


def deserialize_cbor(data: dict) -> FixedUpfrontPricingTerm:
    out: FixedUpfrontPricingTerm = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        out["type"] = data["type"]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("currencyCode") is not None:
        out["currency_code"] = data["currencyCode"]
    if data.get("duration") is not None:
        out["duration"] = data["duration"]
    if data.get("price") is not None:
        out["price"] = data["price"]
    if data.get("grants") is not None:
        import capo_marketplace_agreement.types.grant_list

        out["grants"] = capo_marketplace_agreement.types.grant_list.deserialize_cbor(
            data["grants"]
        )
    return out
