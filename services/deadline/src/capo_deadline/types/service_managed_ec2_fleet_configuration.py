"""Generated from Smithy shape ``com.amazonaws.deadline#ServiceManagedEc2FleetConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_deadline.types.persistent_volume_configuration
    import capo_deadline.types.service_managed_ec2_auto_scaling_configuration
    import capo_deadline.types.service_managed_ec2_instance_capabilities
    import capo_deadline.types.service_managed_ec2_instance_market_options
    import capo_deadline.types.storage_profile_id
    import capo_deadline.types.vpc_configuration


class ServiceManagedEc2FleetConfiguration(TypedDict, closed=True):
    instance_capabilities: "capo_deadline.types.service_managed_ec2_instance_capabilities.ServiceManagedEc2InstanceCapabilities"
    """The instance capabilities for the service managed EC2 fleet."""
    instance_market_options: "capo_deadline.types.service_managed_ec2_instance_market_options.ServiceManagedEc2InstanceMarketOptions"
    """The instance market options for the service managed EC2 fleet."""
    vpc_configuration: NotRequired[
        "capo_deadline.types.vpc_configuration.VpcConfiguration"
    ]
    """The VPC configuration for the service managed EC2 fleet."""
    storage_profile_id: NotRequired[
        "capo_deadline.types.storage_profile_id.StorageProfileId"
    ]
    """The storage profile ID for the service managed EC2 fleet."""
    persistent_volume_configuration: NotRequired[
        "capo_deadline.types.persistent_volume_configuration.PersistentVolumeConfiguration"
    ]
    """The persistent volume configuration for the service managed EC2 fleet."""
    auto_scaling_configuration: NotRequired[
        "capo_deadline.types.service_managed_ec2_auto_scaling_configuration.ServiceManagedEc2AutoScalingConfiguration"
    ]
    """The auto scaling configuration settings for the service managed EC2 fleet."""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceManagedEc2FleetConfiguration) -> dict:
    out: dict = {}
    import capo_deadline.types.service_managed_ec2_instance_capabilities

    out["instanceCapabilities"] = (
        capo_deadline.types.service_managed_ec2_instance_capabilities.serialize_json(
            value["instance_capabilities"]
        )
    )
    import capo_deadline.types.service_managed_ec2_instance_market_options

    out["instanceMarketOptions"] = (
        capo_deadline.types.service_managed_ec2_instance_market_options.serialize_json(
            value["instance_market_options"]
        )
    )
    if "vpc_configuration" in value:
        import capo_deadline.types.vpc_configuration

        out["vpcConfiguration"] = capo_deadline.types.vpc_configuration.serialize_json(
            value["vpc_configuration"]
        )
    if "storage_profile_id" in value:
        out["storageProfileId"] = value["storage_profile_id"]
    if "persistent_volume_configuration" in value:
        import capo_deadline.types.persistent_volume_configuration

        out["persistentVolumeConfiguration"] = (
            capo_deadline.types.persistent_volume_configuration.serialize_json(
                value["persistent_volume_configuration"]
            )
        )
    if "auto_scaling_configuration" in value:
        import capo_deadline.types.service_managed_ec2_auto_scaling_configuration

        out["autoScalingConfiguration"] = (
            capo_deadline.types.service_managed_ec2_auto_scaling_configuration.serialize_json(
                value["auto_scaling_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> ServiceManagedEc2FleetConfiguration:
    out: ServiceManagedEc2FleetConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("instanceCapabilities") is not None:
        import capo_deadline.types.service_managed_ec2_instance_capabilities

        out["instance_capabilities"] = (
            capo_deadline.types.service_managed_ec2_instance_capabilities.deserialize_json(
                data["instanceCapabilities"]
            )
        )
    else:
        raise DeserializationError(
            "ServiceManagedEc2FleetConfiguration.instance_capabilities required"
        )
    if data.get("instanceMarketOptions") is not None:
        import capo_deadline.types.service_managed_ec2_instance_market_options

        out["instance_market_options"] = (
            capo_deadline.types.service_managed_ec2_instance_market_options.deserialize_json(
                data["instanceMarketOptions"]
            )
        )
    else:
        raise DeserializationError(
            "ServiceManagedEc2FleetConfiguration.instance_market_options required"
        )
    if data.get("vpcConfiguration") is not None:
        import capo_deadline.types.vpc_configuration

        out["vpc_configuration"] = (
            capo_deadline.types.vpc_configuration.deserialize_json(
                data["vpcConfiguration"]
            )
        )
    if data.get("storageProfileId") is not None:
        out["storage_profile_id"] = data["storageProfileId"]
    if data.get("persistentVolumeConfiguration") is not None:
        import capo_deadline.types.persistent_volume_configuration

        out["persistent_volume_configuration"] = (
            capo_deadline.types.persistent_volume_configuration.deserialize_json(
                data["persistentVolumeConfiguration"]
            )
        )
    if data.get("autoScalingConfiguration") is not None:
        import capo_deadline.types.service_managed_ec2_auto_scaling_configuration

        out["auto_scaling_configuration"] = (
            capo_deadline.types.service_managed_ec2_auto_scaling_configuration.deserialize_json(
                data["autoScalingConfiguration"]
            )
        )
    return out
