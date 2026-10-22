"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceRevision``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.boolean
    import capo_ecs.types.capacity_provider_strategy
    import capo_ecs.types.container_images
    import capo_ecs.types.deployment_ephemeral_storage
    import capo_ecs.types.ecs_managed_resources
    import capo_ecs.types.gateway_connector_list
    import capo_ecs.types.launch_type
    import capo_ecs.types.load_balancers
    import capo_ecs.types.monitoring_configuration
    import capo_ecs.types.network_configuration
    import capo_ecs.types.resolved_configuration
    import capo_ecs.types.service_connect_configuration
    import capo_ecs.types.service_registries
    import capo_ecs.types.service_revision_overrides
    import capo_ecs.types.service_volume_configurations
    import capo_ecs.types.string
    import capo_ecs.types.timestamp
    import capo_ecs.types.vpc_lattice_configurations


class ServiceRevision(TypedDict, closed=True):
    service_revision_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The ARN of the service revision.</p>"""
    service_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The ARN of the service for the service revision.</p>"""
    cluster_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The ARN of the cluster that hosts the service.</p>"""
    task_definition: NotRequired["capo_ecs.types.string.String"]
    """<p>The task definition the service revision uses.</p>"""
    capacity_provider_strategy: NotRequired[
        "capo_ecs.types.capacity_provider_strategy.CapacityProviderStrategy"
    ]
    """<p>The capacity provider strategy the service revision uses.</p>"""
    launch_type: NotRequired["capo_ecs.types.launch_type.LaunchType"]
    """<p>The launch type the service revision uses.</p>"""
    platform_version: NotRequired["capo_ecs.types.string.String"]
    """<p>For the Fargate launch type, the platform version the service revision uses.</p>"""
    platform_family: NotRequired["capo_ecs.types.string.String"]
    """<p>The platform family the service revision uses.</p>"""
    load_balancers: NotRequired["capo_ecs.types.load_balancers.LoadBalancers"]
    """<p>The load balancers the service revision uses.</p>"""
    service_registries: NotRequired[
        "capo_ecs.types.service_registries.ServiceRegistries"
    ]
    """<p>The service registries (for Service Discovery) the service revision uses.</p>"""
    network_configuration: NotRequired[
        "capo_ecs.types.network_configuration.NetworkConfiguration"
    ]
    container_images: NotRequired["capo_ecs.types.container_images.ContainerImages"]
    """<p>The container images the service revision uses.</p>"""
    guard_duty_enabled: "capo_ecs.types.boolean.Boolean"
    """<p>Indicates whether Runtime Monitoring is turned on.</p>"""
    service_connect_configuration: NotRequired[
        "capo_ecs.types.service_connect_configuration.ServiceConnectConfiguration"
    ]
    volume_configurations: NotRequired[
        "capo_ecs.types.service_volume_configurations.ServiceVolumeConfigurations"
    ]
    """<p>The volumes that are configured at deployment that the service revision uses.</p>"""
    fargate_ephemeral_storage: NotRequired[
        "capo_ecs.types.deployment_ephemeral_storage.DeploymentEphemeralStorage"
    ]
    created_at: NotRequired["capo_ecs.types.timestamp.Timestamp"]
    """<p>The time that the service revision was created. The format is yyyy-mm-dd HH:mm:ss.SSSSS.</p>"""
    vpc_lattice_configurations: NotRequired[
        "capo_ecs.types.vpc_lattice_configurations.VpcLatticeConfigurations"
    ]
    """<p>The VPC Lattice configuration for the service revision.</p>"""
    resolved_configuration: NotRequired[
        "capo_ecs.types.resolved_configuration.ResolvedConfiguration"
    ]
    """<p>The resolved configuration for the service revision which contains the actual resources your service revision uses, such as which target groups serve traffic.</p>"""
    ecs_managed_resources: NotRequired[
        "capo_ecs.types.ecs_managed_resources.ECSManagedResources"
    ]
    """<p>The resources created and managed by Amazon ECS when you create an Express service for Amazon ECS.</p>"""
    overrides: NotRequired[
        "capo_ecs.types.service_revision_overrides.ServiceRevisionOverrides"
    ]
    """<p>The effective runtime overrides that Amazon ECS applies to this service revision. This value is present only when Amazon ECS detects a difference between the task definition and the actual runtime configuration.</p>"""
    gateway_connectors: NotRequired[
        "capo_ecs.types.gateway_connector_list.GatewayConnectorList"
    ]
    """<p>The gateway connectors that are associated with the service revision.</p>"""
    monitoring: NotRequired[
        "capo_ecs.types.monitoring_configuration.MonitoringConfiguration"
    ]
    """<p>The optional monitoring configuration for the service, which defines the resolution for the service-level <code>CPUUtilization</code> and <code>MemoryUtilization</code> Amazon CloudWatch metrics. When not specified, Amazon ECS uses the default resolution of <code>60</code> seconds.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceRevision) -> dict:
    out: dict = {}
    if "service_revision_arn" in value:
        out["serviceRevisionArn"] = value["service_revision_arn"]
    if "service_arn" in value:
        out["serviceArn"] = value["service_arn"]
    if "cluster_arn" in value:
        out["clusterArn"] = value["cluster_arn"]
    if "task_definition" in value:
        out["taskDefinition"] = value["task_definition"]
    if "capacity_provider_strategy" in value:
        import capo_ecs.types.capacity_provider_strategy

        out["capacityProviderStrategy"] = (
            capo_ecs.types.capacity_provider_strategy.serialize_aws_json_1_1(
                value["capacity_provider_strategy"]
            )
        )
    if "launch_type" in value:
        import capo_ecs.types.launch_type

        out["launchType"] = capo_ecs.types.launch_type.serialize_aws_json_1_1(
            value["launch_type"]
        )
    if "platform_version" in value:
        out["platformVersion"] = value["platform_version"]
    if "platform_family" in value:
        out["platformFamily"] = value["platform_family"]
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
    if "network_configuration" in value:
        import capo_ecs.types.network_configuration

        out["networkConfiguration"] = (
            capo_ecs.types.network_configuration.serialize_aws_json_1_1(
                value["network_configuration"]
            )
        )
    if "container_images" in value:
        import capo_ecs.types.container_images

        out["containerImages"] = capo_ecs.types.container_images.serialize_aws_json_1_1(
            value["container_images"]
        )
    out["guardDutyEnabled"] = value.get("guard_duty_enabled", False)
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
    if "fargate_ephemeral_storage" in value:
        import capo_ecs.types.deployment_ephemeral_storage

        out["fargateEphemeralStorage"] = (
            capo_ecs.types.deployment_ephemeral_storage.serialize_aws_json_1_1(
                value["fargate_ephemeral_storage"]
            )
        )
    if "created_at" in value:
        import capo_ecs.types.timestamp

        out["createdAt"] = capo_ecs.types.timestamp.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "vpc_lattice_configurations" in value:
        import capo_ecs.types.vpc_lattice_configurations

        out["vpcLatticeConfigurations"] = (
            capo_ecs.types.vpc_lattice_configurations.serialize_aws_json_1_1(
                value["vpc_lattice_configurations"]
            )
        )
    if "resolved_configuration" in value:
        import capo_ecs.types.resolved_configuration

        out["resolvedConfiguration"] = (
            capo_ecs.types.resolved_configuration.serialize_aws_json_1_1(
                value["resolved_configuration"]
            )
        )
    if "ecs_managed_resources" in value:
        import capo_ecs.types.ecs_managed_resources

        out["ecsManagedResources"] = (
            capo_ecs.types.ecs_managed_resources.serialize_aws_json_1_1(
                value["ecs_managed_resources"]
            )
        )
    if "overrides" in value:
        import capo_ecs.types.service_revision_overrides

        out["overrides"] = (
            capo_ecs.types.service_revision_overrides.serialize_aws_json_1_1(
                value["overrides"]
            )
        )
    if "gateway_connectors" in value:
        import capo_ecs.types.gateway_connector_list

        out["gatewayConnectors"] = (
            capo_ecs.types.gateway_connector_list.serialize_aws_json_1_1(
                value["gateway_connectors"]
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


def deserialize_aws_json_1_1(data: dict) -> ServiceRevision:
    out: ServiceRevision = {}  # type: ignore[typeddict-item]
    if data.get("serviceRevisionArn") is not None:
        out["service_revision_arn"] = data["serviceRevisionArn"]
    if data.get("serviceArn") is not None:
        out["service_arn"] = data["serviceArn"]
    if data.get("clusterArn") is not None:
        out["cluster_arn"] = data["clusterArn"]
    if data.get("taskDefinition") is not None:
        out["task_definition"] = data["taskDefinition"]
    if data.get("capacityProviderStrategy") is not None:
        import capo_ecs.types.capacity_provider_strategy

        out["capacity_provider_strategy"] = (
            capo_ecs.types.capacity_provider_strategy.deserialize_aws_json_1_1(
                data["capacityProviderStrategy"]
            )
        )
    if data.get("launchType") is not None:
        import capo_ecs.types.launch_type

        out["launch_type"] = capo_ecs.types.launch_type.deserialize_aws_json_1_1(
            data["launchType"]
        )
    if data.get("platformVersion") is not None:
        out["platform_version"] = data["platformVersion"]
    if data.get("platformFamily") is not None:
        out["platform_family"] = data["platformFamily"]
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
    if data.get("networkConfiguration") is not None:
        import capo_ecs.types.network_configuration

        out["network_configuration"] = (
            capo_ecs.types.network_configuration.deserialize_aws_json_1_1(
                data["networkConfiguration"]
            )
        )
    if data.get("containerImages") is not None:
        import capo_ecs.types.container_images

        out["container_images"] = (
            capo_ecs.types.container_images.deserialize_aws_json_1_1(
                data["containerImages"]
            )
        )
    if data.get("guardDutyEnabled") is not None:
        out["guard_duty_enabled"] = data["guardDutyEnabled"]
    else:
        out["guard_duty_enabled"] = False
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
    if data.get("fargateEphemeralStorage") is not None:
        import capo_ecs.types.deployment_ephemeral_storage

        out["fargate_ephemeral_storage"] = (
            capo_ecs.types.deployment_ephemeral_storage.deserialize_aws_json_1_1(
                data["fargateEphemeralStorage"]
            )
        )
    if data.get("createdAt") is not None:
        import capo_ecs.types.timestamp

        out["created_at"] = capo_ecs.types.timestamp.deserialize_aws_json_1_1(
            data["createdAt"]
        )
    if data.get("vpcLatticeConfigurations") is not None:
        import capo_ecs.types.vpc_lattice_configurations

        out["vpc_lattice_configurations"] = (
            capo_ecs.types.vpc_lattice_configurations.deserialize_aws_json_1_1(
                data["vpcLatticeConfigurations"]
            )
        )
    if data.get("resolvedConfiguration") is not None:
        import capo_ecs.types.resolved_configuration

        out["resolved_configuration"] = (
            capo_ecs.types.resolved_configuration.deserialize_aws_json_1_1(
                data["resolvedConfiguration"]
            )
        )
    if data.get("ecsManagedResources") is not None:
        import capo_ecs.types.ecs_managed_resources

        out["ecs_managed_resources"] = (
            capo_ecs.types.ecs_managed_resources.deserialize_aws_json_1_1(
                data["ecsManagedResources"]
            )
        )
    if data.get("overrides") is not None:
        import capo_ecs.types.service_revision_overrides

        out["overrides"] = (
            capo_ecs.types.service_revision_overrides.deserialize_aws_json_1_1(
                data["overrides"]
            )
        )
    if data.get("gatewayConnectors") is not None:
        import capo_ecs.types.gateway_connector_list

        out["gateway_connectors"] = (
            capo_ecs.types.gateway_connector_list.deserialize_aws_json_1_1(
                data["gatewayConnectors"]
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
