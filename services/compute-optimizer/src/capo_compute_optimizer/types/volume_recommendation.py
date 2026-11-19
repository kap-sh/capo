"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#VolumeRecommendation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.account_id
    import capo_compute_optimizer.types.current_performance_risk
    import capo_compute_optimizer.types.ebs_effective_recommendation_preferences
    import capo_compute_optimizer.types.ebs_finding
    import capo_compute_optimizer.types.ebs_utilization_metrics
    import capo_compute_optimizer.types.last_refresh_timestamp
    import capo_compute_optimizer.types.look_back_period_in_days
    import capo_compute_optimizer.types.tags
    import capo_compute_optimizer.types.volume_arn
    import capo_compute_optimizer.types.volume_configuration
    import capo_compute_optimizer.types.volume_recommendation_options


class VolumeRecommendation(TypedDict, closed=True):
    volume_arn: NotRequired["capo_compute_optimizer.types.volume_arn.VolumeArn"]
    """<p>The Amazon Resource Name (ARN) of the current volume.</p>"""
    account_id: NotRequired["capo_compute_optimizer.types.account_id.AccountId"]
    """<p>The Amazon Web Services account ID of the volume.</p>"""
    current_configuration: NotRequired[
        "capo_compute_optimizer.types.volume_configuration.VolumeConfiguration"
    ]
    """<p>An array of objects that describe the current configuration of the volume.</p>"""
    finding: NotRequired["capo_compute_optimizer.types.ebs_finding.EBSFinding"]
    """<p>The finding classification of the volume.</p> <p>Findings for volumes include:</p> <ul> <li> <p> <b> <code>NotOptimized</code> </b>—A volume is considered not optimized when Compute Optimizer identifies a recommendation that can provide better performance for your workload.</p> </li> <li> <p> <b> <code>Optimized</code> </b>—An volume is considered optimized when Compute Optimizer determines that the volume is correctly provisioned to run your workload based on the chosen volume type. For optimized resources, Compute Optimizer might recommend a new generation volume type.</p> </li> </ul>"""
    utilization_metrics: NotRequired[
        "capo_compute_optimizer.types.ebs_utilization_metrics.EBSUtilizationMetrics"
    ]
    """<p>An array of objects that describe the utilization metrics of the volume.</p>"""
    look_back_period_in_days: (
        "capo_compute_optimizer.types.look_back_period_in_days.LookBackPeriodInDays"
    )
    """<p>The number of days for which utilization metrics were analyzed for the volume.</p>"""
    volume_recommendation_options: NotRequired[
        "capo_compute_optimizer.types.volume_recommendation_options.VolumeRecommendationOptions"
    ]
    """<p>An array of objects that describe the recommendation options for the volume.</p>"""
    last_refresh_timestamp: NotRequired[
        "capo_compute_optimizer.types.last_refresh_timestamp.LastRefreshTimestamp"
    ]
    """<p>The timestamp of when the volume recommendation was last generated.</p>"""
    current_performance_risk: NotRequired[
        "capo_compute_optimizer.types.current_performance_risk.CurrentPerformanceRisk"
    ]
    """<p>The risk of the current EBS volume not meeting the performance needs of its workloads. The higher the risk, the more likely the current EBS volume doesn't have sufficient capacity.</p>"""
    effective_recommendation_preferences: NotRequired[
        "capo_compute_optimizer.types.ebs_effective_recommendation_preferences.EBSEffectiveRecommendationPreferences"
    ]
    """<p> Describes the effective recommendation preferences for Amazon EBS volume. </p>"""
    tags: NotRequired["capo_compute_optimizer.types.tags.Tags"]
    """<p> A list of tags assigned to your Amazon EBS volume recommendations. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VolumeRecommendation) -> dict:
    out: dict = {}
    if "volume_arn" in value:
        out["volumeArn"] = value["volume_arn"]
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "current_configuration" in value:
        import capo_compute_optimizer.types.volume_configuration

        out["currentConfiguration"] = (
            capo_compute_optimizer.types.volume_configuration.serialize_aws_json_1_0(
                value["current_configuration"]
            )
        )
    if "finding" in value:
        import capo_compute_optimizer.types.ebs_finding

        out["finding"] = (
            capo_compute_optimizer.types.ebs_finding.serialize_aws_json_1_0(
                value["finding"]
            )
        )
    if "utilization_metrics" in value:
        import capo_compute_optimizer.types.ebs_utilization_metrics

        out["utilizationMetrics"] = (
            capo_compute_optimizer.types.ebs_utilization_metrics.serialize_aws_json_1_0(
                value["utilization_metrics"]
            )
        )
    out["lookBackPeriodInDays"] = (
        "NaN"
        if value.get("look_back_period_in_days", 0)
        != value.get("look_back_period_in_days", 0)
        else "Infinity"
        if value.get("look_back_period_in_days", 0) == float("inf")
        else "-Infinity"
        if value.get("look_back_period_in_days", 0) == float("-inf")
        else value.get("look_back_period_in_days", 0)
    )
    if "volume_recommendation_options" in value:
        import capo_compute_optimizer.types.volume_recommendation_options

        out["volumeRecommendationOptions"] = (
            capo_compute_optimizer.types.volume_recommendation_options.serialize_aws_json_1_0(
                value["volume_recommendation_options"]
            )
        )
    if "last_refresh_timestamp" in value:
        import capo_compute_optimizer.types.last_refresh_timestamp

        out["lastRefreshTimestamp"] = (
            capo_compute_optimizer.types.last_refresh_timestamp.serialize_aws_json_1_0(
                value["last_refresh_timestamp"]
            )
        )
    if "current_performance_risk" in value:
        import capo_compute_optimizer.types.current_performance_risk

        out["currentPerformanceRisk"] = (
            capo_compute_optimizer.types.current_performance_risk.serialize_aws_json_1_0(
                value["current_performance_risk"]
            )
        )
    if "effective_recommendation_preferences" in value:
        import capo_compute_optimizer.types.ebs_effective_recommendation_preferences

        out["effectiveRecommendationPreferences"] = (
            capo_compute_optimizer.types.ebs_effective_recommendation_preferences.serialize_aws_json_1_0(
                value["effective_recommendation_preferences"]
            )
        )
    if "tags" in value:
        import capo_compute_optimizer.types.tags

        out["tags"] = capo_compute_optimizer.types.tags.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> VolumeRecommendation:
    out: VolumeRecommendation = {}  # type: ignore[typeddict-item]
    if data.get("volumeArn") is not None:
        out["volume_arn"] = data["volumeArn"]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    if data.get("currentConfiguration") is not None:
        import capo_compute_optimizer.types.volume_configuration

        out["current_configuration"] = (
            capo_compute_optimizer.types.volume_configuration.deserialize_aws_json_1_0(
                data["currentConfiguration"]
            )
        )
    if data.get("finding") is not None:
        import capo_compute_optimizer.types.ebs_finding

        out["finding"] = (
            capo_compute_optimizer.types.ebs_finding.deserialize_aws_json_1_0(
                data["finding"]
            )
        )
    if data.get("utilizationMetrics") is not None:
        import capo_compute_optimizer.types.ebs_utilization_metrics

        out["utilization_metrics"] = (
            capo_compute_optimizer.types.ebs_utilization_metrics.deserialize_aws_json_1_0(
                data["utilizationMetrics"]
            )
        )
    if data.get("lookBackPeriodInDays") is not None:
        out["look_back_period_in_days"] = float(data["lookBackPeriodInDays"])
    else:
        out["look_back_period_in_days"] = 0
    if data.get("volumeRecommendationOptions") is not None:
        import capo_compute_optimizer.types.volume_recommendation_options

        out["volume_recommendation_options"] = (
            capo_compute_optimizer.types.volume_recommendation_options.deserialize_aws_json_1_0(
                data["volumeRecommendationOptions"]
            )
        )
    if data.get("lastRefreshTimestamp") is not None:
        import capo_compute_optimizer.types.last_refresh_timestamp

        out["last_refresh_timestamp"] = (
            capo_compute_optimizer.types.last_refresh_timestamp.deserialize_aws_json_1_0(
                data["lastRefreshTimestamp"]
            )
        )
    if data.get("currentPerformanceRisk") is not None:
        import capo_compute_optimizer.types.current_performance_risk

        out["current_performance_risk"] = (
            capo_compute_optimizer.types.current_performance_risk.deserialize_aws_json_1_0(
                data["currentPerformanceRisk"]
            )
        )
    if data.get("effectiveRecommendationPreferences") is not None:
        import capo_compute_optimizer.types.ebs_effective_recommendation_preferences

        out["effective_recommendation_preferences"] = (
            capo_compute_optimizer.types.ebs_effective_recommendation_preferences.deserialize_aws_json_1_0(
                data["effectiveRecommendationPreferences"]
            )
        )
    if data.get("tags") is not None:
        import capo_compute_optimizer.types.tags

        out["tags"] = capo_compute_optimizer.types.tags.deserialize_aws_json_1_0(
            data["tags"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: VolumeRecommendation) -> dict:
    out: dict = {}
    if "volume_arn" in value:
        out["volumeArn"] = value["volume_arn"]
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "current_configuration" in value:
        import capo_compute_optimizer.types.volume_configuration

        out["currentConfiguration"] = (
            capo_compute_optimizer.types.volume_configuration.serialize_cbor(
                value["current_configuration"]
            )
        )
    if "finding" in value:
        import capo_compute_optimizer.types.ebs_finding

        out["finding"] = capo_compute_optimizer.types.ebs_finding.serialize_cbor(
            value["finding"]
        )
    if "utilization_metrics" in value:
        import capo_compute_optimizer.types.ebs_utilization_metrics

        out["utilizationMetrics"] = (
            capo_compute_optimizer.types.ebs_utilization_metrics.serialize_cbor(
                value["utilization_metrics"]
            )
        )
    out["lookBackPeriodInDays"] = value.get("look_back_period_in_days", 0)
    if "volume_recommendation_options" in value:
        import capo_compute_optimizer.types.volume_recommendation_options

        out["volumeRecommendationOptions"] = (
            capo_compute_optimizer.types.volume_recommendation_options.serialize_cbor(
                value["volume_recommendation_options"]
            )
        )
    if "last_refresh_timestamp" in value:
        import capo_compute_optimizer.types.last_refresh_timestamp

        out["lastRefreshTimestamp"] = (
            capo_compute_optimizer.types.last_refresh_timestamp.serialize_cbor(
                value["last_refresh_timestamp"]
            )
        )
    if "current_performance_risk" in value:
        import capo_compute_optimizer.types.current_performance_risk

        out["currentPerformanceRisk"] = (
            capo_compute_optimizer.types.current_performance_risk.serialize_cbor(
                value["current_performance_risk"]
            )
        )
    if "effective_recommendation_preferences" in value:
        import capo_compute_optimizer.types.ebs_effective_recommendation_preferences

        out["effectiveRecommendationPreferences"] = (
            capo_compute_optimizer.types.ebs_effective_recommendation_preferences.serialize_cbor(
                value["effective_recommendation_preferences"]
            )
        )
    if "tags" in value:
        import capo_compute_optimizer.types.tags

        out["tags"] = capo_compute_optimizer.types.tags.serialize_cbor(value["tags"])
    return out


def deserialize_cbor(data: dict) -> VolumeRecommendation:
    out: VolumeRecommendation = {}  # type: ignore[typeddict-item]
    if data.get("volumeArn") is not None:
        out["volume_arn"] = data["volumeArn"]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    if data.get("currentConfiguration") is not None:
        import capo_compute_optimizer.types.volume_configuration

        out["current_configuration"] = (
            capo_compute_optimizer.types.volume_configuration.deserialize_cbor(
                data["currentConfiguration"]
            )
        )
    if data.get("finding") is not None:
        import capo_compute_optimizer.types.ebs_finding

        out["finding"] = capo_compute_optimizer.types.ebs_finding.deserialize_cbor(
            data["finding"]
        )
    if data.get("utilizationMetrics") is not None:
        import capo_compute_optimizer.types.ebs_utilization_metrics

        out["utilization_metrics"] = (
            capo_compute_optimizer.types.ebs_utilization_metrics.deserialize_cbor(
                data["utilizationMetrics"]
            )
        )
    if data.get("lookBackPeriodInDays") is not None:
        out["look_back_period_in_days"] = float(data["lookBackPeriodInDays"])
    else:
        out["look_back_period_in_days"] = 0
    if data.get("volumeRecommendationOptions") is not None:
        import capo_compute_optimizer.types.volume_recommendation_options

        out["volume_recommendation_options"] = (
            capo_compute_optimizer.types.volume_recommendation_options.deserialize_cbor(
                data["volumeRecommendationOptions"]
            )
        )
    if data.get("lastRefreshTimestamp") is not None:
        import capo_compute_optimizer.types.last_refresh_timestamp

        out["last_refresh_timestamp"] = (
            capo_compute_optimizer.types.last_refresh_timestamp.deserialize_cbor(
                data["lastRefreshTimestamp"]
            )
        )
    if data.get("currentPerformanceRisk") is not None:
        import capo_compute_optimizer.types.current_performance_risk

        out["current_performance_risk"] = (
            capo_compute_optimizer.types.current_performance_risk.deserialize_cbor(
                data["currentPerformanceRisk"]
            )
        )
    if data.get("effectiveRecommendationPreferences") is not None:
        import capo_compute_optimizer.types.ebs_effective_recommendation_preferences

        out["effective_recommendation_preferences"] = (
            capo_compute_optimizer.types.ebs_effective_recommendation_preferences.deserialize_cbor(
                data["effectiveRecommendationPreferences"]
            )
        )
    if data.get("tags") is not None:
        import capo_compute_optimizer.types.tags

        out["tags"] = capo_compute_optimizer.types.tags.deserialize_cbor(data["tags"])
    return out
