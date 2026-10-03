"""Generated from Smithy shape ``com.amazonaws.redshift#ScheduledAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.scheduled_action_state
    import capo_redshift.types.scheduled_action_time_list
    import capo_redshift.types.scheduled_action_type
    import capo_redshift.types.string
    import capo_redshift.types.t_stamp


class ScheduledAction(TypedDict, closed=True):
    scheduled_action_name: NotRequired["capo_redshift.types.string.String"]
    """<p>The name of the scheduled action. </p>"""
    target_action: NotRequired[
        "capo_redshift.types.scheduled_action_type.ScheduledActionType"
    ]
    r"""<p>A JSON format string of the Amazon Redshift API operation with input parameters. </p> <p>"<code>{\"ResizeCluster\":{\"NodeType\":\"ra3.4xlarge\",\"ClusterIdentifier\":\"my-test-cluster\",\"NumberOfNodes\":3}}</code>". </p>"""
    schedule: NotRequired["capo_redshift.types.string.String"]
    """<p>The schedule for a one-time (at format) or recurring (cron format) scheduled action. Schedule invocations must be separated by at least one hour.</p> <p>Format of at expressions is "<code>at(yyyy-mm-ddThh:mm:ss)</code>". For example, "<code>at(2016-03-04T17:27:00)</code>".</p> <p>Format of cron expressions is "<code>cron(Minutes Hours Day-of-month Month Day-of-week Year)</code>". For example, "<code>cron(0 10 ? * MON *)</code>". For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html#CronExpressions">Cron Expressions</a> in the <i>Amazon CloudWatch Events User Guide</i>.</p>"""
    iam_role: NotRequired["capo_redshift.types.string.String"]
    """<p>The IAM role to assume to run the scheduled action. This IAM role must have permission to run the Amazon Redshift API operation in the scheduled action. This IAM role must allow the Amazon Redshift scheduler (Principal scheduler.redshift.amazonaws.com) to assume permissions on your behalf. For more information about the IAM role to use with the Amazon Redshift scheduler, see <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-identity-based.html">Using Identity-Based Policies for Amazon Redshift</a> in the <i>Amazon Redshift Cluster Management Guide</i>. </p>"""
    scheduled_action_description: NotRequired["capo_redshift.types.string.String"]
    """<p>The description of the scheduled action. </p>"""
    state: NotRequired[
        "capo_redshift.types.scheduled_action_state.ScheduledActionState"
    ]
    """<p>The state of the scheduled action. For example, <code>DISABLED</code>. </p>"""
    next_invocations: NotRequired[
        "capo_redshift.types.scheduled_action_time_list.ScheduledActionTimeList"
    ]
    """<p>List of times when the scheduled action will run. </p>"""
    start_time: NotRequired["capo_redshift.types.t_stamp.TStamp"]
    """<p>The start time in UTC when the schedule is active. Before this time, the scheduled action does not trigger. </p>"""
    end_time: NotRequired["capo_redshift.types.t_stamp.TStamp"]
    """<p>The end time in UTC when the schedule is no longer active. After this time, the scheduled action does not trigger. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ScheduledAction, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "scheduled_action_name" in value:
        pairs.append(
            (f"{key_prefix}ScheduledActionName", str(value["scheduled_action_name"]))
        )
    if "target_action" in value:
        import capo_redshift.types.scheduled_action_type

        capo_redshift.types.scheduled_action_type.serialize_query(
            value["target_action"], pairs, f"{key_prefix}TargetAction"
        )
    if "schedule" in value:
        pairs.append((f"{key_prefix}Schedule", str(value["schedule"])))
    if "iam_role" in value:
        pairs.append((f"{key_prefix}IamRole", str(value["iam_role"])))
    if "scheduled_action_description" in value:
        pairs.append(
            (
                f"{key_prefix}ScheduledActionDescription",
                str(value["scheduled_action_description"]),
            )
        )
    if "state" in value:
        import capo_redshift.types.scheduled_action_state

        capo_redshift.types.scheduled_action_state.serialize_query(
            value["state"], pairs, f"{key_prefix}State"
        )
    if "next_invocations" in value:
        import capo_redshift.types.scheduled_action_time_list

        capo_redshift.types.scheduled_action_time_list.serialize_query(
            value["next_invocations"], pairs, f"{key_prefix}NextInvocations"
        )
    if "start_time" in value:
        import capo_redshift.types.t_stamp

        capo_redshift.types.t_stamp.serialize_query(
            value["start_time"], pairs, f"{key_prefix}StartTime"
        )
    if "end_time" in value:
        import capo_redshift.types.t_stamp

        capo_redshift.types.t_stamp.serialize_query(
            value["end_time"], pairs, f"{key_prefix}EndTime"
        )


def deserialize_query(el: Element) -> ScheduledAction:
    out: ScheduledAction = {}  # type: ignore[typeddict-item]
    child_scheduled_action_name = el.find("ScheduledActionName")
    if child_scheduled_action_name is not None:
        out["scheduled_action_name"] = str(child_scheduled_action_name.text or "")
    child_target_action = el.find("TargetAction")
    if child_target_action is not None:
        import capo_redshift.types.scheduled_action_type

        out["target_action"] = (
            capo_redshift.types.scheduled_action_type.deserialize_query(
                child_target_action
            )
        )
    child_schedule = el.find("Schedule")
    if child_schedule is not None:
        out["schedule"] = str(child_schedule.text or "")
    child_iam_role = el.find("IamRole")
    if child_iam_role is not None:
        out["iam_role"] = str(child_iam_role.text or "")
    child_scheduled_action_description = el.find("ScheduledActionDescription")
    if child_scheduled_action_description is not None:
        out["scheduled_action_description"] = str(
            child_scheduled_action_description.text or ""
        )
    child_state = el.find("State")
    if child_state is not None:
        import capo_redshift.types.scheduled_action_state

        out["state"] = capo_redshift.types.scheduled_action_state.deserialize_query(
            child_state
        )
    child_next_invocations = el.find("NextInvocations")
    if child_next_invocations is not None:
        import capo_redshift.types.scheduled_action_time_list

        out["next_invocations"] = (
            capo_redshift.types.scheduled_action_time_list.deserialize_query(
                child_next_invocations
            )
        )
    child_start_time = el.find("StartTime")
    if child_start_time is not None:
        import capo_redshift.types.t_stamp

        out["start_time"] = capo_redshift.types.t_stamp.deserialize_query(
            child_start_time
        )
    child_end_time = el.find("EndTime")
    if child_end_time is not None:
        import capo_redshift.types.t_stamp

        out["end_time"] = capo_redshift.types.t_stamp.deserialize_query(child_end_time)
    return out
