"""Generated from Smithy shape ``com.amazonaws.route53domains#RenewDomainRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_route_53_domains.errors import DeserializationError

if TYPE_CHECKING:
    import capo_route_53_domains.types.current_expiry_year
    import capo_route_53_domains.types.domain_name
    import capo_route_53_domains.types.duration_in_years


class RenewDomainRequest(TypedDict, closed=True):
    domain_name: "capo_route_53_domains.types.domain_name.DomainName"
    """<p>The name of the domain that you want to renew.</p>"""
    duration_in_years: NotRequired[
        "capo_route_53_domains.types.duration_in_years.DurationInYears"
    ]
    """<p>The number of years that you want to renew the domain for. The maximum number of years depends on the top-level domain. For the range of valid values for your domain, see <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/registrar-tld-list.html">Domains that You Can Register with Amazon Route 53</a> in the <i>Amazon Route 53 Developer Guide</i>.</p> <p>Default: 1</p>"""
    current_expiry_year: (
        "capo_route_53_domains.types.current_expiry_year.CurrentExpiryYear"
    )
    """<p>The year when the registration for the domain is set to expire. This value must match the current expiration date for the domain.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RenewDomainRequest) -> dict:
    out: dict = {}
    out["DomainName"] = value["domain_name"]
    if "duration_in_years" in value:
        out["DurationInYears"] = value["duration_in_years"]
    out["CurrentExpiryYear"] = value.get("current_expiry_year", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> RenewDomainRequest:
    out: RenewDomainRequest = {}  # type: ignore[typeddict-item]
    if data.get("DomainName") is not None:
        out["domain_name"] = data["DomainName"]
    else:
        raise DeserializationError("RenewDomainRequest.domain_name required")
    if data.get("DurationInYears") is not None:
        out["duration_in_years"] = data["DurationInYears"]
    if data.get("CurrentExpiryYear") is not None:
        out["current_expiry_year"] = data["CurrentExpiryYear"]
    else:
        out["current_expiry_year"] = 0
    return out
