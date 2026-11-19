"""Generated from Smithy shape ``com.amazonaws.ec2#UnmonitorInstancesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.instance_id_string_list
    import capo_ec2.types.metric_category_id_list


class UnmonitorInstancesRequest(TypedDict, closed=True):
    instance_ids: NotRequired[
        "capo_ec2.types.instance_id_string_list.InstanceIdStringList"
    ]
    """<p>The IDs of the instances.</p>"""
    metric_category_ids: NotRequired[
        "capo_ec2.types.metric_category_id_list.MetricCategoryIdList"
    ]
    """<p>The IDs of the metric categories to remove from the instances. If you specify metric categories, only those metric categories are removed and detailed monitoring remains enabled. If you don't specify metric categories, detailed monitoring and all metric categories are turned off.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: UnmonitorInstancesRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "instance_ids" in value:
        import capo_ec2.types.instance_id_string_list

        capo_ec2.types.instance_id_string_list.serialize_ec2_query(
            value["instance_ids"], pairs, f"{key_prefix}InstanceId"
        )
    if "metric_category_ids" in value:
        import capo_ec2.types.metric_category_id_list

        capo_ec2.types.metric_category_id_list.serialize_ec2_query(
            value["metric_category_ids"], pairs, f"{key_prefix}MetricCategoryId"
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> UnmonitorInstancesRequest:
    out: UnmonitorInstancesRequest = {}  # type: ignore[typeddict-item]
    child_instance_ids = el.find("InstanceId")
    if child_instance_ids is not None:
        import capo_ec2.types.instance_id_string_list

        out["instance_ids"] = (
            capo_ec2.types.instance_id_string_list.deserialize_ec2_query(
                child_instance_ids
            )
        )
    child_metric_category_ids = el.find("MetricCategoryId")
    if child_metric_category_ids is not None:
        import capo_ec2.types.metric_category_id_list

        out["metric_category_ids"] = (
            capo_ec2.types.metric_category_id_list.deserialize_ec2_query(
                child_metric_category_ids
            )
        )
    child_dry_run = el.find("dryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
