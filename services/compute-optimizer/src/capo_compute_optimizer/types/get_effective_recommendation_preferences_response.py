"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#GetEffectiveRecommendationPreferencesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.effective_preferred_resources
    import capo_compute_optimizer.types.enhanced_infrastructure_metrics
    import capo_compute_optimizer.types.external_metrics_preference
    import capo_compute_optimizer.types.look_back_period_preference
    import capo_compute_optimizer.types.utilization_preferences


class GetEffectiveRecommendationPreferencesResponse(TypedDict, closed=True):
    enhanced_infrastructure_metrics: NotRequired[
        "capo_compute_optimizer.types.enhanced_infrastructure_metrics.EnhancedInfrastructureMetrics"
    ]
    """<p>The status of the enhanced infrastructure metrics recommendation preference. Considers all applicable preferences that you might have set at the resource, account, and organization level.</p> <p>A status of <code>Active</code> confirms that the preference is applied in the latest recommendation refresh, and a status of <code>Inactive</code> confirms that it's not yet applied to recommendations.</p> <p>To validate whether the preference is applied to your last generated set of recommendations, review the <code>effectiveRecommendationPreferences</code> value in the response of the <a>GetAutoScalingGroupRecommendations</a> and <a>GetEC2InstanceRecommendations</a> actions.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/compute-optimizer/latest/ug/enhanced-infrastructure-metrics.html">Enhanced infrastructure metrics</a> in the <i>Compute Optimizer User Guide</i>.</p>"""
    external_metrics_preference: NotRequired[
        "capo_compute_optimizer.types.external_metrics_preference.ExternalMetricsPreference"
    ]
    """<p>The provider of the external metrics recommendation preference. Considers all applicable preferences that you might have set at the account and organization level.</p> <p>If the preference is applied in the latest recommendation refresh, an object with a valid <code>source</code> value appears in the response. If the preference isn't applied to the recommendations already, then this object doesn't appear in the response.</p> <p>To validate whether the preference is applied to your last generated set of recommendations, review the <code>effectiveRecommendationPreferences</code> value in the response of the <a>GetEC2InstanceRecommendations</a> actions.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/compute-optimizer/latest/ug/external-metrics-ingestion.html">Enhanced infrastructure metrics</a> in the <i>Compute Optimizer User Guide</i>.</p>"""
    look_back_period: NotRequired[
        "capo_compute_optimizer.types.look_back_period_preference.LookBackPeriodPreference"
    ]
    """<p> The number of days the utilization metrics of the Amazon Web Services resource are analyzed. </p> <p>To validate that the preference is applied to your last generated set of recommendations, review the <code>effectiveRecommendationPreferences</code> value in the response of the GetAutoScalingGroupRecommendations, GetEC2InstanceRecommendations, GetEBSVolumeRecommendations, GetECSServiceRecommendations, or GetRDSDatabaseRecommendations actions.</p>"""
    utilization_preferences: NotRequired[
        "capo_compute_optimizer.types.utilization_preferences.UtilizationPreferences"
    ]
    """<p> The resource’s CPU and memory utilization preferences, such as threshold and headroom, that were used to generate rightsizing recommendations. It considers all applicable preferences that you set at the resource, account, and organization level. </p> <p>To validate that the preference is applied to your last generated set of recommendations, review the <code>effectiveRecommendationPreferences</code> value in the response of the GetAutoScalingGroupRecommendations or GetEC2InstanceRecommendations actions.</p>"""
    preferred_resources: NotRequired[
        "capo_compute_optimizer.types.effective_preferred_resources.EffectivePreferredResources"
    ]
    """<p> The resource type values that are considered as candidates when generating rightsizing recommendations. This object resolves any wildcard expressions and returns the effective list of candidate resource type values. It also considers all applicable preferences that you set at the resource, account, and organization level. </p> <p>To validate that the preference is applied to your last generated set of recommendations, review the <code>effectiveRecommendationPreferences</code> value in the response of the GetAutoScalingGroupRecommendations or GetEC2InstanceRecommendations actions.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: GetEffectiveRecommendationPreferencesResponse,
) -> dict:
    out: dict = {}
    if "enhanced_infrastructure_metrics" in value:
        import capo_compute_optimizer.types.enhanced_infrastructure_metrics

        out["enhancedInfrastructureMetrics"] = (
            capo_compute_optimizer.types.enhanced_infrastructure_metrics.serialize_aws_json_1_0(
                value["enhanced_infrastructure_metrics"]
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
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> GetEffectiveRecommendationPreferencesResponse:
    out: GetEffectiveRecommendationPreferencesResponse = {}  # type: ignore[typeddict-item]
    if data.get("enhancedInfrastructureMetrics") is not None:
        import capo_compute_optimizer.types.enhanced_infrastructure_metrics

        out["enhanced_infrastructure_metrics"] = (
            capo_compute_optimizer.types.enhanced_infrastructure_metrics.deserialize_aws_json_1_0(
                data["enhancedInfrastructureMetrics"]
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
    return out
