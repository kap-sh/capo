"""Generated from Smithy shape ``com.amazonaws.autoscaling#DescribeScalingActivitiesType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.activity_ids
    import capo_auto_scaling.types.filters
    import capo_auto_scaling.types.include_deleted_groups
    import capo_auto_scaling.types.max_records
    import capo_auto_scaling.types.xml_string
    import capo_auto_scaling.types.xml_string_max_len255


class DescribeScalingActivitiesType(TypedDict, closed=True):
    activity_ids: NotRequired["capo_auto_scaling.types.activity_ids.ActivityIds"]
    """<p> The activity IDs of the desired scaling activities. If unknown activity IDs are requested, they are ignored with no error. Only activities started within the last six weeks can be returned regardless of the activity IDs specified. If other filters are specified with the request, only results matching all filter criteria can be returned. </p> <p>Array Members: Maximum number of 50 IDs.</p>"""
    auto_scaling_group_name: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>The name of the Auto Scaling group.</p> <important> <p> Omitting this property performs an account-wide operation, which can result in slower or timed-out requests. </p> </important>"""
    include_deleted_groups: NotRequired[
        "capo_auto_scaling.types.include_deleted_groups.IncludeDeletedGroups"
    ]
    """<p>Indicates whether to include scaling activity from deleted Auto Scaling groups.</p>"""
    max_records: NotRequired["capo_auto_scaling.types.max_records.MaxRecords"]
    """<p>The maximum number of items to return with this call. The default value is <code>100</code> and the maximum value is <code>100</code>.</p>"""
    next_token: NotRequired["capo_auto_scaling.types.xml_string.XmlString"]
    """<p>The token for the next set of items to return. (You received this token from a previous call.)</p>"""
    filters: NotRequired["capo_auto_scaling.types.filters.Filters"]
    """<p> One or more filters to limit the results based on specific criteria. The following filters are supported: </p> <ul> <li> <p> <code>StartTimeLowerBound</code> - The earliest scaling activities to return based on the activity start time. Scaling activities with a start time earlier than this value are not included in the results. Only activities started within the last six weeks can be returned regardless of the value specified. </p> </li> <li> <p> <code>StartTimeUpperBound</code> - The latest scaling activities to return based on the activity start time. Scaling activities with a start time later than this value are not included in the results. Only activities started within the last six weeks can be returned regardless of the value specified. </p> </li> <li> <p> <code>Status</code> - The <code>StatusCode</code> value of the scaling activity. This filter can only be used in combination with the <code>AutoScalingGroupName</code> parameter. For valid <code>StatusCode</code> values, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_Activity.html">Activity</a> in the <i>Amazon EC2 Auto Scaling API Reference</i>. </p> </li> </ul> <p> <code>StartTimeLowerBound</code> and <code>StartTimeUpperBound</code> accept ISO 8601 formatted timestamps. Timestamps without a timezone offset are assumed to be UTC. </p> <ul> <li> <p> <code>2000-01-18T08:15:00Z</code> </p> </li> <li> <p> <code>2000-01-18T16:15:00+08:00</code> </p> </li> </ul>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeScalingActivitiesType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "activity_ids" in value:
        import capo_auto_scaling.types.activity_ids

        capo_auto_scaling.types.activity_ids.serialize_query(
            value["activity_ids"], pairs, f"{key_prefix}ActivityIds"
        )
    if "auto_scaling_group_name" in value:
        pairs.append(
            (f"{key_prefix}AutoScalingGroupName", str(value["auto_scaling_group_name"]))
        )
    if "include_deleted_groups" in value:
        pairs.append(
            (
                f"{key_prefix}IncludeDeletedGroups",
                "true" if value["include_deleted_groups"] else "false",
            )
        )
    if "max_records" in value:
        pairs.append((f"{key_prefix}MaxRecords", str(value["max_records"])))
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "filters" in value:
        import capo_auto_scaling.types.filters

        capo_auto_scaling.types.filters.serialize_query(
            value["filters"], pairs, f"{key_prefix}Filters"
        )


def deserialize_query(el: Element) -> DescribeScalingActivitiesType:
    out: DescribeScalingActivitiesType = {}  # type: ignore[typeddict-item]
    child_activity_ids = el.find("ActivityIds")
    if child_activity_ids is not None:
        import capo_auto_scaling.types.activity_ids

        out["activity_ids"] = capo_auto_scaling.types.activity_ids.deserialize_query(
            child_activity_ids
        )
    child_auto_scaling_group_name = el.find("AutoScalingGroupName")
    if child_auto_scaling_group_name is not None:
        out["auto_scaling_group_name"] = str(child_auto_scaling_group_name.text or "")
    child_include_deleted_groups = el.find("IncludeDeletedGroups")
    if child_include_deleted_groups is not None:
        out["include_deleted_groups"] = (
            child_include_deleted_groups.text or ""
        ).lower() == "true"
    child_max_records = el.find("MaxRecords")
    if child_max_records is not None:
        out["max_records"] = int(child_max_records.text or "")
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_filters = el.find("Filters")
    if child_filters is not None:
        import capo_auto_scaling.types.filters

        out["filters"] = capo_auto_scaling.types.filters.deserialize_query(
            child_filters
        )
    return out
