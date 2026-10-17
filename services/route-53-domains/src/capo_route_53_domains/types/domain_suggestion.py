"""Generated from Smithy shape ``com.amazonaws.route53domains#DomainSuggestion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route_53_domains.types.domain_name
    import capo_route_53_domains.types.string


class DomainSuggestion(TypedDict, closed=True):
    domain_name: NotRequired["capo_route_53_domains.types.domain_name.DomainName"]
    """<p>A suggested domain name.</p>"""
    availability: NotRequired["capo_route_53_domains.types.string.String"]
    """<p>Whether the domain name is available for registering.</p> <note> <p>You can register only the domains that are designated as <code>AVAILABLE</code>.</p> </note> <p>Valid values:</p> <dl> <dt>AVAILABLE</dt> <dd> <p>The domain name is available.</p> </dd> <dt>AVAILABLE_RESERVED</dt> <dd> <p>The domain name is reserved under specific conditions.</p> </dd> <dt>AVAILABLE_PREORDER</dt> <dd> <p>The domain name is available and can be preordered.</p> </dd> <dt>DONT_KNOW</dt> <dd> <p>The TLD registry didn't reply with a definitive answer about whether the domain name is available. Route 53 can return this response for a variety of reasons, for example, the registry is performing maintenance. Try again later.</p> </dd> <dt>PENDING</dt> <dd> <p>The TLD registry didn't return a response in the expected amount of time. When the response is delayed, it usually takes just a few extra seconds. You can resubmit the request immediately.</p> </dd> <dt>RESERVED</dt> <dd> <p>The domain name has been reserved for another person or organization.</p> </dd> <dt>UNAVAILABLE</dt> <dd> <p>The domain name is not available.</p> </dd> <dt>UNAVAILABLE_PREMIUM</dt> <dd> <p>The domain name is not available.</p> </dd> <dt>UNAVAILABLE_RESTRICTED</dt> <dd> <p>The domain name is forbidden.</p> </dd> </dl>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DomainSuggestion) -> dict:
    out: dict = {}
    if "domain_name" in value:
        out["DomainName"] = value["domain_name"]
    if "availability" in value:
        out["Availability"] = value["availability"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DomainSuggestion:
    out: DomainSuggestion = {}  # type: ignore[typeddict-item]
    if data.get("DomainName") is not None:
        out["domain_name"] = data["DomainName"]
    if data.get("Availability") is not None:
        out["availability"] = data["Availability"]
    return out
