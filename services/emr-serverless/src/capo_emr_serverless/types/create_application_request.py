"""Generated from Smithy shape ``com.amazonaws.emrserverless#CreateApplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_emr_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import capo_emr_serverless.types.application_name
    import capo_emr_serverless.types.architecture
    import capo_emr_serverless.types.auto_start_config
    import capo_emr_serverless.types.auto_stop_config
    import capo_emr_serverless.types.client_token
    import capo_emr_serverless.types.configuration_list
    import capo_emr_serverless.types.disk_encryption_configuration
    import capo_emr_serverless.types.engine_type
    import capo_emr_serverless.types.identity_center_configuration_input
    import capo_emr_serverless.types.image_configuration_input
    import capo_emr_serverless.types.initial_capacity_config_map
    import capo_emr_serverless.types.interactive_configuration
    import capo_emr_serverless.types.job_level_cost_allocation_configuration
    import capo_emr_serverless.types.maximum_allowed_resources
    import capo_emr_serverless.types.monitoring_configuration
    import capo_emr_serverless.types.network_configuration
    import capo_emr_serverless.types.release_label
    import capo_emr_serverless.types.scheduler_configuration
    import capo_emr_serverless.types.tag_map
    import capo_emr_serverless.types.worker_type_specification_input_map


class CreateApplicationRequest(TypedDict, closed=True):
    name: NotRequired["capo_emr_serverless.types.application_name.ApplicationName"]
    """<p>The name of the application.</p>"""
    release_label: "capo_emr_serverless.types.release_label.ReleaseLabel"
    """<p>The Amazon EMR release associated with the application.</p>"""
    type: "capo_emr_serverless.types.engine_type.EngineType"
    """<p>The type of application you want to start, such as Spark or Hive.</p>"""
    client_token: "capo_emr_serverless.types.client_token.ClientToken"
    """<p>The client idempotency token of the application to create. Its value must be unique for each request.</p>"""
    initial_capacity: NotRequired[
        "capo_emr_serverless.types.initial_capacity_config_map.InitialCapacityConfigMap"
    ]
    """<p>The capacity to initialize when the application is created.</p>"""
    maximum_capacity: NotRequired[
        "capo_emr_serverless.types.maximum_allowed_resources.MaximumAllowedResources"
    ]
    """<p>The maximum capacity to allocate when the application is created. This is cumulative across all workers at any given point in time, not just when an application is created. No new resources will be created once any one of the defined limits is hit.</p>"""
    tags: NotRequired["capo_emr_serverless.types.tag_map.TagMap"]
    """<p>The tags assigned to the application.</p>"""
    auto_start_configuration: NotRequired[
        "capo_emr_serverless.types.auto_start_config.AutoStartConfig"
    ]
    """<p>The configuration for an application to automatically start on job submission.</p>"""
    auto_stop_configuration: NotRequired[
        "capo_emr_serverless.types.auto_stop_config.AutoStopConfig"
    ]
    """<p>The configuration for an application to automatically stop after a certain amount of time being idle.</p>"""
    network_configuration: NotRequired[
        "capo_emr_serverless.types.network_configuration.NetworkConfiguration"
    ]
    """<p>The network configuration for customer VPC connectivity.</p>"""
    architecture: NotRequired["capo_emr_serverless.types.architecture.Architecture"]
    """<p>The CPU architecture of an application.</p>"""
    image_configuration: NotRequired[
        "capo_emr_serverless.types.image_configuration_input.ImageConfigurationInput"
    ]
    """<p>The image configuration for all worker types. You can either set this parameter or <code>imageConfiguration</code> for each worker type in <code>workerTypeSpecifications</code>.</p>"""
    worker_type_specifications: NotRequired[
        "capo_emr_serverless.types.worker_type_specification_input_map.WorkerTypeSpecificationInputMap"
    ]
    """<p>The key-value pairs that specify worker type to <code>WorkerTypeSpecificationInput</code>. This parameter must contain all valid worker types for a Spark or Hive application. Valid worker types include <code>Driver</code> and <code>Executor</code> for Spark applications and <code>HiveDriver</code> and <code>TezTask</code> for Hive applications. You can either set image details in this parameter for each worker type, or in <code>imageConfiguration</code> for all worker types.</p>"""
    runtime_configuration: NotRequired[
        "capo_emr_serverless.types.configuration_list.ConfigurationList"
    ]
    """<p>The <a href="https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_Configuration.html">Configuration</a> specifications to use when creating an application. Each configuration consists of a classification and properties. This configuration is applied to all the job runs submitted under the application.</p>"""
    monitoring_configuration: NotRequired[
        "capo_emr_serverless.types.monitoring_configuration.MonitoringConfiguration"
    ]
    """<p>The configuration setting for monitoring.</p>"""
    disk_encryption_configuration: NotRequired[
        "capo_emr_serverless.types.disk_encryption_configuration.DiskEncryptionConfiguration"
    ]
    """<p>The configuration object that allows encrypting local disks.</p>"""
    interactive_configuration: NotRequired[
        "capo_emr_serverless.types.interactive_configuration.InteractiveConfiguration"
    ]
    """<p>The interactive configuration object that enables the interactive use cases to use when running an application.</p>"""
    scheduler_configuration: NotRequired[
        "capo_emr_serverless.types.scheduler_configuration.SchedulerConfiguration"
    ]
    """<p>The scheduler configuration for batch and streaming jobs running on this application. Supported with release labels emr-7.0.0 and above.</p>"""
    identity_center_configuration: NotRequired[
        "capo_emr_serverless.types.identity_center_configuration_input.IdentityCenterConfigurationInput"
    ]
    """<p>The IAM Identity Center Configuration accepts the Identity Center instance parameter required to enable trusted identity propagation. This configuration allows identity propagation between integrated services and the Identity Center instance.</p>"""
    job_level_cost_allocation_configuration: NotRequired[
        "capo_emr_serverless.types.job_level_cost_allocation_configuration.JobLevelCostAllocationConfiguration"
    ]
    """<p>The configuration object that enables job level cost allocation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateApplicationRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    out["releaseLabel"] = value["release_label"]
    out["type"] = value["type"]
    out["clientToken"] = value["client_token"]
    if "initial_capacity" in value:
        import capo_emr_serverless.types.initial_capacity_config_map

        out["initialCapacity"] = (
            capo_emr_serverless.types.initial_capacity_config_map.serialize_json(
                value["initial_capacity"]
            )
        )
    if "maximum_capacity" in value:
        import capo_emr_serverless.types.maximum_allowed_resources

        out["maximumCapacity"] = (
            capo_emr_serverless.types.maximum_allowed_resources.serialize_json(
                value["maximum_capacity"]
            )
        )
    if "tags" in value:
        import capo_emr_serverless.types.tag_map

        out["tags"] = capo_emr_serverless.types.tag_map.serialize_json(value["tags"])
    if "auto_start_configuration" in value:
        import capo_emr_serverless.types.auto_start_config

        out["autoStartConfiguration"] = (
            capo_emr_serverless.types.auto_start_config.serialize_json(
                value["auto_start_configuration"]
            )
        )
    if "auto_stop_configuration" in value:
        import capo_emr_serverless.types.auto_stop_config

        out["autoStopConfiguration"] = (
            capo_emr_serverless.types.auto_stop_config.serialize_json(
                value["auto_stop_configuration"]
            )
        )
    if "network_configuration" in value:
        import capo_emr_serverless.types.network_configuration

        out["networkConfiguration"] = (
            capo_emr_serverless.types.network_configuration.serialize_json(
                value["network_configuration"]
            )
        )
    if "architecture" in value:
        out["architecture"] = value["architecture"]
    if "image_configuration" in value:
        import capo_emr_serverless.types.image_configuration_input

        out["imageConfiguration"] = (
            capo_emr_serverless.types.image_configuration_input.serialize_json(
                value["image_configuration"]
            )
        )
    if "worker_type_specifications" in value:
        import capo_emr_serverless.types.worker_type_specification_input_map

        out["workerTypeSpecifications"] = (
            capo_emr_serverless.types.worker_type_specification_input_map.serialize_json(
                value["worker_type_specifications"]
            )
        )
    if "runtime_configuration" in value:
        import capo_emr_serverless.types.configuration_list

        out["runtimeConfiguration"] = (
            capo_emr_serverless.types.configuration_list.serialize_json(
                value["runtime_configuration"]
            )
        )
    if "monitoring_configuration" in value:
        import capo_emr_serverless.types.monitoring_configuration

        out["monitoringConfiguration"] = (
            capo_emr_serverless.types.monitoring_configuration.serialize_json(
                value["monitoring_configuration"]
            )
        )
    if "disk_encryption_configuration" in value:
        import capo_emr_serverless.types.disk_encryption_configuration

        out["diskEncryptionConfiguration"] = (
            capo_emr_serverless.types.disk_encryption_configuration.serialize_json(
                value["disk_encryption_configuration"]
            )
        )
    if "interactive_configuration" in value:
        import capo_emr_serverless.types.interactive_configuration

        out["interactiveConfiguration"] = (
            capo_emr_serverless.types.interactive_configuration.serialize_json(
                value["interactive_configuration"]
            )
        )
    if "scheduler_configuration" in value:
        import capo_emr_serverless.types.scheduler_configuration

        out["schedulerConfiguration"] = (
            capo_emr_serverless.types.scheduler_configuration.serialize_json(
                value["scheduler_configuration"]
            )
        )
    if "identity_center_configuration" in value:
        import capo_emr_serverless.types.identity_center_configuration_input

        out["identityCenterConfiguration"] = (
            capo_emr_serverless.types.identity_center_configuration_input.serialize_json(
                value["identity_center_configuration"]
            )
        )
    if "job_level_cost_allocation_configuration" in value:
        import capo_emr_serverless.types.job_level_cost_allocation_configuration

        out["jobLevelCostAllocationConfiguration"] = (
            capo_emr_serverless.types.job_level_cost_allocation_configuration.serialize_json(
                value["job_level_cost_allocation_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateApplicationRequest:
    out: CreateApplicationRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("releaseLabel") is not None:
        out["release_label"] = data["releaseLabel"]
    else:
        raise DeserializationError("CreateApplicationRequest.release_label required")
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        raise DeserializationError("CreateApplicationRequest.type required")
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError("CreateApplicationRequest.client_token required")
    if data.get("initialCapacity") is not None:
        import capo_emr_serverless.types.initial_capacity_config_map

        out["initial_capacity"] = (
            capo_emr_serverless.types.initial_capacity_config_map.deserialize_json(
                data["initialCapacity"]
            )
        )
    if data.get("maximumCapacity") is not None:
        import capo_emr_serverless.types.maximum_allowed_resources

        out["maximum_capacity"] = (
            capo_emr_serverless.types.maximum_allowed_resources.deserialize_json(
                data["maximumCapacity"]
            )
        )
    if data.get("tags") is not None:
        import capo_emr_serverless.types.tag_map

        out["tags"] = capo_emr_serverless.types.tag_map.deserialize_json(data["tags"])
    if data.get("autoStartConfiguration") is not None:
        import capo_emr_serverless.types.auto_start_config

        out["auto_start_configuration"] = (
            capo_emr_serverless.types.auto_start_config.deserialize_json(
                data["autoStartConfiguration"]
            )
        )
    if data.get("autoStopConfiguration") is not None:
        import capo_emr_serverless.types.auto_stop_config

        out["auto_stop_configuration"] = (
            capo_emr_serverless.types.auto_stop_config.deserialize_json(
                data["autoStopConfiguration"]
            )
        )
    if data.get("networkConfiguration") is not None:
        import capo_emr_serverless.types.network_configuration

        out["network_configuration"] = (
            capo_emr_serverless.types.network_configuration.deserialize_json(
                data["networkConfiguration"]
            )
        )
    if data.get("architecture") is not None:
        out["architecture"] = data["architecture"]
    if data.get("imageConfiguration") is not None:
        import capo_emr_serverless.types.image_configuration_input

        out["image_configuration"] = (
            capo_emr_serverless.types.image_configuration_input.deserialize_json(
                data["imageConfiguration"]
            )
        )
    if data.get("workerTypeSpecifications") is not None:
        import capo_emr_serverless.types.worker_type_specification_input_map

        out["worker_type_specifications"] = (
            capo_emr_serverless.types.worker_type_specification_input_map.deserialize_json(
                data["workerTypeSpecifications"]
            )
        )
    if data.get("runtimeConfiguration") is not None:
        import capo_emr_serverless.types.configuration_list

        out["runtime_configuration"] = (
            capo_emr_serverless.types.configuration_list.deserialize_json(
                data["runtimeConfiguration"]
            )
        )
    if data.get("monitoringConfiguration") is not None:
        import capo_emr_serverless.types.monitoring_configuration

        out["monitoring_configuration"] = (
            capo_emr_serverless.types.monitoring_configuration.deserialize_json(
                data["monitoringConfiguration"]
            )
        )
    if data.get("diskEncryptionConfiguration") is not None:
        import capo_emr_serverless.types.disk_encryption_configuration

        out["disk_encryption_configuration"] = (
            capo_emr_serverless.types.disk_encryption_configuration.deserialize_json(
                data["diskEncryptionConfiguration"]
            )
        )
    if data.get("interactiveConfiguration") is not None:
        import capo_emr_serverless.types.interactive_configuration

        out["interactive_configuration"] = (
            capo_emr_serverless.types.interactive_configuration.deserialize_json(
                data["interactiveConfiguration"]
            )
        )
    if data.get("schedulerConfiguration") is not None:
        import capo_emr_serverless.types.scheduler_configuration

        out["scheduler_configuration"] = (
            capo_emr_serverless.types.scheduler_configuration.deserialize_json(
                data["schedulerConfiguration"]
            )
        )
    if data.get("identityCenterConfiguration") is not None:
        import capo_emr_serverless.types.identity_center_configuration_input

        out["identity_center_configuration"] = (
            capo_emr_serverless.types.identity_center_configuration_input.deserialize_json(
                data["identityCenterConfiguration"]
            )
        )
    if data.get("jobLevelCostAllocationConfiguration") is not None:
        import capo_emr_serverless.types.job_level_cost_allocation_configuration

        out["job_level_cost_allocation_configuration"] = (
            capo_emr_serverless.types.job_level_cost_allocation_configuration.deserialize_json(
                data["jobLevelCostAllocationConfiguration"]
            )
        )
    return out
