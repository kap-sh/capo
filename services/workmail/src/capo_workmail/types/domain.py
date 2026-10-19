"""Generated from Smithy shape ``com.amazonaws.workmail#Domain``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workmail.types.domain_name
    import capo_workmail.types.hosted_zone_id


class Domain(TypedDict, closed=True):
    domain_name: "capo_workmail.types.domain_name.DomainName"
    """<p>The fully qualified domain name.</p>"""
    hosted_zone_id: NotRequired["capo_workmail.types.hosted_zone_id.HostedZoneId"]
    """<p>The hosted zone ID for a domain hosted in Route 53. Required when configuring a domain hosted in Route 53.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Domain) -> dict:
    out: dict = {}
    out["DomainName"] = value["domain_name"]
    if "hosted_zone_id" in value:
        out["HostedZoneId"] = value["hosted_zone_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Domain:
    out: Domain = {}  # type: ignore[typeddict-item]
    if data.get("DomainName") is not None:
        out["domain_name"] = data["DomainName"]
    else:
        out["domain_name"] = ""
    if data.get("HostedZoneId") is not None:
        out["hosted_zone_id"] = data["HostedZoneId"]
    return out
