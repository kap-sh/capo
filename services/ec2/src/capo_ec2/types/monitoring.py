"""Generated from Smithy shape ``com.amazonaws.ec2#Monitoring``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.metric_category_id_list
    import capo_ec2.types.monitoring_state


class Monitoring(TypedDict, closed=True):
    metric_category_ids: NotRequired[
        "capo_ec2.types.metric_category_id_list.MetricCategoryIdList"
    ]
    """<p>The IDs of the metric categories that are associated with the instance.</p>"""
    state: NotRequired["capo_ec2.types.monitoring_state.MonitoringState"]
    """<p>Indicates whether detailed monitoring is enabled. Otherwise, basic monitoring is enabled.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: Monitoring, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "metric_category_ids" in value:
        import capo_ec2.types.metric_category_id_list

        capo_ec2.types.metric_category_id_list.serialize_ec2_query(
            value["metric_category_ids"], pairs, f"{key_prefix}MetricCategoryIdSet"
        )
    if "state" in value:
        import capo_ec2.types.monitoring_state

        capo_ec2.types.monitoring_state.serialize_ec2_query(
            value["state"], pairs, f"{key_prefix}State"
        )


def deserialize_ec2_query(el: Element) -> Monitoring:
    out: Monitoring = {}  # type: ignore[typeddict-item]
    child_metric_category_ids = el.find("metricCategoryIdSet")
    if child_metric_category_ids is not None:
        import capo_ec2.types.metric_category_id_list

        out["metric_category_ids"] = (
            capo_ec2.types.metric_category_id_list.deserialize_ec2_query(
                child_metric_category_ids
            )
        )
    child_state = el.find("state")
    if child_state is not None:
        import capo_ec2.types.monitoring_state

        out["state"] = capo_ec2.types.monitoring_state.deserialize_ec2_query(
            child_state
        )
    return out
