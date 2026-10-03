"""Generated from Smithy shape ``com.amazonaws.ecs#CreateServiceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ecs.types.availability_zone_rebalancing
    import capo_ecs.types.boolean
    import capo_ecs.types.boxed_integer
    import capo_ecs.types.capacity_provider_strategy
    import capo_ecs.types.deployment_configuration
    import capo_ecs.types.deployment_controller
    import capo_ecs.types.launch_type
    import capo_ecs.types.load_balancers
    import capo_ecs.types.monitoring_configuration
    import capo_ecs.types.network_configuration
    import capo_ecs.types.placement_constraints
    import capo_ecs.types.placement_strategies
    import capo_ecs.types.propagate_tags
    import capo_ecs.types.scheduling_strategy
    import capo_ecs.types.service_connect_configuration
    import capo_ecs.types.service_registries
    import capo_ecs.types.service_volume_configurations
    import capo_ecs.types.string
    import capo_ecs.types.tags
    import capo_ecs.types.vpc_lattice_configurations


class CreateServiceRequest(TypedDict, closed=True):
    cluster: NotRequired["capo_ecs.types.string.String"]
    """<p>The short name or full Amazon Resource Name (ARN) of the cluster that you run your service on. If you do not specify a cluster, the default cluster is assumed.</p>"""
    service_name: "capo_ecs.types.string.String"
    """<p>The name of your service. Up to 255 letters (uppercase and lowercase), numbers, underscores, and hyphens are allowed. Service names must be unique within a cluster, but you can have similarly named services in multiple clusters within a Region or across multiple Regions.</p>"""
    task_definition: NotRequired["capo_ecs.types.string.String"]
    """<p>The <code>family</code> and <code>revision</code> (<code>family:revision</code>) or full ARN of the task definition to run in your service. If a <code>revision</code> isn't specified, the latest <code>ACTIVE</code> revision is used.</p> <p>A task definition must be specified if the service uses either the <code>ECS</code> or <code>CODE_DEPLOY</code> deployment controllers.</p> <p>For more information about deployment types, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-types.html">Amazon ECS deployment types</a>.</p>"""
    availability_zone_rebalancing: NotRequired[
        "capo_ecs.types.availability_zone_rebalancing.AvailabilityZoneRebalancing"
    ]
    """<p>Indicates whether to use Availability Zone rebalancing for the service.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-rebalancing.html">Balancing an Amazon ECS service across Availability Zones</a> in the <i> <i>Amazon Elastic Container Service Developer Guide</i> </i>.</p> <p>The default behavior of <code>AvailabilityZoneRebalancing</code> differs between create and update requests:</p> <ul> <li> <p>For create service requests, when no value is specified for <code>AvailabilityZoneRebalancing</code>, Amazon ECS defaults the value to <code>ENABLED</code>.</p> </li> <li> <p>For update service requests, when no value is specified for <code>AvailabilityZoneRebalancing</code>, Amazon ECS defaults to the existing service’s <code>AvailabilityZoneRebalancing</code> value. If the service never had an <code>AvailabilityZoneRebalancing</code> value set, Amazon ECS treats this as <code>DISABLED</code>.</p> </li> </ul>"""
    load_balancers: NotRequired["capo_ecs.types.load_balancers.LoadBalancers"]
    """<p>A load balancer object representing the load balancers to use with your service. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-load-balancing.html">Service load balancing</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>If the service uses the <code>ECS</code> deployment controller and using either an Application Load Balancer or Network Load Balancer, you must specify one or more target group ARNs to attach to the service. The service-linked role is required for services that use multiple target groups. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using-service-linked-roles.html">Using service-linked roles for Amazon ECS</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>If the service uses the <code>CODE_DEPLOY</code> deployment controller, the service is required to use either an Application Load Balancer or Network Load Balancer. When creating an CodeDeploy deployment group, you specify two target groups (referred to as a <code>targetGroupPair</code>). During a deployment, CodeDeploy determines which task set in your service has the status <code>PRIMARY</code>, and it associates one target group with it. Then, it also associates the other target group with the replacement task set. The load balancer can also have up to two listeners: a required listener for production traffic and an optional listener that you can use to perform validation tests with Lambda functions before routing production traffic to it.</p> <p>If you use the <code>CODE_DEPLOY</code> deployment controller, these values can be changed when updating the service.</p> <p>For Application Load Balancers and Network Load Balancers, this object must contain the load balancer target group ARN, the container name, and the container port to access from the load balancer. The container name must be as it appears in a container definition. The load balancer name parameter must be omitted. When a task from this service is placed on a container instance, the container instance and port combination is registered as a target in the target group that's specified here.</p> <p>For Classic Load Balancers, this object must contain the load balancer name, the container name , and the container port to access from the load balancer. The container name must be as it appears in a container definition. The target group ARN parameter must be omitted. When a task from this service is placed on a container instance, the container instance is registered with the load balancer that's specified here.</p> <p>Services with tasks that use the <code>awsvpc</code> network mode (for example, those with the Fargate launch type) only support Application Load Balancers and Network Load Balancers. Classic Load Balancers aren't supported. Also, when you create any target groups for these services, you must choose <code>ip</code> as the target type, not <code>instance</code>. This is because tasks that use the <code>awsvpc</code> network mode are associated with an elastic network interface, not an Amazon EC2 instance.</p>"""
    service_registries: NotRequired[
        "capo_ecs.types.service_registries.ServiceRegistries"
    ]
    """<p>The details of the service discovery registry to associate with this service. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-discovery.html">Service discovery</a>.</p> <note> <p>Each service may be associated with one service registry. Multiple service registries for each service isn't supported.</p> </note>"""
    desired_count: NotRequired["capo_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The number of instantiations of the specified task definition to place and keep running in your service.</p> <p>This is required if <code>schedulingStrategy</code> is <code>REPLICA</code> or isn't specified. If <code>schedulingStrategy</code> is <code>DAEMON</code> then this isn't required.</p>"""
    client_token: NotRequired["capo_ecs.types.string.String"]
    """<p>An identifier that you provide to ensure the idempotency of the request. It must be unique and is case sensitive. Up to 36 ASCII characters in the range of 33-126 (inclusive) are allowed.</p>"""
    launch_type: NotRequired["capo_ecs.types.launch_type.LaunchType"]
    """<p>The infrastructure that you run your service on. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_types.html">Amazon ECS launch types</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <note> <p>If you want to use Amazon ECS Managed Instances, you must use the <code>capacityProviderStrategy</code> request parameter and omit the <code>launchType</code> request parameter.</p> </note> <p>The <code>FARGATE</code> launch type runs your tasks on Fargate On-Demand infrastructure.</p> <note> <p>Fargate Spot infrastructure is available for use but a capacity provider strategy must be used. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/fargate-capacity-providers.html">Fargate capacity providers</a> in the <i>Amazon ECS Developer Guide</i>.</p> </note> <p>The <code>EC2</code> launch type runs your tasks on Amazon EC2 instances registered to your cluster.</p> <p>The <code>EXTERNAL</code> launch type runs your tasks on your on-premises server or virtual machine (VM) capacity registered to your cluster.</p> <p>A service can use either a launch type or a capacity provider strategy. If a <code>launchType</code> is specified, the <code>capacityProviderStrategy</code> parameter must be omitted.</p>"""
    capacity_provider_strategy: NotRequired[
        "capo_ecs.types.capacity_provider_strategy.CapacityProviderStrategy"
    ]
    """<p>The capacity provider strategy to use for the service.</p> <note> <p>If you want to use Amazon ECS Managed Instances, you must use the <code>capacityProviderStrategy</code> request parameter and omit the <code>launchType</code> request parameter.</p> </note> <p>If a <code>capacityProviderStrategy</code> is specified, the <code>launchType</code> parameter must be omitted. If no <code>capacityProviderStrategy</code> or <code>launchType</code> is specified, the <code>defaultCapacityProviderStrategy</code> for the cluster is used.</p> <p>A capacity provider strategy can contain a maximum of 20 capacity providers.</p>"""
    platform_version: NotRequired["capo_ecs.types.string.String"]
    """<p>The platform version that your tasks in the service are running on. A platform version is specified only for tasks using the Fargate launch type. If one isn't specified, the <code>LATEST</code> platform version is used. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html">Fargate platform versions</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""
    role: NotRequired["capo_ecs.types.string.String"]
    """<p>The name or full Amazon Resource Name (ARN) of the IAM role that allows Amazon ECS to make calls to your load balancer on your behalf. This parameter is only permitted if you are using a load balancer with your service and your task definition doesn't use the <code>awsvpc</code> network mode. If you specify the <code>role</code> parameter, you must also specify a load balancer object with the <code>loadBalancers</code> parameter.</p> <important> <p>If your account has already created the Amazon ECS service-linked role, that role is used for your service unless you specify a role here. The service-linked role is required if your task definition uses the <code>awsvpc</code> network mode or if the service is configured to use service discovery, an external deployment controller, multiple target groups, or Elastic Inference accelerators in which case you don't specify a role here. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using-service-linked-roles.html">Using service-linked roles for Amazon ECS</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> </important> <p>If your specified role has a path other than <code>/</code>, then you must either specify the full role ARN (this is recommended) or prefix the role name with the path. For example, if a role with the name <code>bar</code> has a path of <code>/foo/</code> then you would specify <code>/foo/bar</code> as the role name. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-friendly-names">Friendly names and paths</a> in the <i>IAM User Guide</i>.</p>"""
    deployment_configuration: NotRequired[
        "capo_ecs.types.deployment_configuration.DeploymentConfiguration"
    ]
    """<p>Optional deployment parameters that control how many tasks run during the deployment and the ordering of stopping and starting tasks.</p>"""
    placement_constraints: NotRequired[
        "capo_ecs.types.placement_constraints.PlacementConstraints"
    ]
    """<p>An array of placement constraint objects to use for tasks in your service. You can specify a maximum of 10 constraints for each task. This limit includes constraints in the task definition and those specified at runtime.</p>"""
    placement_strategy: NotRequired[
        "capo_ecs.types.placement_strategies.PlacementStrategies"
    ]
    """<p>The placement strategy objects to use for tasks in your service. You can specify a maximum of 5 strategy rules for each service.</p>"""
    network_configuration: NotRequired[
        "capo_ecs.types.network_configuration.NetworkConfiguration"
    ]
    """<p>The network configuration for the service. This parameter is required for task definitions that use the <code>awsvpc</code> network mode to receive their own elastic network interface, and it isn't supported for other network modes. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking.html">Task networking</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""
    health_check_grace_period_seconds: NotRequired[
        "capo_ecs.types.boxed_integer.BoxedInteger"
    ]
    """<p>The period of time, in seconds, that the Amazon ECS service scheduler ignores unhealthy Elastic Load Balancing, VPC Lattice, and container health checks after a task has first started. If you do not specify a health check grace period value, the default value of 0 is used. If you do not use any of the health checks, then <code>healthCheckGracePeriodSeconds</code> is unused.</p> <p>If your service has more running tasks than desired, unhealthy tasks in the grace period might be stopped to reach the desired count.</p>"""
    scheduling_strategy: NotRequired[
        "capo_ecs.types.scheduling_strategy.SchedulingStrategy"
    ]
    """<p>The scheduling strategy to use for the service. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs_services.html">Services</a>.</p> <p>There are two service scheduler strategies available:</p> <ul> <li> <p> <code>REPLICA</code>-The replica scheduling strategy places and maintains the desired number of tasks across your cluster. By default, the service scheduler spreads tasks across Availability Zones. You can use task placement strategies and constraints to customize task placement decisions. This scheduler strategy is required if the service uses the <code>CODE_DEPLOY</code> or <code>EXTERNAL</code> deployment controller types.</p> </li> <li> <p> <code>DAEMON</code>-The daemon scheduling strategy deploys exactly one task on each active container instance that meets all of the task placement constraints that you specify in your cluster. The service scheduler also evaluates the task placement constraints for running tasks and will stop tasks that don't meet the placement constraints. When you're using this strategy, you don't need to specify a desired number of tasks, a task placement strategy, or use Service Auto Scaling policies.</p> <note> <p>Tasks using the Fargate launch type or the <code>CODE_DEPLOY</code> or <code>EXTERNAL</code> deployment controller types don't support the <code>DAEMON</code> scheduling strategy.</p> </note> </li> </ul>"""
    deployment_controller: NotRequired[
        "capo_ecs.types.deployment_controller.DeploymentController"
    ]
    """<p>The deployment controller to use for the service. If no deployment controller is specified, the default value of <code>ECS</code> is used.</p>"""
    tags: NotRequired["capo_ecs.types.tags.Tags"]
    """<p>The metadata that you apply to the service to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. When a service is deleted, the tags are deleted as well.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case-sensitive.</p> </li> <li> <p>Do not use <code>aws:</code>, <code>AWS:</code>, or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for Amazon Web Services use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.</p> </li> </ul>"""
    enable_ecs_managed_tags: "capo_ecs.types.boolean.Boolean"
    """<p>Specifies whether to turn on Amazon ECS managed tags for the tasks within the service. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-using-tags.html">Tagging your Amazon ECS resources</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>When you use Amazon ECS managed tags, you must set the <code>propagateTags</code> request parameter.</p>"""
    propagate_tags: NotRequired["capo_ecs.types.propagate_tags.PropagateTags"]
    """<p>Specifies whether to propagate the tags from the task definition to the task. If no value is specified, the tags aren't propagated. Tags can only be propagated to the task during task creation. To add tags to a task after task creation, use the <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_TagResource.html">TagResource</a> API action.</p> <p>You must set this to a value other than <code>NONE</code> when you use Cost Explorer. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/usage-reports.html">Amazon ECS usage reports</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>The default is <code>NONE</code>.</p>"""
    enable_execute_command: "capo_ecs.types.boolean.Boolean"
    """<p>Determines whether the execute command functionality is turned on for the service. If <code>true</code>, this enables execute command functionality on all containers in the service tasks.</p>"""
    service_connect_configuration: NotRequired[
        "capo_ecs.types.service_connect_configuration.ServiceConnectConfiguration"
    ]
    """<p>The configuration for this service to discover and connect to services, and be discovered by, and connected from, other services within a namespace.</p> <p>Tasks that run in a namespace can use short names to connect to services in the namespace. Tasks can connect to services across all of the clusters in the namespace. Tasks connect through a managed proxy container that collects logs and metrics for increased visibility. Only the tasks that Amazon ECS services create are supported with Service Connect. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-connect.html">Service Connect</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""
    volume_configurations: NotRequired[
        "capo_ecs.types.service_volume_configurations.ServiceVolumeConfigurations"
    ]
    """<p>The configuration for a volume specified in the task definition as a volume that is configured at launch time. Currently, the only supported volume type is an Amazon EBS volume.</p>"""
    vpc_lattice_configurations: NotRequired[
        "capo_ecs.types.vpc_lattice_configurations.VpcLatticeConfigurations"
    ]
    """<p>The VPC Lattice configuration for the service being created.</p>"""
    monitoring: NotRequired[
        "capo_ecs.types.monitoring_configuration.MonitoringConfiguration"
    ]
    """<p>The optional monitoring configuration for the service, which defines the resolution for the service-level <code>CPUUtilization</code> and <code>MemoryUtilization</code> Amazon CloudWatch metrics. When not specified, Amazon ECS uses the default resolution of <code>60</code> seconds.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateServiceRequest) -> dict:
    out: dict = {}
    if "cluster" in value:
        out["cluster"] = value["cluster"]
    out["serviceName"] = value["service_name"]
    if "task_definition" in value:
        out["taskDefinition"] = value["task_definition"]
    if "availability_zone_rebalancing" in value:
        import capo_ecs.types.availability_zone_rebalancing

        out["availabilityZoneRebalancing"] = (
            capo_ecs.types.availability_zone_rebalancing.serialize_aws_json_1_1(
                value["availability_zone_rebalancing"]
            )
        )
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
    if "desired_count" in value:
        out["desiredCount"] = value["desired_count"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
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
    if "role" in value:
        out["role"] = value["role"]
    if "deployment_configuration" in value:
        import capo_ecs.types.deployment_configuration

        out["deploymentConfiguration"] = (
            capo_ecs.types.deployment_configuration.serialize_aws_json_1_1(
                value["deployment_configuration"]
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
    out["enableECSManagedTags"] = value.get("enable_ecs_managed_tags", False)
    if "propagate_tags" in value:
        import capo_ecs.types.propagate_tags

        out["propagateTags"] = capo_ecs.types.propagate_tags.serialize_aws_json_1_1(
            value["propagate_tags"]
        )
    out["enableExecuteCommand"] = value.get("enable_execute_command", False)
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


def deserialize_aws_json_1_1(data: dict) -> CreateServiceRequest:
    out: CreateServiceRequest = {}  # type: ignore[typeddict-item]
    if data.get("cluster") is not None:
        out["cluster"] = data["cluster"]
    if data.get("serviceName") is not None:
        out["service_name"] = data["serviceName"]
    else:
        raise DeserializationError("CreateServiceRequest.service_name required")
    if data.get("taskDefinition") is not None:
        out["task_definition"] = data["taskDefinition"]
    if data.get("availabilityZoneRebalancing") is not None:
        import capo_ecs.types.availability_zone_rebalancing

        out["availability_zone_rebalancing"] = (
            capo_ecs.types.availability_zone_rebalancing.deserialize_aws_json_1_1(
                data["availabilityZoneRebalancing"]
            )
        )
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
    if data.get("desiredCount") is not None:
        out["desired_count"] = data["desiredCount"]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
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
    if data.get("role") is not None:
        out["role"] = data["role"]
    if data.get("deploymentConfiguration") is not None:
        import capo_ecs.types.deployment_configuration

        out["deployment_configuration"] = (
            capo_ecs.types.deployment_configuration.deserialize_aws_json_1_1(
                data["deploymentConfiguration"]
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
