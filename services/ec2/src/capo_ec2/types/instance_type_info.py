"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceTypeInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.auto_recovery_flag
    import capo_ec2.types.bare_metal_flag
    import capo_ec2.types.boot_mode_type_list
    import capo_ec2.types.burstable_performance_flag
    import capo_ec2.types.current_generation_flag
    import capo_ec2.types.dedicated_host_flag
    import capo_ec2.types.ebs_info
    import capo_ec2.types.fpga_info
    import capo_ec2.types.free_tier_eligible_flag
    import capo_ec2.types.gpu_info
    import capo_ec2.types.hibernation_flag
    import capo_ec2.types.inference_accelerator_info
    import capo_ec2.types.instance_storage_flag
    import capo_ec2.types.instance_storage_info
    import capo_ec2.types.instance_type
    import capo_ec2.types.instance_type_hypervisor
    import capo_ec2.types.media_accelerator_info
    import capo_ec2.types.memory_info
    import capo_ec2.types.network_info
    import capo_ec2.types.neuron_info
    import capo_ec2.types.nitro_enclaves_support
    import capo_ec2.types.nitro_tpm_info
    import capo_ec2.types.nitro_tpm_support
    import capo_ec2.types.phc_support
    import capo_ec2.types.placement_group_info
    import capo_ec2.types.processor_info
    import capo_ec2.types.reboot_migration_support
    import capo_ec2.types.root_device_type_list
    import capo_ec2.types.supported_in_region
    import capo_ec2.types.usage_class_type_list
    import capo_ec2.types.v_cpu_info
    import capo_ec2.types.virtualization_type_list


