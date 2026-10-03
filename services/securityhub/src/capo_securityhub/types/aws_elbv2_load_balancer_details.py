"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsElbv2LoadBalancerDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.availability_zones
    import capo_securityhub.types.aws_elbv2_load_balancer_attributes
    import capo_securityhub.types.load_balancer_state
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.security_groups


class AwsElbv2LoadBalancerDetails(TypedDict, closed=True):
    availability_zones: NotRequired[
        "capo_securityhub.types.availability_zones.AvailabilityZones"
    ]
    """<p>The Availability Zones for the load balancer.</p>"""
    canonical_hosted_zone_id: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ID of the Amazon Route 53 hosted zone associated with the load balancer.</p>"""
    created_time: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>Indicates when the load balancer was created.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps">Timestamps</a>.</p>"""
    dns_name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The public DNS name of the load balancer.</p>"""
    ip_address_type: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The type of IP addresses used by the subnets for your load balancer. The possible values are <code>ipv4</code> (for IPv4 addresses) and <code>dualstack</code> (for IPv4 and IPv6 addresses).</p>"""
    scheme: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The nodes of an Internet-facing load balancer have public IP addresses.</p>"""
    security_groups: NotRequired[
        "capo_securityhub.types.security_groups.SecurityGroups"
    ]
    """<p>The IDs of the security groups for the load balancer.</p>"""
    state: NotRequired["capo_securityhub.types.load_balancer_state.LoadBalancerState"]
    """<p>The state of the load balancer.</p>"""
    type: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The type of load balancer.</p>"""
    vpc_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ID of the VPC for the load balancer.</p>"""
    load_balancer_attributes: NotRequired[
        "capo_securityhub.types.aws_elbv2_load_balancer_attributes.AwsElbv2LoadBalancerAttributes"
    ]
    """<p>Attributes of the load balancer.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsElbv2LoadBalancerDetails) -> dict:
    out: dict = {}
    if "availability_zones" in value:
        import capo_securityhub.types.availability_zones

        out["AvailabilityZones"] = (
            capo_securityhub.types.availability_zones.serialize_json(
                value["availability_zones"]
            )
        )
    if "canonical_hosted_zone_id" in value:
        out["CanonicalHostedZoneId"] = value["canonical_hosted_zone_id"]
    if "created_time" in value:
        out["CreatedTime"] = value["created_time"]
    if "dns_name" in value:
        out["DNSName"] = value["dns_name"]
    if "ip_address_type" in value:
        out["IpAddressType"] = value["ip_address_type"]
    if "scheme" in value:
        out["Scheme"] = value["scheme"]
    if "security_groups" in value:
        import capo_securityhub.types.security_groups

        out["SecurityGroups"] = capo_securityhub.types.security_groups.serialize_json(
            value["security_groups"]
        )
    if "state" in value:
        import capo_securityhub.types.load_balancer_state

        out["State"] = capo_securityhub.types.load_balancer_state.serialize_json(
            value["state"]
        )
    if "type" in value:
        out["Type"] = value["type"]
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    if "load_balancer_attributes" in value:
        import capo_securityhub.types.aws_elbv2_load_balancer_attributes

        out["LoadBalancerAttributes"] = (
            capo_securityhub.types.aws_elbv2_load_balancer_attributes.serialize_json(
                value["load_balancer_attributes"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsElbv2LoadBalancerDetails:
    out: AwsElbv2LoadBalancerDetails = {}  # type: ignore[typeddict-item]
    if data.get("AvailabilityZones") is not None:
        import capo_securityhub.types.availability_zones

        out["availability_zones"] = (
            capo_securityhub.types.availability_zones.deserialize_json(
                data["AvailabilityZones"]
            )
        )
    if data.get("CanonicalHostedZoneId") is not None:
        out["canonical_hosted_zone_id"] = data["CanonicalHostedZoneId"]
    if data.get("CreatedTime") is not None:
        out["created_time"] = data["CreatedTime"]
    if data.get("DNSName") is not None:
        out["dns_name"] = data["DNSName"]
    if data.get("IpAddressType") is not None:
        out["ip_address_type"] = data["IpAddressType"]
    if data.get("Scheme") is not None:
        out["scheme"] = data["Scheme"]
    if data.get("SecurityGroups") is not None:
        import capo_securityhub.types.security_groups

        out["security_groups"] = (
            capo_securityhub.types.security_groups.deserialize_json(
                data["SecurityGroups"]
            )
        )
    if data.get("State") is not None:
        import capo_securityhub.types.load_balancer_state

        out["state"] = capo_securityhub.types.load_balancer_state.deserialize_json(
            data["State"]
        )
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    if data.get("VpcId") is not None:
        out["vpc_id"] = data["VpcId"]
    if data.get("LoadBalancerAttributes") is not None:
        import capo_securityhub.types.aws_elbv2_load_balancer_attributes

        out["load_balancer_attributes"] = (
            capo_securityhub.types.aws_elbv2_load_balancer_attributes.deserialize_json(
                data["LoadBalancerAttributes"]
            )
        )
    return out
