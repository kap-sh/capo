"""Generated from Smithy shape ``com.amazonaws.iot#ScheduledAuditMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.audit_frequency
    import capo_iot.types.day_of_month
    import capo_iot.types.day_of_week
    import capo_iot.types.scheduled_audit_arn
    import capo_iot.types.scheduled_audit_name


class ScheduledAuditMetadata(TypedDict, closed=True):
    scheduled_audit_name: NotRequired[
        "capo_iot.types.scheduled_audit_name.ScheduledAuditName"
    ]
    """<p>The name of the scheduled audit.</p>"""
    scheduled_audit_arn: NotRequired[
        "capo_iot.types.scheduled_audit_arn.ScheduledAuditArn"
    ]
    """<p>The ARN of the scheduled audit.</p>"""
    frequency: NotRequired["capo_iot.types.audit_frequency.AuditFrequency"]
    """<p>How often the scheduled audit occurs.</p>"""
    day_of_month: NotRequired["capo_iot.types.day_of_month.DayOfMonth"]
    """<p>The day of the month on which the scheduled audit is run (if the <code>frequency</code> is "MONTHLY"). If days 29-31 are specified, and the month does not have that many days, the audit takes place on the "LAST" day of the month.</p>"""
    day_of_week: NotRequired["capo_iot.types.day_of_week.DayOfWeek"]
    """<p>The day of the week on which the scheduled audit is run (if the <code>frequency</code> is "WEEKLY" or "BIWEEKLY").</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScheduledAuditMetadata) -> dict:
    out: dict = {}
    if "scheduled_audit_name" in value:
        out["scheduledAuditName"] = value["scheduled_audit_name"]
    if "scheduled_audit_arn" in value:
        out["scheduledAuditArn"] = value["scheduled_audit_arn"]
    if "frequency" in value:
        import capo_iot.types.audit_frequency

        out["frequency"] = capo_iot.types.audit_frequency.serialize_json(
            value["frequency"]
        )
    if "day_of_month" in value:
        out["dayOfMonth"] = value["day_of_month"]
    if "day_of_week" in value:
        import capo_iot.types.day_of_week

        out["dayOfWeek"] = capo_iot.types.day_of_week.serialize_json(
            value["day_of_week"]
        )
    return out


def deserialize_json(data: dict) -> ScheduledAuditMetadata:
    out: ScheduledAuditMetadata = {}  # type: ignore[typeddict-item]
    if data.get("scheduledAuditName") is not None:
        out["scheduled_audit_name"] = data["scheduledAuditName"]
    if data.get("scheduledAuditArn") is not None:
        out["scheduled_audit_arn"] = data["scheduledAuditArn"]
    if data.get("frequency") is not None:
        import capo_iot.types.audit_frequency

        out["frequency"] = capo_iot.types.audit_frequency.deserialize_json(
            data["frequency"]
        )
    if data.get("dayOfMonth") is not None:
        out["day_of_month"] = data["dayOfMonth"]
    if data.get("dayOfWeek") is not None:
        import capo_iot.types.day_of_week

        out["day_of_week"] = capo_iot.types.day_of_week.deserialize_json(
            data["dayOfWeek"]
        )
    return out
