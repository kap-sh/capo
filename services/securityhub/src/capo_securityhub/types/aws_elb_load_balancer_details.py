"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsElbLoadBalancerDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_elb_load_balancer_attributes
    import capo_securityhub.types.aws_elb_load_balancer_backend_server_descriptions
    import capo_securityhub.types.aws_elb_load_balancer_health_check
    import capo_securityhub.types.aws_elb_load_balancer_instances
    import capo_securityhub.types.aws_elb_load_balancer_listener_descriptions
    import capo_securityhub.types.aws_elb_load_balancer_policies
    import capo_securityhub.types.aws_elb_load_balancer_source_security_group
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.string_list


class AwsElbLoadBalancerDetails(TypedDict, closed=True):
    availability_zones: NotRequired["capo_securityhub.types.string_list.StringList"]
    """<p>The list of Availability Zones for the load balancer.</p>"""
    backend_server_descriptions: NotRequired[
        "capo_securityhub.types.aws_elb_load_balancer_backend_server_descriptions.AwsElbLoadBalancerBackendServerDescriptions"
    ]
    """<p>Information about the configuration of the EC2 instances.</p>"""
    canonical_hosted_zone_name: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the Amazon Route 53 hosted zone for the load balancer.</p>"""
    canonical_hosted_zone_name_id: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ID of the Amazon Route 53 hosted zone for the load balancer.</p>"""
    created_time: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>Indicates when the load balancer was created.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps">Timestamps</a>.</p>"""
    dns_name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The DNS name of the load balancer.</p>"""
    health_check: NotRequired[
        "capo_securityhub.types.aws_elb_load_balancer_health_check.AwsElbLoadBalancerHealthCheck"
    ]
    """<p>Information about the health checks that are conducted on the load balancer.</p>"""
    instances: NotRequired[
        "capo_securityhub.types.aws_elb_load_balancer_instances.AwsElbLoadBalancerInstances"
    ]
    """<p>List of EC2 instances for the load balancer.</p>"""
    listener_descriptions: NotRequired[
        "capo_securityhub.types.aws_elb_load_balancer_listener_descriptions.AwsElbLoadBalancerListenerDescriptions"
    ]
    """<p>The policies that are enabled for the load balancer listeners.</p>"""
    load_balancer_attributes: NotRequired[
        "capo_securityhub.types.aws_elb_load_balancer_attributes.AwsElbLoadBalancerAttributes"
    ]
    """<p>The attributes for a load balancer.</p>"""
    load_balancer_name: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the load balancer.</p>"""
    policies: NotRequired[
        "capo_securityhub.types.aws_elb_load_balancer_policies.AwsElbLoadBalancerPolicies"
    ]
    """<p>The policies for a load balancer.</p>"""
    scheme: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The type of load balancer. Only provided if the load balancer is in a VPC.</p> <p>If <code>Scheme</code> is <code>internet-facing</code>, the load balancer has a public DNS name that resolves to a public IP address.</p> <p>If <code>Scheme</code> is <code>internal</code>, the load balancer has a public DNS name that resolves to a private IP address.</p>"""
    security_groups: NotRequired["capo_securityhub.types.string_list.StringList"]
    """<p>The security groups for the load balancer. Only provided if the load balancer is in a VPC.</p>"""
    source_security_group: NotRequired[
        "capo_securityhub.types.aws_elb_load_balancer_source_security_group.AwsElbLoadBalancerSourceSecurityGroup"
    ]
    """<p>Information about the security group for the load balancer. This is the security group that is used for inbound rules.</p>"""
    subnets: NotRequired["capo_securityhub.types.string_list.StringList"]
    """<p>The list of subnet identifiers for the load balancer.</p>"""
    vpc_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The identifier of the VPC for the load balancer.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsElbLoadBalancerDetails) -> dict:
    out: dict = {}
    if "availability_zones" in value:
        import capo_securityhub.types.string_list

        out["AvailabilityZones"] = capo_securityhub.types.string_list.serialize_json(
            value["availability_zones"]
        )
    if "backend_server_descriptions" in value:
        import capo_securityhub.types.aws_elb_load_balancer_backend_server_descriptions

        out["BackendServerDescriptions"] = (
            capo_securityhub.types.aws_elb_load_balancer_backend_server_descriptions.serialize_json(
                value["backend_server_descriptions"]
            )
        )
    if "canonical_hosted_zone_name" in value:
        out["CanonicalHostedZoneName"] = value["canonical_hosted_zone_name"]
    if "canonical_hosted_zone_name_id" in value:
        out["CanonicalHostedZoneNameID"] = value["canonical_hosted_zone_name_id"]
    if "created_time" in value:
        out["CreatedTime"] = value["created_time"]
    if "dns_name" in value:
        out["DnsName"] = value["dns_name"]
    if "health_check" in value:
        import capo_securityhub.types.aws_elb_load_balancer_health_check

        out["HealthCheck"] = (
            capo_securityhub.types.aws_elb_load_balancer_health_check.serialize_json(
                value["health_check"]
            )
        )
    if "instances" in value:
        import capo_securityhub.types.aws_elb_load_balancer_instances

        out["Instances"] = (
            capo_securityhub.types.aws_elb_load_balancer_instances.serialize_json(
                value["instances"]
            )
        )
    if "listener_descriptions" in value:
        import capo_securityhub.types.aws_elb_load_balancer_listener_descriptions

        out["ListenerDescriptions"] = (
            capo_securityhub.types.aws_elb_load_balancer_listener_descriptions.serialize_json(
                value["listener_descriptions"]
            )
        )
    if "load_balancer_attributes" in value:
        import capo_securityhub.types.aws_elb_load_balancer_attributes

        out["LoadBalancerAttributes"] = (
            capo_securityhub.types.aws_elb_load_balancer_attributes.serialize_json(
                value["load_balancer_attributes"]
            )
        )
    if "load_balancer_name" in value:
        out["LoadBalancerName"] = value["load_balancer_name"]
    if "policies" in value:
        import capo_securityhub.types.aws_elb_load_balancer_policies

        out["Policies"] = (
            capo_securityhub.types.aws_elb_load_balancer_policies.serialize_json(
                value["policies"]
            )
        )
    if "scheme" in value:
        out["Scheme"] = value["scheme"]
    if "security_groups" in value:
        import capo_securityhub.types.string_list

        out["SecurityGroups"] = capo_securityhub.types.string_list.serialize_json(
            value["security_groups"]
        )
    if "source_security_group" in value:
        import capo_securityhub.types.aws_elb_load_balancer_source_security_group

        out["SourceSecurityGroup"] = (
            capo_securityhub.types.aws_elb_load_balancer_source_security_group.serialize_json(
                value["source_security_group"]
            )
        )
    if "subnets" in value:
        import capo_securityhub.types.string_list

        out["Subnets"] = capo_securityhub.types.string_list.serialize_json(
            value["subnets"]
        )
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    return out


def deserialize_json(data: dict) -> AwsElbLoadBalancerDetails:
    out: AwsElbLoadBalancerDetails = {}  # type: ignore[typeddict-item]
    if data.get("AvailabilityZones") is not None:
        import capo_securityhub.types.string_list

        out["availability_zones"] = capo_securityhub.types.string_list.deserialize_json(
            data["AvailabilityZones"]
        )
    if data.get("BackendServerDescriptions") is not None:
        import capo_securityhub.types.aws_elb_load_balancer_backend_server_descriptions

        out["backend_server_descriptions"] = (
            capo_securityhub.types.aws_elb_load_balancer_backend_server_descriptions.deserialize_json(
                data["BackendServerDescriptions"]
            )
        )
    if data.get("CanonicalHostedZoneName") is not None:
        out["canonical_hosted_zone_name"] = data["CanonicalHostedZoneName"]
    if data.get("CanonicalHostedZoneNameID") is not None:
        out["canonical_hosted_zone_name_id"] = data["CanonicalHostedZoneNameID"]
    if data.get("CreatedTime") is not None:
        out["created_time"] = data["CreatedTime"]
    if data.get("DnsName") is not None:
        out["dns_name"] = data["DnsName"]
    if data.get("HealthCheck") is not None:
        import capo_securityhub.types.aws_elb_load_balancer_health_check

        out["health_check"] = (
            capo_securityhub.types.aws_elb_load_balancer_health_check.deserialize_json(
                data["HealthCheck"]
            )
        )
    if data.get("Instances") is not None:
        import capo_securityhub.types.aws_elb_load_balancer_instances

        out["instances"] = (
            capo_securityhub.types.aws_elb_load_balancer_instances.deserialize_json(
                data["Instances"]
            )
        )
    if data.get("ListenerDescriptions") is not None:
        import capo_securityhub.types.aws_elb_load_balancer_listener_descriptions

        out["listener_descriptions"] = (
            capo_securityhub.types.aws_elb_load_balancer_listener_descriptions.deserialize_json(
                data["ListenerDescriptions"]
            )
        )
    if data.get("LoadBalancerAttributes") is not None:
        import capo_securityhub.types.aws_elb_load_balancer_attributes

        out["load_balancer_attributes"] = (
            capo_securityhub.types.aws_elb_load_balancer_attributes.deserialize_json(
                data["LoadBalancerAttributes"]
            )
        )
    if data.get("LoadBalancerName") is not None:
        out["load_balancer_name"] = data["LoadBalancerName"]
    if data.get("Policies") is not None:
        import capo_securityhub.types.aws_elb_load_balancer_policies

        out["policies"] = (
            capo_securityhub.types.aws_elb_load_balancer_policies.deserialize_json(
                data["Policies"]
            )
        )
    if data.get("Scheme") is not None:
        out["scheme"] = data["Scheme"]
    if data.get("SecurityGroups") is not None:
        import capo_securityhub.types.string_list

        out["security_groups"] = capo_securityhub.types.string_list.deserialize_json(
            data["SecurityGroups"]
        )
    if data.get("SourceSecurityGroup") is not None:
        import capo_securityhub.types.aws_elb_load_balancer_source_security_group

        out["source_security_group"] = (
            capo_securityhub.types.aws_elb_load_balancer_source_security_group.deserialize_json(
                data["SourceSecurityGroup"]
            )
        )
    if data.get("Subnets") is not None:
        import capo_securityhub.types.string_list

        out["subnets"] = capo_securityhub.types.string_list.deserialize_json(
            data["Subnets"]
        )
    if data.get("VpcId") is not None:
        out["vpc_id"] = data["VpcId"]
    return out
