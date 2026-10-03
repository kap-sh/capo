"""Generated from Smithy shape ``com.amazonaws.route53domains#CheckDomainTransferabilityRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_route_53_domains.errors import DeserializationError

if TYPE_CHECKING:
    import capo_route_53_domains.types.domain_auth_code
    import capo_route_53_domains.types.domain_name


class CheckDomainTransferabilityRequest(TypedDict, closed=True):
    domain_name: "capo_route_53_domains.types.domain_name.DomainName"
    """<p>The name of the domain that you want to transfer to Route 53. The top-level domain (TLD), such as .com, must be a TLD that Route 53 supports. For a list of supported TLDs, see <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/registrar-tld-list.html">Domains that You Can Register with Amazon Route 53</a> in the <i>Amazon Route 53 Developer Guide</i>.</p> <p>The domain name can contain only the following characters:</p> <ul> <li> <p>Letters a through z. Domain names are not case sensitive.</p> </li> <li> <p>Numbers 0 through 9.</p> </li> <li> <p>Hyphen (-). You can't specify a hyphen at the beginning or end of a label. </p> </li> <li> <p>Period (.) to separate the labels in the name, such as the <code>.</code> in <code>example.com</code>.</p> </li> </ul>"""
    auth_code: NotRequired[
        "capo_route_53_domains.types.domain_auth_code.DomainAuthCode"
    ]
    """<p>If the registrar for the top-level domain (TLD) requires an authorization code to transfer the domain, the code that you got from the current registrar for the domain.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CheckDomainTransferabilityRequest) -> dict:
    out: dict = {}
    out["DomainName"] = value["domain_name"]
    if "auth_code" in value:
        out["AuthCode"] = value["auth_code"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CheckDomainTransferabilityRequest:
    out: CheckDomainTransferabilityRequest = {}  # type: ignore[typeddict-item]
    if data.get("DomainName") is not None:
        out["domain_name"] = data["DomainName"]
    else:
        raise DeserializationError(
            "CheckDomainTransferabilityRequest.domain_name required"
        )
    if data.get("AuthCode") is not None:
        out["auth_code"] = data["AuthCode"]
    return out
