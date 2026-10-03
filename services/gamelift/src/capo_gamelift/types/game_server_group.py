"""Generated from Smithy shape ``com.amazonaws.gamelift#GameServerGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.auto_scaling_group_arn
    import capo_gamelift.types.balancing_strategy
    import capo_gamelift.types.game_server_group_actions
    import capo_gamelift.types.game_server_group_arn
    import capo_gamelift.types.game_server_group_name
    import capo_gamelift.types.game_server_group_status
    import capo_gamelift.types.game_server_protection_policy
    import capo_gamelift.types.iam_role_arn
    import capo_gamelift.types.instance_definitions
    import capo_gamelift.types.non_zero_and_max_string
    import capo_gamelift.types.timestamp


class GameServerGroup(TypedDict, closed=True):
    game_server_group_name: NotRequired[
        "capo_gamelift.types.game_server_group_name.GameServerGroupName"
    ]
    """<p>A developer-defined identifier for the game server group. The name is unique for each Region in each Amazon Web Services account.</p>"""
    game_server_group_arn: NotRequired[
        "capo_gamelift.types.game_server_group_arn.GameServerGroupArn"
    ]
    """<p>A generated unique ID for the game server group.</p>"""
    role_arn: NotRequired["capo_gamelift.types.iam_role_arn.IamRoleArn"]
    """<p>The Amazon Resource Name (<a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html">ARN</a>) for an IAM role that allows Amazon GameLift Servers to access your Amazon EC2 Auto Scaling groups.</p>"""
    instance_definitions: NotRequired[
        "capo_gamelift.types.instance_definitions.InstanceDefinitions"
    ]
    """<p>The set of Amazon EC2 instance types that Amazon GameLift Servers FleetIQ can use when balancing and automatically scaling instances in the corresponding Auto Scaling group. </p>"""
    balancing_strategy: NotRequired[
        "capo_gamelift.types.balancing_strategy.BalancingStrategy"
    ]
    """<p>Indicates how Amazon GameLift Servers FleetIQ balances the use of Spot Instances and On-Demand Instances in the game server group. Method options include the following:</p> <ul> <li> <p> <code>SPOT_ONLY</code> - Only Spot Instances are used in the game server group. If Spot Instances are unavailable or not viable for game hosting, the game server group provides no hosting capacity until Spot Instances can again be used. Until then, no new instances are started, and the existing nonviable Spot Instances are terminated (after current gameplay ends) and are not replaced.</p> </li> <li> <p> <code>SPOT_PREFERRED</code> - (default value) Spot Instances are used whenever available in the game server group. If Spot Instances are unavailable, the game server group continues to provide hosting capacity by falling back to On-Demand Instances. Existing nonviable Spot Instances are terminated (after current gameplay ends) and are replaced with new On-Demand Instances.</p> </li> <li> <p> <code>ON_DEMAND_ONLY</code> - Only On-Demand Instances are used in the game server group. No Spot Instances are used, even when available, while this balancing strategy is in force.</p> </li> </ul>"""
    game_server_protection_policy: NotRequired[
        "capo_gamelift.types.game_server_protection_policy.GameServerProtectionPolicy"
    ]
    """<p>A flag that indicates whether instances in the game server group are protected from early termination. Unprotected instances that have active game servers running might be terminated during a scale-down event, causing players to be dropped from the game. Protected instances cannot be terminated while there are active game servers running except in the event of a forced game server group deletion (see ). An exception to this is with Spot Instances, which can be terminated by Amazon Web Services regardless of protection status. </p>"""
    auto_scaling_group_arn: NotRequired[
        "capo_gamelift.types.auto_scaling_group_arn.AutoScalingGroupArn"
    ]
    """<p>A generated unique ID for the Amazon EC2 Auto Scaling group that is associated with this game server group.</p>"""
    status: NotRequired[
        "capo_gamelift.types.game_server_group_status.GameServerGroupStatus"
    ]
    """<p>The current status of the game server group. Possible statuses include:</p> <ul> <li> <p> <code>NEW</code> - Amazon GameLift Servers FleetIQ has validated the <code>CreateGameServerGroup()</code> request. </p> </li> <li> <p> <code>ACTIVATING</code> - Amazon GameLift Servers FleetIQ is setting up a game server group, which includes creating an Auto Scaling group in your Amazon Web Services account. </p> </li> <li> <p> <code>ACTIVE</code> - The game server group has been successfully created. </p> </li> <li> <p> <code>DELETE_SCHEDULED</code> - A request to delete the game server group has been received. </p> </li> <li> <p> <code>DELETING</code> - Amazon GameLift Servers FleetIQ has received a valid <code>DeleteGameServerGroup()</code> request and is processing it. Amazon GameLift Servers FleetIQ must first complete and release hosts before it deletes the Auto Scaling group and the game server group. </p> </li> <li> <p> <code>DELETED</code> - The game server group has been successfully deleted. </p> </li> <li> <p> <code>ERROR</code> - The asynchronous processes of activating or deleting a game server group has failed, resulting in an error state.</p> </li> </ul>"""
    status_reason: NotRequired[
        "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>Additional information about the current game server group status. This information might provide additional insight on groups that are in <code>ERROR</code> status.</p>"""
    suspended_actions: NotRequired[
        "capo_gamelift.types.game_server_group_actions.GameServerGroupActions"
    ]
    """<p>A list of activities that are currently suspended for this game server group. If this property is empty, all activities are occurring.</p>"""
    creation_time: NotRequired["capo_gamelift.types.timestamp.Timestamp"]
    """<p>A time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example <code>"1469498468.057"</code>).</p>"""
    last_updated_time: NotRequired["capo_gamelift.types.timestamp.Timestamp"]
    """<p>A timestamp that indicates when this game server group was last updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GameServerGroup) -> dict:
    out: dict = {}
    if "game_server_group_name" in value:
        out["GameServerGroupName"] = value["game_server_group_name"]
    if "game_server_group_arn" in value:
        out["GameServerGroupArn"] = value["game_server_group_arn"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "instance_definitions" in value:
        import capo_gamelift.types.instance_definitions

        out["InstanceDefinitions"] = (
            capo_gamelift.types.instance_definitions.serialize_aws_json_1_1(
                value["instance_definitions"]
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
    if "auto_scaling_group_arn" in value:
        out["AutoScalingGroupArn"] = value["auto_scaling_group_arn"]
    if "status" in value:
        import capo_gamelift.types.game_server_group_status

        out["Status"] = (
            capo_gamelift.types.game_server_group_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "status_reason" in value:
        out["StatusReason"] = value["status_reason"]
    if "suspended_actions" in value:
        import capo_gamelift.types.game_server_group_actions

        out["SuspendedActions"] = (
            capo_gamelift.types.game_server_group_actions.serialize_aws_json_1_1(
                value["suspended_actions"]
            )
        )
    if "creation_time" in value:
        import capo_gamelift.types.timestamp

        out["CreationTime"] = capo_gamelift.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "last_updated_time" in value:
        import capo_gamelift.types.timestamp

        out["LastUpdatedTime"] = capo_gamelift.types.timestamp.serialize_aws_json_1_1(
            value["last_updated_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GameServerGroup:
    out: GameServerGroup = {}  # type: ignore[typeddict-item]
    if data.get("GameServerGroupName") is not None:
        out["game_server_group_name"] = data["GameServerGroupName"]
    if data.get("GameServerGroupArn") is not None:
        out["game_server_group_arn"] = data["GameServerGroupArn"]
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    if data.get("InstanceDefinitions") is not None:
        import capo_gamelift.types.instance_definitions

        out["instance_definitions"] = (
            capo_gamelift.types.instance_definitions.deserialize_aws_json_1_1(
                data["InstanceDefinitions"]
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
    if data.get("AutoScalingGroupArn") is not None:
        out["auto_scaling_group_arn"] = data["AutoScalingGroupArn"]
    if data.get("Status") is not None:
        import capo_gamelift.types.game_server_group_status

        out["status"] = (
            capo_gamelift.types.game_server_group_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if data.get("StatusReason") is not None:
        out["status_reason"] = data["StatusReason"]
    if data.get("SuspendedActions") is not None:
        import capo_gamelift.types.game_server_group_actions

        out["suspended_actions"] = (
            capo_gamelift.types.game_server_group_actions.deserialize_aws_json_1_1(
                data["SuspendedActions"]
            )
        )
    if data.get("CreationTime") is not None:
        import capo_gamelift.types.timestamp

        out["creation_time"] = capo_gamelift.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if data.get("LastUpdatedTime") is not None:
        import capo_gamelift.types.timestamp

        out["last_updated_time"] = (
            capo_gamelift.types.timestamp.deserialize_aws_json_1_1(
                data["LastUpdatedTime"]
            )
        )
    return out
