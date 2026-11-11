"""Generated from Smithy shape ``com.amazonaws.autoscaling#DescribeScheduledActionsType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.include_managed_resources
    import capo_auto_scaling.types.max_records
    import capo_auto_scaling.types.scheduled_action_names
    import capo_auto_scaling.types.timestamp_type
    import capo_auto_scaling.types.xml_string
    import capo_auto_scaling.types.xml_string_max_len255


class DescribeScheduledActionsType(TypedDict, closed=True):
    auto_scaling_group_name: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>The name of the Auto Scaling group.</p>"""
    scheduled_action_names: NotRequired[
        "capo_auto_scaling.types.scheduled_action_names.ScheduledActionNames"
    ]
    """<p>The names of one or more scheduled actions. If you omit this property, all scheduled actions are described. If you specify an unknown scheduled action, it is ignored with no error.</p> <p>Array Members: Maximum number of 50 actions.</p>"""
    start_time: NotRequired["capo_auto_scaling.types.timestamp_type.TimestampType"]
    """<p>The earliest scheduled start time to return. If scheduled action names are provided, this property is ignored.</p>"""
    end_time: NotRequired["capo_auto_scaling.types.timestamp_type.TimestampType"]
    """<p>The latest scheduled start time to return. If scheduled action names are provided, this property is ignored.</p>"""
    include_managed_resources: NotRequired[
        "capo_auto_scaling.types.include_managed_resources.IncludeManagedResources"
    ]
    """<p> Specifies whether to include scheduled actions for managed Auto Scaling groups in the response. When set to <code>true</code> (default), the response includes scheduled actions for managed Auto Scaling groups. </p>"""
    next_token: NotRequired["capo_auto_scaling.types.xml_string.XmlString"]
    """<p>The token for the next set of items to return. (You received this token from a previous call.)</p>"""
    max_records: NotRequired["capo_auto_scaling.types.max_records.MaxRecords"]
    """<p>The maximum number of items to return with this call. The default value is <code>50</code> and the maximum value is <code>100</code>.</p> <p>A response can contain fewer items than the value specified by <code>MaxRecords</code>, even when more items are available. To retrieve the additional items, use the <code>NextToken</code> value in a subsequent call rather than relying on the number of items in the response.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeScheduledActionsType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "auto_scaling_group_name" in value:
        pairs.append(
            (f"{key_prefix}AutoScalingGroupName", str(value["auto_scaling_group_name"]))
        )
    if "scheduled_action_names" in value:
        import capo_auto_scaling.types.scheduled_action_names

        capo_auto_scaling.types.scheduled_action_names.serialize_query(
            value["scheduled_action_names"], pairs, f"{key_prefix}ScheduledActionNames"
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
    if "include_managed_resources" in value:
        pairs.append(
            (
                f"{key_prefix}IncludeManagedResources",
                "true" if value["include_managed_resources"] else "false",
            )
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "max_records" in value:
        pairs.append((f"{key_prefix}MaxRecords", str(value["max_records"])))


def deserialize_query(el: Element) -> DescribeScheduledActionsType:
    out: DescribeScheduledActionsType = {}  # type: ignore[typeddict-item]
    child_auto_scaling_group_name = el.find("AutoScalingGroupName")
    if child_auto_scaling_group_name is not None:
        out["auto_scaling_group_name"] = str(child_auto_scaling_group_name.text or "")
    child_scheduled_action_names = el.find("ScheduledActionNames")
    if child_scheduled_action_names is not None:
        import capo_auto_scaling.types.scheduled_action_names

        out["scheduled_action_names"] = (
            capo_auto_scaling.types.scheduled_action_names.deserialize_query(
                child_scheduled_action_names
            )
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
    child_include_managed_resources = el.find("IncludeManagedResources")
    if child_include_managed_resources is not None:
        out["include_managed_resources"] = (
            child_include_managed_resources.text or ""
        ).lower() == "true"
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_max_records = el.find("MaxRecords")
    if child_max_records is not None:
        out["max_records"] = int(child_max_records.text or "")
    return out
