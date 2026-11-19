"""Generated from Smithy shape ``com.amazonaws.route53domains#GetContactReachabilityStatusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route_53_domains.types.domain_name


class GetContactReachabilityStatusRequest(TypedDict, closed=True):
    domain_name: NotRequired["capo_route_53_domains.types.domain_name.DomainName"]
    """<p>The name of the domain for which you want to know whether the registrant contact has confirmed that the email address is valid.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetContactReachabilityStatusRequest) -> dict:
    out: dict = {}
    if "domain_name" in value:
        out["domainName"] = value["domain_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetContactReachabilityStatusRequest:
    out: GetContactReachabilityStatusRequest = {}  # type: ignore[typeddict-item]
    if data.get("domainName") is not None:
        out["domain_name"] = data["domainName"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetContactReachabilityStatusRequest) -> dict:
    out: dict = {}
    if "domain_name" in value:
        out["domainName"] = value["domain_name"]
    return out


def deserialize_cbor(data: dict) -> GetContactReachabilityStatusRequest:
    out: GetContactReachabilityStatusRequest = {}  # type: ignore[typeddict-item]
    if data.get("domainName") is not None:
        out["domain_name"] = data["domainName"]
    return out
