"""Generated from Smithy shape ``com.amazonaws.networkfirewall#CreateFirewallRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_network_firewall.errors import DeserializationError

if TYPE_CHECKING:
    import capo_network_firewall.types.availability_zone_mappings
    import capo_network_firewall.types.boolean
    import capo_network_firewall.types.description
    import capo_network_firewall.types.enabled_analysis_types
    import capo_network_firewall.types.encryption_configuration
    import capo_network_firewall.types.nat_gateway_mappings_list
    import capo_network_firewall.types.proxy_settings
    import capo_network_firewall.types.resource_arn
    import capo_network_firewall.types.resource_name
    import capo_network_firewall.types.subnet_mappings
    import capo_network_firewall.types.tag_list
    import capo_network_firewall.types.transit_gateway_id
    import capo_network_firewall.types.vpc_endpoint
    import capo_network_firewall.types.vpc_id


class CreateFirewallRequest(TypedDict, closed=True):
    firewall_name: "capo_network_firewall.types.resource_name.ResourceName"
    """<p>The descriptive name of the firewall. You can't change the name of a firewall after you create it.</p>"""
    firewall_policy_arn: "capo_network_firewall.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the <a>FirewallPolicy</a> that you want to use for the firewall.</p>"""
    vpc_id: NotRequired["capo_network_firewall.types.vpc_id.VpcId"]
    """<p>The unique identifier of the VPC where Network Firewall should create the firewall. </p> <p>You can't change this setting after you create the firewall. </p>"""
    subnet_mappings: NotRequired[
        "capo_network_firewall.types.subnet_mappings.SubnetMappings"
    ]
    """<p>The public subnets to use for your Network Firewall firewalls. Each subnet must belong to a different Availability Zone in the VPC. Network Firewall creates a firewall endpoint in each subnet. </p>"""
    delete_protection: "capo_network_firewall.types.boolean.Boolean"
    """<p>A flag indicating whether it is possible to delete the firewall. A setting of <code>TRUE</code> indicates that the firewall is protected against deletion. Use this setting to protect against accidentally deleting a firewall that is in use. When you create a firewall, the operation initializes this flag to <code>TRUE</code>.</p>"""
    subnet_change_protection: "capo_network_firewall.types.boolean.Boolean"
    """<p>A setting indicating whether the firewall is protected against changes to the subnet associations. Use this setting to protect against accidentally modifying the subnet associations for a firewall that is in use. When you create a firewall, the operation initializes this setting to <code>TRUE</code>.</p>"""
    firewall_policy_change_protection: "capo_network_firewall.types.boolean.Boolean"
    """<p>A setting indicating whether the firewall is protected against a change to the firewall policy association. Use this setting to protect against accidentally modifying the firewall policy for a firewall that is in use. When you create a firewall, the operation initializes this setting to <code>TRUE</code>.</p>"""
    description: NotRequired["capo_network_firewall.types.description.Description"]
    """<p>A description of the firewall.</p>"""
    tags: NotRequired["capo_network_firewall.types.tag_list.TagList"]
    """<p>The key:value pairs to associate with the resource.</p>"""
    encryption_configuration: NotRequired[
        "capo_network_firewall.types.encryption_configuration.EncryptionConfiguration"
    ]
    """<p>A complex type that contains settings for encryption of your firewall resources.</p>"""
    enabled_analysis_types: NotRequired[
        "capo_network_firewall.types.enabled_analysis_types.EnabledAnalysisTypes"
    ]
    """<p>An optional setting indicating the specific traffic analysis types to enable on the firewall. </p>"""
    transit_gateway_id: NotRequired[
        "capo_network_firewall.types.transit_gateway_id.TransitGatewayId"
    ]
    """<p>Required when creating a transit gateway-attached firewall. The unique identifier of the transit gateway to attach to this firewall. You can provide either a transit gateway from your account or one that has been shared with you through Resource Access Manager.</p> <important> <p>After creating the firewall, you cannot change the transit gateway association. To use a different transit gateway, you must create a new firewall.</p> </important> <p>For information about creating firewalls, see <a>CreateFirewall</a>. For specific guidance about transit gateway-attached firewalls, see <a href="https://docs.aws.amazon.com/network-firewall/latest/developerguide/tgw-firewall-considerations.html">Considerations for transit gateway-attached firewalls</a> in the <i>Network Firewall Developer Guide</i>.</p>"""
    availability_zone_mappings: NotRequired[
        "capo_network_firewall.types.availability_zone_mappings.AvailabilityZoneMappings"
    ]
    """<p>Required. The Availability Zones where you want to create firewall endpoints for a transit gateway-attached firewall. You must specify at least one Availability Zone. Consider enabling the firewall in every Availability Zone where you have workloads to maintain Availability Zone isolation.</p> <p>You can modify Availability Zones later using <a>AssociateAvailabilityZones</a> or <a>DisassociateAvailabilityZones</a>, but this may briefly disrupt traffic. The <code>AvailabilityZoneChangeProtection</code> setting controls whether you can make these modifications.</p>"""
    availability_zone_change_protection: "capo_network_firewall.types.boolean.Boolean"
    """<p>Optional. A setting indicating whether the firewall is protected against changes to its Availability Zone configuration. When set to <code>TRUE</code>, you cannot add or remove Availability Zones without first disabling this protection using <a>UpdateAvailabilityZoneChangeProtection</a>.</p> <p>Default value: <code>FALSE</code> </p>"""
    nat_gateway_mappings: NotRequired[
        "capo_network_firewall.types.nat_gateway_mappings_list.NatGatewayMappingsList"
    ]
    """<p>The NAT gateways that the firewall uses to proxy traffic when <code>NoSourcePreservation</code> is <code>TRUE</code>. Network Firewall attaches the firewall to each NAT gateway that you specify, so that egress traffic is proxied through the NAT gateway. </p>"""
    proxy_settings: NotRequired[
        "capo_network_firewall.types.proxy_settings.ProxySettings"
    ]
    """<p>The listener configuration for a proxy mode firewall, used when <code>NoSourcePreservation</code> is <code>TRUE</code>. This specifies the ports and protocols on which the firewall's proxy listens for traffic. </p>"""
    no_source_preservation: "capo_network_firewall.types.boolean.Boolean"
    """<p>Optional. Indicates whether the firewall operates in proxy mode, in which the source IP address of the traffic is not preserved. When set to <code>TRUE</code>, the firewall proxies traffic through a NAT gateway and the traffic reaching the destination uses the NAT gateway's IP address as the source. </p> <p>When you set this to <code>TRUE</code>, you must specify <code>NatGatewayMappings</code> and <code>VpcEndpoint</code> instead of a top-level <code>VpcId</code> and <code>SubnetMappings</code>. </p> <p>You can't change this setting after you create the firewall. </p> <p>Default value: <code>FALSE</code> </p>"""
    vpc_endpoint: NotRequired["capo_network_firewall.types.vpc_endpoint.VpcEndpoint"]
    """<p>The VPC and subnets for the firewall endpoint, used when <code>NoSourcePreservation</code> is <code>TRUE</code>. Network Firewall creates the firewall endpoint in the subnets that you specify here. </p> <p>For proxy mode firewalls, provide the firewall's VPC and endpoint subnets through this parameter instead of the top-level <code>VpcId</code> and <code>SubnetMappings</code>. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateFirewallRequest) -> dict:
    out: dict = {}
    out["FirewallName"] = value["firewall_name"]
    out["FirewallPolicyArn"] = value["firewall_policy_arn"]
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    if "subnet_mappings" in value:
        import capo_network_firewall.types.subnet_mappings

        out["SubnetMappings"] = (
            capo_network_firewall.types.subnet_mappings.serialize_aws_json_1_0(
                value["subnet_mappings"]
            )
        )
    out["DeleteProtection"] = value.get("delete_protection", False)
    out["SubnetChangeProtection"] = value.get("subnet_change_protection", False)
    out["FirewallPolicyChangeProtection"] = value.get(
        "firewall_policy_change_protection", False
    )
    if "description" in value:
        out["Description"] = value["description"]
    if "tags" in value:
        import capo_network_firewall.types.tag_list

        out["Tags"] = capo_network_firewall.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    if "encryption_configuration" in value:
        import capo_network_firewall.types.encryption_configuration

        out["EncryptionConfiguration"] = (
            capo_network_firewall.types.encryption_configuration.serialize_aws_json_1_0(
                value["encryption_configuration"]
            )
        )
    if "enabled_analysis_types" in value:
        import capo_network_firewall.types.enabled_analysis_types

        out["EnabledAnalysisTypes"] = (
            capo_network_firewall.types.enabled_analysis_types.serialize_aws_json_1_0(
                value["enabled_analysis_types"]
            )
        )
    if "transit_gateway_id" in value:
        out["TransitGatewayId"] = value["transit_gateway_id"]
    if "availability_zone_mappings" in value:
        import capo_network_firewall.types.availability_zone_mappings

        out["AvailabilityZoneMappings"] = (
            capo_network_firewall.types.availability_zone_mappings.serialize_aws_json_1_0(
                value["availability_zone_mappings"]
            )
        )
    out["AvailabilityZoneChangeProtection"] = value.get(
        "availability_zone_change_protection", False
    )
    if "nat_gateway_mappings" in value:
        import capo_network_firewall.types.nat_gateway_mappings_list

        out["NatGatewayMappings"] = (
            capo_network_firewall.types.nat_gateway_mappings_list.serialize_aws_json_1_0(
                value["nat_gateway_mappings"]
            )
        )
    if "proxy_settings" in value:
        import capo_network_firewall.types.proxy_settings

        out["ProxySettings"] = (
            capo_network_firewall.types.proxy_settings.serialize_aws_json_1_0(
                value["proxy_settings"]
            )
        )
    out["NoSourcePreservation"] = value.get("no_source_preservation", False)
    if "vpc_endpoint" in value:
        import capo_network_firewall.types.vpc_endpoint

        out["VpcEndpoint"] = (
            capo_network_firewall.types.vpc_endpoint.serialize_aws_json_1_0(
                value["vpc_endpoint"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateFirewallRequest:
    out: CreateFirewallRequest = {}  # type: ignore[typeddict-item]
    if data.get("FirewallName") is not None:
        out["firewall_name"] = data["FirewallName"]
    else:
        raise DeserializationError("CreateFirewallRequest.firewall_name required")
    if data.get("FirewallPolicyArn") is not None:
        out["firewall_policy_arn"] = data["FirewallPolicyArn"]
    else:
        raise DeserializationError("CreateFirewallRequest.firewall_policy_arn required")
    if data.get("VpcId") is not None:
        out["vpc_id"] = data["VpcId"]
    if data.get("SubnetMappings") is not None:
        import capo_network_firewall.types.subnet_mappings

        out["subnet_mappings"] = (
            capo_network_firewall.types.subnet_mappings.deserialize_aws_json_1_0(
                data["SubnetMappings"]
            )
        )
    if data.get("DeleteProtection") is not None:
        out["delete_protection"] = data["DeleteProtection"]
    else:
        out["delete_protection"] = False
    if data.get("SubnetChangeProtection") is not None:
        out["subnet_change_protection"] = data["SubnetChangeProtection"]
    else:
        out["subnet_change_protection"] = False
    if data.get("FirewallPolicyChangeProtection") is not None:
        out["firewall_policy_change_protection"] = data[
            "FirewallPolicyChangeProtection"
        ]
    else:
        out["firewall_policy_change_protection"] = False
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Tags") is not None:
        import capo_network_firewall.types.tag_list

        out["tags"] = capo_network_firewall.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    if data.get("EncryptionConfiguration") is not None:
        import capo_network_firewall.types.encryption_configuration

        out["encryption_configuration"] = (
            capo_network_firewall.types.encryption_configuration.deserialize_aws_json_1_0(
                data["EncryptionConfiguration"]
            )
        )
    if data.get("EnabledAnalysisTypes") is not None:
        import capo_network_firewall.types.enabled_analysis_types

        out["enabled_analysis_types"] = (
            capo_network_firewall.types.enabled_analysis_types.deserialize_aws_json_1_0(
                data["EnabledAnalysisTypes"]
            )
        )
    if data.get("TransitGatewayId") is not None:
        out["transit_gateway_id"] = data["TransitGatewayId"]
    if data.get("AvailabilityZoneMappings") is not None:
        import capo_network_firewall.types.availability_zone_mappings

        out["availability_zone_mappings"] = (
            capo_network_firewall.types.availability_zone_mappings.deserialize_aws_json_1_0(
                data["AvailabilityZoneMappings"]
            )
        )
    if data.get("AvailabilityZoneChangeProtection") is not None:
        out["availability_zone_change_protection"] = data[
            "AvailabilityZoneChangeProtection"
        ]
    else:
        out["availability_zone_change_protection"] = False
    if data.get("NatGatewayMappings") is not None:
        import capo_network_firewall.types.nat_gateway_mappings_list

        out["nat_gateway_mappings"] = (
            capo_network_firewall.types.nat_gateway_mappings_list.deserialize_aws_json_1_0(
                data["NatGatewayMappings"]
            )
        )
    if data.get("ProxySettings") is not None:
        import capo_network_firewall.types.proxy_settings

        out["proxy_settings"] = (
            capo_network_firewall.types.proxy_settings.deserialize_aws_json_1_0(
                data["ProxySettings"]
            )
        )
    if data.get("NoSourcePreservation") is not None:
        out["no_source_preservation"] = data["NoSourcePreservation"]
    else:
        out["no_source_preservation"] = False
    if data.get("VpcEndpoint") is not None:
        import capo_network_firewall.types.vpc_endpoint

        out["vpc_endpoint"] = (
            capo_network_firewall.types.vpc_endpoint.deserialize_aws_json_1_0(
                data["VpcEndpoint"]
            )
        )
    return out
