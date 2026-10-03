"""Generated from Smithy shape ``com.amazonaws.gamelift#GameServerGroupAutoScalingPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.positive_integer
    import capo_gamelift.types.target_tracking_configuration


class GameServerGroupAutoScalingPolicy(TypedDict, closed=True):
    estimated_instance_warmup: NotRequired[
        "capo_gamelift.types.positive_integer.PositiveInteger"
    ]
    """<p>Length of time, in seconds, it takes for a new instance to start new game server processes and register with Amazon GameLift Servers FleetIQ. Specifying a warm-up time can be useful, particularly with game servers that take a long time to start up, because it avoids prematurely starting new instances. </p>"""
    target_tracking_configuration: NotRequired[
        "capo_gamelift.types.target_tracking_configuration.TargetTrackingConfiguration"
    ]
    """<p>Settings for a target-based scaling policy applied to Auto Scaling group. These settings are used to create a target-based policy that tracks the Amazon GameLift Servers FleetIQ metric <code>"PercentUtilizedGameServers"</code> and specifies a target value for the metric. As player usage changes, the policy triggers to adjust the game server group capacity so that the metric returns to the target value. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GameServerGroupAutoScalingPolicy) -> dict:
    out: dict = {}
    if "estimated_instance_warmup" in value:
        out["EstimatedInstanceWarmup"] = value["estimated_instance_warmup"]
    if "target_tracking_configuration" in value:
        import capo_gamelift.types.target_tracking_configuration

        out["TargetTrackingConfiguration"] = (
            capo_gamelift.types.target_tracking_configuration.serialize_aws_json_1_1(
                value["target_tracking_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GameServerGroupAutoScalingPolicy:
    out: GameServerGroupAutoScalingPolicy = {}  # type: ignore[typeddict-item]
    if data.get("EstimatedInstanceWarmup") is not None:
        out["estimated_instance_warmup"] = data["EstimatedInstanceWarmup"]
    if data.get("TargetTrackingConfiguration") is not None:
        import capo_gamelift.types.target_tracking_configuration

        out["target_tracking_configuration"] = (
            capo_gamelift.types.target_tracking_configuration.deserialize_aws_json_1_1(
                data["TargetTrackingConfiguration"]
            )
        )
    return out
