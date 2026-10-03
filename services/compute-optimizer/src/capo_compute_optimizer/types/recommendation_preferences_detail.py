"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#RecommendationPreferencesDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.effective_preferred_resources
    import capo_compute_optimizer.types.enhanced_infrastructure_metrics
    import capo_compute_optimizer.types.external_metrics_preference
    import capo_compute_optimizer.types.inferred_workload_types_preference
    import capo_compute_optimizer.types.look_back_period_preference
    import capo_compute_optimizer.types.resource_type
    import capo_compute_optimizer.types.savings_estimation_mode
    import capo_compute_optimizer.types.scope
    import capo_compute_optimizer.types.utilization_preferences


class RecommendationPreferencesDetail(TypedDict, closed=True):
    scope: NotRequired["capo_compute_optimizer.types.scope.Scope"]
    """<p>An object that describes the scope of the recommendation preference.</p> <p>Recommendation preferences can be created at the organization level (for management accounts of an organization only), account level, and resource level. For more information, see <a href="https://docs.aws.amazon.com/compute-optimizer/latest/ug/enhanced-infrastructure-metrics.html">Activating enhanced infrastructure metrics</a> in the <i>Compute Optimizer User Guide</i>.</p>"""
    resource_type: NotRequired[
        "capo_compute_optimizer.types.resource_type.ResourceType"
    ]
    """<p>The target resource type of the recommendation preference to create.</p> <p>The <code>Ec2Instance</code> option encompasses standalone instances and instances that are part of Auto Scaling groups. The <code>AutoScalingGroup</code> option encompasses only instances that are part of an Auto Scaling group.</p>"""
    enhanced_infrastructure_metrics: NotRequired[
        "capo_compute_optimizer.types.enhanced_infrastructure_metrics.EnhancedInfrastructureMetrics"
    ]
    """<p>The status of the enhanced infrastructure metrics recommendation preference.</p> <p>When the recommendations page is refreshed, a status of <code>Active</code> confirms that the preference is applied to the recommendations, and a status of <code>Inactive</code> confirms that the preference isn't yet applied to recommendations.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/compute-optimizer/latest/ug/enhanced-infrastructure-metrics.html">Enhanced infrastructure metrics</a> in the <i>Compute Optimizer User Guide</i>.</p>"""
    inferred_workload_types: NotRequired[
        "capo_compute_optimizer.types.inferred_workload_types_preference.InferredWorkloadTypesPreference"
    ]
    """<p>The status of the inferred workload types recommendation preference.</p> <p>When the recommendations page is refreshed, a status of <code>Active</code> confirms that the preference is applied to the recommendations, and a status of <code>Inactive</code> confirms that the preference isn't yet applied to recommendations.</p>"""
    external_metrics_preference: NotRequired[
        "capo_compute_optimizer.types.external_metrics_preference.ExternalMetricsPreference"
    ]
    """<p> An object that describes the external metrics recommendation preference. </p> <p> If the preference is applied in the latest recommendation refresh, an object with a valid <code>source</code> value appears in the response. If the preference isn't applied to the recommendations already, then this object doesn't appear in the response. </p>"""
    look_back_period: NotRequired[
        "capo_compute_optimizer.types.look_back_period_preference.LookBackPeriodPreference"
    ]
    """<p> The preference to control the number of days the utilization metrics of the Amazon Web Services resource are analyzed. If the preference isn’t set, this object is null. </p>"""
    utilization_preferences: NotRequired[
        "capo_compute_optimizer.types.utilization_preferences.UtilizationPreferences"
    ]
    """<p> The preference to control the resource’s CPU utilization threshold, CPU utilization headroom, and memory utilization headroom. If the preference isn’t set, this object is null. </p> <note> <p>This preference is only available for the Amazon EC2 instance resource type.</p> </note>"""
    preferred_resources: NotRequired[
        "capo_compute_optimizer.types.effective_preferred_resources.EffectivePreferredResources"
    ]
    """<p> The preference to control which resource type values are considered when generating rightsizing recommendations. This object resolves any wildcard expressions and returns the effective list of candidate resource type values. If the preference isn’t set, this object is null. </p>"""
    savings_estimation_mode: NotRequired[
        "capo_compute_optimizer.types.savings_estimation_mode.SavingsEstimationMode"
    ]
    """<p> Describes the savings estimation mode used for calculating savings opportunity. </p> <p>Only the account manager or delegated administrator of your organization can activate this preference.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RecommendationPreferencesDetail) -> dict:
    out: dict = {}
    if "scope" in value:
        import capo_compute_optimizer.types.scope

        out["scope"] = capo_compute_optimizer.types.scope.serialize_aws_json_1_0(
            value["scope"]
        )
    if "resource_type" in value:
        import capo_compute_optimizer.types.resource_type

        out["resourceType"] = (
            capo_compute_optimizer.types.resource_type.serialize_aws_json_1_0(
                value["resource_type"]
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
        import capo_compute_optimizer.types.savings_estimation_mode

        out["savingsEstimationMode"] = (
            capo_compute_optimizer.types.savings_estimation_mode.serialize_aws_json_1_0(
                value["savings_estimation_mode"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> RecommendationPreferencesDetail:
    out: RecommendationPreferencesDetail = {}  # type: ignore[typeddict-item]
    if data.get("scope") is not None:
        import capo_compute_optimizer.types.scope

        out["scope"] = capo_compute_optimizer.types.scope.deserialize_aws_json_1_0(
            data["scope"]
        )
    if data.get("resourceType") is not None:
        import capo_compute_optimizer.types.resource_type

        out["resource_type"] = (
            capo_compute_optimizer.types.resource_type.deserialize_aws_json_1_0(
                data["resourceType"]
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
        import capo_compute_optimizer.types.savings_estimation_mode

        out["savings_estimation_mode"] = (
            capo_compute_optimizer.types.savings_estimation_mode.deserialize_aws_json_1_0(
                data["savingsEstimationMode"]
            )
        )
    return out
