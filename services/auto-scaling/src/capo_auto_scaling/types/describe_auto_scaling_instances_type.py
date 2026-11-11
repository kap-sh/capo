"""Generated from Smithy shape ``com.amazonaws.autoscaling#DescribeAutoScalingInstancesType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.include_managed_resources
    import capo_auto_scaling.types.instance_ids
    import capo_auto_scaling.types.max_records
    import capo_auto_scaling.types.xml_string


class DescribeAutoScalingInstancesType(TypedDict, closed=True):
    instance_ids: NotRequired["capo_auto_scaling.types.instance_ids.InstanceIds"]
    """<p>The IDs of the instances. If you omit this property, all Auto Scaling instances are described. If you specify an ID that does not exist, it is ignored with no error.</p> <p>Array Members: Maximum number of 50 items.</p>"""
    include_managed_resources: NotRequired[
        "capo_auto_scaling.types.include_managed_resources.IncludeManagedResources"
    ]
    """<p> Specifies whether to include managed Auto Scaling instances in the response. When set to <code>true</code> (default), the response includes managed Auto Scaling instances. </p>"""
    max_records: NotRequired["capo_auto_scaling.types.max_records.MaxRecords"]
    """<p>The maximum number of items to return with this call. The default value is <code>50</code> and the maximum value is <code>50</code>.</p> <p>A response can contain fewer items than the value specified by <code>MaxRecords</code>, even when more items are available. To retrieve the additional items, use the <code>NextToken</code> value in a subsequent call rather than relying on the number of items in the response.</p>"""
    next_token: NotRequired["capo_auto_scaling.types.xml_string.XmlString"]
    """<p>The token for the next set of items to return. (You received this token from a previous call.)</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeAutoScalingInstancesType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "instance_ids" in value:
        import capo_auto_scaling.types.instance_ids

        capo_auto_scaling.types.instance_ids.serialize_query(
            value["instance_ids"], pairs, f"{key_prefix}InstanceIds"
        )
    if "include_managed_resources" in value:
        pairs.append(
            (
                f"{key_prefix}IncludeManagedResources",
                "true" if value["include_managed_resources"] else "false",
            )
        )
    if "max_records" in value:
        pairs.append((f"{key_prefix}MaxRecords", str(value["max_records"])))
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> DescribeAutoScalingInstancesType:
    out: DescribeAutoScalingInstancesType = {}  # type: ignore[typeddict-item]
    child_instance_ids = el.find("InstanceIds")
    if child_instance_ids is not None:
        import capo_auto_scaling.types.instance_ids

        out["instance_ids"] = capo_auto_scaling.types.instance_ids.deserialize_query(
            child_instance_ids
        )
    child_include_managed_resources = el.find("IncludeManagedResources")
    if child_include_managed_resources is not None:
        out["include_managed_resources"] = (
            child_include_managed_resources.text or ""
        ).lower() == "true"
    child_max_records = el.find("MaxRecords")
    if child_max_records is not None:
        out["max_records"] = int(child_max_records.text or "")
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
