"""Generated from Smithy shape ``com.amazonaws.pricingplanmanager#ScheduledChange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_pricing_plan_manager.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_pricing_plan_manager.types.scheduled_change_type


class ScheduledChange(TypedDict, closed=True):
    change_type: (
        "capo_pricing_plan_manager.types.scheduled_change_type.ScheduledChangeType"
    )
    """<p>The type of pending change. Possible values are <code>DOWNGRADE</code> (a tier change to a lower level) and <code>CANCELLATION</code> (subscription termination).</p>"""
    effective_date: NotRequired["datetime.datetime"]
    """<p>The date and time when the change takes effect, in ISO 8601 format. This value is populated after the change is confirmed by the billing system.</p>"""
    plan_tier: NotRequired["str"]
    """<p>For downgrades, the tier level that the subscription will change to. Not present for cancellations.</p>"""
    usage_level: NotRequired["str"]
    """<p>For downgrades, the target usage level after the change takes effect.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScheduledChange) -> dict:
    out: dict = {}
    import capo_pricing_plan_manager.types.scheduled_change_type

    out["changeType"] = (
        capo_pricing_plan_manager.types.scheduled_change_type.serialize_json(
            value["change_type"]
        )
    )
    if "effective_date" in value:
        import capo_pricing_plan_manager._protocol.serialize

        out["effectiveDate"] = (
            capo_pricing_plan_manager._protocol.serialize.fmt_date_time(
                value["effective_date"]
            )
        )
    if "plan_tier" in value:
        out["planTier"] = value["plan_tier"]
    if "usage_level" in value:
        out["usageLevel"] = value["usage_level"]
    return out


def deserialize_json(data: dict) -> ScheduledChange:
    out: ScheduledChange = {}  # type: ignore[typeddict-item]
    if data.get("changeType") is not None:
        import capo_pricing_plan_manager.types.scheduled_change_type

        out["change_type"] = (
            capo_pricing_plan_manager.types.scheduled_change_type.deserialize_json(
                data["changeType"]
            )
        )
    else:
        raise DeserializationError("ScheduledChange.change_type required")
    if data.get("effectiveDate") is not None:
        import datetime

        out["effective_date"] = datetime.datetime.fromisoformat(
            data["effectiveDate"].replace("Z", "+00:00")
        )
    if data.get("planTier") is not None:
        out["plan_tier"] = data["planTier"]
    if data.get("usageLevel") is not None:
        out["usage_level"] = data["usageLevel"]
    return out
