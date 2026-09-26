"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#ManagedVpcResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_agent_registry_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_agent_registry_control.types.endpoint_ip_address_type
    import capo_agent_registry_control.types.routing_domain
    import capo_agent_registry_control.types.security_group_ids
    import capo_agent_registry_control.types.subnet_ids
    import capo_agent_registry_control.types.tags_map
    import capo_agent_registry_control.types.vpc_identifier


class ManagedVpcResource(TypedDict, closed=True):
    vpc_identifier: "capo_agent_registry_control.types.vpc_identifier.VpcIdentifier"
    """<p>The identifier of the VPC in which the private endpoint is provisioned.</p>"""
    subnet_ids: "capo_agent_registry_control.types.subnet_ids.SubnetIds"
    """<p>The identifiers of the subnets in which the private endpoint network interfaces are placed.</p>"""
    endpoint_ip_address_type: "capo_agent_registry_control.types.endpoint_ip_address_type.EndpointIpAddressType"
    """<p>The IP address type used by the private endpoint, either IPV4 or IPV6.</p>"""
    security_group_ids: NotRequired[
        "capo_agent_registry_control.types.security_group_ids.SecurityGroupIds"
    ]
    """<p>The identifiers of the security groups associated with the private endpoint network interfaces.</p>"""
    tags: NotRequired["capo_agent_registry_control.types.tags_map.TagsMap"]
    """<p>The tags applied to the service-managed VPC resource.</p>"""
    routing_domain: NotRequired[
        "capo_agent_registry_control.types.routing_domain.RoutingDomain"
    ]
    """<p>The routing domain used to resolve traffic through the private endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ManagedVpcResource) -> dict:
    out: dict = {}
    out["vpcIdentifier"] = value["vpc_identifier"]
    import capo_agent_registry_control.types.subnet_ids

    out["subnetIds"] = capo_agent_registry_control.types.subnet_ids.serialize_json(
        value["subnet_ids"]
    )
    import capo_agent_registry_control.types.endpoint_ip_address_type

    out["endpointIpAddressType"] = (
        capo_agent_registry_control.types.endpoint_ip_address_type.serialize_json(
            value["endpoint_ip_address_type"]
        )
    )
    if "security_group_ids" in value:
        import capo_agent_registry_control.types.security_group_ids

        out["securityGroupIds"] = (
            capo_agent_registry_control.types.security_group_ids.serialize_json(
                value["security_group_ids"]
            )
        )
    if "tags" in value:
        import capo_agent_registry_control.types.tags_map

        out["tags"] = capo_agent_registry_control.types.tags_map.serialize_json(
            value["tags"]
        )
    if "routing_domain" in value:
        out["routingDomain"] = value["routing_domain"]
    return out


def deserialize_json(data: dict) -> ManagedVpcResource:
    out: ManagedVpcResource = {}  # type: ignore[typeddict-item]
    if data.get("vpcIdentifier") is not None:
        out["vpc_identifier"] = data["vpcIdentifier"]
    else:
        raise DeserializationError("ManagedVpcResource.vpc_identifier required")
    if data.get("subnetIds") is not None:
        import capo_agent_registry_control.types.subnet_ids

        out["subnet_ids"] = (
            capo_agent_registry_control.types.subnet_ids.deserialize_json(
                data["subnetIds"]
            )
        )
    else:
        raise DeserializationError("ManagedVpcResource.subnet_ids required")
    if data.get("endpointIpAddressType") is not None:
        import capo_agent_registry_control.types.endpoint_ip_address_type

        out["endpoint_ip_address_type"] = (
            capo_agent_registry_control.types.endpoint_ip_address_type.deserialize_json(
                data["endpointIpAddressType"]
            )
        )
    else:
        raise DeserializationError(
            "ManagedVpcResource.endpoint_ip_address_type required"
        )
    if data.get("securityGroupIds") is not None:
        import capo_agent_registry_control.types.security_group_ids

        out["security_group_ids"] = (
            capo_agent_registry_control.types.security_group_ids.deserialize_json(
                data["securityGroupIds"]
            )
        )
    if data.get("tags") is not None:
        import capo_agent_registry_control.types.tags_map

        out["tags"] = capo_agent_registry_control.types.tags_map.deserialize_json(
            data["tags"]
        )
    if data.get("routingDomain") is not None:
        out["routing_domain"] = data["routingDomain"]
    return out
