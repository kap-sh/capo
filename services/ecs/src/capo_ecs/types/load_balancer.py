"""Generated from Smithy shape ``com.amazonaws.ecs#LoadBalancer``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.advanced_configuration
    import capo_ecs.types.boxed_integer
    import capo_ecs.types.string


class LoadBalancer(TypedDict, closed=True):
    target_group_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The full Amazon Resource Name (ARN) of the Elastic Load Balancing target group or groups associated with a service or task set.</p> <p>A target group ARN is only specified when using an Application Load Balancer or Network Load Balancer. </p> <p>For services using the <code>ECS</code> deployment controller, you can specify one or multiple target groups. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/register-multiple-targetgroups.html">Registering multiple target groups with a service</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>For services using the <code>CODE_DEPLOY</code> deployment controller, you're required to define two target groups for the load balancer. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-type-bluegreen.html">Blue/green deployment with CodeDeploy</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <important> <p>If your service's task definition uses the <code>awsvpc</code> network mode, you must choose <code>ip</code> as the target type, not <code>instance</code>. Do this when creating your target groups because tasks that use the <code>awsvpc</code> network mode are associated with an elastic network interface, not an Amazon EC2 instance. This network mode is required for the Fargate launch type.</p> </important>"""
    load_balancer_name: NotRequired["capo_ecs.types.string.String"]
    """<p>The name of the load balancer to associate with the Amazon ECS service or task set.</p> <p>If you are using an Application Load Balancer or a Network Load Balancer the load balancer name parameter should be omitted.</p>"""
    container_name: NotRequired["capo_ecs.types.string.String"]
    """<p>The name of the container (as it appears in a container definition) to associate with the load balancer.</p> <p>You need to specify the container name when configuring the target group for an Amazon ECS load balancer.</p>"""
    container_port: NotRequired["capo_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The port on the container to associate with the load balancer. This port must correspond to a <code>containerPort</code> in the task definition the tasks in the service are using. For tasks that use the EC2 launch type, the container instance they're launched on must allow ingress traffic on the <code>hostPort</code> of the port mapping.</p>"""
    advanced_configuration: NotRequired[
        "capo_ecs.types.advanced_configuration.AdvancedConfiguration"
    ]
    """<p>The advanced settings for the load balancer used in blue/green deployments. Specify the alternate target group, listener rules, and IAM role required for traffic shifting during blue/green deployments.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LoadBalancer) -> dict:
    out: dict = {}
    if "target_group_arn" in value:
        out["targetGroupArn"] = value["target_group_arn"]
    if "load_balancer_name" in value:
        out["loadBalancerName"] = value["load_balancer_name"]
    if "container_name" in value:
        out["containerName"] = value["container_name"]
    if "container_port" in value:
        out["containerPort"] = value["container_port"]
    if "advanced_configuration" in value:
        import capo_ecs.types.advanced_configuration

        out["advancedConfiguration"] = (
            capo_ecs.types.advanced_configuration.serialize_aws_json_1_1(
                value["advanced_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LoadBalancer:
    out: LoadBalancer = {}  # type: ignore[typeddict-item]
    if data.get("targetGroupArn") is not None:
        out["target_group_arn"] = data["targetGroupArn"]
    if data.get("loadBalancerName") is not None:
        out["load_balancer_name"] = data["loadBalancerName"]
    if data.get("containerName") is not None:
        out["container_name"] = data["containerName"]
    if data.get("containerPort") is not None:
        out["container_port"] = data["containerPort"]
    if data.get("advancedConfiguration") is not None:
        import capo_ecs.types.advanced_configuration

        out["advanced_configuration"] = (
            capo_ecs.types.advanced_configuration.deserialize_aws_json_1_1(
                data["advancedConfiguration"]
            )
        )
    return out
