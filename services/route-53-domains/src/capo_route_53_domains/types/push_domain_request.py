"""Generated from Smithy shape ``com.amazonaws.route53domains#PushDomainRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_route_53_domains.types.domain_name
    import capo_route_53_domains.types.label


class PushDomainRequest(TypedDict, closed=True):
    domain_name: "capo_route_53_domains.types.domain_name.DomainName"
    """<p> Name of the domain. </p>"""
    target: "capo_route_53_domains.types.label.Label"
    """<p> New IPS tag for the domain. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PushDomainRequest) -> dict:
    out: dict = {}
    out["DomainName"] = value["domain_name"]
    out["Target"] = value["target"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PushDomainRequest:
    out: PushDomainRequest = {}  # type: ignore[typeddict-item]
    if data.get("DomainName") is not None:
        out["domain_name"] = data["DomainName"]
    else:
        out["domain_name"] = ""
    if data.get("Target") is not None:
        out["target"] = data["Target"]
    else:
        out["target"] = ""
    return out
