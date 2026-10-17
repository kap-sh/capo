"""Generated from Smithy shape ``com.amazonaws.route53domains#Consent``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_route_53_domains.errors import DeserializationError

if TYPE_CHECKING:
    import capo_route_53_domains.types.currency
    import capo_route_53_domains.types.price


class Consent(TypedDict, closed=True):
    max_price: "capo_route_53_domains.types.price.Price"
    """<p> Maximum amount the customer agreed to accept. </p>"""
    currency: "capo_route_53_domains.types.currency.Currency"
    """<p> Currency for the <code>MaxPrice</code>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Consent) -> dict:
    out: dict = {}
    out["MaxPrice"] = (
        "NaN"
        if value.get("max_price", 0) != value.get("max_price", 0)
        else "Infinity"
        if value.get("max_price", 0) == float("inf")
        else "-Infinity"
        if value.get("max_price", 0) == float("-inf")
        else value.get("max_price", 0)
    )
    out["Currency"] = value["currency"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Consent:
    out: Consent = {}  # type: ignore[typeddict-item]
    if data.get("MaxPrice") is not None:
        out["max_price"] = float(data["MaxPrice"])
    else:
        out["max_price"] = 0
    if data.get("Currency") is not None:
        out["currency"] = data["Currency"]
    else:
        raise DeserializationError("Consent.currency required")
    return out
