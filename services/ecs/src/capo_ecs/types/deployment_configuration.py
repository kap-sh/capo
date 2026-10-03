"""Generated from Smithy shape ``com.amazonaws.ecs#DeploymentConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.boxed_integer
    import capo_ecs.types.canary_configuration
    import capo_ecs.types.deployment_alarms
    import capo_ecs.types.deployment_circuit_breaker
    import capo_ecs.types.deployment_early_success_criteria
    import capo_ecs.types.deployment_lifecycle_hook_list
    import capo_ecs.types.deployment_strategy
    import capo_ecs.types.linear_configuration


class DeploymentConfiguration(TypedDict, closed=True):
    deployment_circuit_breaker: NotRequired[
        "capo_ecs.types.deployment_circuit_breaker.DeploymentCircuitBreaker"
    ]
    """<note> <p>The deployment circuit breaker can only be used for services using the rolling update (<code>ECS</code>) deployment type.</p> </note> <p>The <b>deployment circuit breaker</b> determines whether a service deployment will fail if the service can't reach a steady state. If you use the deployment circuit breaker, a service deployment will transition to a failed state and stop launching new tasks. If you use the rollback option, when a service deployment fails, the service is rolled back to the last deployment that completed successfully. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-type-ecs.html">Rolling update</a> in the <i>Amazon Elastic Container Service Developer Guide</i> </p>"""
    maximum_percent: NotRequired["capo_ecs.types.boxed_integer.BoxedInteger"]
    """<p>If a service is using the rolling update (<code>ECS</code>) deployment type, the <code>maximumPercent</code> parameter represents an upper limit on the number of your service's tasks that are allowed in the <code>RUNNING</code> or <code>PENDING</code> state during a deployment, as a percentage of the <code>desiredCount</code> (rounded down to the nearest integer). This parameter enables you to define the deployment batch size. For example, if your service is using the <code>REPLICA</code> service scheduler and has a <code>desiredCount</code> of four tasks and a <code>maximumPercent</code> value of 200%, the scheduler may start four new tasks before stopping the four older tasks (provided that the cluster resources required to do this are available). The default <code>maximumPercent</code> value for a service using the <code>REPLICA</code> service scheduler is 200%.</p> <p>The Amazon ECS scheduler uses this parameter to replace unhealthy tasks by starting replacement tasks first and then stopping the unhealthy tasks, as long as cluster resources for starting replacement tasks are available. For more information about how the scheduler replaces unhealthy tasks, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs_services.html">Amazon ECS services</a>.</p> <p>If a service is using either the blue/green (<code>CODE_DEPLOY</code>) or <code>EXTERNAL</code> deployment types, and tasks in the service use the EC2 launch type, the <b>maximum percent</b> value is set to the default value. The <b>maximum percent</b> value is used to define the upper limit on the number of the tasks in the service that remain in the <code>RUNNING</code> state while the container instances are in the <code>DRAINING</code> state.</p> <note> <p>You can't specify a custom <code>maximumPercent</code> value for a service that uses either the blue/green (<code>CODE_DEPLOY</code>) or <code>EXTERNAL</code> deployment types and has tasks that use the EC2 launch type.</p> </note> <p>If the service uses either the blue/green (<code>CODE_DEPLOY</code>) or <code>EXTERNAL</code> deployment types, and the tasks in the service use the Fargate launch type, the maximum percent value is not used. The value is still returned when describing your service.</p>"""
    minimum_healthy_percent: NotRequired["capo_ecs.types.boxed_integer.BoxedInteger"]
    """<p>If a service is using the rolling update (<code>ECS</code>) deployment type, the <code>minimumHealthyPercent</code> represents a lower limit on the number of your service's tasks that must remain in the <code>RUNNING</code> state during a deployment, as a percentage of the <code>desiredCount</code> (rounded up to the nearest integer). This parameter enables you to deploy without using additional cluster capacity. For example, if your service has a <code>desiredCount</code> of four tasks and a <code>minimumHealthyPercent</code> of 50%, the service scheduler may stop two existing tasks to free up cluster capacity before starting two new tasks. </p> <p> If any tasks are unhealthy and if <code>maximumPercent</code> doesn't allow the Amazon ECS scheduler to start replacement tasks, the scheduler stops the unhealthy tasks one-by-one — using the <code>minimumHealthyPercent</code> as a constraint — to clear up capacity to launch replacement tasks. For more information about how the scheduler replaces unhealthy tasks, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs_services.html">Amazon ECS services</a>. </p> <p>For services that <i>do not</i> use a load balancer, the following should be noted:</p> <ul> <li> <p>A service is considered healthy if all essential containers within the tasks in the service pass their health checks.</p> </li> <li> <p>If a task has no essential containers with a health check defined, the service scheduler will wait for 40 seconds after a task reaches a <code>RUNNING</code> state before the task is counted towards the minimum healthy percent total.</p> </li> <li> <p>If a task has one or more essential containers with a health check defined, the service scheduler will wait for the task to reach a healthy status before counting it towards the minimum healthy percent total. A task is considered healthy when all essential containers within the task have passed their health checks. The amount of time the service scheduler can wait for is determined by the container health check settings. </p> </li> </ul> <p>For services that <i>do</i> use a load balancer, the following should be noted:</p> <ul> <li> <p>If a task has no essential containers with a health check defined, the service scheduler will wait for the load balancer target group health check to return a healthy status before counting the task towards the minimum healthy percent total.</p> </li> <li> <p>If a task has an essential container with a health check defined, the service scheduler will wait for both the task to reach a healthy status and the load balancer target group health check to return a healthy status before counting the task towards the minimum healthy percent total.</p> </li> </ul> <p>The default value for a replica service for <code>minimumHealthyPercent</code> is 100%. The default <code>minimumHealthyPercent</code> value for a service using the <code>DAEMON</code> service schedule is 0% for the CLI, the Amazon Web Services SDKs, and the APIs and 50% for the Amazon Web Services Management Console.</p> <p>The minimum number of healthy tasks during a deployment is the <code>desiredCount</code> multiplied by the <code>minimumHealthyPercent</code>/100, rounded up to the nearest integer value.</p> <p>If a service is using either the blue/green (<code>CODE_DEPLOY</code>) or <code>EXTERNAL</code> deployment types and is running tasks that use the EC2 launch type, the <b>minimum healthy percent</b> value is set to the default value. The <b>minimum healthy percent</b> value is used to define the lower limit on the number of the tasks in the service that remain in the <code>RUNNING</code> state while the container instances are in the <code>DRAINING</code> state.</p> <note> <p>You can't specify a custom <code>minimumHealthyPercent</code> value for a service that uses either the blue/green (<code>CODE_DEPLOY</code>) or <code>EXTERNAL</code> deployment types and has tasks that use the EC2 launch type.</p> </note> <p>If a service is using either the blue/green (<code>CODE_DEPLOY</code>) or <code>EXTERNAL</code> deployment types and is running tasks that use the Fargate launch type, the minimum healthy percent value is not used, although it is returned when describing your service.</p>"""
    alarms: NotRequired["capo_ecs.types.deployment_alarms.DeploymentAlarms"]
    """<p>Information about the CloudWatch alarms.</p>"""
    strategy: NotRequired["capo_ecs.types.deployment_strategy.DeploymentStrategy"]
    """<p>The deployment strategy for the service. Choose from these valid values:</p> <ul> <li> <p> <code>ROLLING</code> - When you create a service which uses the rolling update (<code>ROLLING</code>) deployment strategy, the Amazon ECS service scheduler replaces the currently running tasks with new tasks. The number of tasks that Amazon ECS adds or removes from the service during a rolling update is controlled by the service deployment configuration.</p> </li> <li> <p> <code>BLUE_GREEN</code> - A blue/green deployment strategy (<code>BLUE_GREEN</code>) is a release methodology that reduces downtime and risk by running two identical production environments called blue and green. With Amazon ECS blue/green deployments, you can validate new service revisions before directing production traffic to them. This approach provides a safer way to deploy changes with the ability to quickly roll back if needed.</p> </li> <li> <p> <code>LINEAR</code> - A <i>linear</i> deployment strategy (<code>LINEAR</code>) gradually shifts traffic from the current production environment to a new environment in equal percentages over time. With Amazon ECS linear deployments, you can control the pace of traffic shifting and validate new service revisions with increasing amounts of production traffic.</p> </li> <li> <p> <code>CANARY</code> - A <i>canary</i> deployment strategy (<code>CANARY</code>) shifts a small percentage of traffic to the new service revision first, then shifts the remaining traffic all at once after a specified time period. This allows you to test the new version with a subset of users before full deployment.</p> </li> </ul>"""
    bake_time_in_minutes: NotRequired["capo_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The time period when both blue and green service revisions are running simultaneously after the production traffic has shifted.</p> <p>You must provide this parameter when you use the <code>BLUE_GREEN</code> deployment strategy.</p>"""
    lifecycle_hooks: NotRequired[
        "capo_ecs.types.deployment_lifecycle_hook_list.DeploymentLifecycleHookList"
    ]
    """<p>An array of deployment lifecycle hook objects to run custom logic or pause the deployment at specific stages of the deployment lifecycle.</p>"""
    linear_configuration: NotRequired[
        "capo_ecs.types.linear_configuration.LinearConfiguration"
    ]
    """<p>Configuration for linear deployment strategy. Only valid when the deployment strategy is <code>LINEAR</code>. This configuration enables progressive traffic shifting in equal percentage increments with configurable bake times between each step.</p>"""
    canary_configuration: NotRequired[
        "capo_ecs.types.canary_configuration.CanaryConfiguration"
    ]
    """<p>Configuration for canary deployment strategy. Only valid when the deployment strategy is <code>CANARY</code>. This configuration enables shifting a fixed percentage of traffic for testing, followed by shifting the remaining traffic after a bake period.</p>"""
    early_success_criteria: NotRequired[
        "capo_ecs.types.deployment_early_success_criteria.DeploymentEarlySuccessCriteria"
    ]
    """<p>The early success criteria configuration for a rolling deployment. With early success criteria, you can configure an Amazon ECS deployment to complete faster. Amazon ECS declares a deployment successful once a target percentage of tasks are healthy, instead of waiting for the service to fully stabilize.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeploymentConfiguration) -> dict:
    out: dict = {}
    if "deployment_circuit_breaker" in value:
        import capo_ecs.types.deployment_circuit_breaker

        out["deploymentCircuitBreaker"] = (
            capo_ecs.types.deployment_circuit_breaker.serialize_aws_json_1_1(
                value["deployment_circuit_breaker"]
            )
        )
    if "maximum_percent" in value:
        out["maximumPercent"] = value["maximum_percent"]
    if "minimum_healthy_percent" in value:
        out["minimumHealthyPercent"] = value["minimum_healthy_percent"]
    if "alarms" in value:
        import capo_ecs.types.deployment_alarms

        out["alarms"] = capo_ecs.types.deployment_alarms.serialize_aws_json_1_1(
            value["alarms"]
        )
    if "strategy" in value:
        import capo_ecs.types.deployment_strategy

        out["strategy"] = capo_ecs.types.deployment_strategy.serialize_aws_json_1_1(
            value["strategy"]
        )
    if "bake_time_in_minutes" in value:
        out["bakeTimeInMinutes"] = value["bake_time_in_minutes"]
    if "lifecycle_hooks" in value:
        import capo_ecs.types.deployment_lifecycle_hook_list

        out["lifecycleHooks"] = (
            capo_ecs.types.deployment_lifecycle_hook_list.serialize_aws_json_1_1(
                value["lifecycle_hooks"]
            )
        )
    if "linear_configuration" in value:
        import capo_ecs.types.linear_configuration

        out["linearConfiguration"] = (
            capo_ecs.types.linear_configuration.serialize_aws_json_1_1(
                value["linear_configuration"]
            )
        )
    if "canary_configuration" in value:
        import capo_ecs.types.canary_configuration

        out["canaryConfiguration"] = (
            capo_ecs.types.canary_configuration.serialize_aws_json_1_1(
                value["canary_configuration"]
            )
        )
    if "early_success_criteria" in value:
        import capo_ecs.types.deployment_early_success_criteria

        out["earlySuccessCriteria"] = (
            capo_ecs.types.deployment_early_success_criteria.serialize_aws_json_1_1(
                value["early_success_criteria"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeploymentConfiguration:
    out: DeploymentConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("deploymentCircuitBreaker") is not None:
        import capo_ecs.types.deployment_circuit_breaker

        out["deployment_circuit_breaker"] = (
            capo_ecs.types.deployment_circuit_breaker.deserialize_aws_json_1_1(
                data["deploymentCircuitBreaker"]
            )
        )
    if data.get("maximumPercent") is not None:
        out["maximum_percent"] = data["maximumPercent"]
    if data.get("minimumHealthyPercent") is not None:
        out["minimum_healthy_percent"] = data["minimumHealthyPercent"]
    if data.get("alarms") is not None:
        import capo_ecs.types.deployment_alarms

        out["alarms"] = capo_ecs.types.deployment_alarms.deserialize_aws_json_1_1(
            data["alarms"]
        )
    if data.get("strategy") is not None:
        import capo_ecs.types.deployment_strategy

        out["strategy"] = capo_ecs.types.deployment_strategy.deserialize_aws_json_1_1(
            data["strategy"]
        )
    if data.get("bakeTimeInMinutes") is not None:
        out["bake_time_in_minutes"] = data["bakeTimeInMinutes"]
    if data.get("lifecycleHooks") is not None:
        import capo_ecs.types.deployment_lifecycle_hook_list

        out["lifecycle_hooks"] = (
            capo_ecs.types.deployment_lifecycle_hook_list.deserialize_aws_json_1_1(
                data["lifecycleHooks"]
            )
        )
    if data.get("linearConfiguration") is not None:
        import capo_ecs.types.linear_configuration

        out["linear_configuration"] = (
            capo_ecs.types.linear_configuration.deserialize_aws_json_1_1(
                data["linearConfiguration"]
            )
        )
    if data.get("canaryConfiguration") is not None:
        import capo_ecs.types.canary_configuration

        out["canary_configuration"] = (
            capo_ecs.types.canary_configuration.deserialize_aws_json_1_1(
                data["canaryConfiguration"]
            )
        )
    if data.get("earlySuccessCriteria") is not None:
        import capo_ecs.types.deployment_early_success_criteria

        out["early_success_criteria"] = (
            capo_ecs.types.deployment_early_success_criteria.deserialize_aws_json_1_1(
                data["earlySuccessCriteria"]
            )
        )
    return out
