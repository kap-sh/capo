"""Generated from Smithy shape ``com.amazonaws.servicediscovery#DnsProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_servicediscovery.types.resource_id
    import capo_servicediscovery.types.soa


class DnsProperties(TypedDict, closed=True):
    hosted_zone_id: NotRequired["capo_servicediscovery.types.resource_id.ResourceId"]
    """<p>The ID for the Route 53 hosted zone that Cloud Map creates when you create a namespace.</p>"""
    soa: NotRequired["capo_servicediscovery.types.soa.SOA"]
    """<p>Start of Authority (SOA) record for the hosted zone.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DnsProperties) -> dict:
    out: dict = {}
    if "hosted_zone_id" in value:
        out["HostedZoneId"] = value["hosted_zone_id"]
    if "soa" in value:
        import capo_servicediscovery.types.soa

        out["SOA"] = capo_servicediscovery.types.soa.serialize_aws_json_1_1(
            value["soa"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DnsProperties:
    out: DnsProperties = {}  # type: ignore[typeddict-item]
    if data.get("HostedZoneId") is not None:
        out["hosted_zone_id"] = data["HostedZoneId"]
    if data.get("SOA") is not None:
        import capo_servicediscovery.types.soa

        out["soa"] = capo_servicediscovery.types.soa.deserialize_aws_json_1_1(
            data["SOA"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DnsProperties) -> dict:
    out: dict = {}
    if "hosted_zone_id" in value:
        out["HostedZoneId"] = value["hosted_zone_id"]
    if "soa" in value:
        import capo_servicediscovery.types.soa

        out["SOA"] = capo_servicediscovery.types.soa.serialize_cbor(value["soa"])
    return out


def deserialize_cbor(data: dict) -> DnsProperties:
    out: DnsProperties = {}  # type: ignore[typeddict-item]
    if data.get("HostedZoneId") is not None:
        out["hosted_zone_id"] = data["HostedZoneId"]
    if data.get("SOA") is not None:
        import capo_servicediscovery.types.soa

        out["soa"] = capo_servicediscovery.types.soa.deserialize_cbor(data["SOA"])
    return out
