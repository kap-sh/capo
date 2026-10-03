"""Generated from Smithy shape ``com.amazonaws.dlm#CreateRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dlm.types.cron_expression
    import capo_dlm.types.interval
    import capo_dlm.types.interval_unit_values
    import capo_dlm.types.location_values
    import capo_dlm.types.scripts_list
    import capo_dlm.types.times_list


class CreateRule(TypedDict, closed=True):
    location: NotRequired["capo_dlm.types.location_values.LocationValues"]
    """<p> <b>[Custom snapshot policies only]</b> Specifies the destination for snapshots created by the policy. The allowed destinations depend on the location of the targeted resources.</p> <ul> <li> <p>If the policy targets resources in a Region, then you must create snapshots in the same Region as the source resource.</p> </li> <li> <p>If the policy targets resources in a Local Zone, you can create snapshots in the same Local Zone or in its parent Region.</p> </li> <li> <p>If the policy targets resources on an Outpost, then you can create snapshots on the same Outpost or in its parent Region.</p> </li> </ul> <p>Specify one of the following values:</p> <ul> <li> <p>To create snapshots in the same Region as the source resource, specify <code>CLOUD</code>.</p> </li> <li> <p>To create snapshots in the same Local Zone as the source resource, specify <code>LOCAL_ZONE</code>.</p> </li> <li> <p>To create snapshots on the same Outpost as the source resource, specify <code>OUTPOST_LOCAL</code>.</p> </li> </ul> <p>Default: <code>CLOUD</code> </p>"""
    interval: NotRequired["capo_dlm.types.interval.Interval"]
    """<p>The interval between snapshots. The supported values are 1, 2, 3, 4, 6, 8, 12, and 24.</p>"""
    interval_unit: NotRequired["capo_dlm.types.interval_unit_values.IntervalUnitValues"]
    """<p>The interval unit.</p>"""
    times: NotRequired["capo_dlm.types.times_list.TimesList"]
    """<p>The time, in UTC, to start the operation. The supported format is hh:mm.</p> <p>The operation occurs within a one-hour window following the specified time. If you do not specify a time, Amazon Data Lifecycle Manager selects a time within the next 24 hours.</p>"""
    cron_expression: NotRequired["capo_dlm.types.cron_expression.CronExpression"]
    """<p>The schedule, as a Cron expression. The schedule interval must be between 1 hour and 1 year. For more information, see the <a href="https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-cron-expressions.html">Cron expressions reference</a> in the <i>Amazon EventBridge User Guide</i>.</p>"""
    scripts: NotRequired["capo_dlm.types.scripts_list.ScriptsList"]
    """<p> <b>[Custom snapshot policies that target instances only]</b> Specifies pre and/or post scripts for a snapshot lifecycle policy that targets instances. This is useful for creating application-consistent snapshots, or for performing specific administrative tasks before or after Amazon Data Lifecycle Manager initiates snapshot creation.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/automate-app-consistent-backups.html">Automating application-consistent snapshots with pre and post scripts</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRule) -> dict:
    out: dict = {}
    if "location" in value:
        import capo_dlm.types.location_values

        out["Location"] = capo_dlm.types.location_values.serialize_json(
            value["location"]
        )
    if "interval" in value:
        out["Interval"] = value["interval"]
    if "interval_unit" in value:
        import capo_dlm.types.interval_unit_values

        out["IntervalUnit"] = capo_dlm.types.interval_unit_values.serialize_json(
            value["interval_unit"]
        )
    if "times" in value:
        import capo_dlm.types.times_list

        out["Times"] = capo_dlm.types.times_list.serialize_json(value["times"])
    if "cron_expression" in value:
        out["CronExpression"] = value["cron_expression"]
    if "scripts" in value:
        import capo_dlm.types.scripts_list

        out["Scripts"] = capo_dlm.types.scripts_list.serialize_json(value["scripts"])
    return out


def deserialize_json(data: dict) -> CreateRule:
    out: CreateRule = {}  # type: ignore[typeddict-item]
    if data.get("Location") is not None:
        import capo_dlm.types.location_values

        out["location"] = capo_dlm.types.location_values.deserialize_json(
            data["Location"]
        )
    if data.get("Interval") is not None:
        out["interval"] = data["Interval"]
    if data.get("IntervalUnit") is not None:
        import capo_dlm.types.interval_unit_values

        out["interval_unit"] = capo_dlm.types.interval_unit_values.deserialize_json(
            data["IntervalUnit"]
        )
    if data.get("Times") is not None:
        import capo_dlm.types.times_list

        out["times"] = capo_dlm.types.times_list.deserialize_json(data["Times"])
    if data.get("CronExpression") is not None:
        out["cron_expression"] = data["CronExpression"]
    if data.get("Scripts") is not None:
        import capo_dlm.types.scripts_list

        out["scripts"] = capo_dlm.types.scripts_list.deserialize_json(data["Scripts"])
    return out
