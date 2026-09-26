"""Generated from Smithy shape ``com.amazonaws.lambdacore#NetworkConnectorVpcEgressConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda_core.types.associated_compute_resource_types_list
    import capo_lambda_core.types.network_connector_security_group_ids
    import capo_lambda_core.types.network_connector_subnet_ids
    import capo_lambda_core.types.network_protocol


class NetworkConnectorVpcEgressConfiguration(TypedDict, closed=True):
    subnet_ids: NotRequired[
        "capo_lambda_core.types.network_connector_subnet_ids.NetworkConnectorSubnetIds"
    ]
    """<p>The IDs of the VPC subnets where Lambda provisions elastic network interfaces (ENIs). Specify 1 to 16 subnets. All subnets must be in the same VPC.</p>"""
    security_group_ids: NotRequired[
        "capo_lambda_core.types.network_connector_security_group_ids.NetworkConnectorSecurityGroupIds"
    ]
    """<p>The IDs of the VPC security groups to attach to the ENIs. Specify 0 to 5 security groups. All security groups must be in the same VPC as the subnets.</p>"""
    network_protocol: NotRequired[
        "capo_lambda_core.types.network_protocol.NetworkProtocol"
    ]
    """<p>The network protocol for the connector. Specify <code>IPv4</code> for IPv4-only networking, or <code>DualStack</code> for both IPv4 and IPv6.</p>"""
    associated_compute_resource_types: NotRequired[
        "capo_lambda_core.types.associated_compute_resource_types_list.AssociatedComputeResourceTypesList"
    ]
    """<p>The types of Lambda compute resources that can use this connector. Currently, only <code>MicroVm</code> is supported.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkConnectorVpcEgressConfiguration) -> dict:
    out: dict = {}
    if "subnet_ids" in value:
        import capo_lambda_core.types.network_connector_subnet_ids

        out["SubnetIds"] = (
            capo_lambda_core.types.network_connector_subnet_ids.serialize_json(
                value["subnet_ids"]
            )
        )
    if "security_group_ids" in value:
        import capo_lambda_core.types.network_connector_security_group_ids

        out["SecurityGroupIds"] = (
            capo_lambda_core.types.network_connector_security_group_ids.serialize_json(
                value["security_group_ids"]
            )
        )
    if "network_protocol" in value:
        import capo_lambda_core.types.network_protocol

        out["NetworkProtocol"] = capo_lambda_core.types.network_protocol.serialize_json(
            value["network_protocol"]
        )
    if "associated_compute_resource_types" in value:
        import capo_lambda_core.types.associated_compute_resource_types_list

        out["AssociatedComputeResourceTypes"] = (
            capo_lambda_core.types.associated_compute_resource_types_list.serialize_json(
                value["associated_compute_resource_types"]
            )
        )
    return out


def deserialize_json(data: dict) -> NetworkConnectorVpcEgressConfiguration:
    out: NetworkConnectorVpcEgressConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("SubnetIds") is not None:
        import capo_lambda_core.types.network_connector_subnet_ids

        out["subnet_ids"] = (
            capo_lambda_core.types.network_connector_subnet_ids.deserialize_json(
                data["SubnetIds"]
            )
        )
    if data.get("SecurityGroupIds") is not None:
        import capo_lambda_core.types.network_connector_security_group_ids

        out["security_group_ids"] = (
            capo_lambda_core.types.network_connector_security_group_ids.deserialize_json(
                data["SecurityGroupIds"]
            )
        )
    if data.get("NetworkProtocol") is not None:
        import capo_lambda_core.types.network_protocol

        out["network_protocol"] = (
            capo_lambda_core.types.network_protocol.deserialize_json(
                data["NetworkProtocol"]
            )
        )
    if data.get("AssociatedComputeResourceTypes") is not None:
        import capo_lambda_core.types.associated_compute_resource_types_list

        out["associated_compute_resource_types"] = (
            capo_lambda_core.types.associated_compute_resource_types_list.deserialize_json(
                data["AssociatedComputeResourceTypes"]
            )
        )
    return out
