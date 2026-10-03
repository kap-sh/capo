"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#InstanceRecommendationOption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.gpu_info
    import capo_compute_optimizer.types.instance_savings_opportunity_after_discounts
    import capo_compute_optimizer.types.instance_type
    import capo_compute_optimizer.types.migration_effort
    import capo_compute_optimizer.types.performance_risk
    import capo_compute_optimizer.types.platform_differences
    import capo_compute_optimizer.types.projected_utilization_metrics
    import capo_compute_optimizer.types.rank
    import capo_compute_optimizer.types.savings_opportunity


class InstanceRecommendationOption(TypedDict, closed=True):
    instance_type: NotRequired[
        "capo_compute_optimizer.types.instance_type.InstanceType"
    ]
    """<p>The instance type of the instance recommendation.</p>"""
    instance_gpu_info: NotRequired["capo_compute_optimizer.types.gpu_info.GpuInfo"]
    """<p> Describes the GPU accelerator settings for the recommended instance type. </p>"""
    projected_utilization_metrics: NotRequired[
        "capo_compute_optimizer.types.projected_utilization_metrics.ProjectedUtilizationMetrics"
    ]
    """<p>An array of objects that describe the projected utilization metrics of the instance recommendation option.</p> <note> <p>The <code>Cpu</code> and <code>Memory</code> metrics are the only projected utilization metrics returned. Additionally, the <code>Memory</code> metric is returned only for resources that have the unified CloudWatch agent installed on them. For more information, see <a href="https://docs.aws.amazon.com/compute-optimizer/latest/ug/metrics.html#cw-agent">Enabling Memory Utilization with the CloudWatch Agent</a>.</p> </note>"""
    platform_differences: NotRequired[
        "capo_compute_optimizer.types.platform_differences.PlatformDifferences"
    ]
    """<p>Describes the configuration differences between the current instance and the recommended instance type. You should consider the configuration differences before migrating your workloads from the current instance to the recommended instance type. The <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-resize.html">Change the instance type guide for Linux</a> and <a href="https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/ec2-instance-resize.html">Change the instance type guide for Windows</a> provide general guidance for getting started with an instance migration.</p> <p>Platform differences include:</p> <ul> <li> <p> <b> <code>Hypervisor</code> </b> — The hypervisor of the recommended instance type is different than that of the current instance. For example, the recommended instance type uses a Nitro hypervisor and the current instance uses a Xen hypervisor. The differences that you should consider between these hypervisors are covered in the <a href="http://aws.amazon.com/ec2/faqs/#Nitro_Hypervisor">Nitro Hypervisor</a> section of the Amazon EC2 frequently asked questions. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html#ec2-nitro-instances">Instances built on the Nitro System</a> in the <i>Amazon EC2 User Guide for Linux</i>, or <a href="https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/instance-types.html#ec2-nitro-instances">Instances built on the Nitro System</a> in the <i>Amazon EC2 User Guide for Windows</i>.</p> </li> <li> <p> <b> <code>NetworkInterface</code> </b> — The network interface of the recommended instance type is different than that of the current instance. For example, the recommended instance type supports enhanced networking and the current instance might not. To enable enhanced networking for the recommended instance type, you must install the Elastic Network Adapter (ENA) driver or the Intel 82599 Virtual Function driver. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html#instance-networking-storage">Networking and storage features</a> and <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enhanced-networking.html">Enhanced networking on Linux</a> in the <i>Amazon EC2 User Guide for Linux</i>, or <a href="https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/instance-types.html#instance-networking-storage">Networking and storage features</a> and <a href="https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/enhanced-networking.html">Enhanced networking on Windows</a> in the <i>Amazon EC2 User Guide for Windows</i>.</p> </li> <li> <p> <b> <code>StorageInterface</code> </b> — The storage interface of the recommended instance type is different than that of the current instance. For example, the recommended instance type uses an NVMe storage interface and the current instance does not. To access NVMe volumes for the recommended instance type, you will need to install or upgrade the NVMe driver. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html#instance-networking-storage">Networking and storage features</a> and <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/nvme-ebs-volumes.html">Amazon EBS and NVMe on Linux instances</a> in the <i>Amazon EC2 User Guide for Linux</i>, or <a href="https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/instance-types.html#instance-networking-storage">Networking and storage features</a> and <a href="https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/nvme-ebs-volumes.html">Amazon EBS and NVMe on Windows instances</a> in the <i>Amazon EC2 User Guide for Windows</i>.</p> </li> <li> <p> <b> <code>InstanceStoreAvailability</code> </b> — The recommended instance type does not support instance store volumes and the current instance does. Before migrating, you might need to back up the data on your instance store volumes if you want to preserve them. For more information, see <a href="https://aws.amazon.com/premiumsupport/knowledge-center/back-up-instance-store-ebs/">How do I back up an instance store volume on my Amazon EC2 instance to Amazon EBS?</a> in the <i>Amazon Web Services Premium Support Knowledge Base</i>. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html#instance-networking-storage">Networking and storage features</a> and <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html">Amazon EC2 instance store</a> in the <i>Amazon EC2 User Guide for Linux</i>, or see <a href="https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/instance-types.html#instance-networking-storage">Networking and storage features</a> and <a href="https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/InstanceStorage.html">Amazon EC2 instance store</a> in the <i>Amazon EC2 User Guide for Windows</i>.</p> </li> <li> <p> <b> <code>VirtualizationType</code> </b> — The recommended instance type uses the hardware virtual machine (HVM) virtualization type and the current instance uses the paravirtual (PV) virtualization type. For more information about the differences between these virtualization types, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/virtualization_types.html">Linux AMI virtualization types</a> in the <i>Amazon EC2 User Guide for Linux</i>, or <a href="https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/windows-ami-version-history.html#virtualization-types">Windows AMI virtualization types</a> in the <i>Amazon EC2 User Guide for Windows</i>.</p> </li> <li> <p> <b> <code>Architecture</code> </b> — The CPU architecture between the recommended instance type and the current instance is different. For example, the recommended instance type might use an Arm CPU architecture and the current instance type might use a different one, such as x86. Before migrating, you should consider recompiling the software on your instance for the new architecture. Alternatively, you might switch to an Amazon Machine Image (AMI) that supports the new architecture. For more information about the CPU architecture for each instance type, see <a href="http://aws.amazon.com/ec2/instance-types/">Amazon EC2 Instance Types</a>.</p> </li> </ul>"""
    performance_risk: "capo_compute_optimizer.types.performance_risk.PerformanceRisk"
    """<p>The performance risk of the instance recommendation option.</p> <p>Performance risk indicates the likelihood of the recommended instance type not meeting the resource needs of your workload. Compute Optimizer calculates an individual performance risk score for each specification of the recommended instance, including CPU, memory, EBS throughput, EBS IOPS, disk throughput, disk IOPS, network throughput, and network PPS. The performance risk of the recommended instance is calculated as the maximum performance risk score across the analyzed resource specifications.</p> <p>The value ranges from <code>0</code> - <code>4</code>, with <code>0</code> meaning that the recommended resource is predicted to always provide enough hardware capability. The higher the performance risk is, the more likely you should validate whether the recommendation will meet the performance requirements of your workload before migrating your resource.</p>"""
    rank: "capo_compute_optimizer.types.rank.Rank"
    """<p>The rank of the instance recommendation option.</p> <p>The top recommendation option is ranked as <code>1</code>.</p>"""
    savings_opportunity: NotRequired[
        "capo_compute_optimizer.types.savings_opportunity.SavingsOpportunity"
    ]
    """<p>An object that describes the savings opportunity for the instance recommendation option. Savings opportunity includes the estimated monthly savings amount and percentage.</p>"""
    savings_opportunity_after_discounts: NotRequired[
        "capo_compute_optimizer.types.instance_savings_opportunity_after_discounts.InstanceSavingsOpportunityAfterDiscounts"
    ]
    """<p> An object that describes the savings opportunity for the instance recommendation option that includes Savings Plans and Reserved Instances discounts. Savings opportunity includes the estimated monthly savings and percentage. </p>"""
    migration_effort: NotRequired[
        "capo_compute_optimizer.types.migration_effort.MigrationEffort"
    ]
    """<p>The level of effort required to migrate from the current instance type to the recommended instance type.</p> <p>For example, the migration effort is <code>Low</code> if Amazon EMR is the inferred workload type and an Amazon Web Services Graviton instance type is recommended. The migration effort is <code>Medium</code> if a workload type couldn't be inferred but an Amazon Web Services Graviton instance type is recommended. The migration effort is <code>VeryLow</code> if both the current and recommended instance types are of the same CPU architecture.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InstanceRecommendationOption) -> dict:
    out: dict = {}
    if "instance_type" in value:
        out["instanceType"] = value["instance_type"]
    if "instance_gpu_info" in value:
        import capo_compute_optimizer.types.gpu_info

        out["instanceGpuInfo"] = (
            capo_compute_optimizer.types.gpu_info.serialize_aws_json_1_0(
                value["instance_gpu_info"]
            )
        )
    if "projected_utilization_metrics" in value:
        import capo_compute_optimizer.types.projected_utilization_metrics

        out["projectedUtilizationMetrics"] = (
            capo_compute_optimizer.types.projected_utilization_metrics.serialize_aws_json_1_0(
                value["projected_utilization_metrics"]
            )
        )
    if "platform_differences" in value:
        import capo_compute_optimizer.types.platform_differences

        out["platformDifferences"] = (
            capo_compute_optimizer.types.platform_differences.serialize_aws_json_1_0(
                value["platform_differences"]
            )
        )
    out["performanceRisk"] = (
        "NaN"
        if value.get("performance_risk", 0) != value.get("performance_risk", 0)
        else "Infinity"
        if value.get("performance_risk", 0) == float("inf")
        else "-Infinity"
        if value.get("performance_risk", 0) == float("-inf")
        else value.get("performance_risk", 0)
    )
    out["rank"] = value.get("rank", 0)
    if "savings_opportunity" in value:
        import capo_compute_optimizer.types.savings_opportunity

        out["savingsOpportunity"] = (
            capo_compute_optimizer.types.savings_opportunity.serialize_aws_json_1_0(
                value["savings_opportunity"]
            )
        )
    if "savings_opportunity_after_discounts" in value:
        import capo_compute_optimizer.types.instance_savings_opportunity_after_discounts

        out["savingsOpportunityAfterDiscounts"] = (
            capo_compute_optimizer.types.instance_savings_opportunity_after_discounts.serialize_aws_json_1_0(
                value["savings_opportunity_after_discounts"]
            )
        )
    if "migration_effort" in value:
        import capo_compute_optimizer.types.migration_effort

        out["migrationEffort"] = (
            capo_compute_optimizer.types.migration_effort.serialize_aws_json_1_0(
                value["migration_effort"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> InstanceRecommendationOption:
    out: InstanceRecommendationOption = {}  # type: ignore[typeddict-item]
    if data.get("instanceType") is not None:
        out["instance_type"] = data["instanceType"]
    if data.get("instanceGpuInfo") is not None:
        import capo_compute_optimizer.types.gpu_info

        out["instance_gpu_info"] = (
            capo_compute_optimizer.types.gpu_info.deserialize_aws_json_1_0(
                data["instanceGpuInfo"]
            )
        )
    if data.get("projectedUtilizationMetrics") is not None:
        import capo_compute_optimizer.types.projected_utilization_metrics

        out["projected_utilization_metrics"] = (
            capo_compute_optimizer.types.projected_utilization_metrics.deserialize_aws_json_1_0(
                data["projectedUtilizationMetrics"]
            )
        )
    if data.get("platformDifferences") is not None:
        import capo_compute_optimizer.types.platform_differences

        out["platform_differences"] = (
            capo_compute_optimizer.types.platform_differences.deserialize_aws_json_1_0(
                data["platformDifferences"]
            )
        )
    if data.get("performanceRisk") is not None:
        out["performance_risk"] = float(data["performanceRisk"])
    else:
        out["performance_risk"] = 0
    if data.get("rank") is not None:
        out["rank"] = data["rank"]
    else:
        out["rank"] = 0
    if data.get("savingsOpportunity") is not None:
        import capo_compute_optimizer.types.savings_opportunity

        out["savings_opportunity"] = (
            capo_compute_optimizer.types.savings_opportunity.deserialize_aws_json_1_0(
                data["savingsOpportunity"]
            )
        )
    if data.get("savingsOpportunityAfterDiscounts") is not None:
        import capo_compute_optimizer.types.instance_savings_opportunity_after_discounts

        out["savings_opportunity_after_discounts"] = (
            capo_compute_optimizer.types.instance_savings_opportunity_after_discounts.deserialize_aws_json_1_0(
                data["savingsOpportunityAfterDiscounts"]
            )
        )
    if data.get("migrationEffort") is not None:
        import capo_compute_optimizer.types.migration_effort

        out["migration_effort"] = (
            capo_compute_optimizer.types.migration_effort.deserialize_aws_json_1_0(
                data["migrationEffort"]
            )
        )
    return out
