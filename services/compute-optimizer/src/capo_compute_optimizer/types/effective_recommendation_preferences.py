"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#EffectiveRecommendationPreferences``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.cpu_vendor_architectures
    import capo_compute_optimizer.types.effective_preferred_resources
    import capo_compute_optimizer.types.enhanced_infrastructure_metrics
    import capo_compute_optimizer.types.external_metrics_preference
    import capo_compute_optimizer.types.inferred_workload_types_preference
    import capo_compute_optimizer.types.instance_savings_estimation_mode
    import capo_compute_optimizer.types.look_back_period_preference
    import capo_compute_optimizer.types.utilization_preferences


class EffectiveRecommendationPreferences(TypedDict, closed=True):
    cpu_vendor_architectures: NotRequired[
        "capo_compute_optimizer.types.cpu_vendor_architectures.CpuVendorArchitectures"
    ]
    """<p>Describes the CPU vendor and architecture for an instance or Auto Scaling group recommendations.</p> <p>For example, when you specify <code>AWS_ARM64</code> with:</p> <ul> <li> <p>A <a>GetEC2InstanceRecommendations</a> or <a>GetAutoScalingGroupRecommendations</a> request, Compute Optimizer returns recommendations that consist of Graviton instance types only.</p> </li> <li> <p>A <a>GetEC2RecommendationProjectedMetrics</a> request, Compute Optimizer returns projected utilization metrics for Graviton instance type recommendations only.</p> </li> <li> <p>A <a>ExportEC2InstanceRecommendations</a> or <a>ExportAutoScalingGroupRecommendations</a> request, Compute Optimizer exports recommendations that consist of Graviton instance types only.</p> </li> </ul>"""
    enhanced_infrastructure_metrics: NotRequired[
        "capo_compute_optimizer.types.enhanced_infrastructure_metrics.EnhancedInfrastructureMetrics"
    ]
    """<p>Describes the activation status of the enhanced infrastructure metrics preference.</p> <p>A status of <code>Active</code> confirms that the preference is applied in the latest recommendation refresh, and a status of <code>Inactive</code> confirms that it's not yet applied to recommendations.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/compute-optimizer/latest/ug/enhanced-infrastructure-metrics.html">Enhanced infrastructure metrics</a> in the <i>Compute Optimizer User Guide</i>.</p>"""
    inferred_workload_types: NotRequired[
        "capo_compute_optimizer.types.inferred_workload_types_preference.InferredWorkloadTypesPreference"
    ]
    """<p>Describes the activation status of the inferred workload types preference.</p> <p>A status of <code>Active</code> confirms that the preference is applied in the latest recommendation refresh. A status of <code>Inactive</code> confirms that it's not yet applied to recommendations.</p>"""
    external_metrics_preference: NotRequired[
        "capo_compute_optimizer.types.external_metrics_preference.ExternalMetricsPreference"
    ]
    """<p> An object that describes the external metrics recommendation preference. </p> <p> If the preference is applied in the latest recommendation refresh, an object with a valid <code>source</code> value appears in the response. If the preference isn't applied to the recommendations already, then this object doesn't appear in the response. </p>"""
    look_back_period: NotRequired[
        "capo_compute_optimizer.types.look_back_period_preference.LookBackPeriodPreference"
    ]
    """<p> The number of days the utilization metrics of the Amazon Web Services resource are analyzed. </p>"""
    utilization_preferences: NotRequired[
        "capo_compute_optimizer.types.utilization_preferences.UtilizationPreferences"
    ]
    """<p> The resource’s CPU and memory utilization preferences, such as threshold and headroom, that are used to generate rightsizing recommendations. </p> <note> <p>This preference is only available for the Amazon EC2 instance resource type.</p> </note>"""
    preferred_resources: NotRequired[
        "capo_compute_optimizer.types.effective_preferred_resources.EffectivePreferredResources"
    ]
    """<p> The resource type values that are considered as candidates when generating rightsizing recommendations. </p>"""
    savings_estimation_mode: NotRequired[
        "capo_compute_optimizer.types.instance_savings_estimation_mode.InstanceSavingsEstimationMode"
    ]
    """<p> Describes the savings estimation mode applied for calculating savings opportunity for a resource. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EffectiveRecommendationPreferences) -> dict:
    out: dict = {}
    if "cpu_vendor_architectures" in value:
        import capo_compute_optimizer.types.cpu_vendor_architectures

        out["cpuVendorArchitectures"] = (
            capo_compute_optimizer.types.cpu_vendor_architectures.serialize_aws_json_1_0(
                value["cpu_vendor_architectures"]
            )
        )
    if "enhanced_infrastructure_metrics" in value:
        import capo_compute_optimizer.types.enhanced_infrastructure_metrics

        out["enhancedInfrastructureMetrics"] = (
            capo_compute_optimizer.types.enhanced_infrastructure_metrics.serialize_aws_json_1_0(
                value["enhanced_infrastructure_metrics"]
            )
        )
    if "inferred_workload_types" in value:
        import capo_compute_optimizer.types.inferred_workload_types_preference

        out["inferredWorkloadTypes"] = (
            capo_compute_optimizer.types.inferred_workload_types_preference.serialize_aws_json_1_0(
                value["inferred_workload_types"]
            )
        )
    if "external_metrics_preference" in value:
        import capo_compute_optimizer.types.external_metrics_preference

        out["externalMetricsPreference"] = (
            capo_compute_optimizer.types.external_metrics_preference.serialize_aws_json_1_0(
                value["external_metrics_preference"]
            )
        )
    if "look_back_period" in value:
        import capo_compute_optimizer.types.look_back_period_preference

        out["lookBackPeriod"] = (
            capo_compute_optimizer.types.look_back_period_preference.serialize_aws_json_1_0(
                value["look_back_period"]
            )
        )
    if "utilization_preferences" in value:
        import capo_compute_optimizer.types.utilization_preferences

        out["utilizationPreferences"] = (
            capo_compute_optimizer.types.utilization_preferences.serialize_aws_json_1_0(
                value["utilization_preferences"]
            )
        )
    if "preferred_resources" in value:
        import capo_compute_optimizer.types.effective_preferred_resources

        out["preferredResources"] = (
            capo_compute_optimizer.types.effective_preferred_resources.serialize_aws_json_1_0(
                value["preferred_resources"]
            )
        )
    if "savings_estimation_mode" in value:
        import capo_compute_optimizer.types.instance_savings_estimation_mode

        out["savingsEstimationMode"] = (
            capo_compute_optimizer.types.instance_savings_estimation_mode.serialize_aws_json_1_0(
                value["savings_estimation_mode"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> EffectiveRecommendationPreferences:
    out: EffectiveRecommendationPreferences = {}  # type: ignore[typeddict-item]
    if data.get("cpuVendorArchitectures") is not None:
        import capo_compute_optimizer.types.cpu_vendor_architectures

        out["cpu_vendor_architectures"] = (
            capo_compute_optimizer.types.cpu_vendor_architectures.deserialize_aws_json_1_0(
                data["cpuVendorArchitectures"]
            )
        )
    if data.get("enhancedInfrastructureMetrics") is not None:
        import capo_compute_optimizer.types.enhanced_infrastructure_metrics

        out["enhanced_infrastructure_metrics"] = (
            capo_compute_optimizer.types.enhanced_infrastructure_metrics.deserialize_aws_json_1_0(
                data["enhancedInfrastructureMetrics"]
            )
        )
    if data.get("inferredWorkloadTypes") is not None:
        import capo_compute_optimizer.types.inferred_workload_types_preference

        out["inferred_workload_types"] = (
            capo_compute_optimizer.types.inferred_workload_types_preference.deserialize_aws_json_1_0(
                data["inferredWorkloadTypes"]
            )
        )
    if data.get("externalMetricsPreference") is not None:
        import capo_compute_optimizer.types.external_metrics_preference

        out["external_metrics_preference"] = (
            capo_compute_optimizer.types.external_metrics_preference.deserialize_aws_json_1_0(
                data["externalMetricsPreference"]
            )
        )
    if data.get("lookBackPeriod") is not None:
        import capo_compute_optimizer.types.look_back_period_preference

        out["look_back_period"] = (
            capo_compute_optimizer.types.look_back_period_preference.deserialize_aws_json_1_0(
                data["lookBackPeriod"]
            )
        )
    if data.get("utilizationPreferences") is not None:
        import capo_compute_optimizer.types.utilization_preferences

        out["utilization_preferences"] = (
            capo_compute_optimizer.types.utilization_preferences.deserialize_aws_json_1_0(
                data["utilizationPreferences"]
            )
        )
    if data.get("preferredResources") is not None:
        import capo_compute_optimizer.types.effective_preferred_resources

        out["preferred_resources"] = (
            capo_compute_optimizer.types.effective_preferred_resources.deserialize_aws_json_1_0(
                data["preferredResources"]
            )
        )
    if data.get("savingsEstimationMode") is not None:
        import capo_compute_optimizer.types.instance_savings_estimation_mode

        out["savings_estimation_mode"] = (
            capo_compute_optimizer.types.instance_savings_estimation_mode.deserialize_aws_json_1_0(
                data["savingsEstimationMode"]
            )
        )
    return out
