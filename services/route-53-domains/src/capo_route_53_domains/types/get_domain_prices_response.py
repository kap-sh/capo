"""Generated from Smithy shape ``com.amazonaws.route53domains#GetDomainPricesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route_53_domains.types.domain_price


class GetDomainPricesResponse(TypedDict, closed=True):
    domain_price: NotRequired["capo_route_53_domains.types.domain_price.DomainPrice"]
    """<p>The registration, transfer, owner change, renewal, and restoration prices for the specified domain.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDomainPricesResponse) -> dict:
    out: dict = {}
    if "domain_price" in value:
        import capo_route_53_domains.types.domain_price

        out["DomainPrice"] = (
            capo_route_53_domains.types.domain_price.serialize_aws_json_1_1(
                value["domain_price"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDomainPricesResponse:
    out: GetDomainPricesResponse = {}  # type: ignore[typeddict-item]
    if data.get("DomainPrice") is not None:
        import capo_route_53_domains.types.domain_price

        out["domain_price"] = (
            capo_route_53_domains.types.domain_price.deserialize_aws_json_1_1(
                data["DomainPrice"]
            )
        )
    return out
