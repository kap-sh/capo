"""Generated from Smithy shape ``com.amazonaws.gamelift#FleetDeployment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.deployment_configuration
    import capo_gamelift.types.deployment_id
    import capo_gamelift.types.deployment_status
    import capo_gamelift.types.fleet_binary_arn
    import capo_gamelift.types.fleet_id
    import capo_gamelift.types.timestamp


class FleetDeployment(TypedDict, closed=True):
    deployment_id: NotRequired["capo_gamelift.types.deployment_id.DeploymentId"]
    """<p>A unique identifier for the deployment. </p>"""
    fleet_id: NotRequired["capo_gamelift.types.fleet_id.FleetId"]
    """<p>A unique identifier for the container fleet. </p>"""
    game_server_binary_arn: NotRequired[
        "capo_gamelift.types.fleet_binary_arn.FleetBinaryArn"
    ]
    """<p>The unique identifier for the version of the game server container group definition that is being deployed.</p>"""
    rollback_game_server_binary_arn: NotRequired[
        "capo_gamelift.types.fleet_binary_arn.FleetBinaryArn"
    ]
    """<p>The unique identifier for the version of the game server container group definition to roll back to if deployment fails. Amazon GameLift Servers sets this property to the container group definition version that the fleet used when it was last active.</p>"""
    per_instance_binary_arn: NotRequired[
        "capo_gamelift.types.fleet_binary_arn.FleetBinaryArn"
    ]
    """<p>The unique identifier for the version of the per-instance container group definition that is being deployed. </p>"""
    rollback_per_instance_binary_arn: NotRequired[
        "capo_gamelift.types.fleet_binary_arn.FleetBinaryArn"
    ]
    """<p>The unique identifier for the version of the per-instance container group definition to roll back to if deployment fails. Amazon GameLift Servers sets this property to the container group definition version that the fleet used when it was last active.</p>"""
    deployment_status: NotRequired[
        "capo_gamelift.types.deployment_status.DeploymentStatus"
    ]
    """<p>The status of the fleet deployment. For per-location status, see <code>LocationalDeployment</code>.</p> <ul> <li> <p> <code>PENDING</code> -- Amazon GameLift Servers has accepted the deployment and hasn't started it yet.</p> </li> <li> <p> <code>IN_PROGRESS</code> -- The deployment is in progress. This status covers validation as well as the replacement of the fleet's containers.</p> </li> <li> <p> <code>IMPAIRED</code> -- The deployment failed validation, and the fleet kept the containers that failed validation so that you can inspect them. A deployment reaches this status when its impairment strategy is <code>MAINTAIN</code>.</p> </li> <li> <p> <code>COMPLETE</code> -- The deployment has completed successfully in every fleet location.</p> </li> <li> <p> <code>ROLLBACK_IN_PROGRESS</code> -- The deployment failed and rollback has been initiated. A deployment reaches this status when its impairment strategy is <code>ROLLBACK</code>.</p> </li> <li> <p> <code>ROLLBACK_COMPLETE</code> -- The deployment failed and rollback has been completed. The fleet is running the configuration from the last successful deployment.</p> </li> <li> <p> <code>CANCELLED</code> -- The deployment was cancelled because a new deployment started for the same fleet.</p> </li> </ul> <p>For how to debug an impaired deployment or cancel one, see <a href="https://docs.aws.amazon.com/gameliftservers/latest/developerguide/containers-deployment-validation.html">Container fleet deployments</a>.</p>"""
    deployment_configuration: NotRequired[
        "capo_gamelift.types.deployment_configuration.DeploymentConfiguration"
    ]
    """<p>Instructions for how to deploy updates to a container fleet and what actions to take if the deployment fails.</p>"""
    creation_time: NotRequired["capo_gamelift.types.timestamp.Timestamp"]
    """<p>A time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example <code>"1469498468.057"</code>).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FleetDeployment) -> dict:
    out: dict = {}
    if "deployment_id" in value:
        out["DeploymentId"] = value["deployment_id"]
    if "fleet_id" in value:
        out["FleetId"] = value["fleet_id"]
    if "game_server_binary_arn" in value:
        out["GameServerBinaryArn"] = value["game_server_binary_arn"]
    if "rollback_game_server_binary_arn" in value:
        out["RollbackGameServerBinaryArn"] = value["rollback_game_server_binary_arn"]
    if "per_instance_binary_arn" in value:
        out["PerInstanceBinaryArn"] = value["per_instance_binary_arn"]
    if "rollback_per_instance_binary_arn" in value:
        out["RollbackPerInstanceBinaryArn"] = value["rollback_per_instance_binary_arn"]
    if "deployment_status" in value:
        import capo_gamelift.types.deployment_status

        out["DeploymentStatus"] = (
            capo_gamelift.types.deployment_status.serialize_aws_json_1_1(
                value["deployment_status"]
            )
        )
    if "deployment_configuration" in value:
        import capo_gamelift.types.deployment_configuration

        out["DeploymentConfiguration"] = (
            capo_gamelift.types.deployment_configuration.serialize_aws_json_1_1(
                value["deployment_configuration"]
            )
        )
    if "creation_time" in value:
        import capo_gamelift.types.timestamp

        out["CreationTime"] = capo_gamelift.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> FleetDeployment:
    out: FleetDeployment = {}  # type: ignore[typeddict-item]
    if data.get("DeploymentId") is not None:
        out["deployment_id"] = data["DeploymentId"]
    if data.get("FleetId") is not None:
        out["fleet_id"] = data["FleetId"]
    if data.get("GameServerBinaryArn") is not None:
        out["game_server_binary_arn"] = data["GameServerBinaryArn"]
    if data.get("RollbackGameServerBinaryArn") is not None:
        out["rollback_game_server_binary_arn"] = data["RollbackGameServerBinaryArn"]
    if data.get("PerInstanceBinaryArn") is not None:
        out["per_instance_binary_arn"] = data["PerInstanceBinaryArn"]
    if data.get("RollbackPerInstanceBinaryArn") is not None:
        out["rollback_per_instance_binary_arn"] = data["RollbackPerInstanceBinaryArn"]
    if data.get("DeploymentStatus") is not None:
        import capo_gamelift.types.deployment_status

        out["deployment_status"] = (
            capo_gamelift.types.deployment_status.deserialize_aws_json_1_1(
                data["DeploymentStatus"]
            )
        )
    if data.get("DeploymentConfiguration") is not None:
        import capo_gamelift.types.deployment_configuration

        out["deployment_configuration"] = (
            capo_gamelift.types.deployment_configuration.deserialize_aws_json_1_1(
                data["DeploymentConfiguration"]
            )
        )
    if data.get("CreationTime") is not None:
        import capo_gamelift.types.timestamp

        out["creation_time"] = capo_gamelift.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    return out
