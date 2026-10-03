"""Generated from Smithy shape ``com.amazonaws.secretsmanager#RotationRulesType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_secrets_manager.types.automatically_rotate_after_days_type
    import capo_secrets_manager.types.duration_type
    import capo_secrets_manager.types.schedule_expression_type


class RotationRulesType(TypedDict, closed=True):
    automatically_after_days: NotRequired[
        "capo_secrets_manager.types.automatically_rotate_after_days_type.AutomaticallyRotateAfterDaysType"
    ]
    """<p>The number of days between rotations of the secret. You can use this value to check that your secret meets your compliance guidelines for how often secrets must be rotated. If you use this field to set the rotation schedule, Secrets Manager calculates the next rotation date based on the previous rotation. Manually updating the secret value by calling <code>PutSecretValue</code> or <code>UpdateSecret</code> is considered a valid rotation.</p> <p>In <code>DescribeSecret</code> and <code>ListSecrets</code>, this value is calculated from the rotation schedule after every successful rotation. In <code>RotateSecret</code>, you can set the rotation schedule in <code>RotationRules</code> with <code>AutomaticallyAfterDays</code> or <code>ScheduleExpression</code>, but not both. To set a rotation schedule in hours, use <code>ScheduleExpression</code>.</p>"""
    duration: NotRequired["capo_secrets_manager.types.duration_type.DurationType"]
    """<p>The length of the rotation window in hours, for example <code>3h</code> for a three hour window. Secrets Manager rotates your secret at any time during this window. The window must not extend into the next rotation window or the next UTC day. The window starts according to the <code>ScheduleExpression</code>. If you don't specify a <code>Duration</code>, for a <code>ScheduleExpression</code> in hours, the window automatically closes after one hour. For a <code>ScheduleExpression</code> in days, the window automatically closes at the end of the UTC day. For more information, including examples, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotate-secrets_schedule.html">Schedule expressions in Secrets Manager rotation</a> in the <i>Secrets Manager Users Guide</i>.</p>"""
    schedule_expression: NotRequired[
        "capo_secrets_manager.types.schedule_expression_type.ScheduleExpressionType"
    ]
    """<p>A <code>cron()</code> or <code>rate()</code> expression that defines the schedule for rotating your secret. Secrets Manager rotation schedules use UTC time zone. Secrets Manager rotates your secret any time during a rotation window.</p> <p>Secrets Manager <code>rate()</code> expressions represent the interval in hours or days that you want to rotate your secret, for example <code>rate(12 hours)</code> or <code>rate(10 days)</code>. You can rotate a secret as often as every four hours. If you use a <code>rate()</code> expression, the rotation window starts at midnight. For a rate in hours, the default rotation window closes after one hour. For a rate in days, the default rotation window closes at the end of the day. You can set the <code>Duration</code> to change the rotation window. The rotation window must not extend into the next UTC day or into the next rotation window.</p> <p>You can use a <code>cron()</code> expression to create a rotation schedule that is more detailed than a rotation interval. For more information, including examples, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotate-secrets_schedule.html">Schedule expressions in Secrets Manager rotation</a> in the <i>Secrets Manager Users Guide</i>. For a cron expression that represents a schedule in hours, the default rotation window closes after one hour. For a cron expression that represents a schedule in days, the default rotation window closes at the end of the day. You can set the <code>Duration</code> to change the rotation window. The rotation window must not extend into the next UTC day or into the next rotation window.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RotationRulesType) -> dict:
    out: dict = {}
    if "automatically_after_days" in value:
        out["AutomaticallyAfterDays"] = value["automatically_after_days"]
    if "duration" in value:
        out["Duration"] = value["duration"]
    if "schedule_expression" in value:
        out["ScheduleExpression"] = value["schedule_expression"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RotationRulesType:
    out: RotationRulesType = {}  # type: ignore[typeddict-item]
    if data.get("AutomaticallyAfterDays") is not None:
        out["automatically_after_days"] = data["AutomaticallyAfterDays"]
    if data.get("Duration") is not None:
        out["duration"] = data["Duration"]
    if data.get("ScheduleExpression") is not None:
        out["schedule_expression"] = data["ScheduleExpression"]
    return out
