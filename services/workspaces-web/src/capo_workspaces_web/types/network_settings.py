"""Generated from Smithy shape ``com.amazonaws.workspacesweb#NetworkSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_web.types.arn
    import capo_workspaces_web.types.arn_list
    import capo_workspaces_web.types.security_group_id_list
    import capo_workspaces_web.types.subnet_id_list
    import capo_workspaces_web.types.vpc_id


class NetworkSettings(TypedDict, closed=True):
    network_settings_arn: "capo_workspaces_web.types.arn.ARN"
    """<p>The ARN of the network settings.</p>"""
    associated_portal_arns: NotRequired["capo_workspaces_web.types.arn_list.ArnList"]
    """<p>A list of web portal ARNs that this network settings is associated with.</p>"""
    vpc_id: NotRequired["capo_workspaces_web.types.vpc_id.VpcId"]
    """<p>The VPC that streaming instances will connect to.</p>"""
    subnet_ids: NotRequired["capo_workspaces_web.types.subnet_id_list.SubnetIdList"]
    """<p>The subnets in which network interfaces are created to connect streaming instances to your VPC. At least two of these subnets must be in different availability zones.</p>"""
    security_group_ids: NotRequired[
        "capo_workspaces_web.types.security_group_id_list.SecurityGroupIdList"
    ]
    """<p>One or more security groups used to control access from streaming instances to your VPC. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkSettings) -> dict:
    out: dict = {}
    out["networkSettingsArn"] = value["network_settings_arn"]
    if "associated_portal_arns" in value:
        import capo_workspaces_web.types.arn_list

        out["associatedPortalArns"] = capo_workspaces_web.types.arn_list.serialize_json(
            value["associated_portal_arns"]
        )
    if "vpc_id" in value:
        out["vpcId"] = value["vpc_id"]
    if "subnet_ids" in value:
        import capo_workspaces_web.types.subnet_id_list

        out["subnetIds"] = capo_workspaces_web.types.subnet_id_list.serialize_json(
            value["subnet_ids"]
        )
    if "security_group_ids" in value:
        import capo_workspaces_web.types.security_group_id_list

        out["securityGroupIds"] = (
            capo_workspaces_web.types.security_group_id_list.serialize_json(
                value["security_group_ids"]
            )
        )
    return out


def deserialize_json(data: dict) -> NetworkSettings:
    out: NetworkSettings = {}  # type: ignore[typeddict-item]
    if data.get("networkSettingsArn") is not None:
        out["network_settings_arn"] = data["networkSettingsArn"]
    else:
        out["network_settings_arn"] = ""
    if data.get("associatedPortalArns") is not None:
        import capo_workspaces_web.types.arn_list

        out["associated_portal_arns"] = (
            capo_workspaces_web.types.arn_list.deserialize_json(
                data["associatedPortalArns"]
            )
        )
    if data.get("vpcId") is not None:
        out["vpc_id"] = data["vpcId"]
    if data.get("subnetIds") is not None:
        import capo_workspaces_web.types.subnet_id_list

        out["subnet_ids"] = capo_workspaces_web.types.subnet_id_list.deserialize_json(
            data["subnetIds"]
        )
    if data.get("securityGroupIds") is not None:
        import capo_workspaces_web.types.security_group_id_list

        out["security_group_ids"] = (
            capo_workspaces_web.types.security_group_id_list.deserialize_json(
                data["securityGroupIds"]
            )
        )
    return out
