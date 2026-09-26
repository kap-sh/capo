"""Generated from Smithy shape ``com.amazonaws.pricingplanmanager#SubscriptionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_pricing_plan_manager.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_pricing_plan_manager.types.resource_arns
    import capo_pricing_plan_manager.types.scheduled_change
    import capo_pricing_plan_manager.types.status
    import capo_pricing_plan_manager.types.subscription_arn


class SubscriptionSummary(TypedDict, closed=True):
    arn: "capo_pricing_plan_manager.types.subscription_arn.SubscriptionArn"
    """<p>The Amazon Resource Name (ARN) that uniquely identifies this subscription.</p>"""
    plan_family: "str"
    """<p>The pricing plan family for the subscription, such as <code>CloudFront</code>.</p>"""
    plan_tier: "str"
    """<p>The current tier level of the pricing plan.</p>"""
    usage_level: NotRequired["str"]
    """<p>The usage level within the plan tier.</p>"""
    scheduled_change: NotRequired[
        "capo_pricing_plan_manager.types.scheduled_change.ScheduledChange"
    ]
    """<p>A pending change that will take effect at the end of the current billing period, if any.</p>"""
    status: "capo_pricing_plan_manager.types.status.Status"
    """<p>The current status of the subscription.</p>"""
    status_reason: NotRequired["str"]
    """<p>A human-readable explanation of the current status, present when additional context is available.</p>"""
    resource_arns: "capo_pricing_plan_manager.types.resource_arns.ResourceArns"
    """<p>The ARNs of the resources covered by this subscription.</p>"""
    created_at: "datetime.datetime"
    """<p>The date and time when the subscription was created, in ISO 8601 format.</p>"""
    updated_at: "datetime.datetime"
    """<p>The date and time when the subscription was last modified, in ISO 8601 format.</p>"""
    e_tag: "str"
    """<p>The entity tag for concurrency control. Pass this value in the <code>If-Match</code> header when making changes to this subscription.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SubscriptionSummary) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["planFamily"] = value["plan_family"]
    out["planTier"] = value["plan_tier"]
    if "usage_level" in value:
        out["usageLevel"] = value["usage_level"]
    if "scheduled_change" in value:
        import capo_pricing_plan_manager.types.scheduled_change

        out["scheduledChange"] = (
            capo_pricing_plan_manager.types.scheduled_change.serialize_json(
                value["scheduled_change"]
            )
        )
    import capo_pricing_plan_manager.types.status

    out["status"] = capo_pricing_plan_manager.types.status.serialize_json(
        value["status"]
    )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    import capo_pricing_plan_manager.types.resource_arns

    out["resourceArns"] = capo_pricing_plan_manager.types.resource_arns.serialize_json(
        value["resource_arns"]
    )
    import capo_pricing_plan_manager._protocol.serialize

    out["createdAt"] = capo_pricing_plan_manager._protocol.serialize.fmt_date_time(
        value["created_at"]
    )
    import capo_pricing_plan_manager._protocol.serialize

    out["updatedAt"] = capo_pricing_plan_manager._protocol.serialize.fmt_date_time(
        value["updated_at"]
    )
    out["eTag"] = value["e_tag"]
    return out


def deserialize_json(data: dict) -> SubscriptionSummary:
    out: SubscriptionSummary = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("SubscriptionSummary.arn required")
    if data.get("planFamily") is not None:
        out["plan_family"] = data["planFamily"]
    else:
        raise DeserializationError("SubscriptionSummary.plan_family required")
    if data.get("planTier") is not None:
        out["plan_tier"] = data["planTier"]
    else:
        raise DeserializationError("SubscriptionSummary.plan_tier required")
    if data.get("usageLevel") is not None:
        out["usage_level"] = data["usageLevel"]
    if data.get("scheduledChange") is not None:
        import capo_pricing_plan_manager.types.scheduled_change

        out["scheduled_change"] = (
            capo_pricing_plan_manager.types.scheduled_change.deserialize_json(
                data["scheduledChange"]
            )
        )
    if data.get("status") is not None:
        import capo_pricing_plan_manager.types.status

        out["status"] = capo_pricing_plan_manager.types.status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("SubscriptionSummary.status required")
    if data.get("statusReason") is not None:
        out["status_reason"] = data["statusReason"]
    if data.get("resourceArns") is not None:
        import capo_pricing_plan_manager.types.resource_arns

        out["resource_arns"] = (
            capo_pricing_plan_manager.types.resource_arns.deserialize_json(
                data["resourceArns"]
            )
        )
    else:
        raise DeserializationError("SubscriptionSummary.resource_arns required")
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    else:
        raise DeserializationError("SubscriptionSummary.created_at required")
    if data.get("updatedAt") is not None:
        import datetime

        out["updated_at"] = datetime.datetime.fromisoformat(
            data["updatedAt"].replace("Z", "+00:00")
        )
    else:
        raise DeserializationError("SubscriptionSummary.updated_at required")
    if data.get("eTag") is not None:
        out["e_tag"] = data["eTag"]
    else:
        raise DeserializationError("SubscriptionSummary.e_tag required")
    return out
