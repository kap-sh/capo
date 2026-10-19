"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleImportJobVPCConnectionOverrideParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.dns_resolver_list
    import capo_quicksight.types.resource_name
    import capo_quicksight.types.role_arn
    import capo_quicksight.types.security_group_id_list
    import capo_quicksight.types.subnet_id_list
    import capo_quicksight.types.vpc_connection_resource_id_unrestricted


class AssetBundleImportJobVPCConnectionOverrideParameters(TypedDict, closed=True):
    vpc_connection_id: "capo_quicksight.types.vpc_connection_resource_id_unrestricted.VPCConnectionResourceIdUnrestricted"
    """<p>The ID of the VPC Connection to apply overrides to.</p>"""
    name: NotRequired["capo_quicksight.types.resource_name.ResourceName"]
    """<p>A new name for the VPC connection.</p>"""
    subnet_ids: NotRequired["capo_quicksight.types.subnet_id_list.SubnetIdList"]
    """<p>A list of new subnet IDs for the VPC connection you are importing. This field is required if you are importing the VPC connection from another Amazon Web Services account or Region.</p>"""
    security_group_ids: NotRequired[
        "capo_quicksight.types.security_group_id_list.SecurityGroupIdList"
    ]
    """<p>A new security group ID for the VPC connection you are importing. This field is required if you are importing the VPC connection from another Amazon Web Services account or Region.</p>"""
    dns_resolvers: NotRequired[
        "capo_quicksight.types.dns_resolver_list.DnsResolverList"
    ]
    """<p>An optional override of DNS resolvers to be used by the VPC connection.</p>"""
    role_arn: NotRequired["capo_quicksight.types.role_arn.RoleArn"]
    """<p>An optional override of the role ARN to be used by the VPC connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleImportJobVPCConnectionOverrideParameters) -> dict:
    out: dict = {}
    out["VPCConnectionId"] = value["vpc_connection_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "subnet_ids" in value:
        import capo_quicksight.types.subnet_id_list

        out["SubnetIds"] = capo_quicksight.types.subnet_id_list.serialize_json(
            value["subnet_ids"]
        )
    if "security_group_ids" in value:
        import capo_quicksight.types.security_group_id_list

        out["SecurityGroupIds"] = (
            capo_quicksight.types.security_group_id_list.serialize_json(
                value["security_group_ids"]
            )
        )
    if "dns_resolvers" in value:
        import capo_quicksight.types.dns_resolver_list

        out["DnsResolvers"] = capo_quicksight.types.dns_resolver_list.serialize_json(
            value["dns_resolvers"]
        )
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> AssetBundleImportJobVPCConnectionOverrideParameters:
    out: AssetBundleImportJobVPCConnectionOverrideParameters = {}  # type: ignore[typeddict-item]
    if data.get("VPCConnectionId") is not None:
        out["vpc_connection_id"] = data["VPCConnectionId"]
    else:
        out["vpc_connection_id"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("SubnetIds") is not None:
        import capo_quicksight.types.subnet_id_list

        out["subnet_ids"] = capo_quicksight.types.subnet_id_list.deserialize_json(
            data["SubnetIds"]
        )
    if data.get("SecurityGroupIds") is not None:
        import capo_quicksight.types.security_group_id_list

        out["security_group_ids"] = (
            capo_quicksight.types.security_group_id_list.deserialize_json(
                data["SecurityGroupIds"]
            )
        )
    if data.get("DnsResolvers") is not None:
        import capo_quicksight.types.dns_resolver_list

        out["dns_resolvers"] = capo_quicksight.types.dns_resolver_list.deserialize_json(
            data["DnsResolvers"]
        )
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    return out
