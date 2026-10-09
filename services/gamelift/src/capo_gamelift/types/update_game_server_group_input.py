"""Generated from Smithy shape ``com.amazonaws.gamelift#UpdateGameServerGroupInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.balancing_strategy
    import capo_gamelift.types.game_server_group_name_or_arn
    import capo_gamelift.types.game_server_protection_policy
    import capo_gamelift.types.iam_role_arn
    import capo_gamelift.types.instance_definitions


class UpdateGameServerGroupInput(TypedDict, closed=True):
    game_server_group_name: NotRequired[
        "capo_gamelift.types.game_server_group_name_or_arn.GameServerGroupNameOrArn"
    ]
    """<p>A unique identifier for the game server group. Use either the name or ARN value.</p>"""
    role_arn: NotRequired["capo_gamelift.types.iam_role_arn.IamRoleArn"]
    """<p>The Amazon Resource Name (<a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html">ARN</a>) for an IAM role that allows Amazon GameLift Servers to access your Amazon EC2 Auto Scaling groups.</p>"""
    instance_definitions: NotRequired[
        "capo_gamelift.types.instance_definitions.InstanceDefinitions"
    ]
    """<p>An updated list of Amazon EC2 instance types to use in the Auto Scaling group. The instance definitions must specify at least two different instance types that are supported by Amazon GameLift Servers FleetIQ. This updated list replaces the entire current list of instance definitions for the game server group. For more information on instance types, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html">EC2 Instance Types</a> in the <i>Amazon EC2 User Guide</i>. You can optionally specify capacity weighting for each instance type. If no weight value is specified for an instance type, it is set to the default value "1". For more information about capacity weighting, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-instance-weighting.html"> Instance Weighting for Amazon EC2 Auto Scaling</a> in the Amazon EC2 Auto Scaling User Guide.</p>"""
    game_server_protection_policy: NotRequired[
        "capo_gamelift.types.game_server_protection_policy.GameServerProtectionPolicy"
    ]
    """<p>A flag that indicates whether instances in the game server group are protected from early termination. Unprotected instances that have active game servers running might be terminated during a scale-down event, causing players to be dropped from the game. Protected instances cannot be terminated while there are active game servers running except in the event of a forced game server group deletion. An exception to this is with Spot Instances, which can be terminated by Amazon Web Services regardless of protection status. This property is set to <code>NO_PROTECTION</code> by default.</p>"""
    balancing_strategy: NotRequired[
        "capo_gamelift.types.balancing_strategy.BalancingStrategy"
    ]
    """<p>Indicates how Amazon GameLift Servers FleetIQ balances the use of Spot Instances and On-Demand Instances in the game server group. Method options include the following:</p> <ul> <li> <p> <code>SPOT_ONLY</code> - Only Spot Instances are used in the game server group. If Spot Instances are unavailable or not viable for game hosting, the game server group provides no hosting capacity until Spot Instances can again be used. Until then, no new instances are started, and the existing nonviable Spot Instances are terminated (after current gameplay ends) and are not replaced.</p> </li> <li> <p> <code>SPOT_PREFERRED</code> - (default value) Spot Instances are used whenever available in the game server group. If Spot Instances are unavailable, the game server group continues to provide hosting capacity by falling back to On-Demand Instances. Existing nonviable Spot Instances are terminated (after current gameplay ends) and are replaced with new On-Demand Instances.</p> </li> <li> <p> <code>ON_DEMAND_ONLY</code> - Only On-Demand Instances are used in the game server group. No Spot Instances are used, even when available, while this balancing strategy is in force.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateGameServerGroupInput) -> dict:
    out: dict = {}
    if "game_server_group_name" in value:
        out["GameServerGroupName"] = value["game_server_group_name"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "instance_definitions" in value:
        import capo_gamelift.types.instance_definitions

        out["InstanceDefinitions"] = (
            capo_gamelift.types.instance_definitions.serialize_aws_json_1_1(
                value["instance_definitions"]
            )
        )
    if "game_server_protection_policy" in value:
        import capo_gamelift.types.game_server_protection_policy

        out["GameServerProtectionPolicy"] = (
            capo_gamelift.types.game_server_protection_policy.serialize_aws_json_1_1(
                value["game_server_protection_policy"]
            )
        )
    if "balancing_strategy" in value:
        import capo_gamelift.types.balancing_strategy

        out["BalancingStrategy"] = (
            capo_gamelift.types.balancing_strategy.serialize_aws_json_1_1(
                value["balancing_strategy"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateGameServerGroupInput:
    out: UpdateGameServerGroupInput = {}  # type: ignore[typeddict-item]
    if data.get("GameServerGroupName") is not None:
        out["game_server_group_name"] = data["GameServerGroupName"]
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    if data.get("InstanceDefinitions") is not None:
        import capo_gamelift.types.instance_definitions

        out["instance_definitions"] = (
            capo_gamelift.types.instance_definitions.deserialize_aws_json_1_1(
                data["InstanceDefinitions"]
            )
        )
    if data.get("GameServerProtectionPolicy") is not None:
        import capo_gamelift.types.game_server_protection_policy

        out["game_server_protection_policy"] = (
            capo_gamelift.types.game_server_protection_policy.deserialize_aws_json_1_1(
                data["GameServerProtectionPolicy"]
            )
        )
    if data.get("BalancingStrategy") is not None:
        import capo_gamelift.types.balancing_strategy

        out["balancing_strategy"] = (
            capo_gamelift.types.balancing_strategy.deserialize_aws_json_1_1(
                data["BalancingStrategy"]
            )
        )
    return out
