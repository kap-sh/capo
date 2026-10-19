"""Generated from Smithy shape ``com.amazonaws.ecs#AwsVpcConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.assign_public_ip
    import capo_ecs.types.string_list


class AwsVpcConfiguration(TypedDict, closed=True):
    subnets: "capo_ecs.types.string_list.StringList"
    """<p>The IDs of the subnets associated with the task or service. There's a limit of 16 subnets that can be specified.</p> <note> <p>All specified subnets must be from the same VPC.</p> </note>"""
    security_groups: NotRequired["capo_ecs.types.string_list.StringList"]
    """<p>The IDs of the security groups associated with the task or service. If you don't specify a security group, the default security group for the VPC is used. There's a limit of 5 security groups that can be specified.</p> <note> <p>All specified security groups must be from the same VPC.</p> </note>"""
    assign_public_ip: NotRequired["capo_ecs.types.assign_public_ip.AssignPublicIp"]
    """<p>Whether the task's elastic network interface receives a public IP address. </p> <p>Consider the following when you set this value:</p> <ul> <li> <p>When you use <code>create-service</code> or <code>update-service</code>, the default is <code>DISABLED</code>. </p> </li> <li> <p>When the service <code>deploymentController</code> is <code>ECS</code>, the value must be <code>DISABLED</code>. </p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AwsVpcConfiguration) -> dict:
    out: dict = {}
    import capo_ecs.types.string_list

    out["subnets"] = capo_ecs.types.string_list.serialize_aws_json_1_1(value["subnets"])
    if "security_groups" in value:
        import capo_ecs.types.string_list

        out["securityGroups"] = capo_ecs.types.string_list.serialize_aws_json_1_1(
            value["security_groups"]
        )
    if "assign_public_ip" in value:
        import capo_ecs.types.assign_public_ip

        out["assignPublicIp"] = capo_ecs.types.assign_public_ip.serialize_aws_json_1_1(
            value["assign_public_ip"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AwsVpcConfiguration:
    out: AwsVpcConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("subnets") is not None:
        import capo_ecs.types.string_list

        out["subnets"] = capo_ecs.types.string_list.deserialize_aws_json_1_1(
            data["subnets"]
        )
    else:
        out["subnets"] = []
    if data.get("securityGroups") is not None:
        import capo_ecs.types.string_list

        out["security_groups"] = capo_ecs.types.string_list.deserialize_aws_json_1_1(
            data["securityGroups"]
        )
    if data.get("assignPublicIp") is not None:
        import capo_ecs.types.assign_public_ip

        out["assign_public_ip"] = (
            capo_ecs.types.assign_public_ip.deserialize_aws_json_1_1(
                data["assignPublicIp"]
            )
        )
    return out
