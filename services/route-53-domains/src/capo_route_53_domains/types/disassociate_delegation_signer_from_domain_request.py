"""Generated from Smithy shape ``com.amazonaws.route53domains#DisassociateDelegationSignerFromDomainRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_route_53_domains.errors import DeserializationError

if TYPE_CHECKING:
    import capo_route_53_domains.types.domain_name
    import capo_route_53_domains.types.string


class DisassociateDelegationSignerFromDomainRequest(TypedDict, closed=True):
    domain_name: "capo_route_53_domains.types.domain_name.DomainName"
    """<p>Name of the domain.</p>"""
    id: "capo_route_53_domains.types.string.String"
    """<p>An internal identification number assigned to each DS record after it’s created. You can retrieve it as part of DNSSEC information returned by <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_GetDomainDetail.html">GetDomainDetail</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DisassociateDelegationSignerFromDomainRequest,
) -> dict:
    out: dict = {}
    out["DomainName"] = value["domain_name"]
    out["Id"] = value["id"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DisassociateDelegationSignerFromDomainRequest:
    out: DisassociateDelegationSignerFromDomainRequest = {}  # type: ignore[typeddict-item]
    if data.get("DomainName") is not None:
        out["domain_name"] = data["DomainName"]
    else:
        raise DeserializationError(
            "DisassociateDelegationSignerFromDomainRequest.domain_name required"
        )
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        raise DeserializationError(
            "DisassociateDelegationSignerFromDomainRequest.id required"
        )
    return out
