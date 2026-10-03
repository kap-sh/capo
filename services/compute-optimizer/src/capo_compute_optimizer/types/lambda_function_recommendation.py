"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#LambdaFunctionRecommendation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.account_id
    import capo_compute_optimizer.types.current_performance_risk
    import capo_compute_optimizer.types.function_arn
    import capo_compute_optimizer.types.function_version
    import capo_compute_optimizer.types.lambda_effective_recommendation_preferences
    import capo_compute_optimizer.types.lambda_function_memory_recommendation_options
    import capo_compute_optimizer.types.lambda_function_recommendation_finding
    import capo_compute_optimizer.types.lambda_function_recommendation_finding_reason_codes
    import capo_compute_optimizer.types.lambda_function_utilization_metrics
    import capo_compute_optimizer.types.last_refresh_timestamp
    import capo_compute_optimizer.types.look_back_period_in_days
    import capo_compute_optimizer.types.memory_size
    import capo_compute_optimizer.types.number_of_invocations
    import capo_compute_optimizer.types.tags


class LambdaFunctionRecommendation(TypedDict, closed=True):
    function_arn: NotRequired["capo_compute_optimizer.types.function_arn.FunctionArn"]
    """<p>The Amazon Resource Name (ARN) of the current function.</p>"""
    function_version: NotRequired[
        "capo_compute_optimizer.types.function_version.FunctionVersion"
    ]
    """<p>The version number of the current function.</p>"""
    account_id: NotRequired["capo_compute_optimizer.types.account_id.AccountId"]
    """<p>The Amazon Web Services account ID of the function.</p>"""
    current_memory_size: "capo_compute_optimizer.types.memory_size.MemorySize"
    """<p>The amount of memory, in MB, that's allocated to the current function.</p>"""
    number_of_invocations: (
        "capo_compute_optimizer.types.number_of_invocations.NumberOfInvocations"
    )
    """<p>The number of times your function code was applied during the look-back period.</p>"""
    utilization_metrics: NotRequired[
        "capo_compute_optimizer.types.lambda_function_utilization_metrics.LambdaFunctionUtilizationMetrics"
    ]
    """<p>An array of objects that describe the utilization metrics of the function.</p>"""
    lookback_period_in_days: (
        "capo_compute_optimizer.types.look_back_period_in_days.LookBackPeriodInDays"
    )
    """<p>The number of days for which utilization metrics were analyzed for the function.</p>"""
    last_refresh_timestamp: NotRequired[
        "capo_compute_optimizer.types.last_refresh_timestamp.LastRefreshTimestamp"
    ]
    """<p>The timestamp of when the function recommendation was last generated.</p>"""
    finding: NotRequired[
        "capo_compute_optimizer.types.lambda_function_recommendation_finding.LambdaFunctionRecommendationFinding"
    ]
    """<p>The finding classification of the function.</p> <p>Findings for functions include:</p> <ul> <li> <p> <b> <code>Optimized</code> </b> — The function is correctly provisioned to run your workload based on its current configuration and its utilization history. This finding classification does not include finding reason codes.</p> </li> <li> <p> <b> <code>NotOptimized</code> </b> — The function is performing at a higher level (over-provisioned) or at a lower level (under-provisioned) than required for your workload because its current configuration is not optimal. Over-provisioned resources might lead to unnecessary infrastructure cost, and under-provisioned resources might lead to poor application performance. This finding classification can include the <code>MemoryUnderprovisioned</code> and <code>MemoryUnderprovisioned</code> finding reason codes.</p> </li> <li> <p> <b> <code>Unavailable</code> </b> — Compute Optimizer was unable to generate a recommendation for the function. This could be because the function has not accumulated sufficient metric data, or the function does not qualify for a recommendation. This finding classification can include the <code>InsufficientData</code> and <code>Inconclusive</code> finding reason codes.</p> <note> <p>Functions with a finding of unavailable are not returned unless you specify the <code>filter</code> parameter with a value of <code>Unavailable</code> in your <code>GetLambdaFunctionRecommendations</code> request.</p> </note> </li> </ul>"""
    finding_reason_codes: NotRequired[
        "capo_compute_optimizer.types.lambda_function_recommendation_finding_reason_codes.LambdaFunctionRecommendationFindingReasonCodes"
    ]
    """<p>The reason for the finding classification of the function.</p> <note> <p>Functions that have a finding classification of <code>Optimized</code> don't have a finding reason code.</p> </note> <p>Finding reason codes for functions include:</p> <ul> <li> <p> <b> <code>MemoryOverprovisioned</code> </b> — The function is over-provisioned when its memory configuration can be sized down while still meeting the performance requirements of your workload. An over-provisioned function might lead to unnecessary infrastructure cost. This finding reason code is part of the <code>NotOptimized</code> finding classification.</p> </li> <li> <p> <b> <code>MemoryUnderprovisioned</code> </b> — The function is under-provisioned when its memory configuration doesn't meet the performance requirements of the workload. An under-provisioned function might lead to poor application performance. This finding reason code is part of the <code>NotOptimized</code> finding classification.</p> </li> <li> <p> <b> <code>InsufficientData</code> </b> — The function does not have sufficient metric data for Compute Optimizer to generate a recommendation. For more information, see the <a href="https://docs.aws.amazon.com/compute-optimizer/latest/ug/requirements.html">Supported resources and requirements</a> in the <i>Compute Optimizer User Guide</i>. This finding reason code is part of the <code>Unavailable</code> finding classification.</p> </li> <li> <p> <b> <code>Inconclusive</code> </b> — The function does not qualify for a recommendation because Compute Optimizer cannot generate a recommendation with a high degree of confidence. This finding reason code is part of the <code>Unavailable</code> finding classification.</p> </li> </ul>"""
    memory_size_recommendation_options: NotRequired[
        "capo_compute_optimizer.types.lambda_function_memory_recommendation_options.LambdaFunctionMemoryRecommendationOptions"
    ]
    """<p>An array of objects that describe the memory configuration recommendation options for the function.</p>"""
    current_performance_risk: NotRequired[
        "capo_compute_optimizer.types.current_performance_risk.CurrentPerformanceRisk"
    ]
    """<p>The risk of the current Lambda function not meeting the performance needs of its workloads. The higher the risk, the more likely the current Lambda function requires more memory.</p>"""
    effective_recommendation_preferences: NotRequired[
        "capo_compute_optimizer.types.lambda_effective_recommendation_preferences.LambdaEffectiveRecommendationPreferences"
    ]
    """<p> Describes the effective recommendation preferences for Lambda functions. </p>"""
    tags: NotRequired["capo_compute_optimizer.types.tags.Tags"]
    """<p> A list of tags assigned to your Lambda function recommendations. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LambdaFunctionRecommendation) -> dict:
    out: dict = {}
    if "function_arn" in value:
        out["functionArn"] = value["function_arn"]
    if "function_version" in value:
        out["functionVersion"] = value["function_version"]
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    out["currentMemorySize"] = value.get("current_memory_size", 0)
    out["numberOfInvocations"] = value.get("number_of_invocations", 0)
    if "utilization_metrics" in value:
        import capo_compute_optimizer.types.lambda_function_utilization_metrics

        out["utilizationMetrics"] = (
            capo_compute_optimizer.types.lambda_function_utilization_metrics.serialize_aws_json_1_0(
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
    if "last_refresh_timestamp" in value:
        import capo_compute_optimizer.types.last_refresh_timestamp

        out["lastRefreshTimestamp"] = (
            capo_compute_optimizer.types.last_refresh_timestamp.serialize_aws_json_1_0(
                value["last_refresh_timestamp"]
            )
        )
    if "finding" in value:
        import capo_compute_optimizer.types.lambda_function_recommendation_finding

        out["finding"] = (
            capo_compute_optimizer.types.lambda_function_recommendation_finding.serialize_aws_json_1_0(
                value["finding"]
            )
        )
    if "finding_reason_codes" in value:
        import capo_compute_optimizer.types.lambda_function_recommendation_finding_reason_codes

        out["findingReasonCodes"] = (
            capo_compute_optimizer.types.lambda_function_recommendation_finding_reason_codes.serialize_aws_json_1_0(
                value["finding_reason_codes"]
            )
        )
    if "memory_size_recommendation_options" in value:
        import capo_compute_optimizer.types.lambda_function_memory_recommendation_options

        out["memorySizeRecommendationOptions"] = (
            capo_compute_optimizer.types.lambda_function_memory_recommendation_options.serialize_aws_json_1_0(
                value["memory_size_recommendation_options"]
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
        import capo_compute_optimizer.types.lambda_effective_recommendation_preferences

        out["effectiveRecommendationPreferences"] = (
            capo_compute_optimizer.types.lambda_effective_recommendation_preferences.serialize_aws_json_1_0(
                value["effective_recommendation_preferences"]
            )
        )
    if "tags" in value:
        import capo_compute_optimizer.types.tags

        out["tags"] = capo_compute_optimizer.types.tags.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> LambdaFunctionRecommendation:
    out: LambdaFunctionRecommendation = {}  # type: ignore[typeddict-item]
    if data.get("functionArn") is not None:
        out["function_arn"] = data["functionArn"]
    if data.get("functionVersion") is not None:
        out["function_version"] = data["functionVersion"]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    if data.get("currentMemorySize") is not None:
        out["current_memory_size"] = data["currentMemorySize"]
    else:
        out["current_memory_size"] = 0
    if data.get("numberOfInvocations") is not None:
        out["number_of_invocations"] = data["numberOfInvocations"]
    else:
        out["number_of_invocations"] = 0
    if data.get("utilizationMetrics") is not None:
        import capo_compute_optimizer.types.lambda_function_utilization_metrics

        out["utilization_metrics"] = (
            capo_compute_optimizer.types.lambda_function_utilization_metrics.deserialize_aws_json_1_0(
                data["utilizationMetrics"]
            )
        )
    if data.get("lookbackPeriodInDays") is not None:
        out["lookback_period_in_days"] = float(data["lookbackPeriodInDays"])
    else:
        out["lookback_period_in_days"] = 0
    if data.get("lastRefreshTimestamp") is not None:
        import capo_compute_optimizer.types.last_refresh_timestamp

        out["last_refresh_timestamp"] = (
            capo_compute_optimizer.types.last_refresh_timestamp.deserialize_aws_json_1_0(
                data["lastRefreshTimestamp"]
            )
        )
    if data.get("finding") is not None:
        import capo_compute_optimizer.types.lambda_function_recommendation_finding

        out["finding"] = (
            capo_compute_optimizer.types.lambda_function_recommendation_finding.deserialize_aws_json_1_0(
                data["finding"]
            )
        )
    if data.get("findingReasonCodes") is not None:
        import capo_compute_optimizer.types.lambda_function_recommendation_finding_reason_codes

        out["finding_reason_codes"] = (
            capo_compute_optimizer.types.lambda_function_recommendation_finding_reason_codes.deserialize_aws_json_1_0(
                data["findingReasonCodes"]
            )
        )
    if data.get("memorySizeRecommendationOptions") is not None:
        import capo_compute_optimizer.types.lambda_function_memory_recommendation_options

        out["memory_size_recommendation_options"] = (
            capo_compute_optimizer.types.lambda_function_memory_recommendation_options.deserialize_aws_json_1_0(
                data["memorySizeRecommendationOptions"]
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
        import capo_compute_optimizer.types.lambda_effective_recommendation_preferences

        out["effective_recommendation_preferences"] = (
            capo_compute_optimizer.types.lambda_effective_recommendation_preferences.deserialize_aws_json_1_0(
                data["effectiveRecommendationPreferences"]
            )
        )
    if data.get("tags") is not None:
        import capo_compute_optimizer.types.tags

        out["tags"] = capo_compute_optimizer.types.tags.deserialize_aws_json_1_0(
            data["tags"]
        )
    return out
