"""Generated from Smithy shape ``com.amazonaws.deadline#ServiceManagedEc2InstanceCapabilities``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_deadline.types.accelerator_capabilities
    import capo_deadline.types.cpu_architecture_type
    import capo_deadline.types.custom_fleet_amount_capabilities
    import capo_deadline.types.custom_fleet_attribute_capabilities
    import capo_deadline.types.ec2_ebs_volume
    import capo_deadline.types.fleet_software_add_ons
    import capo_deadline.types.instance_types
    import capo_deadline.types.memory_mi_b_range
    import capo_deadline.types.service_managed_fleet_operating_system_family
    import capo_deadline.types.v_cpu_count_range


class ServiceManagedEc2InstanceCapabilities(TypedDict, closed=True):
    v_cpu_count: "capo_deadline.types.v_cpu_count_range.VCpuCountRange"
    """The amount of vCPU to require for instances in this fleet."""
    memory_mi_b: "capo_deadline.types.memory_mi_b_range.MemoryMiBRange"
    """The memory, as MiB, for the Amazon EC2 instance type."""
    os_family: "capo_deadline.types.service_managed_fleet_operating_system_family.ServiceManagedFleetOperatingSystemFamily"
    """The operating system (OS) family."""
    cpu_architecture_type: (
        "capo_deadline.types.cpu_architecture_type.CpuArchitectureType"
    )
    """The CPU architecture type."""
    root_ebs_volume: NotRequired["capo_deadline.types.ec2_ebs_volume.Ec2EbsVolume"]
    """The root EBS volume."""
    accelerator_capabilities: NotRequired[
        "capo_deadline.types.accelerator_capabilities.AcceleratorCapabilities"
    ]
    """Describes the GPU accelerator capabilities required for worker host instances in this fleet."""
    allowed_instance_types: NotRequired[
        "capo_deadline.types.instance_types.InstanceTypes"
    ]
    """<p>The allowable Amazon EC2 instance types.</p> <note> <p>If you specify <code>allowedInstanceTypes</code>, you can't specify <code>excludedInstanceTypes</code>.</p> </note>"""
    excluded_instance_types: NotRequired[
        "capo_deadline.types.instance_types.InstanceTypes"
    ]
    """<p>The instance types to exclude from the fleet.</p> <note> <p>If you specify <code>excludedInstanceTypes</code>, you can't specify <code>allowedInstanceTypes</code>.</p> </note>"""
    custom_amounts: NotRequired[
        "capo_deadline.types.custom_fleet_amount_capabilities.CustomFleetAmountCapabilities"
    ]
    """The custom capability amounts to require for instances in this fleet."""
    custom_attributes: NotRequired[
        "capo_deadline.types.custom_fleet_attribute_capabilities.CustomFleetAttributeCapabilities"
    ]
    """The custom capability attributes to require for instances in this fleet."""
    software_add_ons: NotRequired[
        "capo_deadline.types.fleet_software_add_ons.FleetSoftwareAddOns"
    ]
    """The software add-ons that the service installs on worker hosts when they launch."""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceManagedEc2InstanceCapabilities) -> dict:
    out: dict = {}
    import capo_deadline.types.v_cpu_count_range

    out["vCpuCount"] = capo_deadline.types.v_cpu_count_range.serialize_json(
        value["v_cpu_count"]
    )
    import capo_deadline.types.memory_mi_b_range

    out["memoryMiB"] = capo_deadline.types.memory_mi_b_range.serialize_json(
        value["memory_mi_b"]
    )
    import capo_deadline.types.service_managed_fleet_operating_system_family

    out["osFamily"] = (
        capo_deadline.types.service_managed_fleet_operating_system_family.serialize_json(
            value["os_family"]
        )
    )
    import capo_deadline.types.cpu_architecture_type

    out["cpuArchitectureType"] = (
        capo_deadline.types.cpu_architecture_type.serialize_json(
            value["cpu_architecture_type"]
        )
    )
    if "root_ebs_volume" in value:
        import capo_deadline.types.ec2_ebs_volume

        out["rootEbsVolume"] = capo_deadline.types.ec2_ebs_volume.serialize_json(
            value["root_ebs_volume"]
        )
    if "accelerator_capabilities" in value:
        import capo_deadline.types.accelerator_capabilities

        out["acceleratorCapabilities"] = (
            capo_deadline.types.accelerator_capabilities.serialize_json(
                value["accelerator_capabilities"]
            )
        )
    if "allowed_instance_types" in value:
        import capo_deadline.types.instance_types

        out["allowedInstanceTypes"] = capo_deadline.types.instance_types.serialize_json(
            value["allowed_instance_types"]
        )
    if "excluded_instance_types" in value:
        import capo_deadline.types.instance_types

        out["excludedInstanceTypes"] = (
            capo_deadline.types.instance_types.serialize_json(
                value["excluded_instance_types"]
            )
        )
    if "custom_amounts" in value:
        import capo_deadline.types.custom_fleet_amount_capabilities

        out["customAmounts"] = (
            capo_deadline.types.custom_fleet_amount_capabilities.serialize_json(
                value["custom_amounts"]
            )
        )
    if "custom_attributes" in value:
        import capo_deadline.types.custom_fleet_attribute_capabilities

        out["customAttributes"] = (
            capo_deadline.types.custom_fleet_attribute_capabilities.serialize_json(
                value["custom_attributes"]
            )
        )
    if "software_add_ons" in value:
        import capo_deadline.types.fleet_software_add_ons

        out["softwareAddOns"] = (
            capo_deadline.types.fleet_software_add_ons.serialize_json(
                value["software_add_ons"]
            )
        )
    return out


