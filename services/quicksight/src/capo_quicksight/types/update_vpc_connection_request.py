"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateVPCConnectionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.dns_resolver_list
    import capo_quicksight.types.resource_name
    import capo_quicksight.types.role_arn
    import capo_quicksight.types.security_group_id_list
    import capo_quicksight.types.subnet_id_list
    import capo_quicksight.types.vpc_connection_resource_id_unrestricted


class UpdateVPCConnectionRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The Amazon Web Services account ID of the account that contains the VPC connection that you want to update.</p>"""
    vpc_connection_id: "capo_quicksight.types.vpc_connection_resource_id_unrestricted.VPCConnectionResourceIdUnrestricted"
    """<p>The ID of the VPC connection that you're updating. This ID is a unique identifier for each Amazon Web Services Region in an Amazon Web Services account.</p>"""
    name: "capo_quicksight.types.resource_name.ResourceName"
    """<p>The display name for the VPC connection.</p>"""
    subnet_ids: "capo_quicksight.types.subnet_id_list.SubnetIdList"
    """<p>A list of subnet IDs for the VPC connection.</p>"""
    security_group_ids: (
        "capo_quicksight.types.security_group_id_list.SecurityGroupIdList"
    )
    """<p>A list of security group IDs for the VPC connection.</p>"""
    dns_resolvers: NotRequired[
        "capo_quicksight.types.dns_resolver_list.DnsResolverList"
    ]
    """<p>A list of IP addresses of DNS resolver endpoints for the VPC connection.</p>"""
    role_arn: "capo_quicksight.types.role_arn.RoleArn"
    """<p>An IAM role associated with the VPC connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateVPCConnectionRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_quicksight.types.subnet_id_list

    out["SubnetIds"] = capo_quicksight.types.subnet_id_list.serialize_json(
        value["subnet_ids"]
    )
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
    out["RoleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> UpdateVPCConnectionRequest:
    out: UpdateVPCConnectionRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("SubnetIds") is not None:
        import capo_quicksight.types.subnet_id_list

        out["subnet_ids"] = capo_quicksight.types.subnet_id_list.deserialize_json(
            data["SubnetIds"]
        )
    else:
        out["subnet_ids"] = []
    if data.get("SecurityGroupIds") is not None:
        import capo_quicksight.types.security_group_id_list

        out["security_group_ids"] = (
            capo_quicksight.types.security_group_id_list.deserialize_json(
                data["SecurityGroupIds"]
            )
        )
    else:
        out["security_group_ids"] = []
    if data.get("DnsResolvers") is not None:
        import capo_quicksight.types.dns_resolver_list

        out["dns_resolvers"] = capo_quicksight.types.dns_resolver_list.deserialize_json(
            data["DnsResolvers"]
        )
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    else:
        out["role_arn"] = ""
    return out
