"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyMetricCategoryResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.metric_category


class ModifyMetricCategoryResult(TypedDict, closed=True):
    metric_category: NotRequired["capo_ec2.types.metric_category.MetricCategory"]
    """<p>Information about the metric category.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyMetricCategoryResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "metric_category" in value:
        import capo_ec2.types.metric_category

        capo_ec2.types.metric_category.serialize_ec2_query(
            value["metric_category"], pairs, f"{key_prefix}MetricCategory"
        )


def deserialize_ec2_query(el: Element) -> ModifyMetricCategoryResult:
    out: ModifyMetricCategoryResult = {}  # type: ignore[typeddict-item]
    child_metric_category = el.find("metricCategory")
    if child_metric_category is not None:
        import capo_ec2.types.metric_category

        out["metric_category"] = capo_ec2.types.metric_category.deserialize_ec2_query(
            child_metric_category
        )
    return out
