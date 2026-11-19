"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyMetricCategoryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.metric_category_id
    import capo_ec2.types.metric_category_metric_name_list


class ModifyMetricCategoryRequest(TypedDict, closed=True):
    metric_category_id: NotRequired[
        "capo_ec2.types.metric_category_id.MetricCategoryId"
    ]
    """<p>The ID of the metric category.</p>"""
    metrics: NotRequired[
        "capo_ec2.types.metric_category_metric_name_list.MetricCategoryMetricNameList"
    ]
    """<p>The names of the metrics for the metric category. These metrics replace the existing metrics, and must differ from the current set.</p> <p>Specify each metric by its Amazon CloudWatch metric name or its OpenTelemetry metric name. The two names for a measurement are separate entries, and you can include both.</p> <p>In Regions where Amazon CloudWatch OpenTelemetry metrics aren't available, you can't specify OpenTelemetry metric names.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyMetricCategoryRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "metric_category_id" in value:
        pairs.append(
            (f"{key_prefix}MetricCategoryId", str(value["metric_category_id"]))
        )
    if "metrics" in value:
        import capo_ec2.types.metric_category_metric_name_list

        capo_ec2.types.metric_category_metric_name_list.serialize_ec2_query(
            value["metrics"], pairs, f"{key_prefix}Metric"
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> ModifyMetricCategoryRequest:
    out: ModifyMetricCategoryRequest = {}  # type: ignore[typeddict-item]
    child_metric_category_id = el.find("MetricCategoryId")
    if child_metric_category_id is not None:
        out["metric_category_id"] = str(child_metric_category_id.text or "")
    child_metrics = el.find("Metric")
    if child_metrics is not None:
        import capo_ec2.types.metric_category_metric_name_list

        out["metrics"] = (
            capo_ec2.types.metric_category_metric_name_list.deserialize_ec2_query(
                child_metrics
            )
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