class InstanceTypeInfo(TypedDict, closed=True):
    instance_type: NotRequired["capo_ec2.types.instance_type.InstanceType"]
    """<p>The instance type. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html">Instance types</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    current_generation: NotRequired[
        "capo_ec2.types.current_generation_flag.CurrentGenerationFlag"
    ]
    """<p>Indicates whether the instance type is current generation.</p>"""
    free_tier_eligible: NotRequired[
        "capo_ec2.types.free_tier_eligible_flag.FreeTierEligibleFlag"
    ]
    """<p>Indicates whether the instance type is eligible for the free tier.</p>"""
    supported_usage_classes: NotRequired[
        "capo_ec2.types.usage_class_type_list.UsageClassTypeList"
    ]
    """<p>Indicates whether the instance type is offered for spot, On-Demand, or Capacity Blocks.</p>"""
    supported_root_device_types: NotRequired[
        "capo_ec2.types.root_device_type_list.RootDeviceTypeList"
    ]
    """<p>The supported root device types.</p>"""
    supported_virtualization_types: NotRequired[
        "capo_ec2.types.virtualization_type_list.VirtualizationTypeList"
    ]
    """<p>The supported virtualization types.</p>"""
    bare_metal: NotRequired["capo_ec2.types.bare_metal_flag.BareMetalFlag"]
    """<p>Indicates whether the instance is a bare metal instance type.</p>"""
    hypervisor: NotRequired[
        "capo_ec2.types.instance_type_hypervisor.InstanceTypeHypervisor"
    ]
    """<p>The hypervisor for the instance type.</p>"""
    processor_info: NotRequired["capo_ec2.types.processor_info.ProcessorInfo"]
    """<p>Describes the processor.</p>"""
    v_cpu_info: NotRequired["capo_ec2.types.v_cpu_info.VCpuInfo"]
    """<p>Describes the vCPU configurations for the instance type.</p>"""
    memory_info: NotRequired["capo_ec2.types.memory_info.MemoryInfo"]
    """<p>Describes the memory for the instance type.</p>"""
    instance_storage_supported: NotRequired[
        "capo_ec2.types.instance_storage_flag.InstanceStorageFlag"
    ]
    """<p>Indicates whether instance storage is supported.</p>"""
    instance_storage_info: NotRequired[
        "capo_ec2.types.instance_storage_info.InstanceStorageInfo"
    ]
    """<p>Describes the instance storage for the instance type.</p>"""
    ebs_info: NotRequired["capo_ec2.types.ebs_info.EbsInfo"]
    """<p>Describes the Amazon EBS settings for the instance type.</p>"""
    network_info: NotRequired["capo_ec2.types.network_info.NetworkInfo"]
    """<p>Describes the network settings for the instance type.</p>"""
    gpu_info: NotRequired["capo_ec2.types.gpu_info.GpuInfo"]
    """<p>Describes the GPU accelerator settings for the instance type.</p>"""
    fpga_info: NotRequired["capo_ec2.types.fpga_info.FpgaInfo"]
    """<p>Describes the FPGA accelerator settings for the instance type.</p>"""
    placement_group_info: NotRequired[
        "capo_ec2.types.placement_group_info.PlacementGroupInfo"
    ]
    """<p>Describes the placement group settings for the instance type.</p>"""
    inference_accelerator_info: NotRequired[
        "capo_ec2.types.inference_accelerator_info.InferenceAcceleratorInfo"
    ]
    """<p>Describes the Inference accelerator settings for the instance type.</p>"""
    hibernation_supported: NotRequired[
        "capo_ec2.types.hibernation_flag.HibernationFlag"
    ]
    """<p>Indicates whether On-Demand hibernation is supported.</p>"""
    burstable_performance_supported: NotRequired[
        "capo_ec2.types.burstable_performance_flag.BurstablePerformanceFlag"
    ]
    """<p>Indicates whether the instance type is a burstable performance T instance type. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances.html">Burstable performance instances</a>.</p>"""
    dedicated_hosts_supported: NotRequired[
        "capo_ec2.types.dedicated_host_flag.DedicatedHostFlag"
    ]
    """<p>Indicates whether Dedicated Hosts are supported on the instance type.</p>"""
    auto_recovery_supported: NotRequired[
        "capo_ec2.types.auto_recovery_flag.AutoRecoveryFlag"
    ]
    """<p>Indicates whether Amazon CloudWatch action based recovery is supported.</p>"""
    supported_boot_modes: NotRequired[
        "capo_ec2.types.boot_mode_type_list.BootModeTypeList"
    ]
    """<p>The supported boot modes. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ami-boot.html">Boot modes</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    nitro_enclaves_support: NotRequired[
        "capo_ec2.types.nitro_enclaves_support.NitroEnclavesSupport"
    ]
    """<p>Indicates whether Nitro Enclaves is supported.</p>"""
    nitro_tpm_support: NotRequired["capo_ec2.types.nitro_tpm_support.NitroTpmSupport"]
    """<p>Indicates whether NitroTPM is supported.</p>"""
    nitro_tpm_info: NotRequired["capo_ec2.types.nitro_tpm_info.NitroTpmInfo"]
    """<p>Describes the supported NitroTPM versions for the instance type.</p>"""
    media_accelerator_info: NotRequired[
        "capo_ec2.types.media_accelerator_info.MediaAcceleratorInfo"
    ]
    """<p>Describes the media accelerator settings for the instance type.</p>"""
    neuron_info: NotRequired["capo_ec2.types.neuron_info.NeuronInfo"]
    """<p>Describes the Neuron accelerator settings for the instance type.</p>"""
    phc_support: NotRequired["capo_ec2.types.phc_support.PhcSupport"]
    """<p>Indicates whether a local Precision Time Protocol (PTP) hardware clock (PHC) is supported.</p>"""
    reboot_migration_support: NotRequired[
        "capo_ec2.types.reboot_migration_support.RebootMigrationSupport"
    ]
    """<p>Indicates whether reboot migration during a user-initiated reboot is supported for instances that have a scheduled <code>system-reboot</code> event. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/schedevents_actions_reboot.html#reboot-migration">Enable or disable reboot migration</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    supported_in_region: NotRequired[
        "capo_ec2.types.supported_in_region.SupportedInRegion"
    ]
    """<p>Indicates whether the instance type is supported in the current Region.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceTypeInfo, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "instance_type" in value:
        import capo_ec2.types.instance_type

        capo_ec2.types.instance_type.serialize_ec2_query(
            value["instance_type"], pairs, f"{key_prefix}InstanceType"
        )
    if "current_generation" in value:
        pairs.append(
            (
                f"{key_prefix}CurrentGeneration",
                "true" if value["current_generation"] else "false",
            )
        )
    if "free_tier_eligible" in value:
        pairs.append(
            (
                f"{key_prefix}FreeTierEligible",
                "true" if value["free_tier_eligible"] else "false",
            )
        )
    if "supported_usage_classes" in value:
        import capo_ec2.types.usage_class_type_list

        capo_ec2.types.usage_class_type_list.serialize_ec2_query(
            value["supported_usage_classes"],
            pairs,
            f"{key_prefix}SupportedUsageClasses",
        )
    if "supported_root_device_types" in value:
        import capo_ec2.types.root_device_type_list

        capo_ec2.types.root_device_type_list.serialize_ec2_query(
            value["supported_root_device_types"],
            pairs,
            f"{key_prefix}SupportedRootDeviceTypes",
        )
    if "supported_virtualization_types" in value:
        import capo_ec2.types.virtualization_type_list

        capo_ec2.types.virtualization_type_list.serialize_ec2_query(
            value["supported_virtualization_types"],
            pairs,
            f"{key_prefix}SupportedVirtualizationTypes",
        )
    if "bare_metal" in value:
        pairs.append(
            (f"{key_prefix}BareMetal", "true" if value["bare_metal"] else "false")
        )
    if "hypervisor" in value:
        import capo_ec2.types.instance_type_hypervisor

        capo_ec2.types.instance_type_hypervisor.serialize_ec2_query(
            value["hypervisor"], pairs, f"{key_prefix}Hypervisor"
        )
    if "processor_info" in value:
        import capo_ec2.types.processor_info

        capo_ec2.types.processor_info.serialize_ec2_query(
            value["processor_info"], pairs, f"{key_prefix}ProcessorInfo"
        )
    if "v_cpu_info" in value:
        import capo_ec2.types.v_cpu_info

        capo_ec2.types.v_cpu_info.serialize_ec2_query(
            value["v_cpu_info"], pairs, f"{key_prefix}VCpuInfo"
        )
    if "memory_info" in value:
        import capo_ec2.types.memory_info

        capo_ec2.types.memory_info.serialize_ec2_query(
            value["memory_info"], pairs, f"{key_prefix}MemoryInfo"
        )
    if "instance_storage_supported" in value:
        pairs.append(
            (
                f"{key_prefix}InstanceStorageSupported",
                "true" if value["instance_storage_supported"] else "false",
            )
        )
    if "instance_storage_info" in value:
        import capo_ec2.types.instance_storage_info

        capo_ec2.types.instance_storage_info.serialize_ec2_query(
            value["instance_storage_info"], pairs, f"{key_prefix}InstanceStorageInfo"
        )
    if "ebs_info" in value:
        import capo_ec2.types.ebs_info

        capo_ec2.types.ebs_info.serialize_ec2_query(
            value["ebs_info"], pairs, f"{key_prefix}EbsInfo"
        )
    if "network_info" in value:
        import capo_ec2.types.network_info

        capo_ec2.types.network_info.serialize_ec2_query(
            value["network_info"], pairs, f"{key_prefix}NetworkInfo"
        )
    if "gpu_info" in value:
        import capo_ec2.types.gpu_info

        capo_ec2.types.gpu_info.serialize_ec2_query(
            value["gpu_info"], pairs, f"{key_prefix}GpuInfo"
        )
    if "fpga_info" in value:
        import capo_ec2.types.fpga_info

        capo_ec2.types.fpga_info.serialize_ec2_query(
            value["fpga_info"], pairs, f"{key_prefix}FpgaInfo"
        )
    if "placement_group_info" in value:
        import capo_ec2.types.placement_group_info

        capo_ec2.types.placement_group_info.serialize_ec2_query(
            value["placement_group_info"], pairs, f"{key_prefix}PlacementGroupInfo"
        )
    if "inference_accelerator_info" in value:
        import capo_ec2.types.inference_accelerator_info

        capo_ec2.types.inference_accelerator_info.serialize_ec2_query(
            value["inference_accelerator_info"],
            pairs,
            f"{key_prefix}InferenceAcceleratorInfo",
        )
    if "hibernation_supported" in value:
        pairs.append(
            (
                f"{key_prefix}HibernationSupported",
                "true" if value["hibernation_supported"] else "false",
            )
        )
    if "burstable_performance_supported" in value:
        pairs.append(
            (
                f"{key_prefix}BurstablePerformanceSupported",
                "true" if value["burstable_performance_supported"] else "false",
            )
        )
    if "dedicated_hosts_supported" in value:
        pairs.append(
            (
                f"{key_prefix}DedicatedHostsSupported",
                "true" if value["dedicated_hosts_supported"] else "false",
            )
        )
    if "auto_recovery_supported" in value:
        pairs.append(
            (
                f"{key_prefix}AutoRecoverySupported",
                "true" if value["auto_recovery_supported"] else "false",
            )
        )
    if "supported_boot_modes" in value:
        import capo_ec2.types.boot_mode_type_list

        capo_ec2.types.boot_mode_type_list.serialize_ec2_query(
            value["supported_boot_modes"], pairs, f"{key_prefix}SupportedBootModes"
        )
    if "nitro_enclaves_support" in value:
        import capo_ec2.types.nitro_enclaves_support

        capo_ec2.types.nitro_enclaves_support.serialize_ec2_query(
            value["nitro_enclaves_support"], pairs, f"{key_prefix}NitroEnclavesSupport"
        )
    if "nitro_tpm_support" in value:
        import capo_ec2.types.nitro_tpm_support

        capo_ec2.types.nitro_tpm_support.serialize_ec2_query(
            value["nitro_tpm_support"], pairs, f"{key_prefix}NitroTpmSupport"
        )
    if "nitro_tpm_info" in value:
        import capo_ec2.types.nitro_tpm_info

        capo_ec2.types.nitro_tpm_info.serialize_ec2_query(
            value["nitro_tpm_info"], pairs, f"{key_prefix}NitroTpmInfo"
        )
    if "media_accelerator_info" in value:
        import capo_ec2.types.media_accelerator_info

        capo_ec2.types.media_accelerator_info.serialize_ec2_query(
            value["media_accelerator_info"], pairs, f"{key_prefix}MediaAcceleratorInfo"
        )
    if "neuron_info" in value:
        import capo_ec2.types.neuron_info

        capo_ec2.types.neuron_info.serialize_ec2_query(
            value["neuron_info"], pairs, f"{key_prefix}NeuronInfo"
        )
    if "phc_support" in value:
        import capo_ec2.types.phc_support

        capo_ec2.types.phc_support.serialize_ec2_query(
            value["phc_support"], pairs, f"{key_prefix}PhcSupport"
        )
    if "reboot_migration_support" in value:
        import capo_ec2.types.reboot_migration_support

        capo_ec2.types.reboot_migration_support.serialize_ec2_query(
            value["reboot_migration_support"],
            pairs,
            f"{key_prefix}RebootMigrationSupport",
        )
    if "supported_in_region" in value:
        pairs.append(
            (
                f"{key_prefix}SupportedInRegion",
                "true" if value["supported_in_region"] else "false",
            )
        )


def deserialize_ec2_query(el: Element) -> InstanceTypeInfo:
    out: InstanceTypeInfo = {}  # type: ignore[typeddict-item]
    child_instance_type = el.find("instanceType")
    if child_instance_type is not None:
        import capo_ec2.types.instance_type

        out["instance_type"] = capo_ec2.types.instance_type.deserialize_ec2_query(
            child_instance_type
        )
    child_current_generation = el.find("currentGeneration")
    if child_current_generation is not None:
        out["current_generation"] = (
            child_current_generation.text or ""
        ).lower() == "true"
    child_free_tier_eligible = el.find("freeTierEligible")
    if child_free_tier_eligible is not None:
        out["free_tier_eligible"] = (
            child_free_tier_eligible.text or ""
        ).lower() == "true"
    child_supported_usage_classes = el.find("supportedUsageClasses")
    if child_supported_usage_classes is not None:
        import capo_ec2.types.usage_class_type_list

        out["supported_usage_classes"] = (
            capo_ec2.types.usage_class_type_list.deserialize_ec2_query(
                child_supported_usage_classes
            )
        )
    child_supported_root_device_types = el.find("supportedRootDeviceTypes")
    if child_supported_root_device_types is not None:
        import capo_ec2.types.root_device_type_list

        out["supported_root_device_types"] = (
            capo_ec2.types.root_device_type_list.deserialize_ec2_query(
                child_supported_root_device_types
            )
        )
    child_supported_virtualization_types = el.find("supportedVirtualizationTypes")
    if child_supported_virtualization_types is not None:
        import capo_ec2.types.virtualization_type_list

        out["supported_virtualization_types"] = (
            capo_ec2.types.virtualization_type_list.deserialize_ec2_query(
                child_supported_virtualization_types
            )
        )
    child_bare_metal = el.find("bareMetal")
    if child_bare_metal is not None:
        out["bare_metal"] = (child_bare_metal.text or "").lower() == "true"
    child_hypervisor = el.find("hypervisor")
    if child_hypervisor is not None:
        import capo_ec2.types.instance_type_hypervisor

        out["hypervisor"] = (
            capo_ec2.types.instance_type_hypervisor.deserialize_ec2_query(
                child_hypervisor
            )
        )
    child_processor_info = el.find("processorInfo")
    if child_processor_info is not None:
        import capo_ec2.types.processor_info

        out["processor_info"] = capo_ec2.types.processor_info.deserialize_ec2_query(
            child_processor_info
        )
    child_v_cpu_info = el.find("vCpuInfo")
    if child_v_cpu_info is not None:
        import capo_ec2.types.v_cpu_info

        out["v_cpu_info"] = capo_ec2.types.v_cpu_info.deserialize_ec2_query(
            child_v_cpu_info
        )
    child_memory_info = el.find("memoryInfo")
    if child_memory_info is not None:
        import capo_ec2.types.memory_info

        out["memory_info"] = capo_ec2.types.memory_info.deserialize_ec2_query(
            child_memory_info
        )
    child_instance_storage_supported = el.find("instanceStorageSupported")
    if child_instance_storage_supported is not None:
        out["instance_storage_supported"] = (
            child_instance_storage_supported.text or ""
        ).lower() == "true"
    child_instance_storage_info = el.find("instanceStorageInfo")
    if child_instance_storage_info is not None:
        import capo_ec2.types.instance_storage_info

        out["instance_storage_info"] = (
            capo_ec2.types.instance_storage_info.deserialize_ec2_query(
                child_instance_storage_info
            )
        )
    child_ebs_info = el.find("ebsInfo")
    if child_ebs_info is not None:
        import capo_ec2.types.ebs_info

        out["ebs_info"] = capo_ec2.types.ebs_info.deserialize_ec2_query(child_ebs_info)
    child_network_info = el.find("networkInfo")
    if child_network_info is not None:
        import capo_ec2.types.network_info

        out["network_info"] = capo_ec2.types.network_info.deserialize_ec2_query(
            child_network_info
        )
    child_gpu_info = el.find("gpuInfo")
    if child_gpu_info is not None:
        import capo_ec2.types.gpu_info

        out["gpu_info"] = capo_ec2.types.gpu_info.deserialize_ec2_query(child_gpu_info)
    child_fpga_info = el.find("fpgaInfo")
    if child_fpga_info is not None:
        import capo_ec2.types.fpga_info

        out["fpga_info"] = capo_ec2.types.fpga_info.deserialize_ec2_query(
            child_fpga_info
        )
    child_placement_group_info = el.find("placementGroupInfo")
    if child_placement_group_info is not None:
        import capo_ec2.types.placement_group_info

        out["placement_group_info"] = (
            capo_ec2.types.placement_group_info.deserialize_ec2_query(
                child_placement_group_info
            )
        )
    child_inference_accelerator_info = el.find("inferenceAcceleratorInfo")
    if child_inference_accelerator_info is not None:
        import capo_ec2.types.inference_accelerator_info

        out["inference_accelerator_info"] = (
            capo_ec2.types.inference_accelerator_info.deserialize_ec2_query(
                child_inference_accelerator_info
            )
        )
    child_hibernation_supported = el.find("hibernationSupported")
    if child_hibernation_supported is not None:
        out["hibernation_supported"] = (
            child_hibernation_supported.text or ""
        ).lower() == "true"
    child_burstable_performance_supported = el.find("burstablePerformanceSupported")
    if child_burstable_performance_supported is not None:
        out["burstable_performance_supported"] = (
            child_burstable_performance_supported.text or ""
        ).lower() == "true"
    child_dedicated_hosts_supported = el.find("dedicatedHostsSupported")
    if child_dedicated_hosts_supported is not None:
        out["dedicated_hosts_supported"] = (
            child_dedicated_hosts_supported.text or ""
        ).lower() == "true"
    child_auto_recovery_supported = el.find("autoRecoverySupported")
    if child_auto_recovery_supported is not None:
        out["auto_recovery_supported"] = (
            child_auto_recovery_supported.text or ""
        ).lower() == "true"
    child_supported_boot_modes = el.find("supportedBootModes")
    if child_supported_boot_modes is not None:
        import capo_ec2.types.boot_mode_type_list

        out["supported_boot_modes"] = (
            capo_ec2.types.boot_mode_type_list.deserialize_ec2_query(
                child_supported_boot_modes
            )
        )
    child_nitro_enclaves_support = el.find("nitroEnclavesSupport")
    if child_nitro_enclaves_support is not None:
        import capo_ec2.types.nitro_enclaves_support

        out["nitro_enclaves_support"] = (
            capo_ec2.types.nitro_enclaves_support.deserialize_ec2_query(
                child_nitro_enclaves_support
            )
        )
    child_nitro_tpm_support = el.find("nitroTpmSupport")
    if child_nitro_tpm_support is not None:
        import capo_ec2.types.nitro_tpm_support

        out["nitro_tpm_support"] = (
            capo_ec2.types.nitro_tpm_support.deserialize_ec2_query(
                child_nitro_tpm_support
            )
        )
    child_nitro_tpm_info = el.find("nitroTpmInfo")
    if child_nitro_tpm_info is not None:
        import capo_ec2.types.nitro_tpm_info

        out["nitro_tpm_info"] = capo_ec2.types.nitro_tpm_info.deserialize_ec2_query(
            child_nitro_tpm_info
        )
    child_media_accelerator_info = el.find("mediaAcceleratorInfo")
    if child_media_accelerator_info is not None:
        import capo_ec2.types.media_accelerator_info

        out["media_accelerator_info"] = (
            capo_ec2.types.media_accelerator_info.deserialize_ec2_query(
                child_media_accelerator_info
            )
        )
    child_neuron_info = el.find("neuronInfo")
    if child_neuron_info is not None:
        import capo_ec2.types.neuron_info

        out["neuron_info"] = capo_ec2.types.neuron_info.deserialize_ec2_query(
            child_neuron_info
        )
    child_phc_support = el.find("phcSupport")
    if child_phc_support is not None:
        import capo_ec2.types.phc_support

        out["phc_support"] = capo_ec2.types.phc_support.deserialize_ec2_query(
            child_phc_support
        )
    child_reboot_migration_support = el.find("rebootMigrationSupport")
    if child_reboot_migration_support is not None:
        import capo_ec2.types.reboot_migration_support

        out["reboot_migration_support"] = (
            capo_ec2.types.reboot_migration_support.deserialize_ec2_query(
                child_reboot_migration_support
            )
        )
    child_supported_in_region = el.find("supportedInRegion")
    if child_supported_in_region is not None:
        out["supported_in_region"] = (
            child_supported_in_region.text or ""
        ).lower() == "true"
    return out
