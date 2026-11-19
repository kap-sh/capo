"""Generated from Smithy shape ``com.amazonaws.route53domains#ResendContactReachabilityEmailRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route_53_domains.types.domain_name


class ResendContactReachabilityEmailRequest(TypedDict, closed=True):
    domain_name: NotRequired["capo_route_53_domains.types.domain_name.DomainName"]
    """<p>The name of the domain for which you want Route 53 to resend a confirmation email to the registrant contact.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResendContactReachabilityEmailRequest) -> dict:
    out: dict = {}
    if "domain_name" in value:
        out["domainName"] = value["domain_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResendContactReachabilityEmailRequest:
    out: ResendContactReachabilityEmailRequest = {}  # type: ignore[typeddict-item]
    if data.get("domainName") is not None:
        out["domain_name"] = data["domainName"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ResendContactReachabilityEmailRequest) -> dict:
    out: dict = {}
    if "domain_name" in value:
        out["domainName"] = value["domain_name"]
    return out


def deserialize_cbor(data: dict) -> ResendContactReachabilityEmailRequest:
    out: ResendContactReachabilityEmailRequest = {}  # type: ignore[typeddict-item]
    if data.get("domainName") is not None:
        out["domain_name"] = data["domainName"]
    return out
