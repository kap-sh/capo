"""Generated from Smithy shape ``com.amazonaws.route53domains#CheckDomainTransferabilityResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route_53_domains.types.domain_transferability
    import capo_route_53_domains.types.message
    import capo_route_53_domains.types.price_with_currency


class CheckDomainTransferabilityResponse(TypedDict, closed=True):
    transferability: NotRequired[
        "capo_route_53_domains.types.domain_transferability.DomainTransferability"
    ]
    """<p>A complex type that contains information about whether the specified domain can be transferred to Route 53.</p>"""
    message: NotRequired["capo_route_53_domains.types.message.Message"]
    """<p>Provides an explanation for when a domain can't be transferred.</p>"""
    price: NotRequired[
        "capo_route_53_domains.types.price_with_currency.PriceWithCurrency"
    ]
    """<p>The price to transfer the domain name to Route 53, in the currency that <code>Currency</code> specifies. If the domain has registry premium pricing, this price is different from the standard rate for the TLD that <code>ListPrices</code> returns. Use <code>PriceType</code> to determine which rate applies.</p> <p>This element is returned only when Route 53 can determine whether the domain is transferable.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CheckDomainTransferabilityResponse) -> dict:
    out: dict = {}
    if "transferability" in value:
        import capo_route_53_domains.types.domain_transferability

        out["Transferability"] = (
            capo_route_53_domains.types.domain_transferability.serialize_aws_json_1_1(
                value["transferability"]
            )
        )
    if "message" in value:
        out["Message"] = value["message"]
    if "price" in value:
        import capo_route_53_domains.types.price_with_currency

        out["Price"] = (
            capo_route_53_domains.types.price_with_currency.serialize_aws_json_1_1(
                value["price"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CheckDomainTransferabilityResponse:
    out: CheckDomainTransferabilityResponse = {}  # type: ignore[typeddict-item]
    if data.get("Transferability") is not None:
        import capo_route_53_domains.types.domain_transferability

        out["transferability"] = (
            capo_route_53_domains.types.domain_transferability.deserialize_aws_json_1_1(
                data["Transferability"]
            )
        )
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("Price") is not None:
        import capo_route_53_domains.types.price_with_currency

        out["price"] = (
            capo_route_53_domains.types.price_with_currency.deserialize_aws_json_1_1(
                data["Price"]
            )
        )
    return out
