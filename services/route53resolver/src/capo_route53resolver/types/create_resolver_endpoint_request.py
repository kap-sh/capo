"""Generated from Smithy shape ``com.amazonaws.route53resolver#CreateResolverEndpointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_route53resolver.errors import DeserializationError

if TYPE_CHECKING:
    import capo_route53resolver.types.creator_request_id
    import capo_route53resolver.types.dns64_enabled
    import capo_route53resolver.types.ip_addresses_request
    import capo_route53resolver.types.ipv6_internet_access_enabled
    import capo_route53resolver.types.name
    import capo_route53resolver.types.outpost_arn
    import capo_route53resolver.types.outpost_instance_type
    import capo_route53resolver.types.protocol_list
    import capo_route53resolver.types.resolver_endpoint_direction
    import capo_route53resolver.types.resolver_endpoint_type
    import capo_route53resolver.types.rni_enhanced_metrics_enabled
    import capo_route53resolver.types.security_group_ids
    import capo_route53resolver.types.tag_list
    import capo_route53resolver.types.target_name_server_metrics_enabled


class CreateResolverEndpointRequest(TypedDict, closed=True):
    creator_request_id: "capo_route53resolver.types.creator_request_id.CreatorRequestId"
    """<p>A unique string that identifies the request and that allows failed requests to be retried without the risk of running the operation twice. <code>CreatorRequestId</code> can be any unique string, for example, a date/time stamp. </p>"""
    name: NotRequired["capo_route53resolver.types.name.Name"]
    """<p>A friendly name that lets you easily find a configuration in the Resolver dashboard in the Route 53 console.</p>"""
    security_group_ids: "capo_route53resolver.types.security_group_ids.SecurityGroupIds"
    """<p>The ID of one or more security groups that you want to use to control access to this VPC. The security group that you specify must include one or more inbound rules (for inbound Resolver endpoints) or outbound rules (for outbound Resolver endpoints). Inbound and outbound rules must allow TCP and UDP access. For inbound access, open port 53. For outbound access, open the port that you're using for DNS queries on your network.</p> <p>Some security group rules will cause your connection to be tracked. For outbound resolver endpoint, it can potentially impact the maximum queries per second from outbound endpoint to your target name server. For inbound resolver endpoint, it can bring down the overall maximum queries per second per IP address to as low as 1500. To avoid connection tracking caused by security group, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-group-connection-tracking.html#untracked-connectionsl">Untracked connections</a>.</p>"""
    direction: "capo_route53resolver.types.resolver_endpoint_direction.ResolverEndpointDirection"
    """<p>Specify the applicable value:</p> <ul> <li> <p> <code>INBOUND</code>: Resolver forwards DNS queries to the DNS service for a VPC from your network.</p> </li> <li> <p> <code>OUTBOUND</code>: Resolver forwards DNS queries from the DNS service for a VPC to your network.</p> </li> <li> <p> <code>INBOUND_DELEGATION</code>: Resolver delegates queries to Route 53 private hosted zones from your network.</p> </li> </ul>"""
    ip_addresses: "capo_route53resolver.types.ip_addresses_request.IpAddressesRequest"
    """<p>The subnets and IP addresses in your VPC that DNS queries originate from (for outbound endpoints) or that you forward DNS queries to (for inbound endpoints). The subnet ID uniquely identifies a VPC. </p> <note> <p>Even though the minimum is 1, Route 53 requires that you create at least two.</p> </note> <p>We recommend using <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/outpost-resolver-getting-started.html">VPC Resolver on Outposts</a> to create endpoints on Outposts Racks.</p> <important> <p>Outposts subnets with <a href="https://docs.aws.amazon.com/outposts/latest/server-userguide/local-network-interface.html">Local Network Interface (LNI)</a> enabled are not compatible with Route 53 Resolver endpoints. If you enable LNI on a subnet that contains Route 53 Resolver endpoint elastic network interfaces (ENIs), those ENIs will stop functioning. For more information, see <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/best-practices-resolver.html#best-practices-resolver-subnet-compatibility">Subnet compatibility for Resolver endpoints</a> in the <i>Amazon Route 53 Developer Guide</i>.</p> </important>"""
    outpost_arn: NotRequired["capo_route53resolver.types.outpost_arn.OutpostArn"]
    """<p>The Amazon Resource Name (ARN) of the Outpost. If you specify this, you must also specify a value for the <code>PreferredInstanceType</code>. </p> <note> <p>Resolver endpoints on Outposts are supported on first-generation Outposts only. Inbound and outbound Resolver endpoints aren't supported on second-generation Outposts.</p> </note>"""
    preferred_instance_type: NotRequired[
        "capo_route53resolver.types.outpost_instance_type.OutpostInstanceType"
    ]
    """<p>The instance type. If you specify this, you must also specify a value for the <code>OutpostArn</code>.</p>"""
    tags: NotRequired["capo_route53resolver.types.tag_list.TagList"]
    """<p>A list of the tag keys and values that you want to associate with the endpoint.</p>"""
    resolver_endpoint_type: NotRequired[
        "capo_route53resolver.types.resolver_endpoint_type.ResolverEndpointType"
    ]
    """<p> For the endpoint type you can choose either IPv4, IPv6, or dual-stack. A dual-stack endpoint means that it will resolve via both IPv4 and IPv6. This endpoint type is applied to all IP addresses. </p>"""
    protocols: NotRequired["capo_route53resolver.types.protocol_list.ProtocolList"]
    """<p> The protocols you want to use for the endpoint. DoH-FIPS is applicable for default inbound endpoints only. </p> <p>For a default inbound endpoint you can apply the protocols as follows:</p> <ul> <li> <p> Do53 and DoH in combination.</p> </li> <li> <p>Do53 and DoH-FIPS in combination.</p> </li> <li> <p>Do53 alone.</p> </li> <li> <p>DoH alone.</p> </li> <li> <p>DoH-FIPS alone.</p> </li> <li> <p>None, which is treated as Do53.</p> </li> </ul> <p>For a delegation inbound endpoint you can use Do53 only.</p> <p>For an outbound endpoint you can apply the protocols as follows:</p> <ul> <li> <p> Do53 and DoH in combination.</p> </li> <li> <p>Do53 alone.</p> </li> <li> <p>DoH alone.</p> </li> <li> <p>None, which is treated as Do53.</p> </li> </ul>"""
    rni_enhanced_metrics_enabled: NotRequired[
        "capo_route53resolver.types.rni_enhanced_metrics_enabled.RniEnhancedMetricsEnabled"
    ]
    """<p>Specifies whether RNI enhanced metrics are enabled for the Resolver endpoints. When set to true, one-minute granular metrics are published in CloudWatch for each RNI associated with this endpoint. When set to false, metrics are not published. Default is false.</p> <note> <p>Standard CloudWatch pricing and charges are applied for using the Route 53 Resolver endpoint RNI enhanced metrics. For more information, see <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/monitoring-resolver-with-cloudwatch.html">Detailed metrics</a>.</p> </note>"""
    target_name_server_metrics_enabled: NotRequired[
        "capo_route53resolver.types.target_name_server_metrics_enabled.TargetNameServerMetricsEnabled"
    ]
    """<p>Specifies whether target name server metrics are enabled for the outbound Resolver endpoints. When set to true, one-minute granular metrics are published in CloudWatch for each target name server associated with this endpoint. When set to false, metrics are not published. Default is false. This is not supported for inbound Resolver endpoints.</p> <note> <p>Standard CloudWatch pricing and charges are applied for using the Route 53 Resolver endpoint target name server metrics. For more information, see <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/monitoring-resolver-with-cloudwatch.html">Detailed metrics</a>.</p> </note>"""
    dns64_enabled: NotRequired["capo_route53resolver.types.dns64_enabled.Dns64Enabled"]
    """<p>Specifies whether DNS64 is enabled for the inbound Resolver endpoint. When set to <code>true</code>, Route 53 Resolver synthesizes AAAA (IPv6) records for IPv4-only services by prepending the <code>64:ff9b::/96</code> prefix to the IPv4 address. This enables IPv6-only clients that send queries through the inbound endpoint to reach IPv4-only services. DNS64 works with NAT64 to provide complete IPv6-to-IPv4 translation. Default is false.</p>"""
    ipv6_internet_access_enabled: NotRequired[
        "capo_route53resolver.types.ipv6_internet_access_enabled.Ipv6InternetAccessEnabled"
    ]
    """<p>Specifies whether IPv6 internet access is enabled for the outbound Resolver endpoint. When set to <code>true</code>, the endpoint elastic network interfaces (ENIs) can forward DNS queries to public IPv6 targets through an internet gateway. Default is false.</p> <important> <p>When you enable IPv6 internet access, use network controls like security groups, NACLs, or egress-only internet gateways to protect the endpoint ENIs from unsolicited ingress traffic. Be aware that some network controls can affect DNS query throughput due to connection tracking. For more information, see <a href="https://docs.aws.amazon.com/ec2/latest/userguide/security-group-connection-tracking.html">Amazon EC2 security group connection tracking</a> and <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/best-practices-resolver-endpoint-scaling.html">Resolver endpoint scaling</a>.</p> </important>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateResolverEndpointRequest) -> dict:
    out: dict = {}
    out["CreatorRequestId"] = value["creator_request_id"]
    if "name" in value:
        out["Name"] = value["name"]
    import capo_route53resolver.types.security_group_ids

    out["SecurityGroupIds"] = (
        capo_route53resolver.types.security_group_ids.serialize_aws_json_1_1(
            value["security_group_ids"]
        )
    )
    import capo_route53resolver.types.resolver_endpoint_direction

    out["Direction"] = (
        capo_route53resolver.types.resolver_endpoint_direction.serialize_aws_json_1_1(
            value["direction"]
        )
    )
    import capo_route53resolver.types.ip_addresses_request

    out["IpAddresses"] = (
        capo_route53resolver.types.ip_addresses_request.serialize_aws_json_1_1(
            value["ip_addresses"]
        )
    )
    if "outpost_arn" in value:
        out["OutpostArn"] = value["outpost_arn"]
    if "preferred_instance_type" in value:
        out["PreferredInstanceType"] = value["preferred_instance_type"]
    if "tags" in value:
        import capo_route53resolver.types.tag_list

        out["Tags"] = capo_route53resolver.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "resolver_endpoint_type" in value:
        import capo_route53resolver.types.resolver_endpoint_type

        out["ResolverEndpointType"] = (
            capo_route53resolver.types.resolver_endpoint_type.serialize_aws_json_1_1(
                value["resolver_endpoint_type"]
            )
        )
    if "protocols" in value:
        import capo_route53resolver.types.protocol_list

        out["Protocols"] = (
            capo_route53resolver.types.protocol_list.serialize_aws_json_1_1(
                value["protocols"]
            )
        )
    if "rni_enhanced_metrics_enabled" in value:
        out["RniEnhancedMetricsEnabled"] = value["rni_enhanced_metrics_enabled"]
    if "target_name_server_metrics_enabled" in value:
        out["TargetNameServerMetricsEnabled"] = value[
            "target_name_server_metrics_enabled"
        ]
    if "dns64_enabled" in value:
        out["Dns64Enabled"] = value["dns64_enabled"]
    if "ipv6_internet_access_enabled" in value:
        out["Ipv6InternetAccessEnabled"] = value["ipv6_internet_access_enabled"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateResolverEndpointRequest:
    out: CreateResolverEndpointRequest = {}  # type: ignore[typeddict-item]
    if data.get("CreatorRequestId") is not None:
        out["creator_request_id"] = data["CreatorRequestId"]
    else:
        raise DeserializationError(
            "CreateResolverEndpointRequest.creator_request_id required"
        )
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("SecurityGroupIds") is not None:
        import capo_route53resolver.types.security_group_ids

        out["security_group_ids"] = (
            capo_route53resolver.types.security_group_ids.deserialize_aws_json_1_1(
                data["SecurityGroupIds"]
            )
        )
    else:
        raise DeserializationError(
            "CreateResolverEndpointRequest.security_group_ids required"
        )
    if data.get("Direction") is not None:
        import capo_route53resolver.types.resolver_endpoint_direction

        out["direction"] = (
            capo_route53resolver.types.resolver_endpoint_direction.deserialize_aws_json_1_1(
                data["Direction"]
            )
        )
    else:
        raise DeserializationError("CreateResolverEndpointRequest.direction required")
    if data.get("IpAddresses") is not None:
        import capo_route53resolver.types.ip_addresses_request

        out["ip_addresses"] = (
            capo_route53resolver.types.ip_addresses_request.deserialize_aws_json_1_1(
                data["IpAddresses"]
            )
        )
    else:
        raise DeserializationError(
            "CreateResolverEndpointRequest.ip_addresses required"
        )
    if data.get("OutpostArn") is not None:
        out["outpost_arn"] = data["OutpostArn"]
    if data.get("PreferredInstanceType") is not None:
        out["preferred_instance_type"] = data["PreferredInstanceType"]
    if data.get("Tags") is not None:
        import capo_route53resolver.types.tag_list

        out["tags"] = capo_route53resolver.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if data.get("ResolverEndpointType") is not None:
        import capo_route53resolver.types.resolver_endpoint_type

        out["resolver_endpoint_type"] = (
            capo_route53resolver.types.resolver_endpoint_type.deserialize_aws_json_1_1(
                data["ResolverEndpointType"]
            )
        )
    if data.get("Protocols") is not None:
        import capo_route53resolver.types.protocol_list

        out["protocols"] = (
            capo_route53resolver.types.protocol_list.deserialize_aws_json_1_1(
                data["Protocols"]
            )
        )
    if data.get("RniEnhancedMetricsEnabled") is not None:
        out["rni_enhanced_metrics_enabled"] = data["RniEnhancedMetricsEnabled"]
    if data.get("TargetNameServerMetricsEnabled") is not None:
        out["target_name_server_metrics_enabled"] = data[
            "TargetNameServerMetricsEnabled"
        ]
    if data.get("Dns64Enabled") is not None:
        out["dns64_enabled"] = data["Dns64Enabled"]
    if data.get("Ipv6InternetAccessEnabled") is not None:
        out["ipv6_internet_access_enabled"] = data["Ipv6InternetAccessEnabled"]
    return out
