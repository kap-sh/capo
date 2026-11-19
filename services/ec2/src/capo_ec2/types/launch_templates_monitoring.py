"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplatesMonitoring``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.metric_category_id_list


class LaunchTemplatesMonitoring(TypedDict, closed=True):
    enabled: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether detailed monitoring is enabled. Otherwise, basic monitoring is enabled.</p>"""
    metric_category_ids: NotRequired[
        "capo_ec2.types.metric_category_id_list.MetricCategoryIdList"
    ]
    """<p>The IDs of the metric categories to associate with the instance.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: LaunchTemplatesMonitoring, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "enabled" in value:
        pairs.append((f"{key_prefix}Enabled", "true" if value["enabled"] else "false"))
    if "metric_category_ids" in value:
        import capo_ec2.types.metric_category_id_list

        capo_ec2.types.metric_category_id_list.serialize_ec2_query(
            value["metric_category_ids"], pairs, f"{key_prefix}MetricCategoryIdSet"
        )


def deserialize_ec2_query(el: Element) -> LaunchTemplatesMonitoring:
    out: LaunchTemplatesMonitoring = {}  # type: ignore[typeddict-item]
    child_enabled = el.find("enabled")
    if child_enabled is not None:
        out["enabled"] = (child_enabled.text or "").lower() == "true"
    child_metric_category_ids = el.find("metricCategoryIdSet")
    if child_metric_category_ids is not None:
        import capo_ec2.types.metric_category_id_list

        out["metric_category_ids"] = (
            capo_ec2.types.metric_category_id_list.deserialize_ec2_query(
                child_metric_category_ids
            )
        )
    return out
