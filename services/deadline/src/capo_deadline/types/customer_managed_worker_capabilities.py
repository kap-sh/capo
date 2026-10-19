"""Generated from Smithy shape ``com.amazonaws.deadline#CustomerManagedWorkerCapabilities``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_deadline.types.accelerator_count_range
    import capo_deadline.types.accelerator_total_memory_mi_b_range
    import capo_deadline.types.accelerator_types
    import capo_deadline.types.cpu_architecture_type
    import capo_deadline.types.custom_fleet_amount_capabilities
    import capo_deadline.types.custom_fleet_attribute_capabilities
    import capo_deadline.types.customer_managed_fleet_operating_system_family
    import capo_deadline.types.memory_mi_b_range
    import capo_deadline.types.v_cpu_count_range


class CustomerManagedWorkerCapabilities(TypedDict, closed=True):
    v_cpu_count: "capo_deadline.types.v_cpu_count_range.VCpuCountRange"
    """<p>The vCPU count for the customer manged worker capabilities.</p>"""
    memory_mi_b: "capo_deadline.types.memory_mi_b_range.MemoryMiBRange"
    """<p>The memory (MiB).</p>"""
    accelerator_types: NotRequired[
        "capo_deadline.types.accelerator_types.AcceleratorTypes"
    ]
    """<p>The accelerator types for the customer managed worker capabilities.</p>"""
    accelerator_count: NotRequired[
        "capo_deadline.types.accelerator_count_range.AcceleratorCountRange"
    ]
    """<p>The range of the accelerator.</p>"""
    accelerator_total_memory_mi_b: NotRequired[
        "capo_deadline.types.accelerator_total_memory_mi_b_range.AcceleratorTotalMemoryMiBRange"
    ]
    """<p>The total memory (MiB) for the customer managed worker capabilities.</p>"""
    os_family: "capo_deadline.types.customer_managed_fleet_operating_system_family.CustomerManagedFleetOperatingSystemFamily"
    """<p>The operating system (OS) family.</p>"""
    cpu_architecture_type: (
        "capo_deadline.types.cpu_architecture_type.CpuArchitectureType"
    )
    """<p>The CPU architecture type for the customer managed worker capabilities.</p>"""
    custom_amounts: NotRequired[
        "capo_deadline.types.custom_fleet_amount_capabilities.CustomFleetAmountCapabilities"
    ]
    """<p>Custom requirement ranges for customer managed worker capabilities.</p>"""
    custom_attributes: NotRequired[
        "capo_deadline.types.custom_fleet_attribute_capabilities.CustomFleetAttributeCapabilities"
    ]
    """<p>Custom attributes for the customer manged worker capabilities.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomerManagedWorkerCapabilities) -> dict:
    out: dict = {}
    import capo_deadline.types.v_cpu_count_range

    out["vCpuCount"] = capo_deadline.types.v_cpu_count_range.serialize_json(
        value["v_cpu_count"]
    )
    import capo_deadline.types.memory_mi_b_range

    out["memoryMiB"] = capo_deadline.types.memory_mi_b_range.serialize_json(
        value["memory_mi_b"]
    )
    if "accelerator_types" in value:
        import capo_deadline.types.accelerator_types

        out["acceleratorTypes"] = capo_deadline.types.accelerator_types.serialize_json(
            value["accelerator_types"]
        )
    if "accelerator_count" in value:
        import capo_deadline.types.accelerator_count_range

        out["acceleratorCount"] = (
            capo_deadline.types.accelerator_count_range.serialize_json(
                value["accelerator_count"]
            )
        )
    if "accelerator_total_memory_mi_b" in value:
        import capo_deadline.types.accelerator_total_memory_mi_b_range

        out["acceleratorTotalMemoryMiB"] = (
            capo_deadline.types.accelerator_total_memory_mi_b_range.serialize_json(
                value["accelerator_total_memory_mi_b"]
            )
        )
    import capo_deadline.types.customer_managed_fleet_operating_system_family

    out["osFamily"] = (
        capo_deadline.types.customer_managed_fleet_operating_system_family.serialize_json(
            value["os_family"]
        )
    )
    import capo_deadline.types.cpu_architecture_type

    out["cpuArchitectureType"] = (
        capo_deadline.types.cpu_architecture_type.serialize_json(
            value["cpu_architecture_type"]
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
    return out


def deserialize_json(data: dict) -> CustomerManagedWorkerCapabilities:
    out: CustomerManagedWorkerCapabilities = {}  # type: ignore[typeddict-item]
    if data.get("vCpuCount") is not None:
        import capo_deadline.types.v_cpu_count_range

        out["v_cpu_count"] = capo_deadline.types.v_cpu_count_range.deserialize_json(
            data["vCpuCount"]
        )
    else:
        raise DeserializationError(
            "CustomerManagedWorkerCapabilities.v_cpu_count required"
        )
    if data.get("memoryMiB") is not None:
        import capo_deadline.types.memory_mi_b_range

        out["memory_mi_b"] = capo_deadline.types.memory_mi_b_range.deserialize_json(
            data["memoryMiB"]
        )
    else:
        raise DeserializationError(
            "CustomerManagedWorkerCapabilities.memory_mi_b required"
        )
    if data.get("acceleratorTypes") is not None:
        import capo_deadline.types.accelerator_types

        out["accelerator_types"] = (
            capo_deadline.types.accelerator_types.deserialize_json(
                data["acceleratorTypes"]
            )
        )
    if data.get("acceleratorCount") is not None:
        import capo_deadline.types.accelerator_count_range

        out["accelerator_count"] = (
            capo_deadline.types.accelerator_count_range.deserialize_json(
                data["acceleratorCount"]
            )
        )
    if data.get("acceleratorTotalMemoryMiB") is not None:
        import capo_deadline.types.accelerator_total_memory_mi_b_range

        out["accelerator_total_memory_mi_b"] = (
            capo_deadline.types.accelerator_total_memory_mi_b_range.deserialize_json(
                data["acceleratorTotalMemoryMiB"]
            )
        )
    if data.get("osFamily") is not None:
        import capo_deadline.types.customer_managed_fleet_operating_system_family

        out["os_family"] = (
            capo_deadline.types.customer_managed_fleet_operating_system_family.deserialize_json(
                data["osFamily"]
            )
        )
    else:
        import typing

        out["os_family"] = typing.cast(
            "capo_deadline.types.customer_managed_fleet_operating_system_family.CustomerManagedFleetOperatingSystemFamily",
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
    return out
