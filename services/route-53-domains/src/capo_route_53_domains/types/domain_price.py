"""Generated from Smithy shape ``com.amazonaws.route53domains#DomainPrice``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route_53_domains.types.domain_price_name
    import capo_route_53_domains.types.price_with_currency


class DomainPrice(TypedDict, closed=True):
    name: NotRequired["capo_route_53_domains.types.domain_price_name.DomainPriceName"]
    """<p>The name of the TLD for which the prices apply.</p>"""
    registration_price: NotRequired[
        "capo_route_53_domains.types.price_with_currency.PriceWithCurrency"
    ]
    """<p>The price for domain registration with Route 53.</p>"""
    transfer_price: NotRequired[
        "capo_route_53_domains.types.price_with_currency.PriceWithCurrency"
    ]
    """<p>The price for transferring the domain registration to Route 53.</p>"""
    renewal_price: NotRequired[
        "capo_route_53_domains.types.price_with_currency.PriceWithCurrency"
    ]
    """<p>The price for renewing domain registration with Route 53.</p>"""
    change_ownership_price: NotRequired[
        "capo_route_53_domains.types.price_with_currency.PriceWithCurrency"
    ]
    """<p>The price for changing domain ownership.</p>"""
    restoration_price: NotRequired[
        "capo_route_53_domains.types.price_with_currency.PriceWithCurrency"
    ]
    """<p>The price for restoring the domain with Route 53.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DomainPrice) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "registration_price" in value:
        import capo_route_53_domains.types.price_with_currency

        out["RegistrationPrice"] = (
            capo_route_53_domains.types.price_with_currency.serialize_aws_json_1_1(
                value["registration_price"]
            )
        )
    if "transfer_price" in value:
        import capo_route_53_domains.types.price_with_currency

        out["TransferPrice"] = (
            capo_route_53_domains.types.price_with_currency.serialize_aws_json_1_1(
                value["transfer_price"]
            )
        )
    if "renewal_price" in value:
        import capo_route_53_domains.types.price_with_currency

        out["RenewalPrice"] = (
            capo_route_53_domains.types.price_with_currency.serialize_aws_json_1_1(
                value["renewal_price"]
            )
        )
    if "change_ownership_price" in value:
        import capo_route_53_domains.types.price_with_currency

        out["ChangeOwnershipPrice"] = (
            capo_route_53_domains.types.price_with_currency.serialize_aws_json_1_1(
                value["change_ownership_price"]
            )
        )
    if "restoration_price" in value:
        import capo_route_53_domains.types.price_with_currency

        out["RestorationPrice"] = (
            capo_route_53_domains.types.price_with_currency.serialize_aws_json_1_1(
                value["restoration_price"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DomainPrice:
    out: DomainPrice = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("RegistrationPrice") is not None:
        import capo_route_53_domains.types.price_with_currency

        out["registration_price"] = (
            capo_route_53_domains.types.price_with_currency.deserialize_aws_json_1_1(
                data["RegistrationPrice"]
            )
        )
    if data.get("TransferPrice") is not None:
        import capo_route_53_domains.types.price_with_currency

        out["transfer_price"] = (
            capo_route_53_domains.types.price_with_currency.deserialize_aws_json_1_1(
                data["TransferPrice"]
            )
        )
    if data.get("RenewalPrice") is not None:
        import capo_route_53_domains.types.price_with_currency

        out["renewal_price"] = (
            capo_route_53_domains.types.price_with_currency.deserialize_aws_json_1_1(
                data["RenewalPrice"]
            )
        )
    if data.get("ChangeOwnershipPrice") is not None:
        import capo_route_53_domains.types.price_with_currency

        out["change_ownership_price"] = (
            capo_route_53_domains.types.price_with_currency.deserialize_aws_json_1_1(
                data["ChangeOwnershipPrice"]
            )
        )
    if data.get("RestorationPrice") is not None:
        import capo_route_53_domains.types.price_with_currency

        out["restoration_price"] = (
            capo_route_53_domains.types.price_with_currency.deserialize_aws_json_1_1(
                data["RestorationPrice"]
            )
        )
    return out
