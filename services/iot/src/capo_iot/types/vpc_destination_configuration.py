"""Generated from Smithy shape ``com.amazonaws.iot#VpcDestinationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.aws_arn
    import capo_iot.types.security_group_list
    import capo_iot.types.subnet_id_list
    import capo_iot.types.vpc_id


class VpcDestinationConfiguration(TypedDict, closed=True):
    subnet_ids: "capo_iot.types.subnet_id_list.SubnetIdList"
    """<p>The subnet IDs of the VPC destination.</p>"""
    security_groups: NotRequired["capo_iot.types.security_group_list.SecurityGroupList"]
    """<p>The security groups of the VPC destination.</p>"""
    vpc_id: "capo_iot.types.vpc_id.VpcId"
    """<p>The ID of the VPC.</p>"""
    role_arn: "capo_iot.types.aws_arn.AwsArn"
    """<p>The ARN of a role that has permission to create and attach to elastic network interfaces (ENIs).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VpcDestinationConfiguration) -> dict:
    out: dict = {}
    import capo_iot.types.subnet_id_list

    out["subnetIds"] = capo_iot.types.subnet_id_list.serialize_json(value["subnet_ids"])
    if "security_groups" in value:
        import capo_iot.types.security_group_list

        out["securityGroups"] = capo_iot.types.security_group_list.serialize_json(
            value["security_groups"]
        )
    out["vpcId"] = value["vpc_id"]
    out["roleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> VpcDestinationConfiguration:
    out: VpcDestinationConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("subnetIds") is not None:
        import capo_iot.types.subnet_id_list

        out["subnet_ids"] = capo_iot.types.subnet_id_list.deserialize_json(
            data["subnetIds"]
        )
    else:
        out["subnet_ids"] = []
    if data.get("securityGroups") is not None:
        import capo_iot.types.security_group_list

        out["security_groups"] = capo_iot.types.security_group_list.deserialize_json(
            data["securityGroups"]
        )
    if data.get("vpcId") is not None:
        out["vpc_id"] = data["vpcId"]
    else:
        out["vpc_id"] = ""
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        out["role_arn"] = ""
    return out
