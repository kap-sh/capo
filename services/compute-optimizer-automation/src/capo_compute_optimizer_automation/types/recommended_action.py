"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#RecommendedAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer_automation.types.account_id
    import capo_compute_optimizer_automation.types.estimated_monthly_savings
    import capo_compute_optimizer_automation.types.recommended_action_id
    import capo_compute_optimizer_automation.types.recommended_action_type
    import capo_compute_optimizer_automation.types.resource_arn
    import capo_compute_optimizer_automation.types.resource_details
    import capo_compute_optimizer_automation.types.resource_id
    import capo_compute_optimizer_automation.types.resource_type
    import capo_compute_optimizer_automation.types.tag_list


class RecommendedAction(TypedDict, closed=True):
    recommended_action_id: NotRequired[
        "capo_compute_optimizer_automation.types.recommended_action_id.RecommendedActionId"
    ]
    """<p>The unique identifier of the recommended action.</p>"""
    resource_arn: NotRequired[
        "capo_compute_optimizer_automation.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the resource that the recommendation applies to.</p>"""
    resource_id: NotRequired[
        "capo_compute_optimizer_automation.types.resource_id.ResourceId"
    ]
    """<p>The ID of the resource that the recommendation applies to.</p>"""
    account_id: NotRequired[
        "capo_compute_optimizer_automation.types.account_id.AccountId"
    ]
    """<p>The Amazon Web Services account ID that owns the resource.</p>"""
    region: NotRequired["str"]
    """<p>The Amazon Web Services Region where the resource is located.</p>"""
    resource_type: NotRequired[
        "capo_compute_optimizer_automation.types.resource_type.ResourceType"
    ]
    """<p>The type of resource being evaluated.</p>"""
    look_back_period_in_days: NotRequired["int"]
    """<p>The number of days of historical data used to generate the recommendation.</p>"""
    recommended_action_type: NotRequired[
        "capo_compute_optimizer_automation.types.recommended_action_type.RecommendedActionType"
    ]
    """<p>The type of action being recommended.</p>"""
    current_resource_summary: NotRequired["str"]
    """<p>A summary of the resource's current configuration.</p>"""
    current_resource_details: NotRequired[
        "capo_compute_optimizer_automation.types.resource_details.ResourceDetails"
    ]
    recommended_resource_summary: NotRequired["str"]
    """<p>A summary of the resource's recommended configuration.</p>"""
    recommended_resource_details: NotRequired[
        "capo_compute_optimizer_automation.types.resource_details.ResourceDetails"
    ]
    restart_needed: NotRequired["bool"]
    """<p>Indicates whether implementing the recommended action requires a resource restart.</p>"""
    estimated_monthly_savings: NotRequired[
        "capo_compute_optimizer_automation.types.estimated_monthly_savings.EstimatedMonthlySavings"
    ]
    resource_tags: NotRequired[
        "capo_compute_optimizer_automation.types.tag_list.TagList"
    ]
    """<p>The tags associated with the resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RecommendedAction) -> dict:
    out: dict = {}
    if "recommended_action_id" in value:
        out["recommendedActionId"] = value["recommended_action_id"]
    if "resource_arn" in value:
        out["resourceArn"] = value["resource_arn"]
    if "resource_id" in value:
        out["resourceId"] = value["resource_id"]
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "region" in value:
        out["region"] = value["region"]
    if "resource_type" in value:
        import capo_compute_optimizer_automation.types.resource_type

        out["resourceType"] = (
            capo_compute_optimizer_automation.types.resource_type.serialize_aws_json_1_0(
                value["resource_type"]
            )
        )
    if "look_back_period_in_days" in value:
        out["lookBackPeriodInDays"] = value["look_back_period_in_days"]
    if "recommended_action_type" in value:
        import capo_compute_optimizer_automation.types.recommended_action_type

        out["recommendedActionType"] = (
            capo_compute_optimizer_automation.types.recommended_action_type.serialize_aws_json_1_0(
                value["recommended_action_type"]
            )
        )
    if "current_resource_summary" in value:
        out["currentResourceSummary"] = value["current_resource_summary"]
    if "current_resource_details" in value:
        import capo_compute_optimizer_automation.types.resource_details

        out["currentResourceDetails"] = (
            capo_compute_optimizer_automation.types.resource_details.serialize_aws_json_1_0(
                value["current_resource_details"]
            )
        )
    if "recommended_resource_summary" in value:
        out["recommendedResourceSummary"] = value["recommended_resource_summary"]
    if "recommended_resource_details" in value:
        import capo_compute_optimizer_automation.types.resource_details

        out["recommendedResourceDetails"] = (
            capo_compute_optimizer_automation.types.resource_details.serialize_aws_json_1_0(
                value["recommended_resource_details"]
            )
        )
    if "restart_needed" in value:
        out["restartNeeded"] = value["restart_needed"]
    if "estimated_monthly_savings" in value:
        import capo_compute_optimizer_automation.types.estimated_monthly_savings

        out["estimatedMonthlySavings"] = (
            capo_compute_optimizer_automation.types.estimated_monthly_savings.serialize_aws_json_1_0(
                value["estimated_monthly_savings"]
            )
        )
    if "resource_tags" in value:
        import capo_compute_optimizer_automation.types.tag_list

        out["resourceTags"] = (
            capo_compute_optimizer_automation.types.tag_list.serialize_aws_json_1_0(
                value["resource_tags"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> RecommendedAction:
    out: RecommendedAction = {}  # type: ignore[typeddict-item]
    if data.get("recommendedActionId") is not None:
        out["recommended_action_id"] = data["recommendedActionId"]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    if data.get("resourceId") is not None:
        out["resource_id"] = data["resourceId"]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    if data.get("region") is not None:
        out["region"] = data["region"]
    if data.get("resourceType") is not None:
        import capo_compute_optimizer_automation.types.resource_type

        out["resource_type"] = (
            capo_compute_optimizer_automation.types.resource_type.deserialize_aws_json_1_0(
                data["resourceType"]
            )
        )
    if data.get("lookBackPeriodInDays") is not None:
        out["look_back_period_in_days"] = data["lookBackPeriodInDays"]
    if data.get("recommendedActionType") is not None:
        import capo_compute_optimizer_automation.types.recommended_action_type

        out["recommended_action_type"] = (
            capo_compute_optimizer_automation.types.recommended_action_type.deserialize_aws_json_1_0(
                data["recommendedActionType"]
            )
        )
    if data.get("currentResourceSummary") is not None:
        out["current_resource_summary"] = data["currentResourceSummary"]
    if data.get("currentResourceDetails") is not None:
        import capo_compute_optimizer_automation.types.resource_details

        out["current_resource_details"] = (
            capo_compute_optimizer_automation.types.resource_details.deserialize_aws_json_1_0(
                data["currentResourceDetails"]
            )
        )
    if data.get("recommendedResourceSummary") is not None:
        out["recommended_resource_summary"] = data["recommendedResourceSummary"]
    if data.get("recommendedResourceDetails") is not None:
        import capo_compute_optimizer_automation.types.resource_details

        out["recommended_resource_details"] = (
            capo_compute_optimizer_automation.types.resource_details.deserialize_aws_json_1_0(
                data["recommendedResourceDetails"]
            )
        )
    if data.get("restartNeeded") is not None:
        out["restart_needed"] = data["restartNeeded"]
    if data.get("estimatedMonthlySavings") is not None:
        import capo_compute_optimizer_automation.types.estimated_monthly_savings

        out["estimated_monthly_savings"] = (
            capo_compute_optimizer_automation.types.estimated_monthly_savings.deserialize_aws_json_1_0(
                data["estimatedMonthlySavings"]
            )
        )
    if data.get("resourceTags") is not None:
        import capo_compute_optimizer_automation.types.tag_list

        out["resource_tags"] = (
            capo_compute_optimizer_automation.types.tag_list.deserialize_aws_json_1_0(
                data["resourceTags"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RecommendedAction) -> dict:
    out: dict = {}
    if "recommended_action_id" in value:
        out["recommendedActionId"] = value["recommended_action_id"]
    if "resource_arn" in value:
        out["resourceArn"] = value["resource_arn"]
    if "resource_id" in value:
        out["resourceId"] = value["resource_id"]
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "region" in value:
        out["region"] = value["region"]
    if "resource_type" in value:
        import capo_compute_optimizer_automation.types.resource_type

        out["resourceType"] = (
            capo_compute_optimizer_automation.types.resource_type.serialize_cbor(
                value["resource_type"]
            )
        )
    if "look_back_period_in_days" in value:
        out["lookBackPeriodInDays"] = value["look_back_period_in_days"]
    if "recommended_action_type" in value:
        import capo_compute_optimizer_automation.types.recommended_action_type

        out["recommendedActionType"] = (
            capo_compute_optimizer_automation.types.recommended_action_type.serialize_cbor(
                value["recommended_action_type"]
            )
        )
    if "current_resource_summary" in value:
        out["currentResourceSummary"] = value["current_resource_summary"]
    if "current_resource_details" in value:
        import capo_compute_optimizer_automation.types.resource_details

        out["currentResourceDetails"] = (
            capo_compute_optimizer_automation.types.resource_details.serialize_cbor(
                value["current_resource_details"]
            )
        )
    if "recommended_resource_summary" in value:
        out["recommendedResourceSummary"] = value["recommended_resource_summary"]
    if "recommended_resource_details" in value:
        import capo_compute_optimizer_automation.types.resource_details

        out["recommendedResourceDetails"] = (
            capo_compute_optimizer_automation.types.resource_details.serialize_cbor(
                value["recommended_resource_details"]
            )
        )
    if "restart_needed" in value:
        out["restartNeeded"] = value["restart_needed"]
    if "estimated_monthly_savings" in value:
        import capo_compute_optimizer_automation.types.estimated_monthly_savings

        out["estimatedMonthlySavings"] = (
            capo_compute_optimizer_automation.types.estimated_monthly_savings.serialize_cbor(
                value["estimated_monthly_savings"]
            )
        )
    if "resource_tags" in value:
        import capo_compute_optimizer_automation.types.tag_list

        out["resourceTags"] = (
            capo_compute_optimizer_automation.types.tag_list.serialize_cbor(
                value["resource_tags"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> RecommendedAction:
    out: RecommendedAction = {}  # type: ignore[typeddict-item]
    if data.get("recommendedActionId") is not None:
        out["recommended_action_id"] = data["recommendedActionId"]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    if data.get("resourceId") is not None:
        out["resource_id"] = data["resourceId"]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    if data.get("region") is not None:
        out["region"] = data["region"]
    if data.get("resourceType") is not None:
        import capo_compute_optimizer_automation.types.resource_type

        out["resource_type"] = (
            capo_compute_optimizer_automation.types.resource_type.deserialize_cbor(
                data["resourceType"]
            )
        )
    if data.get("lookBackPeriodInDays") is not None:
        out["look_back_period_in_days"] = data["lookBackPeriodInDays"]
    if data.get("recommendedActionType") is not None:
        import capo_compute_optimizer_automation.types.recommended_action_type

        out["recommended_action_type"] = (
            capo_compute_optimizer_automation.types.recommended_action_type.deserialize_cbor(
                data["recommendedActionType"]
            )
        )
    if data.get("currentResourceSummary") is not None:
        out["current_resource_summary"] = data["currentResourceSummary"]
    if data.get("currentResourceDetails") is not None:
        import capo_compute_optimizer_automation.types.resource_details

        out["current_resource_details"] = (
            capo_compute_optimizer_automation.types.resource_details.deserialize_cbor(
                data["currentResourceDetails"]
            )
        )
    if data.get("recommendedResourceSummary") is not None:
        out["recommended_resource_summary"] = data["recommendedResourceSummary"]
    if data.get("recommendedResourceDetails") is not None:
        import capo_compute_optimizer_automation.types.resource_details

        out["recommended_resource_details"] = (
            capo_compute_optimizer_automation.types.resource_details.deserialize_cbor(
                data["recommendedResourceDetails"]
            )
        )
    if data.get("restartNeeded") is not None:
        out["restart_needed"] = data["restartNeeded"]
    if data.get("estimatedMonthlySavings") is not None:
        import capo_compute_optimizer_automation.types.estimated_monthly_savings

        out["estimated_monthly_savings"] = (
            capo_compute_optimizer_automation.types.estimated_monthly_savings.deserialize_cbor(
                data["estimatedMonthlySavings"]
            )
        )
    if data.get("resourceTags") is not None:
        import capo_compute_optimizer_automation.types.tag_list

        out["resource_tags"] = (
            capo_compute_optimizer_automation.types.tag_list.deserialize_cbor(
                data["resourceTags"]
            )
        )
    return out
