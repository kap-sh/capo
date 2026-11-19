"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteMetricCategoryResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.metric_category_id


class DeleteMetricCategoryResult(TypedDict, closed=True):
    metric_category_id: NotRequired[
        "capo_ec2.types.metric_category_id.MetricCategoryId"
    ]
    """<p>The ID of the metric category that was deleted.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteMetricCategoryResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "metric_category_id" in value:
        pairs.append(
            (f"{key_prefix}MetricCategoryId", str(value["metric_category_id"]))
        )


def deserialize_ec2_query(el: Element) -> DeleteMetricCategoryResult:
    out: DeleteMetricCategoryResult = {}  # type: ignore[typeddict-item]
    child_metric_category_id = el.find("metricCategoryId")
    if child_metric_category_id is not None:
        out["metric_category_id"] = str(child_metric_category_id.text or "")
    return out
