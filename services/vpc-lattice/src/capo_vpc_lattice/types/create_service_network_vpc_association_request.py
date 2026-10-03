"""Generated from Smithy shape ``com.amazonaws.vpclattice#CreateServiceNetworkVpcAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_vpc_lattice.errors import DeserializationError

if TYPE_CHECKING:
    import capo_vpc_lattice.types.boolean
    import capo_vpc_lattice.types.client_token
    import capo_vpc_lattice.types.dns_options
    import capo_vpc_lattice.types.security_group_list
    import capo_vpc_lattice.types.service_network_identifier_without_regex
    import capo_vpc_lattice.types.tag_map
    import capo_vpc_lattice.types.vpc_id


class CreateServiceNetworkVpcAssociationRequest(TypedDict, closed=True):
    client_token: NotRequired["capo_vpc_lattice.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren't identical, the retry fails.</p>"""
    service_network_identifier: "capo_vpc_lattice.types.service_network_identifier_without_regex.ServiceNetworkIdentifierWithoutRegex"
    """<p>The ID or ARN of the service network. You must use an ARN if the resources are in different accounts.</p>"""
    vpc_identifier: "capo_vpc_lattice.types.vpc_id.VpcId"
    """<p>The ID of the VPC.</p>"""
    private_dns_enabled: NotRequired["capo_vpc_lattice.types.boolean.Boolean"]
    """<p> Indicates if private DNS is enabled for the VPC association. </p>"""
    security_group_ids: NotRequired[
        "capo_vpc_lattice.types.security_group_list.SecurityGroupList"
    ]
    """<p>The IDs of the security groups. Security groups aren't added by default. You can add a security group to apply network level controls to control which resources in a VPC are allowed to access the service network and its services. For more information, see <a href="https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html">Control traffic to resources using security groups</a> in the <i>Amazon VPC User Guide</i>.</p>"""
    tags: NotRequired["capo_vpc_lattice.types.tag_map.TagMap"]
    """<p>The tags for the association.</p>"""
    dns_options: NotRequired["capo_vpc_lattice.types.dns_options.DnsOptions"]
    """<p> DNS options for the service network VPC association. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateServiceNetworkVpcAssociationRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["serviceNetworkIdentifier"] = value["service_network_identifier"]
    out["vpcIdentifier"] = value["vpc_identifier"]
    if "private_dns_enabled" in value:
        out["privateDnsEnabled"] = value["private_dns_enabled"]
    if "security_group_ids" in value:
        import capo_vpc_lattice.types.security_group_list

        out["securityGroupIds"] = (
            capo_vpc_lattice.types.security_group_list.serialize_json(
                value["security_group_ids"]
            )
        )
    if "tags" in value:
        import capo_vpc_lattice.types.tag_map

        out["tags"] = capo_vpc_lattice.types.tag_map.serialize_json(value["tags"])
    if "dns_options" in value:
        import capo_vpc_lattice.types.dns_options

        out["dnsOptions"] = capo_vpc_lattice.types.dns_options.serialize_json(
            value["dns_options"]
        )
    return out


def deserialize_json(data: dict) -> CreateServiceNetworkVpcAssociationRequest:
    out: CreateServiceNetworkVpcAssociationRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("serviceNetworkIdentifier") is not None:
        out["service_network_identifier"] = data["serviceNetworkIdentifier"]
    else:
        raise DeserializationError(
            "CreateServiceNetworkVpcAssociationRequest.service_network_identifier required"
        )
    if data.get("vpcIdentifier") is not None:
        out["vpc_identifier"] = data["vpcIdentifier"]
    else:
        raise DeserializationError(
            "CreateServiceNetworkVpcAssociationRequest.vpc_identifier required"
        )
    if data.get("privateDnsEnabled") is not None:
        out["private_dns_enabled"] = data["privateDnsEnabled"]
    if data.get("securityGroupIds") is not None:
        import capo_vpc_lattice.types.security_group_list

        out["security_group_ids"] = (
            capo_vpc_lattice.types.security_group_list.deserialize_json(
                data["securityGroupIds"]
            )
        )
    if data.get("tags") is not None:
        import capo_vpc_lattice.types.tag_map

        out["tags"] = capo_vpc_lattice.types.tag_map.deserialize_json(data["tags"])
    if data.get("dnsOptions") is not None:
        import capo_vpc_lattice.types.dns_options

        out["dns_options"] = capo_vpc_lattice.types.dns_options.deserialize_json(
            data["dnsOptions"]
        )
    return out
