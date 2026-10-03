"""Generated from Smithy shape ``com.amazonaws.autoscaling#Filter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.values
    import capo_auto_scaling.types.xml_string


class Filter(TypedDict, closed=True):
    name: NotRequired["capo_auto_scaling.types.xml_string.XmlString"]
    """<p>The name of the filter.</p> <p> The valid values for <code>Name</code> depend on which API operation you're using with the filter. </p> <p> <b> <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeAutoScalingGroups.html">DescribeAutoScalingGroups</a> </b> </p> <p>Valid values for <code>Name</code> include the following: </p> <ul> <li> <p> <code>tag-key</code> - Accepts tag keys. The results only include information about the Auto Scaling groups associated with these tag keys. </p> </li> <li> <p> <code>tag-value</code> - Accepts tag values. The results only include information about the Auto Scaling groups associated with these tag values. </p> </li> <li> <p> <code>tag:<key></code> - Accepts the key/value combination of the tag. Use the tag key in the filter name and the tag value as the filter value. The results only include information about the Auto Scaling groups associated with the specified key/value combination. </p> </li> </ul> <p> <b> <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeTags.html">DescribeTags</a> </b> </p> <p>Valid values for <code>Name</code> include the following: </p> <ul> <li> <p> <code>auto-scaling-group</code> - Accepts the names of Auto Scaling groups. The results only include information about the tags associated with these Auto Scaling groups. </p> </li> <li> <p> <code>key</code> - Accepts tag keys. The results only include information about the tags associated with these tag keys. </p> </li> <li> <p> <code>value</code> - Accepts tag values. The results only include information about the tags associated with these tag values. </p> </li> <li> <p> <code>propagate-at-launch</code> - Accepts a Boolean value, which specifies whether tags propagate to instances at launch. The results only include information about the tags associated with the specified Boolean value. </p> </li> </ul> <p> <b> <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeScalingActivities.html">DescribeScalingActivities</a> </b> </p> <p>Valid values for <code>Name</code> include the following: </p> <ul> <li> <p> <code>StartTimeLowerBound</code> - The earliest scaling activities to return based on the activity start time. Scaling activities with a start time earlier than this value are not included in the results. Only activities started within the last six weeks can be returned regardless of the value specified. </p> </li> <li> <p> <code>StartTimeUpperBound</code> - The latest scaling activities to return based on the activity start time. Scaling activities with a start time later than this value are not included in the results. Only activities started within the last six weeks can be returned regardless of the value specified. </p> </li> <li> <p> <code>Status</code> - The <code>StatusCode</code> value of the scaling activity. This filter can only be used in combination with the <code>AutoScalingGroupName</code> parameter. For valid <code>StatusCode</code> values, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_Activity.html">Activity</a> in the <i>Amazon EC2 Auto Scaling API Reference</i>. </p> </li> </ul> <p> <code>StartTimeLowerBound</code> and <code>StartTimeUpperBound</code> accept ISO 8601 formatted timestamps. Timestamps without a timezone offset are assumed to be UTC. </p> <ul> <li> <p> <code>2000-01-18T08:15:00Z</code> </p> </li> <li> <p> <code>2000-01-18T16:15:00+08:00</code> </p> </li> </ul>"""
    values: NotRequired["capo_auto_scaling.types.values.Values"]
    """<p>One or more filter values. Filter values are case-sensitive. </p> <p>If you specify multiple values for a filter, the values are automatically logically joined with an <code>OR</code>, and the request returns all results that match any of the specified values.</p> <p> <b>DescribeAutoScalingGroups example:</b> Specify "tag:environment" for the filter name and "production,development" for the filter values to find Auto Scaling groups with the tag "environment=production" or "environment=development". </p> <p> <b>DescribeScalingActivities example:</b> Specify "Status" for the filter name and "Successful,Failed" for the filter values to find scaling activities with a status of either "Successful" or "Failed". </p>"""


# --- awsQuery ser/de ---
def serialize_query(value: Filter, pairs: list[tuple[str, str]], prefix: str) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "name" in value:
        pairs.append((f"{key_prefix}Name", str(value["name"])))
    if "values" in value:
        import capo_auto_scaling.types.values

        capo_auto_scaling.types.values.serialize_query(
            value["values"], pairs, f"{key_prefix}Values"
        )


def deserialize_query(el: Element) -> Filter:
    out: Filter = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    child_values = el.find("Values")
    if child_values is not None:
        import capo_auto_scaling.types.values

        out["values"] = capo_auto_scaling.types.values.deserialize_query(child_values)
    return out
