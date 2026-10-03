"""Generated from Smithy shape ``com.amazonaws.ecs#Service``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.availability_zone_rebalancing
    import capo_ecs.types.boolean
    import capo_ecs.types.boxed_integer
    import capo_ecs.types.capacity_provider_strategy
    import capo_ecs.types.deployment_configuration
    import capo_ecs.types.deployment_controller
    import capo_ecs.types.deployments
    import capo_ecs.types.integer
    import capo_ecs.types.launch_type
    import capo_ecs.types.load_balancers
    import capo_ecs.types.network_configuration
    import capo_ecs.types.placement_constraints
    import capo_ecs.types.placement_strategies
    import capo_ecs.types.propagate_tags
    import capo_ecs.types.resource_management_type
    import capo_ecs.types.scheduling_strategy
    import capo_ecs.types.service_current_revision_summary_list
    import capo_ecs.types.service_events
    import capo_ecs.types.service_registries
    import capo_ecs.types.string
    import capo_ecs.types.tags
    import capo_ecs.types.task_sets
    import capo_ecs.types.timestamp


class Service(TypedDict, closed=True):
    service_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The ARN that identifies the service. For more information about the ARN format, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-account-settings.html#ecs-resource-ids">Amazon Resource Name (ARN)</a> in the <i>Amazon ECS Developer Guide</i>.</p>"""
    service_name: NotRequired["capo_ecs.types.string.String"]
    """<p>The name of your service. Up to 255 letters (uppercase and lowercase), numbers, underscores, and hyphens are allowed. Service names must be unique within a cluster. However, you can have similarly named services in multiple clusters within a Region or across multiple Regions.</p>"""
    cluster_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the cluster that hosts the service.</p>"""
    load_balancers: NotRequired["capo_ecs.types.load_balancers.LoadBalancers"]
    """<p>A list of Elastic Load Balancing load balancer objects. It contains the load balancer name, the container name, and the container port to access from the load balancer. The container name is as it appears in a container definition.</p>"""
    service_registries: NotRequired[
        "capo_ecs.types.service_registries.ServiceRegistries"
    ]
    """<p>The details for the service discovery registries to assign to this service. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-discovery.html">Service Discovery</a>.</p>"""
    status: NotRequired["capo_ecs.types.string.String"]
    """<p>The status of the service. The valid values are <code>ACTIVE</code>, <code>DRAINING</code>, or <code>INACTIVE</code>.</p>"""
    desired_count: "capo_ecs.types.integer.Integer"
    """<p>The desired number of instantiations of the task definition to keep running on the service. This value is specified when the service is created with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateService.html">CreateService</a> , and it can be modified with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateService.html">UpdateService</a>.</p>"""
    running_count: "capo_ecs.types.integer.Integer"
    """<p>The number of tasks in the cluster that are in the <code>RUNNING</code> state.</p>"""
    pending_count: "capo_ecs.types.integer.Integer"
    """<p>The number of tasks in the cluster that are in the <code>PENDING</code> state.</p>"""
    launch_type: NotRequired["capo_ecs.types.launch_type.LaunchType"]
    """<p>The launch type the service is using. When using the DescribeServices API, this field is omitted if the service was created using a capacity provider strategy.</p>"""
    capacity_provider_strategy: NotRequired[
        "capo_ecs.types.capacity_provider_strategy.CapacityProviderStrategy"
    ]
    """<p>The capacity provider strategy the service uses. When using the DescribeServices API, this field is omitted if the service was created using a launch type.</p>"""
    platform_version: NotRequired["capo_ecs.types.string.String"]
    """<p>The platform version to run your service on. A platform version is only specified for tasks that are hosted on Fargate. If one isn't specified, the <code>LATEST</code> platform version is used. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html">Fargate Platform Versions</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""
    platform_family: NotRequired["capo_ecs.types.string.String"]
    """<p>The operating system that your tasks in the service run on. A platform family is specified only for tasks using the Fargate launch type. </p> <p> All tasks that run as part of this service must use the same <code>platformFamily</code> value as the service (for example, <code>LINUX</code>).</p>"""
    task_definition: NotRequired["capo_ecs.types.string.String"]
    """<p>The task definition to use for tasks in the service. This value is specified when the service is created with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateService.html">CreateService</a>, and it can be modified with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateService.html">UpdateService</a>.</p>"""
    deployment_configuration: NotRequired[
        "capo_ecs.types.deployment_configuration.DeploymentConfiguration"
    ]
    """<p>Optional deployment parameters that control how many tasks run during the deployment and the ordering of stopping and starting tasks.</p>"""
    task_sets: NotRequired["capo_ecs.types.task_sets.TaskSets"]
    """<p>Information about a set of Amazon ECS tasks in either an CodeDeploy or an <code>EXTERNAL</code> deployment. An Amazon ECS task set includes details such as the desired number of tasks, how many tasks are running, and whether the task set serves production traffic.</p>"""
    deployments: NotRequired["capo_ecs.types.deployments.Deployments"]
    """<p>The current state of deployments for the service.</p>"""
    role_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The ARN of the IAM role that's associated with the service. It allows the Amazon ECS container agent to register container instances with an Elastic Load Balancing load balancer.</p>"""
    events: NotRequired["capo_ecs.types.service_events.ServiceEvents"]
    """<p>The event stream for your service. A maximum of 100 of the latest events are displayed.</p>"""
    created_at: NotRequired["capo_ecs.types.timestamp.Timestamp"]
    """<p>The Unix timestamp for the time when the service was created.</p>"""
    current_service_deployment: NotRequired["capo_ecs.types.string.String"]
    """<p>The ARN of the current service deployment.</p>"""
    current_service_revisions: NotRequired[
        "capo_ecs.types.service_current_revision_summary_list.ServiceCurrentRevisionSummaryList"
    ]
    """<p>The list of the service revisions.</p>"""
    placement_constraints: NotRequired[
        "capo_ecs.types.placement_constraints.PlacementConstraints"
    ]
    """<p>The placement constraints for the tasks in the service.</p>"""
    placement_strategy: NotRequired[
        "capo_ecs.types.placement_strategies.PlacementStrategies"
    ]
    """<p>The placement strategy that determines how tasks for the service are placed.</p>"""
    network_configuration: NotRequired[
        "capo_ecs.types.network_configuration.NetworkConfiguration"
    ]
    """<p>The VPC subnet and security group configuration for tasks that receive their own elastic network interface by using the <code>awsvpc</code> networking mode.</p>"""
    health_check_grace_period_seconds: NotRequired[
        "capo_ecs.types.boxed_integer.BoxedInteger"
    ]
    """<p>The period of time, in seconds, that the Amazon ECS service scheduler ignores unhealthy Elastic Load Balancing, VPC Lattice, and container health checks after a task has first started.</p> <p>If your service has more running tasks than desired, unhealthy tasks in the grace period might be stopped to reach the desired count.</p>"""
    scheduling_strategy: NotRequired[
        "capo_ecs.types.scheduling_strategy.SchedulingStrategy"
    ]
    """<p>The scheduling strategy to use for the service. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs_services.html">Services</a>.</p> <p>There are two service scheduler strategies available.</p> <ul> <li> <p> <code>REPLICA</code>-The replica scheduling strategy places and maintains the desired number of tasks across your cluster. By default, the service scheduler spreads tasks across Availability Zones. You can use task placement strategies and constraints to customize task placement decisions.</p> </li> <li> <p> <code>DAEMON</code>-The daemon scheduling strategy deploys exactly one task on each active container instance. This task meets all of the task placement constraints that you specify in your cluster. The service scheduler also evaluates the task placement constraints for running tasks. It stop tasks that don't meet the placement constraints.</p> <note> <p>Fargate tasks don't support the <code>DAEMON</code> scheduling strategy.</p> </note> </li> </ul>"""
    deployment_controller: NotRequired[
        "capo_ecs.types.deployment_controller.DeploymentController"
    ]
    """<p>The deployment controller type the service is using. </p>"""
    tags: NotRequired["capo_ecs.types.tags.Tags"]
    """<p>The metadata that you apply to the service to help you categorize and organize them. Each tag consists of a key and an optional value. You define bot the key and value.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case-sensitive.</p> </li> <li> <p>Do not use <code>aws:</code>, <code>AWS:</code>, or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for Amazon Web Services use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.</p> </li> </ul>"""
    created_by: NotRequired["capo_ecs.types.string.String"]
    """<p>The principal that created the service.</p>"""
    enable_ecs_managed_tags: "capo_ecs.types.boolean.Boolean"
    """<p>Determines whether to use Amazon ECS managed tags for the tasks in the service. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-using-tags.html">Tagging Your Amazon ECS Resources</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""
    propagate_tags: NotRequired["capo_ecs.types.propagate_tags.PropagateTags"]
    """<p>Determines whether to propagate the tags from the task definition or the service to the task. If no value is specified, the tags aren't propagated.</p>"""
    enable_execute_command: "capo_ecs.types.boolean.Boolean"
    """<p>Determines whether the execute command functionality is turned on for the service. If <code>true</code>, the execute command functionality is turned on for all containers in tasks as part of the service.</p>"""
    availability_zone_rebalancing: NotRequired[
        "capo_ecs.types.availability_zone_rebalancing.AvailabilityZoneRebalancing"
    ]
    """<p>Indicates whether to use Availability Zone rebalancing for the service.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-rebalancing.html">Balancing an Amazon ECS service across Availability Zones</a> in the <i> <i>Amazon Elastic Container Service Developer Guide</i> </i>.</p> <p>The default behavior of <code>AvailabilityZoneRebalancing</code> differs between create and update requests:</p> <ul> <li> <p>For create service requests, when no value is specified for <code>AvailabilityZoneRebalancing</code>, Amazon ECS defaults the value to <code>ENABLED</code>.</p> </li> <li> <p>For update service requests, when no value is specified for <code>AvailabilityZoneRebalancing</code>, Amazon ECS defaults to the existing service’s <code>AvailabilityZoneRebalancing</code> value. If the service never had an <code>AvailabilityZoneRebalancing</code> value set, Amazon ECS treats this as <code>DISABLED</code>.</p> </li> </ul>"""
    resource_management_type: NotRequired[
        "capo_ecs.types.resource_management_type.ResourceManagementType"
    ]
    """<p>Identifies whether an ECS Service is an Express Service managed by ECS, or managed by the customer. The valid values are <code>ECS</code> and <code>CUSTOMER</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Service) -> dict:
    out: dict = {}
    if "service_arn" in value:
        out["serviceArn"] = value["service_arn"]
    if "service_name" in value:
        out["serviceName"] = value["service_name"]
    if "cluster_arn" in value:
        out["clusterArn"] = value["cluster_arn"]
    if "load_balancers" in value:
        import capo_ecs.types.load_balancers

        out["loadBalancers"] = capo_ecs.types.load_balancers.serialize_aws_json_1_1(
            value["load_balancers"]
        )
    if "service_registries" in value:
        import capo_ecs.types.service_registries

        out["serviceRegistries"] = (
            capo_ecs.types.service_registries.serialize_aws_json_1_1(
                value["service_registries"]
            )
        )
    if "status" in value:
        out["status"] = value["status"]
    out["desiredCount"] = value.get("desired_count", 0)
    out["runningCount"] = value.get("running_count", 0)
    out["pendingCount"] = value.get("pending_count", 0)
    if "launch_type" in value:
        import capo_ecs.types.launch_type

        out["launchType"] = capo_ecs.types.launch_type.serialize_aws_json_1_1(
            value["launch_type"]
        )
    if "capacity_provider_strategy" in value:
        import capo_ecs.types.capacity_provider_strategy

        out["capacityProviderStrategy"] = (
            capo_ecs.types.capacity_provider_strategy.serialize_aws_json_1_1(
                value["capacity_provider_strategy"]
            )
        )
    if "platform_version" in value:
        out["platformVersion"] = value["platform_version"]
    if "platform_family" in value:
        out["platformFamily"] = value["platform_family"]
    if "task_definition" in value:
        out["taskDefinition"] = value["task_definition"]
    if "deployment_configuration" in value:
        import capo_ecs.types.deployment_configuration

        out["deploymentConfiguration"] = (
            capo_ecs.types.deployment_configuration.serialize_aws_json_1_1(
                value["deployment_configuration"]
            )
        )
    if "task_sets" in value:
        import capo_ecs.types.task_sets

        out["taskSets"] = capo_ecs.types.task_sets.serialize_aws_json_1_1(
            value["task_sets"]
        )
    if "deployments" in value:
        import capo_ecs.types.deployments

        out["deployments"] = capo_ecs.types.deployments.serialize_aws_json_1_1(
            value["deployments"]
        )
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "events" in value:
        import capo_ecs.types.service_events

        out["events"] = capo_ecs.types.service_events.serialize_aws_json_1_1(
            value["events"]
        )
    if "created_at" in value:
        import capo_ecs.types.timestamp

        out["createdAt"] = capo_ecs.types.timestamp.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "current_service_deployment" in value:
        out["currentServiceDeployment"] = value["current_service_deployment"]
    if "current_service_revisions" in value:
        import capo_ecs.types.service_current_revision_summary_list

        out["currentServiceRevisions"] = (
            capo_ecs.types.service_current_revision_summary_list.serialize_aws_json_1_1(
                value["current_service_revisions"]
            )
        )
    if "placement_constraints" in value:
        import capo_ecs.types.placement_constraints

        out["placementConstraints"] = (
            capo_ecs.types.placement_constraints.serialize_aws_json_1_1(
                value["placement_constraints"]
            )
        )
    if "placement_strategy" in value:
        import capo_ecs.types.placement_strategies

        out["placementStrategy"] = (
            capo_ecs.types.placement_strategies.serialize_aws_json_1_1(
                value["placement_strategy"]
            )
        )
    if "network_configuration" in value:
        import capo_ecs.types.network_configuration

        out["networkConfiguration"] = (
            capo_ecs.types.network_configuration.serialize_aws_json_1_1(
                value["network_configuration"]
            )
        )
    if "health_check_grace_period_seconds" in value:
        out["healthCheckGracePeriodSeconds"] = value[
            "health_check_grace_period_seconds"
        ]
    if "scheduling_strategy" in value:
        import capo_ecs.types.scheduling_strategy

        out["schedulingStrategy"] = (
            capo_ecs.types.scheduling_strategy.serialize_aws_json_1_1(
                value["scheduling_strategy"]
            )
        )
    if "deployment_controller" in value:
        import capo_ecs.types.deployment_controller

        out["deploymentController"] = (
            capo_ecs.types.deployment_controller.serialize_aws_json_1_1(
                value["deployment_controller"]
            )
        )
    if "tags" in value:
        import capo_ecs.types.tags

        out["tags"] = capo_ecs.types.tags.serialize_aws_json_1_1(value["tags"])
    if "created_by" in value:
        out["createdBy"] = value["created_by"]
    out["enableECSManagedTags"] = value.get("enable_ecs_managed_tags", False)
    if "propagate_tags" in value:
        import capo_ecs.types.propagate_tags

        out["propagateTags"] = capo_ecs.types.propagate_tags.serialize_aws_json_1_1(
            value["propagate_tags"]
        )
    out["enableExecuteCommand"] = value.get("enable_execute_command", False)
    if "availability_zone_rebalancing" in value:
        import capo_ecs.types.availability_zone_rebalancing

        out["availabilityZoneRebalancing"] = (
            capo_ecs.types.availability_zone_rebalancing.serialize_aws_json_1_1(
                value["availability_zone_rebalancing"]
            )
        )
    if "resource_management_type" in value:
        import capo_ecs.types.resource_management_type

        out["resourceManagementType"] = (
            capo_ecs.types.resource_management_type.serialize_aws_json_1_1(
                value["resource_management_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Service:
    out: Service = {}  # type: ignore[typeddict-item]
    if data.get("serviceArn") is not None:
        out["service_arn"] = data["serviceArn"]
    if data.get("serviceName") is not None:
        out["service_name"] = data["serviceName"]
    if data.get("clusterArn") is not None:
        out["cluster_arn"] = data["clusterArn"]
    if data.get("loadBalancers") is not None:
        import capo_ecs.types.load_balancers

        out["load_balancers"] = capo_ecs.types.load_balancers.deserialize_aws_json_1_1(
            data["loadBalancers"]
        )
    if data.get("serviceRegistries") is not None:
        import capo_ecs.types.service_registries

        out["service_registries"] = (
            capo_ecs.types.service_registries.deserialize_aws_json_1_1(
                data["serviceRegistries"]
            )
        )
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("desiredCount") is not None:
        out["desired_count"] = data["desiredCount"]
    else:
        out["desired_count"] = 0
    if data.get("runningCount") is not None:
        out["running_count"] = data["runningCount"]
    else:
        out["running_count"] = 0
    if data.get("pendingCount") is not None:
        out["pending_count"] = data["pendingCount"]
    else:
        out["pending_count"] = 0
    if data.get("launchType") is not None:
        import capo_ecs.types.launch_type

        out["launch_type"] = capo_ecs.types.launch_type.deserialize_aws_json_1_1(
            data["launchType"]
        )
    if data.get("capacityProviderStrategy") is not None:
        import capo_ecs.types.capacity_provider_strategy

        out["capacity_provider_strategy"] = (
            capo_ecs.types.capacity_provider_strategy.deserialize_aws_json_1_1(
                data["capacityProviderStrategy"]
            )
        )
    if data.get("platformVersion") is not None:
        out["platform_version"] = data["platformVersion"]
    if data.get("platformFamily") is not None:
        out["platform_family"] = data["platformFamily"]
    if data.get("taskDefinition") is not None:
        out["task_definition"] = data["taskDefinition"]
    if data.get("deploymentConfiguration") is not None:
        import capo_ecs.types.deployment_configuration

        out["deployment_configuration"] = (
            capo_ecs.types.deployment_configuration.deserialize_aws_json_1_1(
                data["deploymentConfiguration"]
            )
        )
    if data.get("taskSets") is not None:
        import capo_ecs.types.task_sets

        out["task_sets"] = capo_ecs.types.task_sets.deserialize_aws_json_1_1(
            data["taskSets"]
        )
    if data.get("deployments") is not None:
        import capo_ecs.types.deployments

        out["deployments"] = capo_ecs.types.deployments.deserialize_aws_json_1_1(
            data["deployments"]
        )
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    if data.get("events") is not None:
        import capo_ecs.types.service_events

        out["events"] = capo_ecs.types.service_events.deserialize_aws_json_1_1(
            data["events"]
        )
    if data.get("createdAt") is not None:
        import capo_ecs.types.timestamp

        out["created_at"] = capo_ecs.types.timestamp.deserialize_aws_json_1_1(
            data["createdAt"]
        )
    if data.get("currentServiceDeployment") is not None:
        out["current_service_deployment"] = data["currentServiceDeployment"]
    if data.get("currentServiceRevisions") is not None:
        import capo_ecs.types.service_current_revision_summary_list

        out["current_service_revisions"] = (
            capo_ecs.types.service_current_revision_summary_list.deserialize_aws_json_1_1(
                data["currentServiceRevisions"]
            )
        )
    if data.get("placementConstraints") is not None:
        import capo_ecs.types.placement_constraints

        out["placement_constraints"] = (
            capo_ecs.types.placement_constraints.deserialize_aws_json_1_1(
                data["placementConstraints"]
            )
        )
    if data.get("placementStrategy") is not None:
        import capo_ecs.types.placement_strategies

        out["placement_strategy"] = (
            capo_ecs.types.placement_strategies.deserialize_aws_json_1_1(
                data["placementStrategy"]
            )
        )
    if data.get("networkConfiguration") is not None:
        import capo_ecs.types.network_configuration

        out["network_configuration"] = (
            capo_ecs.types.network_configuration.deserialize_aws_json_1_1(
                data["networkConfiguration"]
            )
        )
    if data.get("healthCheckGracePeriodSeconds") is not None:
        out["health_check_grace_period_seconds"] = data["healthCheckGracePeriodSeconds"]
    if data.get("schedulingStrategy") is not None:
        import capo_ecs.types.scheduling_strategy

        out["scheduling_strategy"] = (
            capo_ecs.types.scheduling_strategy.deserialize_aws_json_1_1(
                data["schedulingStrategy"]
            )
        )
    if data.get("deploymentController") is not None:
        import capo_ecs.types.deployment_controller

        out["deployment_controller"] = (
            capo_ecs.types.deployment_controller.deserialize_aws_json_1_1(
                data["deploymentController"]
            )
        )
    if data.get("tags") is not None:
        import capo_ecs.types.tags

        out["tags"] = capo_ecs.types.tags.deserialize_aws_json_1_1(data["tags"])
    if data.get("createdBy") is not None:
        out["created_by"] = data["createdBy"]
    if data.get("enableECSManagedTags") is not None:
        out["enable_ecs_managed_tags"] = data["enableECSManagedTags"]
    else:
        out["enable_ecs_managed_tags"] = False
    if data.get("propagateTags") is not None:
        import capo_ecs.types.propagate_tags

        out["propagate_tags"] = capo_ecs.types.propagate_tags.deserialize_aws_json_1_1(
            data["propagateTags"]
        )
    if data.get("enableExecuteCommand") is not None:
        out["enable_execute_command"] = data["enableExecuteCommand"]
    else:
        out["enable_execute_command"] = False
    if data.get("availabilityZoneRebalancing") is not None:
        import capo_ecs.types.availability_zone_rebalancing

        out["availability_zone_rebalancing"] = (
            capo_ecs.types.availability_zone_rebalancing.deserialize_aws_json_1_1(
                data["availabilityZoneRebalancing"]
            )
        )
    if data.get("resourceManagementType") is not None:
        import capo_ecs.types.resource_management_type

        out["resource_management_type"] = (
            capo_ecs.types.resource_management_type.deserialize_aws_json_1_1(
                data["resourceManagementType"]
            )
        )
    return out
