"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#IdleRecommendation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.account_id
    import capo_compute_optimizer.types.idle_finding
    import capo_compute_optimizer.types.idle_finding_description
    import capo_compute_optimizer.types.idle_recommendation_resource_type
    import capo_compute_optimizer.types.idle_savings_opportunity
    import capo_compute_optimizer.types.idle_savings_opportunity_after_discounts
    import capo_compute_optimizer.types.idle_utilization_metrics
    import capo_compute_optimizer.types.last_refresh_timestamp
    import capo_compute_optimizer.types.look_back_period_in_days
    import capo_compute_optimizer.types.resource_arn
    import capo_compute_optimizer.types.resource_id
    import capo_compute_optimizer.types.tags


class IdleRecommendation(TypedDict, closed=True):
    resource_arn: NotRequired["capo_compute_optimizer.types.resource_arn.ResourceArn"]
    """<p>The ARN of the current idle resource.</p>"""
    resource_id: NotRequired["capo_compute_optimizer.types.resource_id.ResourceId"]
    """<p>The unique identifier for the resource.</p>"""
    resource_type: NotRequired[
        "capo_compute_optimizer.types.idle_recommendation_resource_type.IdleRecommendationResourceType"
    ]
    """<p>The type of resource that is idle.</p>"""
    account_id: NotRequired["capo_compute_optimizer.types.account_id.AccountId"]
    """<p>The Amazon Web Services account ID of the idle resource.</p>"""
    finding: NotRequired["capo_compute_optimizer.types.idle_finding.IdleFinding"]
    """<p>The finding classification of an idle resource.</p>"""
    finding_description: NotRequired[
        "capo_compute_optimizer.types.idle_finding_description.IdleFindingDescription"
    ]
    """<p>A summary of the findings for the resource.</p>"""
    savings_opportunity: NotRequired[
        "capo_compute_optimizer.types.idle_savings_opportunity.IdleSavingsOpportunity"
    ]
    """<p>The savings opportunity for the idle resource.</p>"""
    savings_opportunity_after_discounts: NotRequired[
        "capo_compute_optimizer.types.idle_savings_opportunity_after_discounts.IdleSavingsOpportunityAfterDiscounts"
    ]
    """<p>The savings opportunity for the idle resource after any applying discounts.</p>"""
    utilization_metrics: NotRequired[
        "capo_compute_optimizer.types.idle_utilization_metrics.IdleUtilizationMetrics"
    ]
    """<p>An array of objects that describe the utilization metrics of the idle resource.</p>"""
    look_back_period_in_days: (
        "capo_compute_optimizer.types.look_back_period_in_days.LookBackPeriodInDays"
    )
    """<p>The number of days the idle resource utilization metrics were analyzed.</p>"""
    last_refresh_timestamp: NotRequired[
        "capo_compute_optimizer.types.last_refresh_timestamp.LastRefreshTimestamp"
    ]
    """<p>The timestamp of when the idle resource recommendation was last generated.</p>"""
    tags: NotRequired["capo_compute_optimizer.types.tags.Tags"]
    """<p>A list of tags assigned to your idle resource recommendations.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IdleRecommendation) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["resourceArn"] = value["resource_arn"]
    if "resource_id" in value:
        out["resourceId"] = value["resource_id"]
    if "resource_type" in value:
        import capo_compute_optimizer.types.idle_recommendation_resource_type

        out["resourceType"] = (
            capo_compute_optimizer.types.idle_recommendation_resource_type.serialize_aws_json_1_0(
                value["resource_type"]
            )
        )
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "finding" in value:
        import capo_compute_optimizer.types.idle_finding

        out["finding"] = (
            capo_compute_optimizer.types.idle_finding.serialize_aws_json_1_0(
                value["finding"]
            )
        )
    if "finding_description" in value:
        out["findingDescription"] = value["finding_description"]
    if "savings_opportunity" in value:
        import capo_compute_optimizer.types.idle_savings_opportunity

        out["savingsOpportunity"] = (
            capo_compute_optimizer.types.idle_savings_opportunity.serialize_aws_json_1_0(
                value["savings_opportunity"]
            )
        )
    if "savings_opportunity_after_discounts" in value:
        import capo_compute_optimizer.types.idle_savings_opportunity_after_discounts

        out["savingsOpportunityAfterDiscounts"] = (
            capo_compute_optimizer.types.idle_savings_opportunity_after_discounts.serialize_aws_json_1_0(
                value["savings_opportunity_after_discounts"]
            )
        )
    if "utilization_metrics" in value:
        import capo_compute_optimizer.types.idle_utilization_metrics

        out["utilizationMetrics"] = (
            capo_compute_optimizer.types.idle_utilization_metrics.serialize_aws_json_1_0(
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
    if "last_refresh_timestamp" in value:
        import capo_compute_optimizer.types.last_refresh_timestamp

        out["lastRefreshTimestamp"] = (
            capo_compute_optimizer.types.last_refresh_timestamp.serialize_aws_json_1_0(
                value["last_refresh_timestamp"]
            )
        )
    if "tags" in value:
        import capo_compute_optimizer.types.tags

        out["tags"] = capo_compute_optimizer.types.tags.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> IdleRecommendation:
    out: IdleRecommendation = {}  # type: ignore[typeddict-item]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    if data.get("resourceId") is not None:
        out["resource_id"] = data["resourceId"]
    if data.get("resourceType") is not None:
        import capo_compute_optimizer.types.idle_recommendation_resource_type

        out["resource_type"] = (
            capo_compute_optimizer.types.idle_recommendation_resource_type.deserialize_aws_json_1_0(
                data["resourceType"]
            )
        )
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    if data.get("finding") is not None:
        import capo_compute_optimizer.types.idle_finding

        out["finding"] = (
            capo_compute_optimizer.types.idle_finding.deserialize_aws_json_1_0(
                data["finding"]
            )
        )
    if data.get("findingDescription") is not None:
        out["finding_description"] = data["findingDescription"]
    if data.get("savingsOpportunity") is not None:
        import capo_compute_optimizer.types.idle_savings_opportunity

        out["savings_opportunity"] = (
            capo_compute_optimizer.types.idle_savings_opportunity.deserialize_aws_json_1_0(
                data["savingsOpportunity"]
            )
        )
    if data.get("savingsOpportunityAfterDiscounts") is not None:
        import capo_compute_optimizer.types.idle_savings_opportunity_after_discounts

        out["savings_opportunity_after_discounts"] = (
            capo_compute_optimizer.types.idle_savings_opportunity_after_discounts.deserialize_aws_json_1_0(
                data["savingsOpportunityAfterDiscounts"]
            )
        )
    if data.get("utilizationMetrics") is not None:
        import capo_compute_optimizer.types.idle_utilization_metrics

        out["utilization_metrics"] = (
            capo_compute_optimizer.types.idle_utilization_metrics.deserialize_aws_json_1_0(
                data["utilizationMetrics"]
            )
        )
    if data.get("lookBackPeriodInDays") is not None:
        out["look_back_period_in_days"] = float(data["lookBackPeriodInDays"])
    else:
        out["look_back_period_in_days"] = 0
    if data.get("lastRefreshTimestamp") is not None:
        import capo_compute_optimizer.types.last_refresh_timestamp

        out["last_refresh_timestamp"] = (
            capo_compute_optimizer.types.last_refresh_timestamp.deserialize_aws_json_1_0(
                data["lastRefreshTimestamp"]
            )
        )
    if data.get("tags") is not None:
        import capo_compute_optimizer.types.tags

        out["tags"] = capo_compute_optimizer.types.tags.deserialize_aws_json_1_0(
            data["tags"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: IdleRecommendation) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["resourceArn"] = value["resource_arn"]
    if "resource_id" in value:
        out["resourceId"] = value["resource_id"]
    if "resource_type" in value:
        import capo_compute_optimizer.types.idle_recommendation_resource_type

        out["resourceType"] = (
            capo_compute_optimizer.types.idle_recommendation_resource_type.serialize_cbor(
                value["resource_type"]
            )
        )
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "finding" in value:
        import capo_compute_optimizer.types.idle_finding

        out["finding"] = capo_compute_optimizer.types.idle_finding.serialize_cbor(
            value["finding"]
        )
    if "finding_description" in value:
        out["findingDescription"] = value["finding_description"]
    if "savings_opportunity" in value:
        import capo_compute_optimizer.types.idle_savings_opportunity

        out["savingsOpportunity"] = (
            capo_compute_optimizer.types.idle_savings_opportunity.serialize_cbor(
                value["savings_opportunity"]
            )
        )
    if "savings_opportunity_after_discounts" in value:
        import capo_compute_optimizer.types.idle_savings_opportunity_after_discounts

        out["savingsOpportunityAfterDiscounts"] = (
            capo_compute_optimizer.types.idle_savings_opportunity_after_discounts.serialize_cbor(
                value["savings_opportunity_after_discounts"]
            )
        )
    if "utilization_metrics" in value:
        import capo_compute_optimizer.types.idle_utilization_metrics

        out["utilizationMetrics"] = (
            capo_compute_optimizer.types.idle_utilization_metrics.serialize_cbor(
                value["utilization_metrics"]
            )
        )
    out["lookBackPeriodInDays"] = value.get("look_back_period_in_days", 0)
    if "last_refresh_timestamp" in value:
        import capo_compute_optimizer.types.last_refresh_timestamp

        out["lastRefreshTimestamp"] = (
            capo_compute_optimizer.types.last_refresh_timestamp.serialize_cbor(
                value["last_refresh_timestamp"]
            )
        )
    if "tags" in value:
        import capo_compute_optimizer.types.tags

        out["tags"] = capo_compute_optimizer.types.tags.serialize_cbor(value["tags"])
    return out


def deserialize_cbor(data: dict) -> IdleRecommendation:
    out: IdleRecommendation = {}  # type: ignore[typeddict-item]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    if data.get("resourceId") is not None:
        out["resource_id"] = data["resourceId"]
    if data.get("resourceType") is not None:
        import capo_compute_optimizer.types.idle_recommendation_resource_type

        out["resource_type"] = (
            capo_compute_optimizer.types.idle_recommendation_resource_type.deserialize_cbor(
                data["resourceType"]
            )
        )
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    if data.get("finding") is not None:
        import capo_compute_optimizer.types.idle_finding

        out["finding"] = capo_compute_optimizer.types.idle_finding.deserialize_cbor(
            data["finding"]
        )
    if data.get("findingDescription") is not None:
        out["finding_description"] = data["findingDescription"]
    if data.get("savingsOpportunity") is not None:
        import capo_compute_optimizer.types.idle_savings_opportunity

        out["savings_opportunity"] = (
            capo_compute_optimizer.types.idle_savings_opportunity.deserialize_cbor(
                data["savingsOpportunity"]
            )
        )
    if data.get("savingsOpportunityAfterDiscounts") is not None:
        import capo_compute_optimizer.types.idle_savings_opportunity_after_discounts

        out["savings_opportunity_after_discounts"] = (
            capo_compute_optimizer.types.idle_savings_opportunity_after_discounts.deserialize_cbor(
                data["savingsOpportunityAfterDiscounts"]
            )
        )
    if data.get("utilizationMetrics") is not None:
        import capo_compute_optimizer.types.idle_utilization_metrics

        out["utilization_metrics"] = (
            capo_compute_optimizer.types.idle_utilization_metrics.deserialize_cbor(
                data["utilizationMetrics"]
            )
        )
    if data.get("lookBackPeriodInDays") is not None:
        out["look_back_period_in_days"] = float(data["lookBackPeriodInDays"])
    else:
        out["look_back_period_in_days"] = 0
    if data.get("lastRefreshTimestamp") is not None:
        import capo_compute_optimizer.types.last_refresh_timestamp

        out["last_refresh_timestamp"] = (
            capo_compute_optimizer.types.last_refresh_timestamp.deserialize_cbor(
                data["lastRefreshTimestamp"]
            )
        )
    if data.get("tags") is not None:
        import capo_compute_optimizer.types.tags

        out["tags"] = capo_compute_optimizer.types.tags.deserialize_cbor(data["tags"])
    return out
