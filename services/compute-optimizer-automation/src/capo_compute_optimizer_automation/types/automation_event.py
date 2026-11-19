"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#AutomationEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_compute_optimizer_automation.types.account_id
    import capo_compute_optimizer_automation.types.estimated_monthly_savings
    import capo_compute_optimizer_automation.types.event_id
    import capo_compute_optimizer_automation.types.event_status
    import capo_compute_optimizer_automation.types.event_type
    import capo_compute_optimizer_automation.types.recommended_action_id
    import capo_compute_optimizer_automation.types.resource_arn
    import capo_compute_optimizer_automation.types.resource_id
    import capo_compute_optimizer_automation.types.resource_type
    import capo_compute_optimizer_automation.types.rule_id


class AutomationEvent(TypedDict, closed=True):
    event_id: NotRequired["capo_compute_optimizer_automation.types.event_id.EventId"]
    """<p> The unique identifier for the automation event. </p>"""
    event_description: NotRequired["str"]
    """<p> A description of the automation event. </p>"""
    event_type: NotRequired[
        "capo_compute_optimizer_automation.types.event_type.EventType"
    ]
    """<p> The type of automation event. </p>"""
    event_status: NotRequired[
        "capo_compute_optimizer_automation.types.event_status.EventStatus"
    ]
    """<p> The current status of the automation event. </p>"""
    event_status_reason: NotRequired["str"]
    """<p> The reason for the current event status. </p>"""
    resource_arn: NotRequired[
        "capo_compute_optimizer_automation.types.resource_arn.ResourceArn"
    ]
    """<p> The Amazon Resource Name (ARN) of the resource affected by the automation event. </p>"""
    resource_id: NotRequired[
        "capo_compute_optimizer_automation.types.resource_id.ResourceId"
    ]
    """<p> The ID of the resource affected by the automation event. </p>"""
    recommended_action_id: NotRequired[
        "capo_compute_optimizer_automation.types.recommended_action_id.RecommendedActionId"
    ]
    """<p> The ID of the recommended action associated with this automation event. </p>"""
    account_id: NotRequired[
        "capo_compute_optimizer_automation.types.account_id.AccountId"
    ]
    """<p> The Amazon Web Services account ID associated with the automation event. </p>"""
    region: NotRequired["str"]
    """<p> The Amazon Web Services Region where the automation event occurred. </p>"""
    rule_id: NotRequired["capo_compute_optimizer_automation.types.rule_id.RuleId"]
    """<p> The ID of the automation rule that triggered this event. </p>"""
    resource_type: NotRequired[
        "capo_compute_optimizer_automation.types.resource_type.ResourceType"
    ]
    """<p> The type of resource affected by the automation event. </p>"""
    created_timestamp: NotRequired["datetime.datetime"]
    """<p>The timestamp when the automation event was created.</p>"""
    completed_timestamp: NotRequired["datetime.datetime"]
    """<p> The timestamp when the automation event completed. </p>"""
    estimated_monthly_savings: NotRequired[
        "capo_compute_optimizer_automation.types.estimated_monthly_savings.EstimatedMonthlySavings"
    ]
    """<p> The estimated monthly cost savings associated with this automation event. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AutomationEvent) -> dict:
    out: dict = {}
    if "event_id" in value:
        out["eventId"] = value["event_id"]
    if "event_description" in value:
        out["eventDescription"] = value["event_description"]
    if "event_type" in value:
        import capo_compute_optimizer_automation.types.event_type

        out["eventType"] = (
            capo_compute_optimizer_automation.types.event_type.serialize_aws_json_1_0(
                value["event_type"]
            )
        )
    if "event_status" in value:
        import capo_compute_optimizer_automation.types.event_status

        out["eventStatus"] = (
            capo_compute_optimizer_automation.types.event_status.serialize_aws_json_1_0(
                value["event_status"]
            )
        )
    if "event_status_reason" in value:
        out["eventStatusReason"] = value["event_status_reason"]
    if "resource_arn" in value:
        out["resourceArn"] = value["resource_arn"]
    if "resource_id" in value:
        out["resourceId"] = value["resource_id"]
    if "recommended_action_id" in value:
        out["recommendedActionId"] = value["recommended_action_id"]
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "region" in value:
        out["region"] = value["region"]
    if "rule_id" in value:
        out["ruleId"] = value["rule_id"]
    if "resource_type" in value:
        import capo_compute_optimizer_automation.types.resource_type

        out["resourceType"] = (
            capo_compute_optimizer_automation.types.resource_type.serialize_aws_json_1_0(
                value["resource_type"]
            )
        )
    if "created_timestamp" in value:
        import capo_compute_optimizer_automation.types._prelude.timestamp

        out["createdTimestamp"] = (
            capo_compute_optimizer_automation.types._prelude.timestamp.serialize_aws_json_1_0(
                value["created_timestamp"]
            )
        )
    if "completed_timestamp" in value:
        import capo_compute_optimizer_automation.types._prelude.timestamp

        out["completedTimestamp"] = (
            capo_compute_optimizer_automation.types._prelude.timestamp.serialize_aws_json_1_0(
                value["completed_timestamp"]
            )
        )
    if "estimated_monthly_savings" in value:
        import capo_compute_optimizer_automation.types.estimated_monthly_savings

        out["estimatedMonthlySavings"] = (
            capo_compute_optimizer_automation.types.estimated_monthly_savings.serialize_aws_json_1_0(
                value["estimated_monthly_savings"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> AutomationEvent:
    out: AutomationEvent = {}  # type: ignore[typeddict-item]
    if data.get("eventId") is not None:
        out["event_id"] = data["eventId"]
    if data.get("eventDescription") is not None:
        out["event_description"] = data["eventDescription"]
    if data.get("eventType") is not None:
        import capo_compute_optimizer_automation.types.event_type

        out["event_type"] = (
            capo_compute_optimizer_automation.types.event_type.deserialize_aws_json_1_0(
                data["eventType"]
            )
        )
    if data.get("eventStatus") is not None:
        import capo_compute_optimizer_automation.types.event_status

        out["event_status"] = (
            capo_compute_optimizer_automation.types.event_status.deserialize_aws_json_1_0(
                data["eventStatus"]
            )
        )
    if data.get("eventStatusReason") is not None:
        out["event_status_reason"] = data["eventStatusReason"]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    if data.get("resourceId") is not None:
        out["resource_id"] = data["resourceId"]
    if data.get("recommendedActionId") is not None:
        out["recommended_action_id"] = data["recommendedActionId"]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    if data.get("region") is not None:
        out["region"] = data["region"]
    if data.get("ruleId") is not None:
        out["rule_id"] = data["ruleId"]
    if data.get("resourceType") is not None:
        import capo_compute_optimizer_automation.types.resource_type

        out["resource_type"] = (
            capo_compute_optimizer_automation.types.resource_type.deserialize_aws_json_1_0(
                data["resourceType"]
            )
        )
    if data.get("createdTimestamp") is not None:
        import capo_compute_optimizer_automation.types._prelude.timestamp

        out["created_timestamp"] = (
            capo_compute_optimizer_automation.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["createdTimestamp"]
            )
        )
    if data.get("completedTimestamp") is not None:
        import capo_compute_optimizer_automation.types._prelude.timestamp

        out["completed_timestamp"] = (
            capo_compute_optimizer_automation.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["completedTimestamp"]
            )
        )
    if data.get("estimatedMonthlySavings") is not None:
        import capo_compute_optimizer_automation.types.estimated_monthly_savings

        out["estimated_monthly_savings"] = (
            capo_compute_optimizer_automation.types.estimated_monthly_savings.deserialize_aws_json_1_0(
                data["estimatedMonthlySavings"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AutomationEvent) -> dict:
    out: dict = {}
    if "event_id" in value:
        out["eventId"] = value["event_id"]
    if "event_description" in value:
        out["eventDescription"] = value["event_description"]
    if "event_type" in value:
        import capo_compute_optimizer_automation.types.event_type

        out["eventType"] = (
            capo_compute_optimizer_automation.types.event_type.serialize_cbor(
                value["event_type"]
            )
        )
    if "event_status" in value:
        import capo_compute_optimizer_automation.types.event_status

        out["eventStatus"] = (
            capo_compute_optimizer_automation.types.event_status.serialize_cbor(
                value["event_status"]
            )
        )
    if "event_status_reason" in value:
        out["eventStatusReason"] = value["event_status_reason"]
    if "resource_arn" in value:
        out["resourceArn"] = value["resource_arn"]
    if "resource_id" in value:
        out["resourceId"] = value["resource_id"]
    if "recommended_action_id" in value:
        out["recommendedActionId"] = value["recommended_action_id"]
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "region" in value:
        out["region"] = value["region"]
    if "rule_id" in value:
        out["ruleId"] = value["rule_id"]
    if "resource_type" in value:
        import capo_compute_optimizer_automation.types.resource_type

        out["resourceType"] = (
            capo_compute_optimizer_automation.types.resource_type.serialize_cbor(
                value["resource_type"]
            )
        )
    if "created_timestamp" in value:
        import capo_compute_optimizer_automation.types._prelude.timestamp

        out["createdTimestamp"] = (
            capo_compute_optimizer_automation.types._prelude.timestamp.serialize_cbor(
                value["created_timestamp"]
            )
        )
    if "completed_timestamp" in value:
        import capo_compute_optimizer_automation.types._prelude.timestamp

        out["completedTimestamp"] = (
            capo_compute_optimizer_automation.types._prelude.timestamp.serialize_cbor(
                value["completed_timestamp"]
            )
        )
    if "estimated_monthly_savings" in value:
        import capo_compute_optimizer_automation.types.estimated_monthly_savings

        out["estimatedMonthlySavings"] = (
            capo_compute_optimizer_automation.types.estimated_monthly_savings.serialize_cbor(
                value["estimated_monthly_savings"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> AutomationEvent:
    out: AutomationEvent = {}  # type: ignore[typeddict-item]
    if data.get("eventId") is not None:
        out["event_id"] = data["eventId"]
    if data.get("eventDescription") is not None:
        out["event_description"] = data["eventDescription"]
    if data.get("eventType") is not None:
        import capo_compute_optimizer_automation.types.event_type

        out["event_type"] = (
            capo_compute_optimizer_automation.types.event_type.deserialize_cbor(
                data["eventType"]
            )
        )
    if data.get("eventStatus") is not None:
        import capo_compute_optimizer_automation.types.event_status

        out["event_status"] = (
            capo_compute_optimizer_automation.types.event_status.deserialize_cbor(
                data["eventStatus"]
            )
        )
    if data.get("eventStatusReason") is not None:
        out["event_status_reason"] = data["eventStatusReason"]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    if data.get("resourceId") is not None:
        out["resource_id"] = data["resourceId"]
    if data.get("recommendedActionId") is not None:
        out["recommended_action_id"] = data["recommendedActionId"]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    if data.get("region") is not None:
        out["region"] = data["region"]
    if data.get("ruleId") is not None:
        out["rule_id"] = data["ruleId"]
    if data.get("resourceType") is not None:
        import capo_compute_optimizer_automation.types.resource_type

        out["resource_type"] = (
            capo_compute_optimizer_automation.types.resource_type.deserialize_cbor(
                data["resourceType"]
            )
        )
    if data.get("createdTimestamp") is not None:
        import capo_compute_optimizer_automation.types._prelude.timestamp

        out["created_timestamp"] = (
            capo_compute_optimizer_automation.types._prelude.timestamp.deserialize_cbor(
                data["createdTimestamp"]
            )
        )
    if data.get("completedTimestamp") is not None:
        import capo_compute_optimizer_automation.types._prelude.timestamp

        out["completed_timestamp"] = (
            capo_compute_optimizer_automation.types._prelude.timestamp.deserialize_cbor(
                data["completedTimestamp"]
            )
        )
    if data.get("estimatedMonthlySavings") is not None:
        import capo_compute_optimizer_automation.types.estimated_monthly_savings

        out["estimated_monthly_savings"] = (
            capo_compute_optimizer_automation.types.estimated_monthly_savings.deserialize_cbor(
                data["estimatedMonthlySavings"]
            )
        )
    return out
