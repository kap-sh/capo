"""Generated from Smithy shape ``com.amazonaws.route53domains#PriceWithCurrency``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route_53_domains.types.currency
    import capo_route_53_domains.types.price
    import capo_route_53_domains.types.price_type


class PriceWithCurrency(TypedDict, closed=True):
    price: "capo_route_53_domains.types.price.Price"
    """<p>The price of a domain, in a specific currency.</p>"""
    currency: "capo_route_53_domains.types.currency.Currency"
    """<p>The currency specifier.</p>"""
    price_type: NotRequired["capo_route_53_domains.types.price_type.PriceType"]
    """<p>Indicates whether the domain has standard or premium pricing. A value of <code>STANDARD</code> means the domain is priced at the regular rate for its TLD. A value of <code>REGISTRY_PREMIUM</code> means the domain has registry premium pricing, which may be different than the standard rate.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PriceWithCurrency) -> dict:
    out: dict = {}
    out["Price"] = (
        "NaN"
        if value.get("price", 0) != value.get("price", 0)
        else "Infinity"
        if value.get("price", 0) == float("inf")
        else "-Infinity"
        if value.get("price", 0) == float("-inf")
        else value.get("price", 0)
    )
    out["Currency"] = value["currency"]
    if "price_type" in value:
        import capo_route_53_domains.types.price_type

        out["PriceType"] = (
            capo_route_53_domains.types.price_type.serialize_aws_json_1_1(
                value["price_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PriceWithCurrency:
    out: PriceWithCurrency = {}  # type: ignore[typeddict-item]
    if data.get("Price") is not None:
        out["price"] = float(data["Price"])
    else:
        out["price"] = 0
    if data.get("Currency") is not None:
        out["currency"] = data["Currency"]
    else:
        out["currency"] = ""
    if data.get("PriceType") is not None:
        import capo_route_53_domains.types.price_type

        out["price_type"] = (
            capo_route_53_domains.types.price_type.deserialize_aws_json_1_1(
                data["PriceType"]
            )
        )
    return out
