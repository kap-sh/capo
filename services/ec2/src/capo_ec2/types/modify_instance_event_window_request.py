"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyInstanceEventWindowRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.instance_event_window_cron_expression
    import capo_ec2.types.instance_event_window_id
    import capo_ec2.types.instance_event_window_time_range_request_set
    import capo_ec2.types.string


class ModifyInstanceEventWindowRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    name: NotRequired["capo_ec2.types.string.String"]
    """<p>The name of the event window.</p>"""
    instance_event_window_id: NotRequired[
        "capo_ec2.types.instance_event_window_id.InstanceEventWindowId"
    ]
    """<p>The ID of the event window.</p>"""
    time_ranges: NotRequired[
        "capo_ec2.types.instance_event_window_time_range_request_set.InstanceEventWindowTimeRangeRequestSet"
    ]
    """<p>The time ranges of the event window.</p>"""
    cron_expression: NotRequired[
        "capo_ec2.types.instance_event_window_cron_expression.InstanceEventWindowCronExpression"
    ]
    """<p>The cron expression of the event window, for example, <code>* 0-4,20-23 * * 1,5</code>.</p> <p>Constraints:</p> <ul> <li> <p>Only hour and day of the week values are supported.</p> </li> <li> <p>For day of the week values, you can specify either integers <code>0</code> through <code>6</code>, or alternative single values <code>SUN</code> through <code>SAT</code>.</p> </li> <li> <p>The minute, month, and year must be specified by <code>*</code>.</p> </li> <li> <p>The hour value must be one or a multiple range, for example, <code>0-4</code> or <code>0-4,20-23</code>.</p> </li> <li> <p>Each hour range must be >= 2 hours, for example, <code>0-2</code> or <code>20-23</code>.</p> </li> <li> <p>The event window must be >= 4 hours. The combined total time ranges in the event window must be >= 4 hours.</p> </li> </ul> <p>For more information about cron expressions, see <a href="https://en.wikipedia.org/wiki/Cron">cron</a> on the <i>Wikipedia website</i>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyInstanceEventWindowRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "name" in value:
        pairs.append((f"{key_prefix}Name", str(value["name"])))
    if "instance_event_window_id" in value:
        pairs.append(
            (
                f"{key_prefix}InstanceEventWindowId",
                str(value["instance_event_window_id"]),
            )
        )
    if "time_ranges" in value:
        import capo_ec2.types.instance_event_window_time_range_request_set

        capo_ec2.types.instance_event_window_time_range_request_set.serialize_ec2_query(
            value["time_ranges"], pairs, f"{key_prefix}TimeRange"
        )
    if "cron_expression" in value:
        pairs.append((f"{key_prefix}CronExpression", str(value["cron_expression"])))


def deserialize_ec2_query(el: Element) -> ModifyInstanceEventWindowRequest:
    out: ModifyInstanceEventWindowRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    child_instance_event_window_id = el.find("InstanceEventWindowId")
    if child_instance_event_window_id is not None:
        out["instance_event_window_id"] = str(child_instance_event_window_id.text or "")
    child_time_ranges = el.find("TimeRange")
    if child_time_ranges is not None:
        import capo_ec2.types.instance_event_window_time_range_request_set

        out["time_ranges"] = (
            capo_ec2.types.instance_event_window_time_range_request_set.deserialize_ec2_query(
                child_time_ranges
            )
        )
    child_cron_expression = el.find("CronExpression")
    if child_cron_expression is not None:
        out["cron_expression"] = str(child_cron_expression.text or "")
    return out
