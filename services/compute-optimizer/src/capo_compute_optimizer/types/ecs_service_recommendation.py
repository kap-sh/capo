"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ECSServiceRecommendation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.account_id
    import capo_compute_optimizer.types.current_performance_risk
    import capo_compute_optimizer.types.ecs_effective_recommendation_preferences
    import capo_compute_optimizer.types.ecs_service_launch_type
    import capo_compute_optimizer.types.ecs_service_recommendation_finding
    import capo_compute_optimizer.types.ecs_service_recommendation_finding_reason_codes
    import capo_compute_optimizer.types.ecs_service_recommendation_options
    import capo_compute_optimizer.types.ecs_service_utilization_metrics
    import capo_compute_optimizer.types.last_refresh_timestamp
    import capo_compute_optimizer.types.look_back_period_in_days
    import capo_compute_optimizer.types.service_arn
    import capo_compute_optimizer.types.service_configuration
    import capo_compute_optimizer.types.tags


class ECSServiceRecommendation(TypedDict, closed=True):
    service_arn: NotRequired["capo_compute_optimizer.types.service_arn.ServiceArn"]
    """<p> The Amazon Resource Name (ARN) of the current Amazon ECS service. </p> <p> The following is the format of the ARN: </p> <p> <code>arn:aws:ecs:region:aws_account_id:service/cluster-name/service-name</code> </p>"""
    account_id: NotRequired["capo_compute_optimizer.types.account_id.AccountId"]
    """<p> The Amazon Web Services account ID of the Amazon ECS service. </p>"""
    current_service_configuration: NotRequired[
        "capo_compute_optimizer.types.service_configuration.ServiceConfiguration"
    ]
    """<p> The configuration of the current Amazon ECS service. </p>"""
    utilization_metrics: NotRequired[
        "capo_compute_optimizer.types.ecs_service_utilization_metrics.ECSServiceUtilizationMetrics"
    ]
    """<p> An array of objects that describe the utilization metrics of the Amazon ECS service. </p>"""
    lookback_period_in_days: (
        "capo_compute_optimizer.types.look_back_period_in_days.LookBackPeriodInDays"
    )
    """<p> The number of days the Amazon ECS service utilization metrics were analyzed. </p>"""
    launch_type: NotRequired[
        "capo_compute_optimizer.types.ecs_service_launch_type.ECSServiceLaunchType"
    ]
    """<p> The launch type the Amazon ECS service is using. </p> <note> <p>Compute Optimizer only supports the Fargate launch type.</p> </note>"""
    last_refresh_timestamp: NotRequired[
        "capo_compute_optimizer.types.last_refresh_timestamp.LastRefreshTimestamp"
    ]
    """<p> The timestamp of when the Amazon ECS service recommendation was last generated. </p>"""
    finding: NotRequired[
        "capo_compute_optimizer.types.ecs_service_recommendation_finding.ECSServiceRecommendationFinding"
    ]
    """<p> The finding classification of an Amazon ECS service. </p> <p>Findings for Amazon ECS services include:</p> <ul> <li> <p> <b> <code>Underprovisioned</code> </b> — When Compute Optimizer detects that there’s not enough memory or CPU, an Amazon ECS service is considered under-provisioned. An under-provisioned service might result in poor application performance.</p> </li> <li> <p> <b> <code>Overprovisioned</code> </b> — When Compute Optimizer detects that there’s excessive memory or CPU, an Amazon ECS service is considered over-provisioned. An over-provisioned service might result in additional infrastructure costs. </p> </li> <li> <p> <b> <code>Optimized</code> </b> — When both the CPU and memory of your Amazon ECS service meet the performance requirements of your workload, the service is considered optimized.</p> </li> </ul>"""
    finding_reason_codes: NotRequired[
        "capo_compute_optimizer.types.ecs_service_recommendation_finding_reason_codes.ECSServiceRecommendationFindingReasonCodes"
    ]
    """<p> The reason for the finding classification of an Amazon ECS service. </p> <p>Finding reason codes for Amazon ECS services include:</p> <ul> <li> <p> <b> <code>CPUUnderprovisioned</code> </b> — The service CPU configuration can be sized up to enhance the performance of your workload. This is identified by analyzing the <code>CPUUtilization</code> metric of the current service during the look-back period.</p> </li> <li> <p> <b> <code>CPUOverprovisioned</code> </b> — The service CPU configuration can be sized down while still meeting the performance requirements of your workload. This is identified by analyzing the <code>CPUUtilization</code> metric of the current service during the look-back period. </p> </li> <li> <p> <b> <code>MemoryUnderprovisioned</code> </b> — The service memory configuration can be sized up to enhance the performance of your workload. This is identified by analyzing the <code>MemoryUtilization</code> metric of the current service during the look-back period.</p> </li> <li> <p> <b> <code>MemoryOverprovisioned</code> </b> — The service memory configuration can be sized down while still meeting the performance requirements of your workload. This is identified by analyzing the <code>MemoryUtilization</code> metric of the current service during the look-back period.</p> </li> </ul>"""
    service_recommendation_options: NotRequired[
        "capo_compute_optimizer.types.ecs_service_recommendation_options.ECSServiceRecommendationOptions"
    ]
    """<p> An array of objects that describe the recommendation options for the Amazon ECS service. </p>"""
    current_performance_risk: NotRequired[
        "capo_compute_optimizer.types.current_performance_risk.CurrentPerformanceRisk"
    ]
    """<p> The risk of the current Amazon ECS service not meeting the performance needs of its workloads. The higher the risk, the more likely the current service can't meet the performance requirements of its workload. </p>"""
    effective_recommendation_preferences: NotRequired[
        "capo_compute_optimizer.types.ecs_effective_recommendation_preferences.ECSEffectiveRecommendationPreferences"
    ]
    """<p> Describes the effective recommendation preferences for Amazon ECS services. </p>"""
    tags: NotRequired["capo_compute_optimizer.types.tags.Tags"]
    """<p> A list of tags assigned to your Amazon ECS service recommendations. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ECSServiceRecommendation) -> dict:
    out: dict = {}
    if "service_arn" in value:
        out["serviceArn"] = value["service_arn"]
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "current_service_configuration" in value:
        import capo_compute_optimizer.types.service_configuration

        out["currentServiceConfiguration"] = (
            capo_compute_optimizer.types.service_configuration.serialize_aws_json_1_0(
                value["current_service_configuration"]
            )
        )
    if "utilization_metrics" in value:
        import capo_compute_optimizer.types.ecs_service_utilization_metrics

        out["utilizationMetrics"] = (
            capo_compute_optimizer.types.ecs_service_utilization_metrics.serialize_aws_json_1_0(
                value["utilization_metrics"]
            )
        )
    out["lookbackPeriodInDays"] = (
        "NaN"
        if value.get("lookback_period_in_days", 0)
        != value.get("lookback_period_in_days", 0)
        else "Infinity"
        if value.get("lookback_period_in_days", 0) == float("inf")
        else "-Infinity"
        if value.get("lookback_period_in_days", 0) == float("-inf")
        else value.get("lookback_period_in_days", 0)
    )
    if "launch_type" in value:
        import capo_compute_optimizer.types.ecs_service_launch_type

        out["launchType"] = (
            capo_compute_optimizer.types.ecs_service_launch_type.serialize_aws_json_1_0(
                value["launch_type"]
            )
        )
    if "last_refresh_timestamp" in value:
        import capo_compute_optimizer.types.last_refresh_timestamp

        out["lastRefreshTimestamp"] = (
            capo_compute_optimizer.types.last_refresh_timestamp.serialize_aws_json_1_0(
                value["last_refresh_timestamp"]
            )
        )
    if "finding" in value:
        import capo_compute_optimizer.types.ecs_service_recommendation_finding

        out["finding"] = (
            capo_compute_optimizer.types.ecs_service_recommendation_finding.serialize_aws_json_1_0(
                value["finding"]
            )
        )
    if "finding_reason_codes" in value:
        import capo_compute_optimizer.types.ecs_service_recommendation_finding_reason_codes

        out["findingReasonCodes"] = (
            capo_compute_optimizer.types.ecs_service_recommendation_finding_reason_codes.serialize_aws_json_1_0(
                value["finding_reason_codes"]
            )
        )
    if "service_recommendation_options" in value:
        import capo_compute_optimizer.types.ecs_service_recommendation_options

        out["serviceRecommendationOptions"] = (
            capo_compute_optimizer.types.ecs_service_recommendation_options.serialize_aws_json_1_0(
                value["service_recommendation_options"]
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
        import capo_compute_optimizer.types.ecs_effective_recommendation_preferences

        out["effectiveRecommendationPreferences"] = (
            capo_compute_optimizer.types.ecs_effective_recommendation_preferences.serialize_aws_json_1_0(
                value["effective_recommendation_preferences"]
            )
        )
    if "tags" in value:
        import capo_compute_optimizer.types.tags

        out["tags"] = capo_compute_optimizer.types.tags.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ECSServiceRecommendation:
    out: ECSServiceRecommendation = {}  # type: ignore[typeddict-item]
    if data.get("serviceArn") is not None:
        out["service_arn"] = data["serviceArn"]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    if data.get("currentServiceConfiguration") is not None:
        import capo_compute_optimizer.types.service_configuration

        out["current_service_configuration"] = (
            capo_compute_optimizer.types.service_configuration.deserialize_aws_json_1_0(
                data["currentServiceConfiguration"]
            )
        )
    if data.get("utilizationMetrics") is not None:
        import capo_compute_optimizer.types.ecs_service_utilization_metrics

        out["utilization_metrics"] = (
            capo_compute_optimizer.types.ecs_service_utilization_metrics.deserialize_aws_json_1_0(
                data["utilizationMetrics"]
            )
        )
    if data.get("lookbackPeriodInDays") is not None:
        out["lookback_period_in_days"] = float(data["lookbackPeriodInDays"])
    else:
        out["lookback_period_in_days"] = 0
    if data.get("launchType") is not None:
        import capo_compute_optimizer.types.ecs_service_launch_type

        out["launch_type"] = (
            capo_compute_optimizer.types.ecs_service_launch_type.deserialize_aws_json_1_0(
                data["launchType"]
            )
        )
    if data.get("lastRefreshTimestamp") is not None:
        import capo_compute_optimizer.types.last_refresh_timestamp

        out["last_refresh_timestamp"] = (
            capo_compute_optimizer.types.last_refresh_timestamp.deserialize_aws_json_1_0(
                data["lastRefreshTimestamp"]
            )
        )
    if data.get("finding") is not None:
        import capo_compute_optimizer.types.ecs_service_recommendation_finding

        out["finding"] = (
            capo_compute_optimizer.types.ecs_service_recommendation_finding.deserialize_aws_json_1_0(
                data["finding"]
            )
        )
    if data.get("findingReasonCodes") is not None:
        import capo_compute_optimizer.types.ecs_service_recommendation_finding_reason_codes

        out["finding_reason_codes"] = (
            capo_compute_optimizer.types.ecs_service_recommendation_finding_reason_codes.deserialize_aws_json_1_0(
                data["findingReasonCodes"]
            )
        )
    if data.get("serviceRecommendationOptions") is not None:
        import capo_compute_optimizer.types.ecs_service_recommendation_options

        out["service_recommendation_options"] = (
            capo_compute_optimizer.types.ecs_service_recommendation_options.deserialize_aws_json_1_0(
                data["serviceRecommendationOptions"]
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
        import capo_compute_optimizer.types.ecs_effective_recommendation_preferences

        out["effective_recommendation_preferences"] = (
            capo_compute_optimizer.types.ecs_effective_recommendation_preferences.deserialize_aws_json_1_0(
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
def serialize_cbor(value: ECSServiceRecommendation) -> dict:
    out: dict = {}
    if "service_arn" in value:
        out["serviceArn"] = value["service_arn"]
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "current_service_configuration" in value:
        import capo_compute_optimizer.types.service_configuration

        out["currentServiceConfiguration"] = (
            capo_compute_optimizer.types.service_configuration.serialize_cbor(
                value["current_service_configuration"]
            )
        )
    if "utilization_metrics" in value:
        import capo_compute_optimizer.types.ecs_service_utilization_metrics

        out["utilizationMetrics"] = (
            capo_compute_optimizer.types.ecs_service_utilization_metrics.serialize_cbor(
                value["utilization_metrics"]
            )
        )
    out["lookbackPeriodInDays"] = value.get("lookback_period_in_days", 0)
    if "launch_type" in value:
        import capo_compute_optimizer.types.ecs_service_launch_type

        out["launchType"] = (
            capo_compute_optimizer.types.ecs_service_launch_type.serialize_cbor(
                value["launch_type"]
            )
        )
    if "last_refresh_timestamp" in value:
        import capo_compute_optimizer.types.last_refresh_timestamp

        out["lastRefreshTimestamp"] = (
            capo_compute_optimizer.types.last_refresh_timestamp.serialize_cbor(
                value["last_refresh_timestamp"]
            )
        )
    if "finding" in value:
        import capo_compute_optimizer.types.ecs_service_recommendation_finding

        out["finding"] = (
            capo_compute_optimizer.types.ecs_service_recommendation_finding.serialize_cbor(
                value["finding"]
            )
        )
    if "finding_reason_codes" in value:
        import capo_compute_optimizer.types.ecs_service_recommendation_finding_reason_codes

        out["findingReasonCodes"] = (
            capo_compute_optimizer.types.ecs_service_recommendation_finding_reason_codes.serialize_cbor(
                value["finding_reason_codes"]
            )
        )
    if "service_recommendation_options" in value:
        import capo_compute_optimizer.types.ecs_service_recommendation_options

        out["serviceRecommendationOptions"] = (
            capo_compute_optimizer.types.ecs_service_recommendation_options.serialize_cbor(
                value["service_recommendation_options"]
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
        import capo_compute_optimizer.types.ecs_effective_recommendation_preferences

        out["effectiveRecommendationPreferences"] = (
            capo_compute_optimizer.types.ecs_effective_recommendation_preferences.serialize_cbor(
                value["effective_recommendation_preferences"]
            )
        )
    if "tags" in value:
        import capo_compute_optimizer.types.tags

        out["tags"] = capo_compute_optimizer.types.tags.serialize_cbor(value["tags"])
    return out


def deserialize_cbor(data: dict) -> ECSServiceRecommendation:
    out: ECSServiceRecommendation = {}  # type: ignore[typeddict-item]
    if data.get("serviceArn") is not None:
        out["service_arn"] = data["serviceArn"]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    if data.get("currentServiceConfiguration") is not None:
        import capo_compute_optimizer.types.service_configuration

        out["current_service_configuration"] = (
            capo_compute_optimizer.types.service_configuration.deserialize_cbor(
                data["currentServiceConfiguration"]
            )
        )
    if data.get("utilizationMetrics") is not None:
        import capo_compute_optimizer.types.ecs_service_utilization_metrics

        out["utilization_metrics"] = (
            capo_compute_optimizer.types.ecs_service_utilization_metrics.deserialize_cbor(
                data["utilizationMetrics"]
            )
        )
    if data.get("lookbackPeriodInDays") is not None:
        out["lookback_period_in_days"] = float(data["lookbackPeriodInDays"])
    else:
        out["lookback_period_in_days"] = 0
    if data.get("launchType") is not None:
        import capo_compute_optimizer.types.ecs_service_launch_type

        out["launch_type"] = (
            capo_compute_optimizer.types.ecs_service_launch_type.deserialize_cbor(
                data["launchType"]
            )
        )
    if data.get("lastRefreshTimestamp") is not None:
        import capo_compute_optimizer.types.last_refresh_timestamp

        out["last_refresh_timestamp"] = (
            capo_compute_optimizer.types.last_refresh_timestamp.deserialize_cbor(
                data["lastRefreshTimestamp"]
            )
        )
    if data.get("finding") is not None:
        import capo_compute_optimizer.types.ecs_service_recommendation_finding

        out["finding"] = (
            capo_compute_optimizer.types.ecs_service_recommendation_finding.deserialize_cbor(
                data["finding"]
            )
        )
    if data.get("findingReasonCodes") is not None:
        import capo_compute_optimizer.types.ecs_service_recommendation_finding_reason_codes

        out["finding_reason_codes"] = (
            capo_compute_optimizer.types.ecs_service_recommendation_finding_reason_codes.deserialize_cbor(
                data["findingReasonCodes"]
            )
        )
    if data.get("serviceRecommendationOptions") is not None:
        import capo_compute_optimizer.types.ecs_service_recommendation_options

        out["service_recommendation_options"] = (
            capo_compute_optimizer.types.ecs_service_recommendation_options.deserialize_cbor(
                data["serviceRecommendationOptions"]
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
        import capo_compute_optimizer.types.ecs_effective_recommendation_preferences

        out["effective_recommendation_preferences"] = (
            capo_compute_optimizer.types.ecs_effective_recommendation_preferences.deserialize_cbor(
                data["effectiveRecommendationPreferences"]
            )
        )
    if data.get("tags") is not None:
        import capo_compute_optimizer.types.tags

        out["tags"] = capo_compute_optimizer.types.tags.deserialize_cbor(data["tags"])
    return out
