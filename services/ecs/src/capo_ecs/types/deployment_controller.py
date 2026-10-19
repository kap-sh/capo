"""Generated from Smithy shape ``com.amazonaws.ecs#DeploymentController``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.deployment_controller_type


class DeploymentController(TypedDict, closed=True):
    type: "capo_ecs.types.deployment_controller_type.DeploymentControllerType"
    """<p>The deployment controller type to use.</p> <p>The deployment controller is the mechanism that determines how tasks are deployed for your service. The valid options are:</p> <ul> <li> <p>ECS</p> <p>When you create a service which uses the <code>ECS</code> deployment controller, you can choose between the following deployment strategies:</p> <ul> <li> <p> <code>ROLLING</code>: When you create a service which uses the <i>rolling update</i> (<code>ROLLING</code>) deployment strategy, the Amazon ECS service scheduler replaces the currently running tasks with new tasks. The number of tasks that Amazon ECS adds or removes from the service during a rolling update is controlled by the service deployment configuration. </p> <p>Rolling update deployments are best suited for the following scenarios:</p> <ul> <li> <p>Gradual service updates: You need to update your service incrementally without taking the entire service offline at once.</p> </li> <li> <p>Limited resource requirements: You want to avoid the additional resource costs of running two complete environments simultaneously (as required by blue/green deployments).</p> </li> <li> <p>Acceptable deployment time: Your application can tolerate a longer deployment process, as rolling updates replace tasks one by one.</p> </li> <li> <p>No need for instant roll back: Your service can tolerate a rollback process that takes minutes rather than seconds.</p> </li> <li> <p>Simple deployment process: You prefer a straightforward deployment approach without the complexity of managing multiple environments, target groups, and listeners.</p> </li> <li> <p>No load balancer requirement: Your service doesn't use or require a load balancer, Application Load Balancer, Network Load Balancer, or Service Connect (which are required for blue/green deployments).</p> </li> <li> <p>Stateful applications: Your application maintains state that makes it difficult to run two parallel environments.</p> </li> <li> <p>Cost sensitivity: You want to minimize deployment costs by not running duplicate environments during deployment.</p> </li> </ul> <p>Rolling updates are the default deployment strategy for services and provide a balance between deployment safety and resource efficiency for many common application scenarios.</p> </li> <li> <p> <code>BLUE_GREEN</code>: A <i>blue/green</i> deployment strategy (<code>BLUE_GREEN</code>) is a release methodology that reduces downtime and risk by running two identical production environments called blue and green. With Amazon ECS blue/green deployments, you can validate new service revisions before directing production traffic to them. This approach provides a safer way to deploy changes with the ability to quickly roll back if needed.</p> <p>Amazon ECS blue/green deployments are best suited for the following scenarios:</p> <ul> <li> <p>Service validation: When you need to validate new service revisions before directing production traffic to them</p> </li> <li> <p>Zero downtime: When your service requires zero-downtime deployments</p> </li> <li> <p>Instant roll back: When you need the ability to quickly roll back if issues are detected</p> </li> <li> <p>Load balancer requirement: When your service uses Application Load Balancer, Network Load Balancer, or Service Connect</p> </li> </ul> </li> </ul> </li> <li> <p>External</p> <p>Use a third-party deployment controller.</p> </li> <li> <p>Blue/green deployment (powered by CodeDeploy)</p> <p>CodeDeploy installs an updated version of the application as a new replacement task set and reroutes production traffic from the original application task set to the replacement task set. The original task set is terminated after a successful deployment. Use this deployment controller to verify a new deployment of a service before sending production traffic to it.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeploymentController) -> dict:
    out: dict = {}
    import capo_ecs.types.deployment_controller_type

    out["type"] = capo_ecs.types.deployment_controller_type.serialize_aws_json_1_1(
        value["type"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeploymentController:
    out: DeploymentController = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_ecs.types.deployment_controller_type

        out["type"] = (
            capo_ecs.types.deployment_controller_type.deserialize_aws_json_1_1(
                data["type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_ecs.types.deployment_controller_type.DeploymentControllerType", ""
        )
    return out
