"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceRequirements``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.accelerator_count
    import capo_ec2.types.accelerator_manufacturer_set
    import capo_ec2.types.accelerator_name_set
    import capo_ec2.types.accelerator_total_memory_mi_b
    import capo_ec2.types.accelerator_type_set
    import capo_ec2.types.allowed_instance_type_set
    import capo_ec2.types.bare_metal
    import capo_ec2.types.baseline_ebs_bandwidth_mbps
    import capo_ec2.types.baseline_performance_factors
    import capo_ec2.types.boolean
    import capo_ec2.types.burstable_performance
    import capo_ec2.types.cpu_manufacturer_set
    import capo_ec2.types.excluded_instance_type_set
    import capo_ec2.types.instance_generation_set
    import capo_ec2.types.integer
    import capo_ec2.types.local_storage
    import capo_ec2.types.local_storage_type_set
    import capo_ec2.types.memory_gi_b_per_v_cpu
    import capo_ec2.types.memory_mi_b
    import capo_ec2.types.network_bandwidth_gbps
    import capo_ec2.types.network_interface_count
    import capo_ec2.types.total_local_storage_gb
    import capo_ec2.types.v_cpu_count_range


class InstanceRequirements(TypedDict, closed=True):
    v_cpu_count: NotRequired["capo_ec2.types.v_cpu_count_range.VCpuCountRange"]
    """<p>The minimum and maximum number of vCPUs.</p>"""
    memory_mi_b: NotRequired["capo_ec2.types.memory_mi_b.MemoryMiB"]
    """<p>The minimum and maximum amount of memory, in MiB.</p>"""
    cpu_manufacturers: NotRequired[
        "capo_ec2.types.cpu_manufacturer_set.CpuManufacturerSet"
    ]
    """<p>The CPU manufacturers to include.</p> <ul> <li> <p>For instance types with Intel CPUs, specify <code>intel</code>.</p> </li> <li> <p>For instance types with AMD CPUs, specify <code>amd</code>.</p> </li> <li> <p>For instance types with Amazon Web Services CPUs, specify <code>amazon-web-services</code>.</p> </li> <li> <p>For instance types with Apple CPUs, specify <code>apple</code>.</p> </li> </ul> <note> <p>Don't confuse the CPU manufacturer with the CPU architecture. Instances will be launched with a compatible CPU architecture based on the Amazon Machine Image (AMI) that you specify in your launch template.</p> </note> <p>Default: Any manufacturer</p>"""
    memory_gi_b_per_v_cpu: NotRequired[
        "capo_ec2.types.memory_gi_b_per_v_cpu.MemoryGiBPerVCpu"
    ]
    """<p>The minimum and maximum amount of memory per vCPU, in GiB.</p> <p>Default: No minimum or maximum limits</p>"""
    excluded_instance_types: NotRequired[
        "capo_ec2.types.excluded_instance_type_set.ExcludedInstanceTypeSet"
    ]
    """<p>The instance types to exclude.</p> <p>You can use strings with one or more wild cards, represented by an asterisk (<code>*</code>), to exclude an instance type, size, or generation. The following are examples: <code>m5.8xlarge</code>, <code>c5*.*</code>, <code>m5a.*</code>, <code>r*</code>, <code>*3*</code>.</p> <p>For example, if you specify <code>c5*</code>,Amazon EC2 will exclude the entire C5 instance family, which includes all C5a and C5n instance types. If you specify <code>m5a.*</code>, Amazon EC2 will exclude all the M5a instance types, but not the M5n instance types.</p> <note> <p>If you specify <code>ExcludedInstanceTypes</code>, you can't specify <code>AllowedInstanceTypes</code>.</p> </note> <p>Default: No excluded instance types</p>"""
    instance_generations: NotRequired[
        "capo_ec2.types.instance_generation_set.InstanceGenerationSet"
    ]
    """<p>Indicates whether current or previous generation instance types are included. The current generation instance types are recommended for use. Current generation instance types are typically the latest two to three generations in each instance family. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html">Instance types</a> in the <i>Amazon EC2 User Guide</i>.</p> <p>For current generation instance types, specify <code>current</code>.</p> <p>For previous generation instance types, specify <code>previous</code>.</p> <p>Default: Current and previous generation instance types</p>"""
    spot_max_price_percentage_over_lowest_price: NotRequired[
        "capo_ec2.types.integer.Integer"
    ]
    """<p>[Price protection] The price protection threshold for Spot Instances, as a percentage higher than an identified Spot price. The identified Spot price is the Spot price of the lowest priced current generation C, M, or R instance type with your specified attributes. If no current generation C, M, or R instance type matches your attributes, then the identified Spot price is from the lowest priced current generation instance types, and failing that, from the lowest priced previous generation instance types that match your attributes. When Amazon EC2 selects instance types with your attributes, it will exclude instance types whose Spot price exceeds your specified threshold.</p> <p>The parameter accepts an integer, which Amazon EC2 interprets as a percentage.</p> <p>If you set <code>TargetCapacityUnitType</code> to <code>vcpu</code> or <code>memory-mib</code>, the price protection threshold is applied based on the per-vCPU or per-memory price instead of the per-instance price.</p> <p>This parameter is not supported for <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetSpotPlacementScores.html">GetSpotPlacementScores</a> and <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetInstanceTypesFromInstanceRequirements.html">GetInstanceTypesFromInstanceRequirements</a>.</p> <note> <p>Only one of <code>SpotMaxPricePercentageOverLowestPrice</code> or <code>MaxSpotPriceAsPercentageOfOptimalOnDemandPrice</code> can be specified. If you don't specify either, Amazon EC2 will automatically apply optimal price protection to consistently select from a wide range of instance types. To indicate no price protection threshold for Spot Instances, meaning you want to consider all instance types that match your attributes, include one of these parameters and specify a high value, such as <code>999999</code>.</p> </note> <p>Default: <code>100</code> </p>"""
    on_demand_max_price_percentage_over_lowest_price: NotRequired[
        "capo_ec2.types.integer.Integer"
    ]
    """<p>[Price protection] The price protection threshold for On-Demand Instances, as a percentage higher than an identified On-Demand price. The identified On-Demand price is the price of the lowest priced current generation C, M, or R instance type with your specified attributes. When Amazon EC2 selects instance types with your attributes, it will exclude instance types whose price exceeds your specified threshold.</p> <p>The parameter accepts an integer, which Amazon EC2 interprets as a percentage.</p> <p>To turn off price protection, specify a high value, such as <code>999999</code>.</p> <p>This parameter is not supported for <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetSpotPlacementScores.html">GetSpotPlacementScores</a> and <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetInstanceTypesFromInstanceRequirements.html">GetInstanceTypesFromInstanceRequirements</a>.</p> <note> <p>If you set <code>TargetCapacityUnitType</code> to <code>vcpu</code> or <code>memory-mib</code>, the price protection threshold is applied based on the per-vCPU or per-memory price instead of the per-instance price.</p> </note> <p>Default: <code>20</code> </p>"""
    bare_metal: NotRequired["capo_ec2.types.bare_metal.BareMetal"]
    """<p>Indicates whether bare metal instance types must be included, excluded, or required.</p> <ul> <li> <p>To include bare metal instance types, specify <code>included</code>.</p> </li> <li> <p>To require only bare metal instance types, specify <code>required</code>.</p> </li> <li> <p>To exclude bare metal instance types, specify <code>excluded</code>.</p> </li> </ul> <p>Default: <code>excluded</code> </p>"""
    burstable_performance: NotRequired[
        "capo_ec2.types.burstable_performance.BurstablePerformance"
    ]
    """<p>Indicates whether burstable performance T instance types are included, excluded, or required. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances.html">Burstable performance instances</a>.</p> <ul> <li> <p>To include burstable performance instance types, specify <code>included</code>.</p> </li> <li> <p>To require only burstable performance instance types, specify <code>required</code>.</p> </li> <li> <p>To exclude burstable performance instance types, specify <code>excluded</code>.</p> </li> </ul> <p>Default: <code>excluded</code> </p>"""
    require_hibernate_support: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether instance types must support hibernation for On-Demand Instances.</p> <p>This parameter is not supported for <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetSpotPlacementScores.html">GetSpotPlacementScores</a>.</p> <p>Default: <code>false</code> </p>"""
    network_interface_count: NotRequired[
        "capo_ec2.types.network_interface_count.NetworkInterfaceCount"
    ]
    """<p>The minimum and maximum number of network interfaces.</p> <p>Default: No minimum or maximum limits</p>"""
    local_storage: NotRequired["capo_ec2.types.local_storage.LocalStorage"]
    """<p>Indicates whether instance types with instance store volumes are included, excluded, or required. For more information, <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html">Amazon EC2 instance store</a> in the <i>Amazon EC2 User Guide</i>.</p> <ul> <li> <p>To include instance types with instance store volumes, specify <code>included</code>.</p> </li> <li> <p>To require only instance types with instance store volumes, specify <code>required</code>.</p> </li> <li> <p>To exclude instance types with instance store volumes, specify <code>excluded</code>.</p> </li> </ul> <p>Default: <code>included</code> </p>"""
    local_storage_types: NotRequired[
        "capo_ec2.types.local_storage_type_set.LocalStorageTypeSet"
    ]
    """<p>The type of local storage that is required.</p> <ul> <li> <p>For instance types with hard disk drive (HDD) storage, specify <code>hdd</code>.</p> </li> <li> <p>For instance types with solid state drive (SSD) storage, specify <code>ssd</code>.</p> </li> </ul> <p>Default: <code>hdd</code> and <code>ssd</code> </p>"""
    total_local_storage_gb: NotRequired[
        "capo_ec2.types.total_local_storage_gb.TotalLocalStorageGB"
    ]
    """<p>The minimum and maximum amount of total local storage, in GB.</p> <p>Default: No minimum or maximum limits</p>"""
    baseline_ebs_bandwidth_mbps: NotRequired[
        "capo_ec2.types.baseline_ebs_bandwidth_mbps.BaselineEbsBandwidthMbps"
    ]
    """<p>The minimum and maximum baseline bandwidth to Amazon EBS, in Mbps. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-optimized.html">Amazon EBS–optimized instances</a> in the <i>Amazon EC2 User Guide</i>.</p> <p>Default: No minimum or maximum limits</p>"""
    accelerator_types: NotRequired[
        "capo_ec2.types.accelerator_type_set.AcceleratorTypeSet"
    ]
    """<p>The accelerator types that must be on the instance type.</p> <ul> <li> <p>For instance types with FPGA accelerators, specify <code>fpga</code>.</p> </li> <li> <p>For instance types with GPU accelerators, specify <code>gpu</code>.</p> </li> <li> <p>For instance types with Inference accelerators, specify <code>inference</code>.</p> </li> <li> <p>For instance types with Media accelerators, specify <code>media</code>.</p> </li> </ul> <p>Default: Any accelerator type</p>"""
    accelerator_count: NotRequired["capo_ec2.types.accelerator_count.AcceleratorCount"]
    """<p>The minimum and maximum number of accelerators (GPUs, FPGAs, or Amazon Web Services Inferentia chips) on an instance.</p> <p>To exclude accelerator-enabled instance types, set <code>Max</code> to <code>0</code>.</p> <p>Default: No minimum or maximum limits</p>"""
    accelerator_manufacturers: NotRequired[
        "capo_ec2.types.accelerator_manufacturer_set.AcceleratorManufacturerSet"
    ]
    """<p>Indicates whether instance types must have accelerators by specific manufacturers.</p> <ul> <li> <p>For instance types with Amazon Web Services devices, specify <code>amazon-web-services</code>.</p> </li> <li> <p>For instance types with AMD devices, specify <code>amd</code>.</p> </li> <li> <p>For instance types with Habana devices, specify <code>habana</code>.</p> </li> <li> <p>For instance types with NVIDIA devices, specify <code>nvidia</code>.</p> </li> <li> <p>For instance types with Xilinx devices, specify <code>xilinx</code>.</p> </li> </ul> <p>Default: Any manufacturer</p>"""
    accelerator_names: NotRequired[
        "capo_ec2.types.accelerator_name_set.AcceleratorNameSet"
    ]
    """<p>The accelerators that must be on the instance type.</p> <ul> <li> <p>For instance types with NVIDIA A10G GPUs, specify <code>a10g</code>.</p> </li> <li> <p>For instance types with NVIDIA A100 GPUs, specify <code>a100</code>.</p> </li> <li> <p>For instance types with NVIDIA H100 GPUs, specify <code>h100</code>.</p> </li> <li> <p>For instance types with Amazon Web Services Inferentia chips, specify <code>inferentia</code>.</p> </li> <li> <p>For instance types with Amazon Web Services Inferentia2 chips, specify <code>inferentia2</code>.</p> </li> <li> <p>For instance types with Habana Gaudi HL-205 GPUs, specify <code>gaudi-hl-205</code>.</p> </li> <li> <p>For instance types with NVIDIA GRID K520 GPUs, specify <code>k520</code>.</p> </li> <li> <p>For instance types with NVIDIA K80 GPUs, specify <code>k80</code>.</p> </li> <li> <p>For instance types with NVIDIA L4 GPUs, specify <code>l4</code>.</p> </li> <li> <p>For instance types with NVIDIA L40S GPUs, specify <code>l40s</code>.</p> </li> <li> <p>For instance types with NVIDIA M60 GPUs, specify <code>m60</code>.</p> </li> <li> <p>For instance types with AMD Radeon Pro V520 GPUs, specify <code>radeon-pro-v520</code>.</p> </li> <li> <p>For instance types with Amazon Web Services Trainium chips, specify <code>trainium</code>.</p> </li> <li> <p>For instance types with Amazon Web Services Trainium2 chips, specify <code>trainium2</code>.</p> </li> <li> <p>For instance types with NVIDIA T4 GPUs, specify <code>t4</code>.</p> </li> <li> <p>For instance types with NVIDIA T4G GPUs, specify <code>t4g</code>.</p> </li> <li> <p>For instance types with Xilinx U30 cards, specify <code>u30</code>.</p> </li> <li> <p>For instance types with Xilinx VU9P FPGAs, specify <code>vu9p</code>.</p> </li> <li> <p>For instance types with NVIDIA V100 GPUs, specify <code>v100</code>.</p> </li> </ul> <p>Default: Any accelerator</p>"""
    accelerator_total_memory_mi_b: NotRequired[
        "capo_ec2.types.accelerator_total_memory_mi_b.AcceleratorTotalMemoryMiB"
    ]
    """<p>The minimum and maximum amount of total accelerator memory, in MiB.</p> <p>Default: No minimum or maximum limits</p>"""
    network_bandwidth_gbps: NotRequired[
        "capo_ec2.types.network_bandwidth_gbps.NetworkBandwidthGbps"
    ]
    """<p>The minimum and maximum amount of network bandwidth, in gigabits per second (Gbps).</p> <p>Default: No minimum or maximum limits</p>"""
    allowed_instance_types: NotRequired[
        "capo_ec2.types.allowed_instance_type_set.AllowedInstanceTypeSet"
    ]
    """<p>The instance types to apply your specified attributes against. All other instance types are ignored, even if they match your specified attributes.</p> <p>You can use strings with one or more wild cards, represented by an asterisk (<code>*</code>), to allow an instance type, size, or generation. The following are examples: <code>m5.8xlarge</code>, <code>c5*.*</code>, <code>m5a.*</code>, <code>r*</code>, <code>*3*</code>.</p> <p>For example, if you specify <code>c5*</code>,Amazon EC2 will allow the entire C5 instance family, which includes all C5a and C5n instance types. If you specify <code>m5a.*</code>, Amazon EC2 will allow all the M5a instance types, but not the M5n instance types.</p> <note> <p>If you specify <code>AllowedInstanceTypes</code>, you can't specify <code>ExcludedInstanceTypes</code>.</p> </note> <p>Default: All instance types</p>"""
    max_spot_price_as_percentage_of_optimal_on_demand_price: NotRequired[
        "capo_ec2.types.integer.Integer"
    ]
    """<p>[Price protection] The price protection threshold for Spot Instances, as a percentage of an identified On-Demand price. The identified On-Demand price is the price of the lowest priced current generation C, M, or R instance type with your specified attributes. If no current generation C, M, or R instance type matches your attributes, then the identified price is from the lowest priced current generation instance types, and failing that, from the lowest priced previous generation instance types that match your attributes. When Amazon EC2 selects instance types with your attributes, it will exclude instance types whose price exceeds your specified threshold.</p> <p>The parameter accepts an integer, which Amazon EC2 interprets as a percentage.</p> <p>If you set <code>TargetCapacityUnitType</code> to <code>vcpu</code> or <code>memory-mib</code>, the price protection threshold is based on the per vCPU or per memory price instead of the per instance price.</p> <note> <p>Only one of <code>SpotMaxPricePercentageOverLowestPrice</code> or <code>MaxSpotPriceAsPercentageOfOptimalOnDemandPrice</code> can be specified. If you don't specify either, Amazon EC2 will automatically apply optimal price protection to consistently select from a wide range of instance types. To indicate no price protection threshold for Spot Instances, meaning you want to consider all instance types that match your attributes, include one of these parameters and specify a high value, such as <code>999999</code>.</p> </note>"""
    baseline_performance_factors: NotRequired[
        "capo_ec2.types.baseline_performance_factors.BaselinePerformanceFactors"
    ]
    """<p>The baseline performance to consider, using an instance family as a baseline reference. The instance family establishes the lowest acceptable level of performance. Amazon EC2 uses this baseline to guide instance type selection, but there is no guarantee that the selected instance types will always exceed the baseline for every application. Currently, this parameter only supports CPU performance as a baseline performance factor. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-attribute-based-instance-type-selection.html#ec2fleet-abis-performance-protection">Performance protection</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    require_encryption_in_transit: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Specifies whether instance types must support encrypting in-transit traffic between instances. For more information, including the supported instance types, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/data-protection.html#encryption-transit">Encryption in transit</a> in the <i>Amazon EC2 User Guide</i>.</p> <p>Default: <code>false</code> </p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceRequirements, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "v_cpu_count" in value:
        import capo_ec2.types.v_cpu_count_range

        capo_ec2.types.v_cpu_count_range.serialize_ec2_query(
            value["v_cpu_count"], pairs, f"{key_prefix}VCpuCount"
        )
    if "memory_mi_b" in value:
        import capo_ec2.types.memory_mi_b

        capo_ec2.types.memory_mi_b.serialize_ec2_query(
            value["memory_mi_b"], pairs, f"{key_prefix}MemoryMiB"
        )
    if "cpu_manufacturers" in value:
        import capo_ec2.types.cpu_manufacturer_set

        capo_ec2.types.cpu_manufacturer_set.serialize_ec2_query(
            value["cpu_manufacturers"], pairs, f"{key_prefix}CpuManufacturerSet"
        )
    if "memory_gi_b_per_v_cpu" in value:
        import capo_ec2.types.memory_gi_b_per_v_cpu

        capo_ec2.types.memory_gi_b_per_v_cpu.serialize_ec2_query(
            value["memory_gi_b_per_v_cpu"], pairs, f"{key_prefix}MemoryGiBPerVCpu"
        )
    if "excluded_instance_types" in value:
        import capo_ec2.types.excluded_instance_type_set

        capo_ec2.types.excluded_instance_type_set.serialize_ec2_query(
            value["excluded_instance_types"],
            pairs,
            f"{key_prefix}ExcludedInstanceTypeSet",
        )
    if "instance_generations" in value:
        import capo_ec2.types.instance_generation_set

        capo_ec2.types.instance_generation_set.serialize_ec2_query(
            value["instance_generations"], pairs, f"{key_prefix}InstanceGenerationSet"
        )
    if "spot_max_price_percentage_over_lowest_price" in value:
        pairs.append(
            (
                f"{key_prefix}SpotMaxPricePercentageOverLowestPrice",
                str(value["spot_max_price_percentage_over_lowest_price"]),
            )
        )
    if "on_demand_max_price_percentage_over_lowest_price" in value:
        pairs.append(
            (
                f"{key_prefix}OnDemandMaxPricePercentageOverLowestPrice",
                str(value["on_demand_max_price_percentage_over_lowest_price"]),
            )
        )
    if "bare_metal" in value:
        import capo_ec2.types.bare_metal

        capo_ec2.types.bare_metal.serialize_ec2_query(
            value["bare_metal"], pairs, f"{key_prefix}BareMetal"
        )
    if "burstable_performance" in value:
        import capo_ec2.types.burstable_performance

        capo_ec2.types.burstable_performance.serialize_ec2_query(
            value["burstable_performance"], pairs, f"{key_prefix}BurstablePerformance"
        )
    if "require_hibernate_support" in value:
        pairs.append(
            (
                f"{key_prefix}RequireHibernateSupport",
                "true" if value["require_hibernate_support"] else "false",
            )
        )
    if "network_interface_count" in value:
        import capo_ec2.types.network_interface_count

        capo_ec2.types.network_interface_count.serialize_ec2_query(
            value["network_interface_count"],
            pairs,
            f"{key_prefix}NetworkInterfaceCount",
        )
    if "local_storage" in value:
        import capo_ec2.types.local_storage

        capo_ec2.types.local_storage.serialize_ec2_query(
            value["local_storage"], pairs, f"{key_prefix}LocalStorage"
        )
    if "local_storage_types" in value:
        import capo_ec2.types.local_storage_type_set

        capo_ec2.types.local_storage_type_set.serialize_ec2_query(
            value["local_storage_types"], pairs, f"{key_prefix}LocalStorageTypeSet"
        )
    if "total_local_storage_gb" in value:
        import capo_ec2.types.total_local_storage_gb

        capo_ec2.types.total_local_storage_gb.serialize_ec2_query(
            value["total_local_storage_gb"], pairs, f"{key_prefix}TotalLocalStorageGB"
        )
    if "baseline_ebs_bandwidth_mbps" in value:
        import capo_ec2.types.baseline_ebs_bandwidth_mbps

        capo_ec2.types.baseline_ebs_bandwidth_mbps.serialize_ec2_query(
            value["baseline_ebs_bandwidth_mbps"],
            pairs,
            f"{key_prefix}BaselineEbsBandwidthMbps",
        )
    if "accelerator_types" in value:
        import capo_ec2.types.accelerator_type_set

        capo_ec2.types.accelerator_type_set.serialize_ec2_query(
            value["accelerator_types"], pairs, f"{key_prefix}AcceleratorTypeSet"
        )
    if "accelerator_count" in value:
        import capo_ec2.types.accelerator_count

        capo_ec2.types.accelerator_count.serialize_ec2_query(
            value["accelerator_count"], pairs, f"{key_prefix}AcceleratorCount"
        )
    if "accelerator_manufacturers" in value:
        import capo_ec2.types.accelerator_manufacturer_set

        capo_ec2.types.accelerator_manufacturer_set.serialize_ec2_query(
            value["accelerator_manufacturers"],
            pairs,
            f"{key_prefix}AcceleratorManufacturerSet",
        )
    if "accelerator_names" in value:
        import capo_ec2.types.accelerator_name_set

        capo_ec2.types.accelerator_name_set.serialize_ec2_query(
            value["accelerator_names"], pairs, f"{key_prefix}AcceleratorNameSet"
        )
    if "accelerator_total_memory_mi_b" in value:
        import capo_ec2.types.accelerator_total_memory_mi_b

        capo_ec2.types.accelerator_total_memory_mi_b.serialize_ec2_query(
            value["accelerator_total_memory_mi_b"],
            pairs,
            f"{key_prefix}AcceleratorTotalMemoryMiB",
        )
    if "network_bandwidth_gbps" in value:
        import capo_ec2.types.network_bandwidth_gbps

        capo_ec2.types.network_bandwidth_gbps.serialize_ec2_query(
            value["network_bandwidth_gbps"], pairs, f"{key_prefix}NetworkBandwidthGbps"
        )
    if "allowed_instance_types" in value:
        import capo_ec2.types.allowed_instance_type_set

        capo_ec2.types.allowed_instance_type_set.serialize_ec2_query(
            value["allowed_instance_types"],
            pairs,
            f"{key_prefix}AllowedInstanceTypeSet",
        )
    if "max_spot_price_as_percentage_of_optimal_on_demand_price" in value:
        pairs.append(
            (
                f"{key_prefix}MaxSpotPriceAsPercentageOfOptimalOnDemandPrice",
                str(value["max_spot_price_as_percentage_of_optimal_on_demand_price"]),
            )
        )
    if "baseline_performance_factors" in value:
        import capo_ec2.types.baseline_performance_factors

        capo_ec2.types.baseline_performance_factors.serialize_ec2_query(
            value["baseline_performance_factors"],
            pairs,
            f"{key_prefix}BaselinePerformanceFactors",
        )
    if "require_encryption_in_transit" in value:
        pairs.append(
            (
                f"{key_prefix}RequireEncryptionInTransit",
                "true" if value["require_encryption_in_transit"] else "false",
            )
        )


def deserialize_ec2_query(el: Element) -> InstanceRequirements:
    out: InstanceRequirements = {}  # type: ignore[typeddict-item]
    child_v_cpu_count = el.find("vCpuCount")
    if child_v_cpu_count is not None:
        import capo_ec2.types.v_cpu_count_range

        out["v_cpu_count"] = capo_ec2.types.v_cpu_count_range.deserialize_ec2_query(
            child_v_cpu_count
        )
    child_memory_mi_b = el.find("memoryMiB")
    if child_memory_mi_b is not None:
        import capo_ec2.types.memory_mi_b

        out["memory_mi_b"] = capo_ec2.types.memory_mi_b.deserialize_ec2_query(
            child_memory_mi_b
        )
    child_cpu_manufacturers = el.find("cpuManufacturerSet")
    if child_cpu_manufacturers is not None:
        import capo_ec2.types.cpu_manufacturer_set

        out["cpu_manufacturers"] = (
            capo_ec2.types.cpu_manufacturer_set.deserialize_ec2_query(
                child_cpu_manufacturers
            )
        )
    child_memory_gi_b_per_v_cpu = el.find("memoryGiBPerVCpu")
    if child_memory_gi_b_per_v_cpu is not None:
        import capo_ec2.types.memory_gi_b_per_v_cpu

        out["memory_gi_b_per_v_cpu"] = (
            capo_ec2.types.memory_gi_b_per_v_cpu.deserialize_ec2_query(
                child_memory_gi_b_per_v_cpu
            )
        )
    child_excluded_instance_types = el.find("excludedInstanceTypeSet")
    if child_excluded_instance_types is not None:
        import capo_ec2.types.excluded_instance_type_set

        out["excluded_instance_types"] = (
            capo_ec2.types.excluded_instance_type_set.deserialize_ec2_query(
                child_excluded_instance_types
            )
        )
    child_instance_generations = el.find("instanceGenerationSet")
    if child_instance_generations is not None:
        import capo_ec2.types.instance_generation_set

        out["instance_generations"] = (
            capo_ec2.types.instance_generation_set.deserialize_ec2_query(
                child_instance_generations
            )
        )
    child_spot_max_price_percentage_over_lowest_price = el.find(
        "spotMaxPricePercentageOverLowestPrice"
    )
    if child_spot_max_price_percentage_over_lowest_price is not None:
        out["spot_max_price_percentage_over_lowest_price"] = int(
            child_spot_max_price_percentage_over_lowest_price.text or ""
        )
    child_on_demand_max_price_percentage_over_lowest_price = el.find(
        "onDemandMaxPricePercentageOverLowestPrice"
    )
    if child_on_demand_max_price_percentage_over_lowest_price is not None:
        out["on_demand_max_price_percentage_over_lowest_price"] = int(
            child_on_demand_max_price_percentage_over_lowest_price.text or ""
        )
    child_bare_metal = el.find("bareMetal")
    if child_bare_metal is not None:
        import capo_ec2.types.bare_metal

        out["bare_metal"] = capo_ec2.types.bare_metal.deserialize_ec2_query(
            child_bare_metal
        )
    child_burstable_performance = el.find("burstablePerformance")
    if child_burstable_performance is not None:
        import capo_ec2.types.burstable_performance

        out["burstable_performance"] = (
            capo_ec2.types.burstable_performance.deserialize_ec2_query(
                child_burstable_performance
            )
        )
    child_require_hibernate_support = el.find("requireHibernateSupport")
    if child_require_hibernate_support is not None:
        out["require_hibernate_support"] = (
            child_require_hibernate_support.text or ""
        ).lower() == "true"
    child_network_interface_count = el.find("networkInterfaceCount")
    if child_network_interface_count is not None:
        import capo_ec2.types.network_interface_count

        out["network_interface_count"] = (
            capo_ec2.types.network_interface_count.deserialize_ec2_query(
                child_network_interface_count
            )
        )
    child_local_storage = el.find("localStorage")
    if child_local_storage is not None:
        import capo_ec2.types.local_storage

        out["local_storage"] = capo_ec2.types.local_storage.deserialize_ec2_query(
            child_local_storage
        )
    child_local_storage_types = el.find("localStorageTypeSet")
    if child_local_storage_types is not None:
        import capo_ec2.types.local_storage_type_set

        out["local_storage_types"] = (
            capo_ec2.types.local_storage_type_set.deserialize_ec2_query(
                child_local_storage_types
            )
        )
    child_total_local_storage_gb = el.find("totalLocalStorageGB")
    if child_total_local_storage_gb is not None:
        import capo_ec2.types.total_local_storage_gb

        out["total_local_storage_gb"] = (
            capo_ec2.types.total_local_storage_gb.deserialize_ec2_query(
                child_total_local_storage_gb
            )
        )
    child_baseline_ebs_bandwidth_mbps = el.find("baselineEbsBandwidthMbps")
    if child_baseline_ebs_bandwidth_mbps is not None:
        import capo_ec2.types.baseline_ebs_bandwidth_mbps

        out["baseline_ebs_bandwidth_mbps"] = (
            capo_ec2.types.baseline_ebs_bandwidth_mbps.deserialize_ec2_query(
                child_baseline_ebs_bandwidth_mbps
            )
        )
    child_accelerator_types = el.find("acceleratorTypeSet")
    if child_accelerator_types is not None:
        import capo_ec2.types.accelerator_type_set

        out["accelerator_types"] = (
            capo_ec2.types.accelerator_type_set.deserialize_ec2_query(
                child_accelerator_types
            )
        )
    child_accelerator_count = el.find("acceleratorCount")
    if child_accelerator_count is not None:
        import capo_ec2.types.accelerator_count

        out["accelerator_count"] = (
            capo_ec2.types.accelerator_count.deserialize_ec2_query(
                child_accelerator_count
            )
        )
    child_accelerator_manufacturers = el.find("acceleratorManufacturerSet")
    if child_accelerator_manufacturers is not None:
        import capo_ec2.types.accelerator_manufacturer_set

        out["accelerator_manufacturers"] = (
            capo_ec2.types.accelerator_manufacturer_set.deserialize_ec2_query(
                child_accelerator_manufacturers
            )
        )
    child_accelerator_names = el.find("acceleratorNameSet")
    if child_accelerator_names is not None:
        import capo_ec2.types.accelerator_name_set

        out["accelerator_names"] = (
            capo_ec2.types.accelerator_name_set.deserialize_ec2_query(
                child_accelerator_names
            )
        )
    child_accelerator_total_memory_mi_b = el.find("acceleratorTotalMemoryMiB")
    if child_accelerator_total_memory_mi_b is not None:
        import capo_ec2.types.accelerator_total_memory_mi_b

        out["accelerator_total_memory_mi_b"] = (
            capo_ec2.types.accelerator_total_memory_mi_b.deserialize_ec2_query(
                child_accelerator_total_memory_mi_b
            )
        )
    child_network_bandwidth_gbps = el.find("networkBandwidthGbps")
    if child_network_bandwidth_gbps is not None:
        import capo_ec2.types.network_bandwidth_gbps

        out["network_bandwidth_gbps"] = (
            capo_ec2.types.network_bandwidth_gbps.deserialize_ec2_query(
                child_network_bandwidth_gbps
            )
        )
    child_allowed_instance_types = el.find("allowedInstanceTypeSet")
    if child_allowed_instance_types is not None:
        import capo_ec2.types.allowed_instance_type_set

        out["allowed_instance_types"] = (
            capo_ec2.types.allowed_instance_type_set.deserialize_ec2_query(
                child_allowed_instance_types
            )
        )
    child_max_spot_price_as_percentage_of_optimal_on_demand_price = el.find(
        "maxSpotPriceAsPercentageOfOptimalOnDemandPrice"
    )
    if child_max_spot_price_as_percentage_of_optimal_on_demand_price is not None:
        out["max_spot_price_as_percentage_of_optimal_on_demand_price"] = int(
            child_max_spot_price_as_percentage_of_optimal_on_demand_price.text or ""
        )
    child_baseline_performance_factors = el.find("baselinePerformanceFactors")
    if child_baseline_performance_factors is not None:
        import capo_ec2.types.baseline_performance_factors

        out["baseline_performance_factors"] = (
            capo_ec2.types.baseline_performance_factors.deserialize_ec2_query(
                child_baseline_performance_factors
            )
        )
    child_require_encryption_in_transit = el.find("requireEncryptionInTransit")
    if child_require_encryption_in_transit is not None:
        out["require_encryption_in_transit"] = (
            child_require_encryption_in_transit.text or ""
        ).lower() == "true"
    return out
