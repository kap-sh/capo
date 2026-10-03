"""Generated from Smithy shape ``com.amazonaws.backup#RestoreTestingPlanForCreate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_backup.errors import DeserializationError

if TYPE_CHECKING:
    import capo_backup.types.integer
    import capo_backup.types.restore_testing_recovery_point_selection


class RestoreTestingPlanForCreate(TypedDict, closed=True):
    recovery_point_selection: "capo_backup.types.restore_testing_recovery_point_selection.RestoreTestingRecoveryPointSelection"
    """<p> <code>RecoveryPointSelection</code> has five parameters (three required and two optional). The values you specify determine which recovery point is included in the restore test. You must indicate with <code>Algorithm</code> if you want the latest recovery point within your <code>SelectionWindowDays</code> or if you want a random recovery point, and you must indicate through <code>IncludeVaults</code> from which vaults the recovery points can be chosen.</p> <p> <code>Algorithm</code> (<i>required</i>) Valid values: "<code>LATEST_WITHIN_WINDOW</code>" or "<code>RANDOM_WITHIN_WINDOW</code>".</p> <p> <code>Recovery point types</code> (<i>required</i>) Valid values: "<code>SNAPSHOT</code>" and/or "<code>CONTINUOUS</code>". Include <code>SNAPSHOT</code> to restore only snapshot recovery points; include <code>CONTINUOUS</code> to restore continuous recovery points (point in time restore / PITR); use both to restore either a snapshot or a continuous recovery point. The recovery point will be determined by the value for <code>Algorithm</code>.</p> <p> <code>IncludeVaults</code> (<i>required</i>). You must include one or more backup vaults. Use the wildcard ["*"] or specific ARNs.</p> <p> <code>SelectionWindowDays</code> (<i>optional</i>) Value must be an integer (in days) from 1 to 365. If not included, the value defaults to <code>30</code>.</p> <p> <code>ExcludeVaults</code> (<i>optional</i>). You can choose to input one or more specific backup vault ARNs to exclude those vaults' contents from restore eligibility. Or, you can include a list of selectors. If this parameter and its value are not included, it defaults to empty list.</p>"""
    restore_testing_plan_name: "str"
    """<p>The RestoreTestingPlanName is a unique string that is the name of the restore testing plan. This cannot be changed after creation, and it must consist of only alphanumeric characters and underscores.</p>"""
    schedule_expression: "str"
    """<p>A CRON expression in specified timezone when a restore testing plan is executed. When no CRON expression is provided, Backup will use the default expression <code>cron(0 5 ? * * *)</code>.</p>"""
    schedule_expression_timezone: NotRequired["str"]
    """<p>Optional. This is the timezone in which the schedule expression is set. By default, ScheduleExpressions are in UTC. You can modify this to a specified timezone.</p>"""
    start_window_hours: "capo_backup.types.integer.integer"
    """<p>Defaults to 24 hours.</p> <p>A value in hours after a restore test is scheduled before a job will be canceled if it doesn't start successfully. This value is optional. If this value is included, this parameter has a maximum value of 168 hours (one week).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RestoreTestingPlanForCreate) -> dict:
    out: dict = {}
    import capo_backup.types.restore_testing_recovery_point_selection

    out["RecoveryPointSelection"] = (
        capo_backup.types.restore_testing_recovery_point_selection.serialize_json(
            value["recovery_point_selection"]
        )
    )
    out["RestoreTestingPlanName"] = value["restore_testing_plan_name"]
    out["ScheduleExpression"] = value["schedule_expression"]
    if "schedule_expression_timezone" in value:
        out["ScheduleExpressionTimezone"] = value["schedule_expression_timezone"]
    out["StartWindowHours"] = value.get("start_window_hours", 0)
    return out


def deserialize_json(data: dict) -> RestoreTestingPlanForCreate:
    out: RestoreTestingPlanForCreate = {}  # type: ignore[typeddict-item]
    if data.get("RecoveryPointSelection") is not None:
        import capo_backup.types.restore_testing_recovery_point_selection

        out["recovery_point_selection"] = (
            capo_backup.types.restore_testing_recovery_point_selection.deserialize_json(
                data["RecoveryPointSelection"]
            )
        )
    else:
        raise DeserializationError(
            "RestoreTestingPlanForCreate.recovery_point_selection required"
        )
    if data.get("RestoreTestingPlanName") is not None:
        out["restore_testing_plan_name"] = data["RestoreTestingPlanName"]
    else:
        raise DeserializationError(
            "RestoreTestingPlanForCreate.restore_testing_plan_name required"
        )
    if data.get("ScheduleExpression") is not None:
        out["schedule_expression"] = data["ScheduleExpression"]
    else:
        raise DeserializationError(
            "RestoreTestingPlanForCreate.schedule_expression required"
        )
    if data.get("ScheduleExpressionTimezone") is not None:
        out["schedule_expression_timezone"] = data["ScheduleExpressionTimezone"]
    if data.get("StartWindowHours") is not None:
        out["start_window_hours"] = data["StartWindowHours"]
    else:
        out["start_window_hours"] = 0
    return out