def deserialize_json(data: dict) -> ServiceManagedEc2InstanceCapabilities:
    out: ServiceManagedEc2InstanceCapabilities = {}  # type: ignore[typeddict-item]
    if data.get("vCpuCount") is not None:
        import capo_deadline.types.v_cpu_count_range

        out["v_cpu_count"] = capo_deadline.types.v_cpu_count_range.deserialize_json(
            data["vCpuCount"]
        )
    else:
        raise DeserializationError(
            "ServiceManagedEc2InstanceCapabilities.v_cpu_count required"
        )
    if data.get("memoryMiB") is not None:
        import capo_deadline.types.memory_mi_b_range

        out["memory_mi_b"] = capo_deadline.types.memory_mi_b_range.deserialize_json(
            data["memoryMiB"]
        )
    else:
        raise DeserializationError(
            "ServiceManagedEc2InstanceCapabilities.memory_mi_b required"
        )
    if data.get("osFamily") is not None:
        import capo_deadline.types.service_managed_fleet_operating_system_family

        out["os_family"] = (
            capo_deadline.types.service_managed_fleet_operating_system_family.deserialize_json(
                data["osFamily"]
            )
        )
    else:
        import typing

        out["os_family"] = typing.cast(
            "capo_deadline.types.service_managed_fleet_operating_system_family.ServiceManagedFleetOperatingSystemFamily",
            "",
        )
    if data.get("cpuArchitectureType") is not None:
        import capo_deadline.types.cpu_architecture_type

        out["cpu_architecture_type"] = (
            capo_deadline.types.cpu_architecture_type.deserialize_json(
                data["cpuArchitectureType"]
            )
        )
    else:
        import typing

        out["cpu_architecture_type"] = typing.cast(
            "capo_deadline.types.cpu_architecture_type.CpuArchitectureType", ""
        )
    if data.get("rootEbsVolume") is not None:
        import capo_deadline.types.ec2_ebs_volume

        out["root_ebs_volume"] = capo_deadline.types.ec2_ebs_volume.deserialize_json(
            data["rootEbsVolume"]
        )
    if data.get("acceleratorCapabilities") is not None:
        import capo_deadline.types.accelerator_capabilities

        out["accelerator_capabilities"] = (
            capo_deadline.types.accelerator_capabilities.deserialize_json(
                data["acceleratorCapabilities"]
            )
        )
    if data.get("allowedInstanceTypes") is not None:
        import capo_deadline.types.instance_types

        out["allowed_instance_types"] = (
            capo_deadline.types.instance_types.deserialize_json(
                data["allowedInstanceTypes"]
            )
        )
    if data.get("excludedInstanceTypes") is not None:
        import capo_deadline.types.instance_types

        out["excluded_instance_types"] = (
            capo_deadline.types.instance_types.deserialize_json(
                data["excludedInstanceTypes"]
            )
        )
    if data.get("customAmounts") is not None:
        import capo_deadline.types.custom_fleet_amount_capabilities

        out["custom_amounts"] = (
            capo_deadline.types.custom_fleet_amount_capabilities.deserialize_json(
                data["customAmounts"]
            )
        )
    if data.get("customAttributes") is not None:
        import capo_deadline.types.custom_fleet_attribute_capabilities

        out["custom_attributes"] = (
            capo_deadline.types.custom_fleet_attribute_capabilities.deserialize_json(
                data["customAttributes"]
            )
        )
    if data.get("softwareAddOns") is not None:
        import capo_deadline.types.fleet_software_add_ons

        out["software_add_ons"] = (
            capo_deadline.types.fleet_software_add_ons.deserialize_json(
                data["softwareAddOns"]
            )
        )
    return out
