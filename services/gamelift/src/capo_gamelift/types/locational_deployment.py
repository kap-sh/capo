"""Generated from Smithy shape ``com.amazonaws.gamelift#LocationalDeployment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.deployment_status


class LocationalDeployment(TypedDict, closed=True):
    deployment_status: NotRequired[
        "capo_gamelift.types.deployment_status.DeploymentStatus"
    ]
    """<p>The status of fleet deployment activity in the location. </p> <ul> <li> <p> <code>IN_PROGRESS</code> -- The deployment is in progress in the location. This status covers validation as well as the replacement of the location's containers.</p> </li> <li> <p> <code>IMPAIRED</code> -- The deployment failed validation in the location, and the location kept the containers that failed validation so that you can inspect them. A location reaches this status when the deployment's impairment strategy is <code>MAINTAIN</code>.</p> </li> <li> <p> <code>COMPLETE</code> -- The deployment has completed successfully in the location.</p> </li> <li> <p> <code>ROLLBACK_IN_PROGRESS</code> -- The deployment failed and rollback has been initiated in the location. A location reaches this status when the deployment's impairment strategy is <code>ROLLBACK</code>.</p> </li> <li> <p> <code>ROLLBACK_COMPLETE</code> -- The deployment failed and rollback has been completed in the location. The location is running the configuration from the last successful deployment.</p> </li> <li> <p> <code>CANCELLED</code> -- The deployment was cancelled because a new deployment started for the same fleet.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LocationalDeployment) -> dict:
    out: dict = {}
    if "deployment_status" in value:
        import capo_gamelift.types.deployment_status

        out["DeploymentStatus"] = (
            capo_gamelift.types.deployment_status.serialize_aws_json_1_1(
                value["deployment_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LocationalDeployment:
    out: LocationalDeployment = {}  # type: ignore[typeddict-item]
    if data.get("DeploymentStatus") is not None:
        import capo_gamelift.types.deployment_status

        out["deployment_status"] = (
            capo_gamelift.types.deployment_status.deserialize_aws_json_1_1(
                data["DeploymentStatus"]
            )
        )
    return out
