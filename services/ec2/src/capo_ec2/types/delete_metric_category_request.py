"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteMetricCategoryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.metric_category_id


class DeleteMetricCategoryRequest(TypedDict, closed=True):
    metric_category_id: NotRequired[
        "capo_ec2.types.metric_category_id.MetricCategoryId"
    ]
    """<p>The ID of the metric category.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteMetricCategoryRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "metric_category_id" in value:
        pairs.append(
            (f"{key_prefix}MetricCategoryId", str(value["metric_category_id"]))
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> DeleteMetricCategoryRequest:
    out: DeleteMetricCategoryRequest = {}  # type: ignore[typeddict-item]
    child_metric_category_id = el.find("MetricCategoryId")
    if child_metric_category_id is not None:
        out["metric_category_id"] = str(child_metric_category_id.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
