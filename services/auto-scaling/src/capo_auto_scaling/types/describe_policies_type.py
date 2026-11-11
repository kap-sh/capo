"""Generated from Smithy shape ``com.amazonaws.autoscaling#DescribePoliciesType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.include_managed_resources
    import capo_auto_scaling.types.max_records
    import capo_auto_scaling.types.policy_names
    import capo_auto_scaling.types.policy_types
    import capo_auto_scaling.types.xml_string
    import capo_auto_scaling.types.xml_string_max_len255


class DescribePoliciesType(TypedDict, closed=True):
    auto_scaling_group_name: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>The name of the Auto Scaling group.</p>"""
    policy_names: NotRequired["capo_auto_scaling.types.policy_names.PolicyNames"]
    """<p>The names of one or more policies. If you omit this property, all policies are described. If a group name is provided, the results are limited to that group. If you specify an unknown policy name, it is ignored with no error.</p> <p>Array Members: Maximum number of 50 items.</p>"""
    policy_types: NotRequired["capo_auto_scaling.types.policy_types.PolicyTypes"]
    """<p>One or more policy types. The valid values are <code>SimpleScaling</code>, <code>StepScaling</code>, <code>TargetTrackingScaling</code>, and <code>PredictiveScaling</code>.</p>"""
    include_managed_resources: NotRequired[
        "capo_auto_scaling.types.include_managed_resources.IncludeManagedResources"
    ]
    """<p> Specifies whether to include scaling policies for managed Auto Scaling groups in the response. When set to <code>true</code> (default), the response includes scaling policies for managed Auto Scaling groups. </p>"""
    next_token: NotRequired["capo_auto_scaling.types.xml_string.XmlString"]
    """<p>The token for the next set of items to return. (You received this token from a previous call.)</p>"""
    max_records: NotRequired["capo_auto_scaling.types.max_records.MaxRecords"]
    """<p>The maximum number of items to be returned with each call. The default value is <code>50</code> and the maximum value is <code>100</code>.</p> <p>A response can contain fewer items than the value specified by <code>MaxRecords</code>, even when more items are available. To retrieve the additional items, use the <code>NextToken</code> value in a subsequent call rather than relying on the number of items in the response.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribePoliciesType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "auto_scaling_group_name" in value:
        pairs.append(
            (f"{key_prefix}AutoScalingGroupName", str(value["auto_scaling_group_name"]))
        )
    if "policy_names" in value:
        import capo_auto_scaling.types.policy_names

        capo_auto_scaling.types.policy_names.serialize_query(
            value["policy_names"], pairs, f"{key_prefix}PolicyNames"
        )
    if "policy_types" in value:
        import capo_auto_scaling.types.policy_types

        capo_auto_scaling.types.policy_types.serialize_query(
            value["policy_types"], pairs, f"{key_prefix}PolicyTypes"
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


def deserialize_query(el: Element) -> DescribePoliciesType:
    out: DescribePoliciesType = {}  # type: ignore[typeddict-item]
    child_auto_scaling_group_name = el.find("AutoScalingGroupName")
    if child_auto_scaling_group_name is not None:
        out["auto_scaling_group_name"] = str(child_auto_scaling_group_name.text or "")
    child_policy_names = el.find("PolicyNames")
    if child_policy_names is not None:
        import capo_auto_scaling.types.policy_names

        out["policy_names"] = capo_auto_scaling.types.policy_names.deserialize_query(
            child_policy_names
        )
    child_policy_types = el.find("PolicyTypes")
    if child_policy_types is not None:
        import capo_auto_scaling.types.policy_types

        out["policy_types"] = capo_auto_scaling.types.policy_types.deserialize_query(
            child_policy_types
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
