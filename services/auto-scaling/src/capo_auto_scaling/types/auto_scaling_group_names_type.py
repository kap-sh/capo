"""Generated from Smithy shape ``com.amazonaws.autoscaling#AutoScalingGroupNamesType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.auto_scaling_group_names
    import capo_auto_scaling.types.filters
    import capo_auto_scaling.types.include_instances
    import capo_auto_scaling.types.include_managed_resources
    import capo_auto_scaling.types.max_records
    import capo_auto_scaling.types.xml_string


class AutoScalingGroupNamesType(TypedDict, closed=True):
    auto_scaling_group_names: NotRequired[
        "capo_auto_scaling.types.auto_scaling_group_names.AutoScalingGroupNames"
    ]
    """<p>The names of the Auto Scaling groups. By default, you can only specify up to 50 names. You can optionally increase this limit using the <code>MaxRecords</code> property.</p> <p>If you omit this property, all Auto Scaling groups are described.</p>"""
    include_instances: NotRequired[
        "capo_auto_scaling.types.include_instances.IncludeInstances"
    ]
    """<p> Specifies whether to include information about Amazon EC2 instances in the response. When set to <code>true</code> (default), the response includes instance details. </p>"""
    include_managed_resources: NotRequired[
        "capo_auto_scaling.types.include_managed_resources.IncludeManagedResources"
    ]
    """<p> Specifies whether to include managed Auto Scaling groups in the response. When set to <code>true</code> (default), the response includes managed Auto Scaling groups. </p>"""
    next_token: NotRequired["capo_auto_scaling.types.xml_string.XmlString"]
    """<p>The token for the next set of items to return. (You received this token from a previous call.)</p>"""
    max_records: NotRequired["capo_auto_scaling.types.max_records.MaxRecords"]
    """<p>The maximum number of items to return with this call. The default value is <code>50</code> and the maximum value is <code>100</code>.</p> <p>A response can contain fewer items than the value specified by <code>MaxRecords</code>, even when more items are available. To retrieve the additional items, use the <code>NextToken</code> value in a subsequent call rather than relying on the number of items in the response.</p>"""
    filters: NotRequired["capo_auto_scaling.types.filters.Filters"]
    """<p>One or more filters to limit the results based on specific tags. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AutoScalingGroupNamesType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "auto_scaling_group_names" in value:
        import capo_auto_scaling.types.auto_scaling_group_names

        capo_auto_scaling.types.auto_scaling_group_names.serialize_query(
            value["auto_scaling_group_names"],
            pairs,
            f"{key_prefix}AutoScalingGroupNames",
        )
    if "include_instances" in value:
        pairs.append(
            (
                f"{key_prefix}IncludeInstances",
                "true" if value["include_instances"] else "false",
            )
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
    if "filters" in value:
        import capo_auto_scaling.types.filters

        capo_auto_scaling.types.filters.serialize_query(
            value["filters"], pairs, f"{key_prefix}Filters"
        )


def deserialize_query(el: Element) -> AutoScalingGroupNamesType:
    out: AutoScalingGroupNamesType = {}  # type: ignore[typeddict-item]
    child_auto_scaling_group_names = el.find("AutoScalingGroupNames")
    if child_auto_scaling_group_names is not None:
        import capo_auto_scaling.types.auto_scaling_group_names

        out["auto_scaling_group_names"] = (
            capo_auto_scaling.types.auto_scaling_group_names.deserialize_query(
                child_auto_scaling_group_names
            )
        )
    child_include_instances = el.find("IncludeInstances")
    if child_include_instances is not None:
        out["include_instances"] = (
            child_include_instances.text or ""
        ).lower() == "true"
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
    child_filters = el.find("Filters")
    if child_filters is not None:
        import capo_auto_scaling.types.filters

        out["filters"] = capo_auto_scaling.types.filters.deserialize_query(
            child_filters
        )
    return out
