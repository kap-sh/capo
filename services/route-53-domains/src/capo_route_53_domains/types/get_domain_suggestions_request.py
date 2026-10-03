"""Generated from Smithy shape ``com.amazonaws.route53domains#GetDomainSuggestionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_route_53_domains.errors import DeserializationError

if TYPE_CHECKING:
    import capo_route_53_domains.types.boolean
    import capo_route_53_domains.types.domain_name
    import capo_route_53_domains.types.integer


class GetDomainSuggestionsRequest(TypedDict, closed=True):
    domain_name: "capo_route_53_domains.types.domain_name.DomainName"
    """<p>A domain name that you want to use as the basis for a list of possible domain names. The top-level domain (TLD), such as .com, must be a TLD that Route 53 supports. For a list of supported TLDs, see <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/registrar-tld-list.html">Domains that You Can Register with Amazon Route 53</a> in the <i>Amazon Route 53 Developer Guide</i>.</p> <p>The domain name can contain only the following characters:</p> <ul> <li> <p>Letters a through z. Domain names are not case sensitive.</p> </li> <li> <p>Numbers 0 through 9.</p> </li> <li> <p>Hyphen (-). You can't specify a hyphen at the beginning or end of a label. </p> </li> <li> <p>Period (.) to separate the labels in the name, such as the <code>.</code> in <code>example.com</code>.</p> </li> </ul> <p>Internationalized domain names are not supported for some top-level domains. To determine whether the TLD that you want to use supports internationalized domain names, see <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/registrar-tld-list.html">Domains that You Can Register with Amazon Route 53</a>. </p>"""
    suggestion_count: "capo_route_53_domains.types.integer.Integer"
    """<p>The number of suggested domain names that you want Route 53 to return. Specify a value between 1 and 50. Note that fewer than the requested number might be returned.</p>"""
    only_available: "capo_route_53_domains.types.boolean.Boolean"
    """<p>If <code>OnlyAvailable</code> is <code>true</code>, Route 53 returns only domain names that are available. If <code>OnlyAvailable</code> is <code>false</code>, Route 53 returns domain names without checking whether they're available to be registered. To determine whether the domain is available, you can call <code>checkDomainAvailability</code> for each suggestion.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDomainSuggestionsRequest) -> dict:
    out: dict = {}
    out["DomainName"] = value["domain_name"]
    out["SuggestionCount"] = value.get("suggestion_count", 0)
    out["OnlyAvailable"] = value["only_available"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDomainSuggestionsRequest:
    out: GetDomainSuggestionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("DomainName") is not None:
        out["domain_name"] = data["DomainName"]
    else:
        raise DeserializationError("GetDomainSuggestionsRequest.domain_name required")
    if data.get("SuggestionCount") is not None:
        out["suggestion_count"] = data["SuggestionCount"]
    else:
        out["suggestion_count"] = 0
    if data.get("OnlyAvailable") is not None:
        out["only_available"] = data["OnlyAvailable"]
    else:
        raise DeserializationError(
            "GetDomainSuggestionsRequest.only_available required"
        )
    return out
