"""Generated from Smithy shape ``com.amazonaws.ecs#VpcLatticeConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ecs.types.iam_role_arn
    import capo_ecs.types.string
    import capo_ecs.types.vpc_lattice_advanced_configuration


class VpcLatticeConfiguration(TypedDict, closed=True):
    role_arn: "capo_ecs.types.iam_role_arn.IAMRoleArn"
    """<p>The ARN of the IAM role to associate with this VPC Lattice configuration. This is the Amazon ECS infrastructure IAM role that is used to manage your VPC Lattice infrastructure.</p>"""
    target_group_arn: "capo_ecs.types.string.String"
    """<p>The full Amazon Resource Name (ARN) of the target group or groups associated with the VPC Lattice configuration that the Amazon ECS tasks will be registered to.</p>"""
    port_name: "capo_ecs.types.string.String"
    """<p>The name of the port mapping to register in the VPC Lattice target group. This is the name of the <code>portMapping</code> you defined in your task definition.</p>"""
    advanced_configuration: NotRequired[
        "capo_ecs.types.vpc_lattice_advanced_configuration.VpcLatticeAdvancedConfiguration"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VpcLatticeConfiguration) -> dict:
    out: dict = {}
    out["roleArn"] = value["role_arn"]
    out["targetGroupArn"] = value["target_group_arn"]
    out["portName"] = value["port_name"]
    if "advanced_configuration" in value:
        import capo_ecs.types.vpc_lattice_advanced_configuration

        out["advancedConfiguration"] = (
            capo_ecs.types.vpc_lattice_advanced_configuration.serialize_aws_json_1_1(
                value["advanced_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> VpcLatticeConfiguration:
    out: VpcLatticeConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("VpcLatticeConfiguration.role_arn required")
    if data.get("targetGroupArn") is not None:
        out["target_group_arn"] = data["targetGroupArn"]
    else:
        raise DeserializationError("VpcLatticeConfiguration.target_group_arn required")
    if data.get("portName") is not None:
        out["port_name"] = data["portName"]
    else:
        raise DeserializationError("VpcLatticeConfiguration.port_name required")
    if data.get("advancedConfiguration") is not None:
        import capo_ecs.types.vpc_lattice_advanced_configuration

        out["advanced_configuration"] = (
            capo_ecs.types.vpc_lattice_advanced_configuration.deserialize_aws_json_1_1(
                data["advancedConfiguration"]
            )
        )
    return out
