"""Generated from Smithy shape ``com.amazonaws.ecs#UpdateServiceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ecs.types.availability_zone_rebalancing
    import capo_ecs.types.boolean
    import capo_ecs.types.boxed_boolean
    import capo_ecs.types.boxed_integer
    import capo_ecs.types.capacity_provider_strategy
    import capo_ecs.types.deployment_configuration
    import capo_ecs.types.deployment_controller
    import capo_ecs.types.load_balancers
    import capo_ecs.types.monitoring_configuration
    import capo_ecs.types.network_configuration
    import capo_ecs.types.placement_constraints
    import capo_ecs.types.placement_strategies
    import capo_ecs.types.propagate_tags
    import capo_ecs.types.service_connect_configuration
    import capo_ecs.types.service_registries
    import capo_ecs.types.service_volume_configurations
    import capo_ecs.types.string
    import capo_ecs.types.vpc_lattice_configurations


class UpdateServiceRequest(TypedDict, closed=True):
    cluster: NotRequired["capo_ecs.types.string.String"]
    """<p>The short name or full Amazon Resource Name (ARN) of the cluster that your service runs on. If you do not specify a cluster, the default cluster is assumed.</p> <p>You can't change the cluster name.</p>"""
    service: "capo_ecs.types.string.String"
    """<p>The name of the service to update.</p>"""
    desired_count: NotRequired["capo_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The number of instantiations of the task to place and keep running in your service.</p> <p>This parameter doesn't trigger a new service deployment.</p>"""
    task_definition: NotRequired["capo_ecs.types.string.String"]
    """<p>The <code>family</code> and <code>revision</code> (<code>family:revision</code>) or full ARN of the task definition to run in your service. If a <code>revision</code> is not specified, the latest <code>ACTIVE</code> revision is used. If you modify the task definition with <code>UpdateService</code>, Amazon ECS spawns a task with the new version of the task definition and then stops an old task after the new version is running.</p> <p>This parameter triggers a new service deployment.</p>"""
    capacity_provider_strategy: NotRequired[
        "capo_ecs.types.capacity_provider_strategy.CapacityProviderStrategy"
    ]
    """<p>The details of a capacity provider strategy. You can set a capacity provider when you create a cluster, run a task, or update a service.</p> <note> <p>If you want to use Amazon ECS Managed Instances, you must use the <code>capacityProviderStrategy</code> request parameter.</p> </note> <p>When you use Fargate, the capacity providers are <code>FARGATE</code> or <code>FARGATE_SPOT</code>.</p> <p>When you use Amazon EC2, the capacity providers are Auto Scaling groups.</p> <p>You can change capacity providers for rolling deployments and blue/green deployments.</p> <p>The following list provides the valid transitions:</p> <ul> <li> <p>Update the Fargate launch type to an Auto Scaling group capacity provider.</p> </li> <li> <p>Update the Amazon EC2 launch type to a Fargate capacity provider.</p> </li> <li> <p>Update the Fargate capacity provider to an Auto Scaling group capacity provider.</p> </li> <li> <p>Update the Amazon EC2 capacity provider to a Fargate capacity provider. </p> </li> <li> <p>Update the Auto Scaling group or Fargate capacity provider back to the launch type.</p> <p>Pass an empty list in the <code>capacityProviderStrategy</code> parameter.</p> </li> </ul> <p>For information about Amazon Web Services CDK considerations, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/update-service-parameters.html">Amazon Web Services CDK considerations</a>.</p> <p>This parameter doesn't trigger a new service deployment.</p>"""
    deployment_configuration: NotRequired[
        "capo_ecs.types.deployment_configuration.DeploymentConfiguration"
    ]
    """<p>Optional deployment parameters that control how many tasks run during the deployment and the ordering of stopping and starting tasks.</p> <p>This parameter doesn't trigger a new service deployment.</p>"""
    availability_zone_rebalancing: NotRequired[
        "capo_ecs.types.availability_zone_rebalancing.AvailabilityZoneRebalancing"
    ]
    """<p>Indicates whether to use Availability Zone rebalancing for the service.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-rebalancing.html">Balancing an Amazon ECS service across Availability Zones</a> in the <i> <i>Amazon Elastic Container Service Developer Guide</i> </i>.</p> <p>The default behavior of <code>AvailabilityZoneRebalancing</code> differs between create and update requests:</p> <ul> <li> <p>For create service requests, when no value is specified for <code>AvailabilityZoneRebalancing</code>, Amazon ECS defaults the value to <code>ENABLED</code>.</p> </li> <li> <p>For update service requests, when no value is specified for <code>AvailabilityZoneRebalancing</code>, Amazon ECS defaults to the existing service’s <code>AvailabilityZoneRebalancing</code> value. If the service never had an <code>AvailabilityZoneRebalancing</code> value set, Amazon ECS treats this as <code>DISABLED</code>.</p> </li> </ul> <p>This parameter doesn't trigger a new service deployment.</p>"""
    network_configuration: NotRequired[
        "capo_ecs.types.network_configuration.NetworkConfiguration"
    ]
    """<p>An object representing the network configuration for the service.</p> <p>This parameter triggers a new service deployment.</p>"""
    placement_constraints: NotRequired[
        "capo_ecs.types.placement_constraints.PlacementConstraints"
    ]
    """<p>An array of task placement constraint objects to update the service to use. If no value is specified, the existing placement constraints for the service will remain unchanged. If this value is specified, it will override any existing placement constraints defined for the service. To remove all existing placement constraints, specify an empty array.</p> <p>You can specify a maximum of 10 constraints for each task. This limit includes constraints in the task definition and those specified at runtime.</p> <p>This parameter doesn't trigger a new service deployment.</p>"""
    placement_strategy: NotRequired[
        "capo_ecs.types.placement_strategies.PlacementStrategies"
    ]
    """<p>The task placement strategy objects to update the service to use. If no value is specified, the existing placement strategy for the service will remain unchanged. If this value is specified, it will override the existing placement strategy defined for the service. To remove an existing placement strategy, specify an empty object.</p> <p>You can specify a maximum of five strategy rules for each service.</p> <p>This parameter doesn't trigger a new service deployment.</p>"""
    platform_version: NotRequired["capo_ecs.types.string.String"]
    """<p>The platform version that your tasks in the service run on. A platform version is only specified for tasks using the Fargate launch type. If a platform version is not specified, the <code>LATEST</code> platform version is used. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html">Fargate Platform Versions</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>This parameter triggers a new service deployment.</p>"""
    force_new_deployment: "capo_ecs.types.boolean.Boolean"
    """<p>Determines whether to force a new deployment of the service. By default, deployments aren't forced. You can use this option to start a new deployment with no service definition changes. For example, you can update a service's tasks to use a newer Docker image with the same image/tag combination (<code>my_image:latest</code>) or to roll Fargate tasks onto a newer platform version.</p>"""
    health_check_grace_period_seconds: NotRequired[
        "capo_ecs.types.boxed_integer.BoxedInteger"
    ]
    """<p>The period of time, in seconds, that the Amazon ECS service scheduler ignores unhealthy Elastic Load Balancing, VPC Lattice, and container health checks after a task has first started. If you don't specify a health check grace period value, the default value of <code>0</code> is used. If you don't use any of the health checks, then <code>healthCheckGracePeriodSeconds</code> is unused.</p> <p>If your service's tasks take a while to start and respond to health checks, you can specify a health check grace period of up to 2,147,483,647 seconds (about 69 years). During that time, the Amazon ECS service scheduler ignores health check status. This grace period can prevent the service scheduler from marking tasks as unhealthy and stopping them before they have time to come up.</p> <p>If your service has more running tasks than desired, unhealthy tasks in the grace period might be stopped to reach the desired count.</p> <p>This parameter doesn't trigger a new service deployment.</p>"""
    deployment_controller: NotRequired[
        "capo_ecs.types.deployment_controller.DeploymentController"
    ]
    enable_execute_command: NotRequired["capo_ecs.types.boxed_boolean.BoxedBoolean"]
    """<p>If <code>true</code>, this enables execute command functionality on all task containers.</p> <p>If you do not want to override the value that was set when the service was created, you can set this to <code>null</code> when performing this action.</p> <p>This parameter doesn't trigger a new service deployment.</p>"""
    enable_ecs_managed_tags: NotRequired["capo_ecs.types.boxed_boolean.BoxedBoolean"]
    """<p>Determines whether to turn on Amazon ECS managed tags for the tasks in the service. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-using-tags.html">Tagging Your Amazon ECS Resources</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>Only tasks launched after the update will reflect the update. To update the tags on all tasks, set <code>forceNewDeployment</code> to <code>true</code>, so that Amazon ECS starts new tasks with the updated tags.</p> <p>This parameter doesn't trigger a new service deployment.</p>"""
    load_balancers: NotRequired["capo_ecs.types.load_balancers.LoadBalancers"]
    """<note> <p>You must have a service-linked role when you update this property</p> </note> <p>A list of Elastic Load Balancing load balancer objects. It contains the load balancer name, the container name, and the container port to access from the load balancer. The container name is as it appears in a container definition.</p> <p>When you add, update, or remove a load balancer configuration, Amazon ECS starts new tasks with the updated Elastic Load Balancing configuration, and then stops the old tasks when the new tasks are running.</p> <p>For services that use rolling updates, you can add, update, or remove Elastic Load Balancing target groups. You can update from a single target group to multiple target groups and from multiple target groups to a single target group.</p> <p>For services that use blue/green deployments, you can update Elastic Load Balancing target groups by using <code> <a href="https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_CreateDeployment.html">CreateDeployment</a> </code> through CodeDeploy. Note that multiple target groups are not supported for blue/green deployments. For more information see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/register-multiple-targetgroups.html">Register multiple target groups with a service</a> in the <i>Amazon Elastic Container Service Developer Guide</i>. </p> <p>For services that use the external deployment controller, you can add, update, or remove load balancers by using <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateTaskSet.html">CreateTaskSet</a>. Note that multiple target groups are not supported for external deployments. For more information see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/register-multiple-targetgroups.html">Register multiple target groups with a service</a> in the <i>Amazon Elastic Container Service Developer Guide</i>. </p> <p>You can remove existing <code>loadBalancers</code> by passing an empty list.</p> <p>This parameter triggers a new service deployment.</p>"""
    propagate_tags: NotRequired["capo_ecs.types.propagate_tags.PropagateTags"]
    """<p>Determines whether to propagate the tags from the task definition or the service to the task. If no value is specified, the tags aren't propagated.</p> <p>Only tasks launched after the update will reflect the update. To update the tags on all tasks, set <code>forceNewDeployment</code> to <code>true</code>, so that Amazon ECS starts new tasks with the updated tags.</p> <p>This parameter doesn't trigger a new service deployment.</p>"""
    service_registries: NotRequired[
        "capo_ecs.types.service_registries.ServiceRegistries"
    ]
    """<note> <p>You must have a service-linked role when you update this property.</p> <p>For more information about the role see the <code>CreateService</code> request parameter <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateService.html#ECS-CreateService-request-role"> <code>role</code> </a>. </p> </note> <p>The details for the service discovery registries to assign to this service. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-discovery.html">Service Discovery</a>.</p> <p>When you add, update, or remove the service registries configuration, Amazon ECS starts new tasks with the updated service registries configuration, and then stops the old tasks when the new tasks are running.</p> <p>You can remove existing <code>serviceRegistries</code> by passing an empty list.</p> <p>This parameter triggers a new service deployment.</p>"""
    service_connect_configuration: NotRequired[
        "capo_ecs.types.service_connect_configuration.ServiceConnectConfiguration"
    ]
    """<p>The configuration for this service to discover and connect to services, and be discovered by, and connected from, other services within a namespace.</p> <p>Tasks that run in a namespace can use short names to connect to services in the namespace. Tasks can connect to services across all of the clusters in the namespace. Tasks connect through a managed proxy container that collects logs and metrics for increased visibility. Only the tasks that Amazon ECS services create are supported with Service Connect. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-connect.html">Service Connect</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>This parameter triggers a new service deployment.</p>"""
    volume_configurations: NotRequired[
        "capo_ecs.types.service_volume_configurations.ServiceVolumeConfigurations"
    ]
    """<p>The details of the volume that was <code>configuredAtLaunch</code>. You can configure the size, volumeType, IOPS, throughput, snapshot and encryption in <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ServiceManagedEBSVolumeConfiguration.html">ServiceManagedEBSVolumeConfiguration</a>. The <code>name</code> of the volume must match the <code>name</code> from the task definition. If set to null, no new deployment is triggered. Otherwise, if this configuration differs from the existing one, it triggers a new deployment.</p> <p>This parameter triggers a new service deployment.</p>"""
    vpc_lattice_configurations: NotRequired[
        "capo_ecs.types.vpc_lattice_configurations.VpcLatticeConfigurations"
    ]
    """<p>An object representing the VPC Lattice configuration for the service being updated.</p> <p>This parameter triggers a new service deployment.</p>"""
    monitoring: NotRequired[
        "capo_ecs.types.monitoring_configuration.MonitoringConfiguration"
    ]
    """<p>The optional monitoring configuration for the service, which defines the resolution for the service-level <code>CPUUtilization</code> and <code>MemoryUtilization</code> Amazon CloudWatch metrics. When not specified, Amazon ECS uses the default resolution of <code>60</code> seconds.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateServiceRequest) -> dict:
    out: dict = {}
    if "cluster" in value:
        out["cluster"] = value["cluster"]
    out["service"] = value["service"]
    if "desired_count" in value:
        out["desiredCount"] = value["desired_count"]
    if "task_definition" in value:
        out["taskDefinition"] = value["task_definition"]
    if "capacity_provider_strategy" in value:
        import capo_ecs.types.capacity_provider_strategy

        out["capacityProviderStrategy"] = (
            capo_ecs.types.capacity_provider_strategy.serialize_aws_json_1_1(
                value["capacity_provider_strategy"]
            )
        )
    if "deployment_configuration" in value:
        import capo_ecs.types.deployment_configuration

        out["deploymentConfiguration"] = (
            capo_ecs.types.deployment_configuration.serialize_aws_json_1_1(
                value["deployment_configuration"]
            )
        )
    if "availability_zone_rebalancing" in value:
        import capo_ecs.types.availability_zone_rebalancing

        out["availabilityZoneRebalancing"] = (
            capo_ecs.types.availability_zone_rebalancing.serialize_aws_json_1_1(
                value["availability_zone_rebalancing"]
            )
        )
    if "network_configuration" in value:
        import capo_ecs.types.network_configuration

        out["networkConfiguration"] = (
            capo_ecs.types.network_configuration.serialize_aws_json_1_1(
                value["network_configuration"]
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
    if "platform_version" in value:
        out["platformVersion"] = value["platform_version"]
    out["forceNewDeployment"] = value.get("force_new_deployment", False)
    if "health_check_grace_period_seconds" in value:
        out["healthCheckGracePeriodSeconds"] = value[
            "health_check_grace_period_seconds"
        ]
    if "deployment_controller" in value:
        import capo_ecs.types.deployment_controller

        out["deploymentController"] = (
            capo_ecs.types.deployment_controller.serialize_aws_json_1_1(
                value["deployment_controller"]
            )
        )
    if "enable_execute_command" in value:
        out["enableExecuteCommand"] = value["enable_execute_command"]
    if "enable_ecs_managed_tags" in value:
        out["enableECSManagedTags"] = value["enable_ecs_managed_tags"]
    if "load_balancers" in value:
        import capo_ecs.types.load_balancers

        out["loadBalancers"] = capo_ecs.types.load_balancers.serialize_aws_json_1_1(
            value["load_balancers"]
        )
    if "propagate_tags" in value:
        import capo_ecs.types.propagate_tags

        out["propagateTags"] = capo_ecs.types.propagate_tags.serialize_aws_json_1_1(
            value["propagate_tags"]
        )
    if "service_registries" in value:
        import capo_ecs.types.service_registries

        out["serviceRegistries"] = (
            capo_ecs.types.service_registries.serialize_aws_json_1_1(
                value["service_registries"]
            )
        )
    if "service_connect_configuration" in value:
        import capo_ecs.types.service_connect_configuration

        out["serviceConnectConfiguration"] = (
            capo_ecs.types.service_connect_configuration.serialize_aws_json_1_1(
                value["service_connect_configuration"]
            )
        )
    if "volume_configurations" in value:
        import capo_ecs.types.service_volume_configurations

        out["volumeConfigurations"] = (
            capo_ecs.types.service_volume_configurations.serialize_aws_json_1_1(
                value["volume_configurations"]
            )
        )
    if "vpc_lattice_configurations" in value:
        import capo_ecs.types.vpc_lattice_configurations

        out["vpcLatticeConfigurations"] = (
            capo_ecs.types.vpc_lattice_configurations.serialize_aws_json_1_1(
                value["vpc_lattice_configurations"]
            )
        )
    if "monitoring" in value:
        import capo_ecs.types.monitoring_configuration

        out["monitoring"] = (
            capo_ecs.types.monitoring_configuration.serialize_aws_json_1_1(
                value["monitoring"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateServiceRequest:
    out: UpdateServiceRequest = {}  # type: ignore[typeddict-item]
    if data.get("cluster") is not None:
        out["cluster"] = data["cluster"]
    if data.get("service") is not None:
        out["service"] = data["service"]
    else:
        raise DeserializationError("UpdateServiceRequest.service required")
    if data.get("desiredCount") is not None:
        out["desired_count"] = data["desiredCount"]
    if data.get("taskDefinition") is not None:
        out["task_definition"] = data["taskDefinition"]
    if data.get("capacityProviderStrategy") is not None:
        import capo_ecs.types.capacity_provider_strategy

        out["capacity_provider_strategy"] = (
            capo_ecs.types.capacity_provider_strategy.deserialize_aws_json_1_1(
                data["capacityProviderStrategy"]
            )
        )
    if data.get("deploymentConfiguration") is not None:
        import capo_ecs.types.deployment_configuration

        out["deployment_configuration"] = (
            capo_ecs.types.deployment_configuration.deserialize_aws_json_1_1(
                data["deploymentConfiguration"]
            )
        )
    if data.get("availabilityZoneRebalancing") is not None:
        import capo_ecs.types.availability_zone_rebalancing

        out["availability_zone_rebalancing"] = (
            capo_ecs.types.availability_zone_rebalancing.deserialize_aws_json_1_1(
                data["availabilityZoneRebalancing"]
            )
        )
    if data.get("networkConfiguration") is not None:
        import capo_ecs.types.network_configuration

        out["network_configuration"] = (
            capo_ecs.types.network_configuration.deserialize_aws_json_1_1(
                data["networkConfiguration"]
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
    if data.get("platformVersion") is not None:
        out["platform_version"] = data["platformVersion"]
    if data.get("forceNewDeployment") is not None:
        out["force_new_deployment"] = data["forceNewDeployment"]
    else:
        out["force_new_deployment"] = False
    if data.get("healthCheckGracePeriodSeconds") is not None:
        out["health_check_grace_period_seconds"] = data["healthCheckGracePeriodSeconds"]
    if data.get("deploymentController") is not None:
        import capo_ecs.types.deployment_controller

        out["deployment_controller"] = (
            capo_ecs.types.deployment_controller.deserialize_aws_json_1_1(
                data["deploymentController"]
            )
        )
    if data.get("enableExecuteCommand") is not None:
        out["enable_execute_command"] = data["enableExecuteCommand"]
    if data.get("enableECSManagedTags") is not None:
        out["enable_ecs_managed_tags"] = data["enableECSManagedTags"]
    if data.get("loadBalancers") is not None:
        import capo_ecs.types.load_balancers

        out["load_balancers"] = capo_ecs.types.load_balancers.deserialize_aws_json_1_1(
            data["loadBalancers"]
        )
    if data.get("propagateTags") is not None:
        import capo_ecs.types.propagate_tags

        out["propagate_tags"] = capo_ecs.types.propagate_tags.deserialize_aws_json_1_1(
            data["propagateTags"]
        )
    if data.get("serviceRegistries") is not None:
        import capo_ecs.types.service_registries

        out["service_registries"] = (
            capo_ecs.types.service_registries.deserialize_aws_json_1_1(
                data["serviceRegistries"]
            )
        )
    if data.get("serviceConnectConfiguration") is not None:
        import capo_ecs.types.service_connect_configuration

        out["service_connect_configuration"] = (
            capo_ecs.types.service_connect_configuration.deserialize_aws_json_1_1(
                data["serviceConnectConfiguration"]
            )
        )
    if data.get("volumeConfigurations") is not None:
        import capo_ecs.types.service_volume_configurations

        out["volume_configurations"] = (
            capo_ecs.types.service_volume_configurations.deserialize_aws_json_1_1(
                data["volumeConfigurations"]
            )
        )
    if data.get("vpcLatticeConfigurations") is not None:
        import capo_ecs.types.vpc_lattice_configurations

        out["vpc_lattice_configurations"] = (
            capo_ecs.types.vpc_lattice_configurations.deserialize_aws_json_1_1(
                data["vpcLatticeConfigurations"]
            )
        )
    if data.get("monitoring") is not None:
        import capo_ecs.types.monitoring_configuration

        out["monitoring"] = (
            capo_ecs.types.monitoring_configuration.deserialize_aws_json_1_1(
                data["monitoring"]
            )
        )
    return out
