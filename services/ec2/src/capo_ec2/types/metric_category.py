"""Generated from Smithy shape ``com.amazonaws.ec2#MetricCategory``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.metric_category_id
    import capo_ec2.types.metric_category_metric_name_list
    import capo_ec2.types.tag_list


class MetricCategory(TypedDict, closed=True):
    metric_category_id: NotRequired[
        "capo_ec2.types.metric_category_id.MetricCategoryId"
    ]
    """<p>The ID of the metric category.</p>"""
    metrics: NotRequired[
        "capo_ec2.types.metric_category_metric_name_list.MetricCategoryMetricNameList"
    ]
    """<p>The names of the metrics in the metric category.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>Any tags assigned to the metric category.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: MetricCategory, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "metric_category_id" in value:
        pairs.append(
            (f"{key_prefix}MetricCategoryId", str(value["metric_category_id"]))
        )
    if "metrics" in value:
        import capo_ec2.types.metric_category_metric_name_list

        capo_ec2.types.metric_category_metric_name_list.serialize_ec2_query(
            value["metrics"], pairs, f"{key_prefix}MetricSet"
        )
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )


def deserialize_ec2_query(el: Element) -> MetricCategory:
    out: MetricCategory = {}  # type: ignore[typeddict-item]
    child_metric_category_id = el.find("metricCategoryId")
    if child_metric_category_id is not None:
        out["metric_category_id"] = str(child_metric_category_id.text or "")
    child_metrics = el.find("metricSet")
    if child_metrics is not None:
        import capo_ec2.types.metric_category_metric_name_list

        out["metrics"] = (
            capo_ec2.types.metric_category_metric_name_list.deserialize_ec2_query(
                child_metrics
            )
        )
    child_tags = el.find("tagSet")
    if child_tags is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(child_tags)
    return out
