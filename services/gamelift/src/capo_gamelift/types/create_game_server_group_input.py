"""Generated from Smithy shape ``com.amazonaws.gamelift#CreateGameServerGroupInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.balancing_strategy
    import capo_gamelift.types.game_server_group_auto_scaling_policy
    import capo_gamelift.types.game_server_group_name
    import capo_gamelift.types.game_server_protection_policy
    import capo_gamelift.types.iam_role_arn
    import capo_gamelift.types.instance_definitions
    import capo_gamelift.types.launch_template_specification
    import capo_gamelift.types.positive_integer
    import capo_gamelift.types.tag_list
    import capo_gamelift.types.vpc_subnets
    import capo_gamelift.types.whole_number


class CreateGameServerGroupInput(TypedDict, closed=True):
    game_server_group_name: NotRequired[
        "capo_gamelift.types.game_server_group_name.GameServerGroupName"
    ]
    """<p>An identifier for the new game server group. This value is used to generate unique ARN identifiers for the Amazon EC2 Auto Scaling group and the Amazon GameLift Servers FleetIQ game server group. The name must be unique per Region per Amazon Web Services account.</p>"""
    role_arn: NotRequired["capo_gamelift.types.iam_role_arn.IamRoleArn"]
    """<p>The Amazon Resource Name (<a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html">ARN</a>) for an IAM role that allows Amazon GameLift Servers to access your Amazon EC2 Auto Scaling groups.</p>"""
    min_size: NotRequired["capo_gamelift.types.whole_number.WholeNumber"]
    """<p>The minimum number of instances allowed in the Amazon EC2 Auto Scaling group. During automatic scaling events, Amazon GameLift Servers FleetIQ and Amazon EC2 do not scale down the group below this minimum. In production, this value should be set to at least 1. After the Auto Scaling group is created, update this value directly in the Auto Scaling group using the Amazon Web Services console or APIs.</p>"""
    max_size: NotRequired["capo_gamelift.types.positive_integer.PositiveInteger"]
    """<p>The maximum number of instances allowed in the Amazon EC2 Auto Scaling group. During automatic scaling events, Amazon GameLift Servers FleetIQ and EC2 do not scale up the group above this maximum. After the Auto Scaling group is created, update this value directly in the Auto Scaling group using the Amazon Web Services console or APIs.</p>"""
    launch_template: NotRequired[
        "capo_gamelift.types.launch_template_specification.LaunchTemplateSpecification"
    ]
    """<p>The Amazon EC2 launch template that contains configuration settings and game server code to be deployed to all instances in the game server group. You can specify the template using either the template name or ID. For help with creating a launch template, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-launch-template.html">Creating a Launch Template for an Auto Scaling Group</a> in the <i>Amazon Elastic Compute Cloud Auto Scaling User Guide</i>. After the Auto Scaling group is created, update this value directly in the Auto Scaling group using the Amazon Web Services console or APIs.</p> <note> <p>If you specify network interfaces in your launch template, you must explicitly set the property <code>AssociatePublicIpAddress</code> to "true". If no network interface is specified in the launch template, Amazon GameLift Servers FleetIQ uses your account's default VPC.</p> </note>"""
    instance_definitions: NotRequired[
        "capo_gamelift.types.instance_definitions.InstanceDefinitions"
    ]
    """<p>The Amazon EC2 instance types and sizes to use in the Auto Scaling group. The instance definitions must specify at least two different instance types that are supported by Amazon GameLift Servers FleetIQ. For more information on instance types, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html">EC2 Instance Types</a> in the <i>Amazon Elastic Compute Cloud User Guide</i>. You can optionally specify capacity weighting for each instance type. If no weight value is specified for an instance type, it is set to the default value "1". For more information about capacity weighting, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-instance-weighting.html"> Instance Weighting for Amazon EC2 Auto Scaling</a> in the Amazon EC2 Auto Scaling User Guide.</p>"""
    auto_scaling_policy: NotRequired[
        "capo_gamelift.types.game_server_group_auto_scaling_policy.GameServerGroupAutoScalingPolicy"
    ]
    """<p>Configuration settings to define a scaling policy for the Auto Scaling group that is optimized for game hosting. The scaling policy uses the metric <code>"PercentUtilizedGameServers"</code> to maintain a buffer of idle game servers that can immediately accommodate new games and players. After the Auto Scaling group is created, update this value directly in the Auto Scaling group using the Amazon Web Services console or APIs.</p>"""
    balancing_strategy: NotRequired[
        "capo_gamelift.types.balancing_strategy.BalancingStrategy"
    ]
    """<p>Indicates how Amazon GameLift Servers FleetIQ balances the use of Spot Instances and On-Demand Instances in the game server group. Method options include the following:</p> <ul> <li> <p> <code>SPOT_ONLY</code> - Only Spot Instances are used in the game server group. If Spot Instances are unavailable or not viable for game hosting, the game server group provides no hosting capacity until Spot Instances can again be used. Until then, no new instances are started, and the existing nonviable Spot Instances are terminated (after current gameplay ends) and are not replaced.</p> </li> <li> <p> <code>SPOT_PREFERRED</code> - (default value) Spot Instances are used whenever available in the game server group. If Spot Instances are unavailable, the game server group continues to provide hosting capacity by falling back to On-Demand Instances. Existing nonviable Spot Instances are terminated (after current gameplay ends) and are replaced with new On-Demand Instances.</p> </li> <li> <p> <code>ON_DEMAND_ONLY</code> - Only On-Demand Instances are used in the game server group. No Spot Instances are used, even when available, while this balancing strategy is in force.</p> </li> </ul>"""
    game_server_protection_policy: NotRequired[
        "capo_gamelift.types.game_server_protection_policy.GameServerProtectionPolicy"
    ]
    """<p>A flag that indicates whether instances in the game server group are protected from early termination. Unprotected instances that have active game servers running might be terminated during a scale-down event, causing players to be dropped from the game. Protected instances cannot be terminated while there are active game servers running except in the event of a forced game server group deletion. An exception to this is with Spot Instances, which can be terminated by Amazon Web Services regardless of protection status. This property is set to <code>NO_PROTECTION</code> by default.</p>"""
    vpc_subnets: NotRequired["capo_gamelift.types.vpc_subnets.VpcSubnets"]
    """<p>A list of virtual private cloud (VPC) subnets to use with instances in the game server group. By default, all Amazon GameLift Servers FleetIQ-supported Availability Zones are used. You can use this parameter to specify VPCs that you've set up. This property cannot be updated after the game server group is created, and the corresponding Auto Scaling group will always use the property value that is set with this request, even if the Auto Scaling group is updated directly.</p>"""
    tags: NotRequired["capo_gamelift.types.tag_list.TagList"]
    """<p>A list of labels to assign to the new game server group resource. Tags are developer-defined key-value pairs. Tagging Amazon Web Services resources is useful for resource management, access management, and cost allocation. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html"> Tagging Amazon Web Services Resources</a> in the <i>Amazon Web Services General Reference</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateGameServerGroupInput) -> dict:
    out: dict = {}
    if "game_server_group_name" in value:
        out["GameServerGroupName"] = value["game_server_group_name"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "min_size" in value:
        out["MinSize"] = value["min_size"]
    if "max_size" in value:
        out["MaxSize"] = value["max_size"]
    if "launch_template" in value:
        import capo_gamelift.types.launch_template_specification

        out["LaunchTemplate"] = (
            capo_gamelift.types.launch_template_specification.serialize_aws_json_1_1(
                value["launch_template"]
            )
        )
    if "instance_definitions" in value:
        import capo_gamelift.types.instance_definitions

        out["InstanceDefinitions"] = (
            capo_gamelift.types.instance_definitions.serialize_aws_json_1_1(
                value["instance_definitions"]
            )
        )
    if "auto_scaling_policy" in value:
        import capo_gamelift.types.game_server_group_auto_scaling_policy

        out["AutoScalingPolicy"] = (
            capo_gamelift.types.game_server_group_auto_scaling_policy.serialize_aws_json_1_1(
                value["auto_scaling_policy"]
            )
        )
    if "balancing_strategy" in value:
        import capo_gamelift.types.balancing_strategy

        out["BalancingStrategy"] = (
            capo_gamelift.types.balancing_strategy.serialize_aws_json_1_1(
                value["balancing_strategy"]
            )
        )
    if "game_server_protection_policy" in value:
        import capo_gamelift.types.game_server_protection_policy

        out["GameServerProtectionPolicy"] = (
            capo_gamelift.types.game_server_protection_policy.serialize_aws_json_1_1(
                value["game_server_protection_policy"]
            )
        )
    if "vpc_subnets" in value:
        import capo_gamelift.types.vpc_subnets

        out["VpcSubnets"] = capo_gamelift.types.vpc_subnets.serialize_aws_json_1_1(
            value["vpc_subnets"]
        )
    if "tags" in value:
        import capo_gamelift.types.tag_list

        out["Tags"] = capo_gamelift.types.tag_list.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateGameServerGroupInput:
    out: CreateGameServerGroupInput = {}  # type: ignore[typeddict-item]
    if data.get("GameServerGroupName") is not None:
        out["game_server_group_name"] = data["GameServerGroupName"]
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    if data.get("MinSize") is not None:
        out["min_size"] = data["MinSize"]
    if data.get("MaxSize") is not None:
        out["max_size"] = data["MaxSize"]
    if data.get("LaunchTemplate") is not None:
        import capo_gamelift.types.launch_template_specification

        out["launch_template"] = (
            capo_gamelift.types.launch_template_specification.deserialize_aws_json_1_1(
                data["LaunchTemplate"]
            )
        )
    if data.get("InstanceDefinitions") is not None:
        import capo_gamelift.types.instance_definitions

        out["instance_definitions"] = (
            capo_gamelift.types.instance_definitions.deserialize_aws_json_1_1(
                data["InstanceDefinitions"]
            )
        )
    if data.get("AutoScalingPolicy") is not None:
        import capo_gamelift.types.game_server_group_auto_scaling_policy

        out["auto_scaling_policy"] = (
            capo_gamelift.types.game_server_group_auto_scaling_policy.deserialize_aws_json_1_1(
                data["AutoScalingPolicy"]
            )
        )
    if data.get("BalancingStrategy") is not None:
        import capo_gamelift.types.balancing_strategy

        out["balancing_strategy"] = (
            capo_gamelift.types.balancing_strategy.deserialize_aws_json_1_1(
                data["BalancingStrategy"]
            )
        )
    if data.get("GameServerProtectionPolicy") is not None:
        import capo_gamelift.types.game_server_protection_policy

        out["game_server_protection_policy"] = (
            capo_gamelift.types.game_server_protection_policy.deserialize_aws_json_1_1(
                data["GameServerProtectionPolicy"]
            )
        )
    if data.get("VpcSubnets") is not None:
        import capo_gamelift.types.vpc_subnets

        out["vpc_subnets"] = capo_gamelift.types.vpc_subnets.deserialize_aws_json_1_1(
            data["VpcSubnets"]
        )
    if data.get("Tags") is not None:
        import capo_gamelift.types.tag_list

        out["tags"] = capo_gamelift.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
