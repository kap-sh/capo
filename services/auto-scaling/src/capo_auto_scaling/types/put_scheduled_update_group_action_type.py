"""Generated from Smithy shape ``com.amazonaws.autoscaling#PutScheduledUpdateGroupActionType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.auto_scaling_group_desired_capacity
    import capo_auto_scaling.types.auto_scaling_group_max_size
    import capo_auto_scaling.types.auto_scaling_group_min_size
    import capo_auto_scaling.types.timestamp_type
    import capo_auto_scaling.types.xml_string_max_len255


class PutScheduledUpdateGroupActionType(TypedDict, closed=True):
    auto_scaling_group_name: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>The name of the Auto Scaling group.</p>"""
    scheduled_action_name: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>The name of this scaling action.</p>"""
    time: NotRequired["capo_auto_scaling.types.timestamp_type.TimestampType"]
    """<p>This property is no longer used.</p>"""
    start_time: NotRequired["capo_auto_scaling.types.timestamp_type.TimestampType"]
    """<p>The date and time for this action to start, in YYYY-MM-DDThh:mm:ssZ format in UTC/GMT only and in quotes (for example, <code>"2021-06-01T00:00:00Z"</code>).</p> <p>If you specify <code>Recurrence</code> and <code>StartTime</code>, Amazon EC2 Auto Scaling performs the action at this time, and then performs the action based on the specified recurrence.</p>"""
    end_time: NotRequired["capo_auto_scaling.types.timestamp_type.TimestampType"]
    """<p>The date and time for the recurring schedule to end, in UTC. For example, <code>"2021-06-01T00:00:00Z"</code>.</p>"""
    recurrence: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>The recurring schedule for this action. This format consists of five fields separated by white spaces: [Minute] [Hour] [Day_of_Month] [Month_of_Year] [Day_of_Week]. The value must be in quotes (for example, <code>"30 0 1 1,6,12 *"</code>). For more information about this format, see <a href="http://crontab.org">Crontab</a>.</p> <p>When <code>StartTime</code> and <code>EndTime</code> are specified with <code>Recurrence</code>, they form the boundaries of when the recurring action starts and stops.</p> <p>Cron expressions use Universal Coordinated Time (UTC) by default.</p>"""
    min_size: NotRequired[
        "capo_auto_scaling.types.auto_scaling_group_min_size.AutoScalingGroupMinSize"
    ]
    """<p>The minimum size of the Auto Scaling group.</p>"""
    max_size: NotRequired[
        "capo_auto_scaling.types.auto_scaling_group_max_size.AutoScalingGroupMaxSize"
    ]
    """<p>The maximum size of the Auto Scaling group.</p>"""
    desired_capacity: NotRequired[
        "capo_auto_scaling.types.auto_scaling_group_desired_capacity.AutoScalingGroupDesiredCapacity"
    ]
    """<p>The desired capacity is the initial capacity of the Auto Scaling group after the scheduled action runs and the capacity it attempts to maintain. It can scale beyond this capacity if you add more scaling conditions. </p> <note> <p>You must specify at least one of the following properties: <code>MaxSize</code>, <code>MinSize</code>, or <code>DesiredCapacity</code>. </p> </note>"""
    time_zone: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>Specifies the time zone for a cron expression. If a time zone is not provided, UTC is used by default. </p> <p>Valid values are the canonical names of the IANA time zones, derived from the IANA Time Zone Database (such as <code>Etc/GMT+9</code> or <code>Pacific/Tahiti</code>). For more information, see <a href="https://en.wikipedia.org/wiki/List_of_tz_database_time_zones">https://en.wikipedia.org/wiki/List_of_tz_database_time_zones</a>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: PutScheduledUpdateGroupActionType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "auto_scaling_group_name" in value:
        pairs.append(
            (f"{key_prefix}AutoScalingGroupName", str(value["auto_scaling_group_name"]))
        )
    if "scheduled_action_name" in value:
        pairs.append(
            (f"{key_prefix}ScheduledActionName", str(value["scheduled_action_name"]))
        )
    if "time" in value:
        import capo_auto_scaling.types.timestamp_type

        capo_auto_scaling.types.timestamp_type.serialize_query(
            value["time"], pairs, f"{key_prefix}Time"
        )
    if "start_time" in value:
        import capo_auto_scaling.types.timestamp_type

        capo_auto_scaling.types.timestamp_type.serialize_query(
            value["start_time"], pairs, f"{key_prefix}StartTime"
        )
    if "end_time" in value:
        import capo_auto_scaling.types.timestamp_type

        capo_auto_scaling.types.timestamp_type.serialize_query(
            value["end_time"], pairs, f"{key_prefix}EndTime"
        )
    if "recurrence" in value:
        pairs.append((f"{key_prefix}Recurrence", str(value["recurrence"])))
    if "min_size" in value:
        pairs.append((f"{key_prefix}MinSize", str(value["min_size"])))
    if "max_size" in value:
        pairs.append((f"{key_prefix}MaxSize", str(value["max_size"])))
    if "desired_capacity" in value:
        pairs.append((f"{key_prefix}DesiredCapacity", str(value["desired_capacity"])))
    if "time_zone" in value:
        pairs.append((f"{key_prefix}TimeZone", str(value["time_zone"])))


def deserialize_query(el: Element) -> PutScheduledUpdateGroupActionType:
    out: PutScheduledUpdateGroupActionType = {}  # type: ignore[typeddict-item]
    child_auto_scaling_group_name = el.find("AutoScalingGroupName")
    if child_auto_scaling_group_name is not None:
        out["auto_scaling_group_name"] = str(child_auto_scaling_group_name.text or "")
    child_scheduled_action_name = el.find("ScheduledActionName")
    if child_scheduled_action_name is not None:
        out["scheduled_action_name"] = str(child_scheduled_action_name.text or "")
    child_time = el.find("Time")
    if child_time is not None:
        import capo_auto_scaling.types.timestamp_type

        out["time"] = capo_auto_scaling.types.timestamp_type.deserialize_query(
            child_time
        )
    child_start_time = el.find("StartTime")
    if child_start_time is not None:
        import capo_auto_scaling.types.timestamp_type

        out["start_time"] = capo_auto_scaling.types.timestamp_type.deserialize_query(
            child_start_time
        )
    child_end_time = el.find("EndTime")
    if child_end_time is not None:
        import capo_auto_scaling.types.timestamp_type

        out["end_time"] = capo_auto_scaling.types.timestamp_type.deserialize_query(
            child_end_time
        )
    child_recurrence = el.find("Recurrence")
    if child_recurrence is not None:
        out["recurrence"] = str(child_recurrence.text or "")
    child_min_size = el.find("MinSize")
    if child_min_size is not None:
        out["min_size"] = int(child_min_size.text or "")
    child_max_size = el.find("MaxSize")
    if child_max_size is not None:
        out["max_size"] = int(child_max_size.text or "")
    child_desired_capacity = el.find("DesiredCapacity")
    if child_desired_capacity is not None:
        out["desired_capacity"] = int(child_desired_capacity.text or "")
    child_time_zone = el.find("TimeZone")
    if child_time_zone is not None:
        out["time_zone"] = str(child_time_zone.text or "")
    return out
