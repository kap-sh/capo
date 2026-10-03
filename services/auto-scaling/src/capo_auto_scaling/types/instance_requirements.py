"""Generated from Smithy shape ``com.amazonaws.autoscaling#InstanceRequirements``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.accelerator_count_request
    import capo_auto_scaling.types.accelerator_manufacturers
    import capo_auto_scaling.types.accelerator_names
    import capo_auto_scaling.types.accelerator_total_memory_mi_b_request
    import capo_auto_scaling.types.accelerator_types
    import capo_auto_scaling.types.allowed_instance_types
    import capo_auto_scaling.types.bare_metal
    import capo_auto_scaling.types.baseline_ebs_bandwidth_mbps_request
    import capo_auto_scaling.types.baseline_performance_factors_request
    import capo_auto_scaling.types.burstable_performance
    import capo_auto_scaling.types.cpu_manufacturers
    import capo_auto_scaling.types.excluded_instance_types
    import capo_auto_scaling.types.instance_generations
    import capo_auto_scaling.types.local_storage
    import capo_auto_scaling.types.local_storage_types
    import capo_auto_scaling.types.memory_gi_b_per_v_cpu_request
    import capo_auto_scaling.types.memory_mi_b_request
    import capo_auto_scaling.types.network_bandwidth_gbps_request
    import capo_auto_scaling.types.network_interface_count_request
    import capo_auto_scaling.types.nullable_boolean
    import capo_auto_scaling.types.nullable_positive_integer
    import capo_auto_scaling.types.total_local_storage_gb_request
    import capo_auto_scaling.types.v_cpu_count_request


class InstanceRequirements(TypedDict, closed=True):
    v_cpu_count: NotRequired[
        "capo_auto_scaling.types.v_cpu_count_request.VCpuCountRequest"
    ]
    """<p>The minimum and maximum number of vCPUs for an instance type.</p>"""
    memory_mi_b: NotRequired[
        "capo_auto_scaling.types.memory_mi_b_request.MemoryMiBRequest"
    ]
    """<p>The minimum and maximum instance memory size for an instance type, in MiB.</p>"""
    cpu_manufacturers: NotRequired[
        "capo_auto_scaling.types.cpu_manufacturers.CpuManufacturers"
    ]
    """<p>Lists which specific CPU manufacturers to include.</p> <ul> <li> <p>For instance types with Intel CPUs, specify <code>intel</code>.</p> </li> <li> <p>For instance types with AMD CPUs, specify <code>amd</code>.</p> </li> <li> <p>For instance types with Amazon Web Services CPUs, specify <code>amazon-web-services</code>.</p> </li> <li> <p>For instance types with Apple CPUs, specify <code>apple</code>.</p> </li> </ul> <note> <p>Don't confuse the CPU hardware manufacturer with the CPU hardware architecture. Instances will be launched with a compatible CPU architecture based on the Amazon Machine Image (AMI) that you specify in your launch template. </p> </note> <p>Default: Any manufacturer</p>"""
    memory_gi_b_per_v_cpu: NotRequired[
        "capo_auto_scaling.types.memory_gi_b_per_v_cpu_request.MemoryGiBPerVCpuRequest"
    ]
    """<p>The minimum and maximum amount of memory per vCPU for an instance type, in GiB.</p> <p>Default: No minimum or maximum limits</p>"""
    excluded_instance_types: NotRequired[
        "capo_auto_scaling.types.excluded_instance_types.ExcludedInstanceTypes"
    ]
    """<p>The instance types to exclude. You can use strings with one or more wild cards, represented by an asterisk (<code>*</code>), to exclude an instance family, type, size, or generation. The following are examples: <code>m5.8xlarge</code>, <code>c5*.*</code>, <code>m5a.*</code>, <code>r*</code>, <code>*3*</code>. </p> <p>For example, if you specify <code>c5*</code>, you are excluding the entire C5 instance family, which includes all C5a and C5n instance types. If you specify <code>m5a.*</code>, Amazon EC2 Auto Scaling will exclude all the M5a instance types, but not the M5n instance types.</p> <note> <p>If you specify <code>ExcludedInstanceTypes</code>, you can't specify <code>AllowedInstanceTypes</code>.</p> </note> <p>Default: No excluded instance types</p>"""
    instance_generations: NotRequired[
        "capo_auto_scaling.types.instance_generations.InstanceGenerations"
    ]
    """<p>Indicates whether current or previous generation instance types are included.</p> <ul> <li> <p>For current generation instance types, specify <code>current</code>. The current generation includes EC2 instance types currently recommended for use. This typically includes the latest two to three generations in each instance family. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html">Instance types</a> in the <i>Amazon EC2 User Guide</i>.</p> </li> <li> <p>For previous generation instance types, specify <code>previous</code>.</p> </li> </ul> <p>Default: Any current or previous generation</p>"""
    spot_max_price_percentage_over_lowest_price: NotRequired[
        "capo_auto_scaling.types.nullable_positive_integer.NullablePositiveInteger"
    ]
    """<p>[Price protection] The price protection threshold for Spot Instances, as a percentage higher than an identified Spot price. The identified Spot price is the price of the lowest priced current generation C, M, or R instance type with your specified attributes. If no current generation C, M, or R instance type matches your attributes, then the identified price is from either the lowest priced current generation instance types or, failing that, the lowest priced previous generation instance types that match your attributes. When Amazon EC2 Auto Scaling selects instance types with your attributes, we will exclude instance types whose price exceeds your specified threshold.</p> <p>The parameter accepts an integer, which Amazon EC2 Auto Scaling interprets as a percentage. </p> <p>If you set <code>DesiredCapacityType</code> to <code>vcpu</code> or <code>memory-mib</code>, the price protection threshold is based on the per-vCPU or per-memory price instead of the per instance price. </p> <note> <p>Only one of <code>SpotMaxPricePercentageOverLowestPrice</code> or <code>MaxSpotPriceAsPercentageOfOptimalOnDemandPrice</code> can be specified. If you don't specify either, Amazon EC2 Auto Scaling will automatically apply optimal price protection to consistently select from a wide range of instance types. To indicate no price protection threshold for Spot Instances, meaning you want to consider all instance types that match your attributes, include one of these parameters and specify a high value, such as <code>999999</code>. </p> </note>"""
    max_spot_price_as_percentage_of_optimal_on_demand_price: NotRequired[
        "capo_auto_scaling.types.nullable_positive_integer.NullablePositiveInteger"
    ]
    """<p>[Price protection] The price protection threshold for Spot Instances, as a percentage of an identified On-Demand price. The identified On-Demand price is the price of the lowest priced current generation C, M, or R instance type with your specified attributes. If no current generation C, M, or R instance type matches your attributes, then the identified price is from either the lowest priced current generation instance types or, failing that, the lowest priced previous generation instance types that match your attributes. When Amazon EC2 Auto Scaling selects instance types with your attributes, we will exclude instance types whose price exceeds your specified threshold.</p> <p>The parameter accepts an integer, which Amazon EC2 Auto Scaling interprets as a percentage.</p> <p>If you set <code>DesiredCapacityType</code> to <code>vcpu</code> or <code>memory-mib</code>, the price protection threshold is based on the per-vCPU or per-memory price instead of the per instance price. </p> <note> <p>Only one of <code>SpotMaxPricePercentageOverLowestPrice</code> or <code>MaxSpotPriceAsPercentageOfOptimalOnDemandPrice</code> can be specified. If you don't specify either, Amazon EC2 Auto Scaling will automatically apply optimal price protection to consistently select from a wide range of instance types. To indicate no price protection threshold for Spot Instances, meaning you want to consider all instance types that match your attributes, include one of these parameters and specify a high value, such as <code>999999</code>. </p> </note>"""
    on_demand_max_price_percentage_over_lowest_price: NotRequired[
        "capo_auto_scaling.types.nullable_positive_integer.NullablePositiveInteger"
    ]
    """<p>[Price protection] The price protection threshold for On-Demand Instances, as a percentage higher than an identified On-Demand price. The identified On-Demand price is the price of the lowest priced current generation C, M, or R instance type with your specified attributes. If no current generation C, M, or R instance type matches your attributes, then the identified price is from either the lowest priced current generation instance types or, failing that, the lowest priced previous generation instance types that match your attributes. When Amazon EC2 Auto Scaling selects instance types with your attributes, we will exclude instance types whose price exceeds your specified threshold. </p> <p>The parameter accepts an integer, which Amazon EC2 Auto Scaling interprets as a percentage.</p> <p>To turn off price protection, specify a high value, such as <code>999999</code>. </p> <p>If you set <code>DesiredCapacityType</code> to <code>vcpu</code> or <code>memory-mib</code>, the price protection threshold is applied based on the per-vCPU or per-memory price instead of the per instance price. </p> <p>Default: <code>20</code> </p>"""
    bare_metal: NotRequired["capo_auto_scaling.types.bare_metal.BareMetal"]
    """<p>Indicates whether bare metal instance types are included, excluded, or required.</p> <p>Default: <code>excluded</code> </p>"""
    burstable_performance: NotRequired[
        "capo_auto_scaling.types.burstable_performance.BurstablePerformance"
    ]
    """<p>Indicates whether burstable performance instance types are included, excluded, or required. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances.html">Burstable performance instances</a> in the <i>Amazon EC2 User Guide</i>.</p> <p>Default: <code>excluded</code> </p>"""
    require_hibernate_support: NotRequired[
        "capo_auto_scaling.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Indicates whether instance types must provide On-Demand Instance hibernation support.</p> <p>Default: <code>false</code> </p>"""
    network_interface_count: NotRequired[
        "capo_auto_scaling.types.network_interface_count_request.NetworkInterfaceCountRequest"
    ]
    """<p>The minimum and maximum number of network interfaces for an instance type.</p> <p>Default: No minimum or maximum limits</p>"""
    local_storage: NotRequired["capo_auto_scaling.types.local_storage.LocalStorage"]
    """<p>Indicates whether instance types with instance store volumes are included, excluded, or required. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html">Amazon EC2 instance store</a> in the <i>Amazon EC2 User Guide</i>.</p> <p>Default: <code>included</code> </p>"""
    local_storage_types: NotRequired[
        "capo_auto_scaling.types.local_storage_types.LocalStorageTypes"
    ]
    """<p>Indicates the type of local storage that is required.</p> <ul> <li> <p>For instance types with hard disk drive (HDD) storage, specify <code>hdd</code>.</p> </li> <li> <p>For instance types with solid state drive (SSD) storage, specify <code>ssd</code>.</p> </li> </ul> <p>Default: Any local storage type</p>"""
    total_local_storage_gb: NotRequired[
        "capo_auto_scaling.types.total_local_storage_gb_request.TotalLocalStorageGBRequest"
    ]
    """<p>The minimum and maximum total local storage size for an instance type, in GB.</p> <p>Default: No minimum or maximum limits</p>"""
    baseline_ebs_bandwidth_mbps: NotRequired[
        "capo_auto_scaling.types.baseline_ebs_bandwidth_mbps_request.BaselineEbsBandwidthMbpsRequest"
    ]
    """<p>The minimum and maximum baseline bandwidth performance for an instance type, in Mbps. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-optimized.html">Amazon EBS–optimized instances</a> in the <i>Amazon EC2 User Guide</i>.</p> <p>Default: No minimum or maximum limits</p>"""
    accelerator_types: NotRequired[
        "capo_auto_scaling.types.accelerator_types.AcceleratorTypes"
    ]
    """<p>Lists the accelerator types that must be on an instance type.</p> <ul> <li> <p>For instance types with GPU accelerators, specify <code>gpu</code>.</p> </li> <li> <p>For instance types with FPGA accelerators, specify <code>fpga</code>.</p> </li> <li> <p>For instance types with inference accelerators, specify <code>inference</code>.</p> </li> </ul> <p>Default: Any accelerator type</p>"""
    accelerator_count: NotRequired[
        "capo_auto_scaling.types.accelerator_count_request.AcceleratorCountRequest"
    ]
    """<p>The minimum and maximum number of accelerators (GPUs, FPGAs, or Amazon Web Services Inferentia chips) for an instance type.</p> <p>To exclude accelerator-enabled instance types, set <code>Max</code> to <code>0</code>.</p> <p>Default: No minimum or maximum limits</p>"""
    accelerator_manufacturers: NotRequired[
        "capo_auto_scaling.types.accelerator_manufacturers.AcceleratorManufacturers"
    ]
    """<p>Indicates whether instance types must have accelerators by specific manufacturers.</p> <ul> <li> <p>For instance types with NVIDIA devices, specify <code>nvidia</code>.</p> </li> <li> <p>For instance types with AMD devices, specify <code>amd</code>.</p> </li> <li> <p>For instance types with Amazon Web Services devices, specify <code>amazon-web-services</code>.</p> </li> <li> <p>For instance types with Xilinx devices, specify <code>xilinx</code>.</p> </li> </ul> <p>Default: Any manufacturer</p>"""
    accelerator_names: NotRequired[
        "capo_auto_scaling.types.accelerator_names.AcceleratorNames"
    ]
    """<p>Lists the accelerators that must be on an instance type.</p> <ul> <li> <p>For instance types with NVIDIA A100 GPUs, specify <code>a100</code>.</p> </li> <li> <p>For instance types with NVIDIA V100 GPUs, specify <code>v100</code>.</p> </li> <li> <p>For instance types with NVIDIA K80 GPUs, specify <code>k80</code>.</p> </li> <li> <p>For instance types with NVIDIA T4 GPUs, specify <code>t4</code>.</p> </li> <li> <p>For instance types with NVIDIA M60 GPUs, specify <code>m60</code>.</p> </li> <li> <p>For instance types with AMD Radeon Pro V520 GPUs, specify <code>radeon-pro-v520</code>.</p> </li> <li> <p>For instance types with Xilinx VU9P FPGAs, specify <code>vu9p</code>.</p> </li> </ul> <p>Default: Any accelerator</p>"""
    accelerator_total_memory_mi_b: NotRequired[
        "capo_auto_scaling.types.accelerator_total_memory_mi_b_request.AcceleratorTotalMemoryMiBRequest"
    ]
    """<p>The minimum and maximum total memory size for the accelerators on an instance type, in MiB.</p> <p>Default: No minimum or maximum limits</p>"""
    network_bandwidth_gbps: NotRequired[
        "capo_auto_scaling.types.network_bandwidth_gbps_request.NetworkBandwidthGbpsRequest"
    ]
    """<p>The minimum and maximum amount of network bandwidth, in gigabits per second (Gbps).</p> <p>Default: No minimum or maximum limits</p>"""
    allowed_instance_types: NotRequired[
        "capo_auto_scaling.types.allowed_instance_types.AllowedInstanceTypes"
    ]
    """<p>The instance types to apply your specified attributes against. All other instance types are ignored, even if they match your specified attributes.</p> <p>You can use strings with one or more wild cards, represented by an asterisk (<code>*</code>), to allow an instance type, size, or generation. The following are examples: <code>m5.8xlarge</code>, <code>c5*.*</code>, <code>m5a.*</code>, <code>r*</code>, <code>*3*</code>.</p> <p>For example, if you specify <code>c5*</code>, Amazon EC2 Auto Scaling will allow the entire C5 instance family, which includes all C5a and C5n instance types. If you specify <code>m5a.*</code>, Amazon EC2 Auto Scaling will allow all the M5a instance types, but not the M5n instance types.</p> <note> <p>If you specify <code>AllowedInstanceTypes</code>, you can't specify <code>ExcludedInstanceTypes</code>.</p> </note> <p>Default: All instance types</p>"""
    baseline_performance_factors: NotRequired[
        "capo_auto_scaling.types.baseline_performance_factors_request.BaselinePerformanceFactorsRequest"
    ]
    """<p> The baseline performance factors for the instance requirements. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: InstanceRequirements, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "v_cpu_count" in value:
        import capo_auto_scaling.types.v_cpu_count_request

        capo_auto_scaling.types.v_cpu_count_request.serialize_query(
            value["v_cpu_count"], pairs, f"{key_prefix}VCpuCount"
        )
    if "memory_mi_b" in value:
        import capo_auto_scaling.types.memory_mi_b_request

        capo_auto_scaling.types.memory_mi_b_request.serialize_query(
            value["memory_mi_b"], pairs, f"{key_prefix}MemoryMiB"
        )
    if "cpu_manufacturers" in value:
        import capo_auto_scaling.types.cpu_manufacturers

        capo_auto_scaling.types.cpu_manufacturers.serialize_query(
            value["cpu_manufacturers"], pairs, f"{key_prefix}CpuManufacturers"
        )
    if "memory_gi_b_per_v_cpu" in value:
        import capo_auto_scaling.types.memory_gi_b_per_v_cpu_request

        capo_auto_scaling.types.memory_gi_b_per_v_cpu_request.serialize_query(
            value["memory_gi_b_per_v_cpu"], pairs, f"{key_prefix}MemoryGiBPerVCpu"
        )
    if "excluded_instance_types" in value:
        import capo_auto_scaling.types.excluded_instance_types

        capo_auto_scaling.types.excluded_instance_types.serialize_query(
            value["excluded_instance_types"],
            pairs,
            f"{key_prefix}ExcludedInstanceTypes",
        )
    if "instance_generations" in value:
        import capo_auto_scaling.types.instance_generations

        capo_auto_scaling.types.instance_generations.serialize_query(
            value["instance_generations"], pairs, f"{key_prefix}InstanceGenerations"
        )
    if "spot_max_price_percentage_over_lowest_price" in value:
        pairs.append(
            (
                f"{key_prefix}SpotMaxPricePercentageOverLowestPrice",
                str(value["spot_max_price_percentage_over_lowest_price"]),
            )
        )
    if "max_spot_price_as_percentage_of_optimal_on_demand_price" in value:
        pairs.append(
            (
                f"{key_prefix}MaxSpotPriceAsPercentageOfOptimalOnDemandPrice",
                str(value["max_spot_price_as_percentage_of_optimal_on_demand_price"]),
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
        import capo_auto_scaling.types.bare_metal

        capo_auto_scaling.types.bare_metal.serialize_query(
            value["bare_metal"], pairs, f"{key_prefix}BareMetal"
        )
    if "burstable_performance" in value:
        import capo_auto_scaling.types.burstable_performance

        capo_auto_scaling.types.burstable_performance.serialize_query(
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
        import capo_auto_scaling.types.network_interface_count_request

        capo_auto_scaling.types.network_interface_count_request.serialize_query(
            value["network_interface_count"],
            pairs,
            f"{key_prefix}NetworkInterfaceCount",
        )
    if "local_storage" in value:
        import capo_auto_scaling.types.local_storage

        capo_auto_scaling.types.local_storage.serialize_query(
            value["local_storage"], pairs, f"{key_prefix}LocalStorage"
        )
    if "local_storage_types" in value:
        import capo_auto_scaling.types.local_storage_types

        capo_auto_scaling.types.local_storage_types.serialize_query(
            value["local_storage_types"], pairs, f"{key_prefix}LocalStorageTypes"
        )
    if "total_local_storage_gb" in value:
        import capo_auto_scaling.types.total_local_storage_gb_request

        capo_auto_scaling.types.total_local_storage_gb_request.serialize_query(
            value["total_local_storage_gb"], pairs, f"{key_prefix}TotalLocalStorageGB"
        )
    if "baseline_ebs_bandwidth_mbps" in value:
        import capo_auto_scaling.types.baseline_ebs_bandwidth_mbps_request

        capo_auto_scaling.types.baseline_ebs_bandwidth_mbps_request.serialize_query(
            value["baseline_ebs_bandwidth_mbps"],
            pairs,
            f"{key_prefix}BaselineEbsBandwidthMbps",
        )
    if "accelerator_types" in value:
        import capo_auto_scaling.types.accelerator_types

        capo_auto_scaling.types.accelerator_types.serialize_query(
            value["accelerator_types"], pairs, f"{key_prefix}AcceleratorTypes"
        )
    if "accelerator_count" in value:
        import capo_auto_scaling.types.accelerator_count_request

        capo_auto_scaling.types.accelerator_count_request.serialize_query(
            value["accelerator_count"], pairs, f"{key_prefix}AcceleratorCount"
        )
    if "accelerator_manufacturers" in value:
        import capo_auto_scaling.types.accelerator_manufacturers

        capo_auto_scaling.types.accelerator_manufacturers.serialize_query(
            value["accelerator_manufacturers"],
            pairs,
            f"{key_prefix}AcceleratorManufacturers",
        )
    if "accelerator_names" in value:
        import capo_auto_scaling.types.accelerator_names

        capo_auto_scaling.types.accelerator_names.serialize_query(
            value["accelerator_names"], pairs, f"{key_prefix}AcceleratorNames"
        )
    if "accelerator_total_memory_mi_b" in value:
        import capo_auto_scaling.types.accelerator_total_memory_mi_b_request

        capo_auto_scaling.types.accelerator_total_memory_mi_b_request.serialize_query(
            value["accelerator_total_memory_mi_b"],
            pairs,
            f"{key_prefix}AcceleratorTotalMemoryMiB",
        )
    if "network_bandwidth_gbps" in value:
        import capo_auto_scaling.types.network_bandwidth_gbps_request

        capo_auto_scaling.types.network_bandwidth_gbps_request.serialize_query(
            value["network_bandwidth_gbps"], pairs, f"{key_prefix}NetworkBandwidthGbps"
        )
    if "allowed_instance_types" in value:
        import capo_auto_scaling.types.allowed_instance_types

        capo_auto_scaling.types.allowed_instance_types.serialize_query(
            value["allowed_instance_types"], pairs, f"{key_prefix}AllowedInstanceTypes"
        )
    if "baseline_performance_factors" in value:
        import capo_auto_scaling.types.baseline_performance_factors_request

        capo_auto_scaling.types.baseline_performance_factors_request.serialize_query(
            value["baseline_performance_factors"],
            pairs,
            f"{key_prefix}BaselinePerformanceFactors",
        )


def deserialize_query(el: Element) -> InstanceRequirements:
    out: InstanceRequirements = {}  # type: ignore[typeddict-item]
    child_v_cpu_count = el.find("VCpuCount")
    if child_v_cpu_count is not None:
        import capo_auto_scaling.types.v_cpu_count_request

        out["v_cpu_count"] = (
            capo_auto_scaling.types.v_cpu_count_request.deserialize_query(
                child_v_cpu_count
            )
        )
    child_memory_mi_b = el.find("MemoryMiB")
    if child_memory_mi_b is not None:
        import capo_auto_scaling.types.memory_mi_b_request

        out["memory_mi_b"] = (
            capo_auto_scaling.types.memory_mi_b_request.deserialize_query(
                child_memory_mi_b
            )
        )
    child_cpu_manufacturers = el.find("CpuManufacturers")
    if child_cpu_manufacturers is not None:
        import capo_auto_scaling.types.cpu_manufacturers

        out["cpu_manufacturers"] = (
            capo_auto_scaling.types.cpu_manufacturers.deserialize_query(
                child_cpu_manufacturers
            )
        )
    child_memory_gi_b_per_v_cpu = el.find("MemoryGiBPerVCpu")
    if child_memory_gi_b_per_v_cpu is not None:
        import capo_auto_scaling.types.memory_gi_b_per_v_cpu_request

        out["memory_gi_b_per_v_cpu"] = (
            capo_auto_scaling.types.memory_gi_b_per_v_cpu_request.deserialize_query(
                child_memory_gi_b_per_v_cpu
            )
        )
    child_excluded_instance_types = el.find("ExcludedInstanceTypes")
    if child_excluded_instance_types is not None:
        import capo_auto_scaling.types.excluded_instance_types

        out["excluded_instance_types"] = (
            capo_auto_scaling.types.excluded_instance_types.deserialize_query(
                child_excluded_instance_types
            )
        )
    child_instance_generations = el.find("InstanceGenerations")
    if child_instance_generations is not None:
        import capo_auto_scaling.types.instance_generations

        out["instance_generations"] = (
            capo_auto_scaling.types.instance_generations.deserialize_query(
                child_instance_generations
            )
        )
    child_spot_max_price_percentage_over_lowest_price = el.find(
        "SpotMaxPricePercentageOverLowestPrice"
    )
    if child_spot_max_price_percentage_over_lowest_price is not None:
        out["spot_max_price_percentage_over_lowest_price"] = int(
            child_spot_max_price_percentage_over_lowest_price.text or ""
        )
    child_max_spot_price_as_percentage_of_optimal_on_demand_price = el.find(
        "MaxSpotPriceAsPercentageOfOptimalOnDemandPrice"
    )
    if child_max_spot_price_as_percentage_of_optimal_on_demand_price is not None:
        out["max_spot_price_as_percentage_of_optimal_on_demand_price"] = int(
            child_max_spot_price_as_percentage_of_optimal_on_demand_price.text or ""
        )
    child_on_demand_max_price_percentage_over_lowest_price = el.find(
        "OnDemandMaxPricePercentageOverLowestPrice"
    )
    if child_on_demand_max_price_percentage_over_lowest_price is not None:
        out["on_demand_max_price_percentage_over_lowest_price"] = int(
            child_on_demand_max_price_percentage_over_lowest_price.text or ""
        )
    child_bare_metal = el.find("BareMetal")
    if child_bare_metal is not None:
        import capo_auto_scaling.types.bare_metal

        out["bare_metal"] = capo_auto_scaling.types.bare_metal.deserialize_query(
            child_bare_metal
        )
    child_burstable_performance = el.find("BurstablePerformance")
    if child_burstable_performance is not None:
        import capo_auto_scaling.types.burstable_performance

        out["burstable_performance"] = (
            capo_auto_scaling.types.burstable_performance.deserialize_query(
                child_burstable_performance
            )
        )
    child_require_hibernate_support = el.find("RequireHibernateSupport")
    if child_require_hibernate_support is not None:
        out["require_hibernate_support"] = (
            child_require_hibernate_support.text or ""
        ).lower() == "true"
    child_network_interface_count = el.find("NetworkInterfaceCount")
    if child_network_interface_count is not None:
        import capo_auto_scaling.types.network_interface_count_request

        out["network_interface_count"] = (
            capo_auto_scaling.types.network_interface_count_request.deserialize_query(
                child_network_interface_count
            )
        )
    child_local_storage = el.find("LocalStorage")
    if child_local_storage is not None:
        import capo_auto_scaling.types.local_storage

        out["local_storage"] = capo_auto_scaling.types.local_storage.deserialize_query(
            child_local_storage
        )
    child_local_storage_types = el.find("LocalStorageTypes")
    if child_local_storage_types is not None:
        import capo_auto_scaling.types.local_storage_types

        out["local_storage_types"] = (
            capo_auto_scaling.types.local_storage_types.deserialize_query(
                child_local_storage_types
            )
        )
    child_total_local_storage_gb = el.find("TotalLocalStorageGB")
    if child_total_local_storage_gb is not None:
        import capo_auto_scaling.types.total_local_storage_gb_request

        out["total_local_storage_gb"] = (
            capo_auto_scaling.types.total_local_storage_gb_request.deserialize_query(
                child_total_local_storage_gb
            )
        )
    child_baseline_ebs_bandwidth_mbps = el.find("BaselineEbsBandwidthMbps")
    if child_baseline_ebs_bandwidth_mbps is not None:
        import capo_auto_scaling.types.baseline_ebs_bandwidth_mbps_request

        out["baseline_ebs_bandwidth_mbps"] = (
            capo_auto_scaling.types.baseline_ebs_bandwidth_mbps_request.deserialize_query(
                child_baseline_ebs_bandwidth_mbps
            )
        )
    child_accelerator_types = el.find("AcceleratorTypes")
    if child_accelerator_types is not None:
        import capo_auto_scaling.types.accelerator_types

        out["accelerator_types"] = (
            capo_auto_scaling.types.accelerator_types.deserialize_query(
                child_accelerator_types
            )
        )
    child_accelerator_count = el.find("AcceleratorCount")
    if child_accelerator_count is not None:
        import capo_auto_scaling.types.accelerator_count_request

        out["accelerator_count"] = (
            capo_auto_scaling.types.accelerator_count_request.deserialize_query(
                child_accelerator_count
            )
        )
    child_accelerator_manufacturers = el.find("AcceleratorManufacturers")
    if child_accelerator_manufacturers is not None:
        import capo_auto_scaling.types.accelerator_manufacturers

        out["accelerator_manufacturers"] = (
            capo_auto_scaling.types.accelerator_manufacturers.deserialize_query(
                child_accelerator_manufacturers
            )
        )
    child_accelerator_names = el.find("AcceleratorNames")
    if child_accelerator_names is not None:
        import capo_auto_scaling.types.accelerator_names

        out["accelerator_names"] = (
            capo_auto_scaling.types.accelerator_names.deserialize_query(
                child_accelerator_names
            )
        )
    child_accelerator_total_memory_mi_b = el.find("AcceleratorTotalMemoryMiB")
    if child_accelerator_total_memory_mi_b is not None:
        import capo_auto_scaling.types.accelerator_total_memory_mi_b_request

        out["accelerator_total_memory_mi_b"] = (
            capo_auto_scaling.types.accelerator_total_memory_mi_b_request.deserialize_query(
                child_accelerator_total_memory_mi_b
            )
        )
    child_network_bandwidth_gbps = el.find("NetworkBandwidthGbps")
    if child_network_bandwidth_gbps is not None:
        import capo_auto_scaling.types.network_bandwidth_gbps_request

        out["network_bandwidth_gbps"] = (
            capo_auto_scaling.types.network_bandwidth_gbps_request.deserialize_query(
                child_network_bandwidth_gbps
            )
        )
    child_allowed_instance_types = el.find("AllowedInstanceTypes")
    if child_allowed_instance_types is not None:
        import capo_auto_scaling.types.allowed_instance_types

        out["allowed_instance_types"] = (
            capo_auto_scaling.types.allowed_instance_types.deserialize_query(
                child_allowed_instance_types
            )
        )
    child_baseline_performance_factors = el.find("BaselinePerformanceFactors")
    if child_baseline_performance_factors is not None:
        import capo_auto_scaling.types.baseline_performance_factors_request

        out["baseline_performance_factors"] = (
            capo_auto_scaling.types.baseline_performance_factors_request.deserialize_query(
                child_baseline_performance_factors
            )
        )
    return out
