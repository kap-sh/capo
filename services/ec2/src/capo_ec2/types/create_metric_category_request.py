"""Generated from Smithy shape ``com.amazonaws.ec2#CreateMetricCategoryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.metric_category_metric_name_list
    import capo_ec2.types.string
    import capo_ec2.types.tag_specification_list


class CreateMetricCategoryRequest(TypedDict, closed=True):
    metrics: NotRequired[
        "capo_ec2.types.metric_category_metric_name_list.MetricCategoryMetricNameList"
    ]
    """<p>The names of the metrics to include in the metric category.</p> <p>Specify each metric by its Amazon CloudWatch metric name or its OpenTelemetry metric name. The two names for a measurement are separate entries, and you can include both.</p> <p>In Regions where Amazon CloudWatch OpenTelemetry metrics aren't available, you can't specify OpenTelemetry metric names.</p>"""
    tag_specifications: NotRequired[
        "capo_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply to the metric category during creation.</p>"""
    client_token: NotRequired["capo_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensure Idempotency</a>.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateMetricCategoryRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "metrics" in value:
        import capo_ec2.types.metric_category_metric_name_list

        capo_ec2.types.metric_category_metric_name_list.serialize_ec2_query(
            value["metrics"], pairs, f"{key_prefix}Metric"
        )
    if "tag_specifications" in value:
        import capo_ec2.types.tag_specification_list

        capo_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{key_prefix}TagSpecification"
        )
    if "client_token" in value:
        pairs.append((f"{key_prefix}ClientToken", str(value["client_token"])))
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> CreateMetricCategoryRequest:
    out: CreateMetricCategoryRequest = {}  # type: ignore[typeddict-item]
    child_metrics = el.find("Metric")
    if child_metrics is not None:
        import capo_ec2.types.metric_category_metric_name_list

        out["metrics"] = (
            capo_ec2.types.metric_category_metric_name_list.deserialize_ec2_query(
                child_metrics
            )
        )
    child_tag_specifications = el.find("TagSpecification")
    if child_tag_specifications is not None:
        import capo_ec2.types.tag_specification_list

        out["tag_specifications"] = (
            capo_ec2.types.tag_specification_list.deserialize_ec2_query(
                child_tag_specifications
            )
        )
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
