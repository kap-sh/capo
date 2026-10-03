"""Generated from Smithy shape ``com.amazonaws.route53resolver#UpdateResolverEndpointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_route53resolver.errors import DeserializationError

if TYPE_CHECKING:
    import capo_route53resolver.types.dns64_enabled
    import capo_route53resolver.types.ipv6_internet_access_enabled
    import capo_route53resolver.types.name
    import capo_route53resolver.types.protocol_list
    import capo_route53resolver.types.resolver_endpoint_type
    import capo_route53resolver.types.resource_id
    import capo_route53resolver.types.rni_enhanced_metrics_enabled
    import capo_route53resolver.types.target_name_server_metrics_enabled
    import capo_route53resolver.types.update_ip_addresses


class UpdateResolverEndpointRequest(TypedDict, closed=True):
    resolver_endpoint_id: "capo_route53resolver.types.resource_id.ResourceId"
    """<p>The ID of the Resolver endpoint that you want to update.</p>"""
    name: NotRequired["capo_route53resolver.types.name.Name"]
    """<p>The name of the Resolver endpoint that you want to update.</p>"""
    resolver_endpoint_type: NotRequired[
        "capo_route53resolver.types.resolver_endpoint_type.ResolverEndpointType"
    ]
    """<p> Specifies the endpoint type for what type of IP address the endpoint uses to forward DNS queries. </p> <p>Updating to <code>IPV6</code> type isn't currently supported.</p>"""
    update_ip_addresses: NotRequired[
        "capo_route53resolver.types.update_ip_addresses.UpdateIpAddresses"
    ]
    """<p> Specifies the IPv6 address when you update the Resolver endpoint from IPv4 to dual-stack. If you don't specify an IPv6 address, one will be automatically chosen from your subnet. </p>"""
    protocols: NotRequired["capo_route53resolver.types.protocol_list.ProtocolList"]
    """<p> The protocols you want to use for the endpoint. DoH-FIPS is applicable for default inbound endpoints only. </p> <p>For a default inbound endpoint you can apply the protocols as follows:</p> <ul> <li> <p> Do53 and DoH in combination.</p> </li> <li> <p>Do53 and DoH-FIPS in combination.</p> </li> <li> <p>Do53 alone.</p> </li> <li> <p>DoH alone.</p> </li> <li> <p>DoH-FIPS alone.</p> </li> <li> <p>None, which is treated as Do53.</p> </li> </ul> <p>For a delegation inbound endpoint you can use Do53 only.</p> <p>For an outbound endpoint you can apply the protocols as follows:</p> <ul> <li> <p> Do53 and DoH in combination.</p> </li> <li> <p>Do53 alone.</p> </li> <li> <p>DoH alone.</p> </li> <li> <p>None, which is treated as Do53.</p> </li> </ul> <important> <p> You can't change the protocol of an inbound endpoint directly from only Do53 to only DoH, or DoH-FIPS. This is to prevent a sudden disruption to incoming traffic that relies on Do53. To change the protocol from Do53 to DoH, or DoH-FIPS, you must first enable both Do53 and DoH, or Do53 and DoH-FIPS, to make sure that all incoming traffic has transferred to using the DoH protocol, or DoH-FIPS, and then remove the Do53.</p> </important>"""
    rni_enhanced_metrics_enabled: NotRequired[
        "capo_route53resolver.types.rni_enhanced_metrics_enabled.RniEnhancedMetricsEnabled"
    ]
    """<p>Updates whether RNI enhanced metrics are enabled for the Resolver endpoints. When set to true, one-minute granular metrics are published in CloudWatch for each RNI associated with this endpoint. When set to false, metrics are not published.</p> <note> <p>Standard CloudWatch pricing and charges are applied for using the Route 53 Resolver endpoint RNI enhanced metrics. For more information, see <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/monitoring-resolver-with-cloudwatch.html">Detailed metrics</a>.</p> </note>"""
    target_name_server_metrics_enabled: NotRequired[
        "capo_route53resolver.types.target_name_server_metrics_enabled.TargetNameServerMetricsEnabled"
    ]
    """<p>Updates whether target name server metrics are enabled for the outbound Resolver endpoints. When set to true, one-minute granular metrics are published in CloudWatch for each target name server associated with this endpoint. When set to false, metrics are not published. This setting is not supported for inbound Resolver endpoints.</p> <note> <p>Standard CloudWatch pricing and charges are applied for using the Route 53 Resolver endpoint target name server metrics. For more information, see <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/monitoring-resolver-with-cloudwatch.html">Detailed metrics</a>.</p> </note>"""
    dns64_enabled: NotRequired["capo_route53resolver.types.dns64_enabled.Dns64Enabled"]
    """<p>Specifies whether DNS64 is enabled for the inbound Resolver endpoint. When set to <code>true</code>, Route 53 Resolver synthesizes AAAA (IPv6) records for IPv4-only services by prepending the <code>64:ff9b::/96</code> prefix to the IPv4 address. This enables IPv6-only clients that send queries through the inbound endpoint to reach IPv4-only services. DNS64 works with NAT64 to provide complete IPv6-to-IPv4 translation.</p>"""
    ipv6_internet_access_enabled: NotRequired[
        "capo_route53resolver.types.ipv6_internet_access_enabled.Ipv6InternetAccessEnabled"
    ]
    """<p>Specifies whether IPv6 internet access is enabled for the outbound Resolver endpoint. When set to <code>true</code>, the endpoint elastic network interfaces (ENIs) can forward DNS queries to public IPv6 targets through an internet gateway.</p> <important> <p>When you enable IPv6 internet access, use network controls like security groups, NACLs, or egress-only internet gateways to protect the endpoint ENIs from unsolicited ingress traffic. Be aware that some network controls can affect DNS query throughput due to connection tracking. For more information, see <a href="https://docs.aws.amazon.com/ec2/latest/userguide/security-group-connection-tracking.html">Amazon EC2 security group connection tracking</a> and <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/best-practices-resolver-endpoint-scaling.html">Resolver endpoint scaling</a>.</p> </important>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateResolverEndpointRequest) -> dict:
    out: dict = {}
    out["ResolverEndpointId"] = value["resolver_endpoint_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "resolver_endpoint_type" in value:
        import capo_route53resolver.types.resolver_endpoint_type

        out["ResolverEndpointType"] = (
            capo_route53resolver.types.resolver_endpoint_type.serialize_aws_json_1_1(
                value["resolver_endpoint_type"]
            )
        )
    if "update_ip_addresses" in value:
        import capo_route53resolver.types.update_ip_addresses

        out["UpdateIpAddresses"] = (
            capo_route53resolver.types.update_ip_addresses.serialize_aws_json_1_1(
                value["update_ip_addresses"]
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


def deserialize_aws_json_1_1(data: dict) -> UpdateResolverEndpointRequest:
    out: UpdateResolverEndpointRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResolverEndpointId") is not None:
        out["resolver_endpoint_id"] = data["ResolverEndpointId"]
    else:
        raise DeserializationError(
            "UpdateResolverEndpointRequest.resolver_endpoint_id required"
        )
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("ResolverEndpointType") is not None:
        import capo_route53resolver.types.resolver_endpoint_type

        out["resolver_endpoint_type"] = (
            capo_route53resolver.types.resolver_endpoint_type.deserialize_aws_json_1_1(
                data["ResolverEndpointType"]
            )
        )
    if data.get("UpdateIpAddresses") is not None:
        import capo_route53resolver.types.update_ip_addresses

        out["update_ip_addresses"] = (
            capo_route53resolver.types.update_ip_addresses.deserialize_aws_json_1_1(
                data["UpdateIpAddresses"]
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
