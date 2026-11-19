"""Generated from Smithy shape ``com.amazonaws.cloudwatch#UpdateResourceMetricsConfigurationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.resource_arn
    import capo_cloudwatch.types.resource_metric_selection_list


class UpdateResourceMetricsConfigurationInput(TypedDict, closed=True):
    resource_arn: NotRequired["capo_cloudwatch.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the Amazon Web Services resource to update the resource metrics configuration for.</p>"""
    metric_selections: NotRequired[
        "capo_cloudwatch.types.resource_metric_selection_list.ResourceMetricSelectionList"
    ]
    """<p>Specifies which metrics Amazon CloudWatch collects for the resource. The selections that you provide completely replace any existing metric selections.</p> <p>If you omit this parameter, Amazon CloudWatch removes any existing metric selection filter and collects all available detailed metrics for the resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateResourceMetricsConfigurationInput) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "metric_selections" in value:
        import capo_cloudwatch.types.resource_metric_selection_list

        out["MetricSelections"] = (
            capo_cloudwatch.types.resource_metric_selection_list.serialize_aws_json_1_0(
                value["metric_selections"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateResourceMetricsConfigurationInput:
    out: UpdateResourceMetricsConfigurationInput = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    if data.get("MetricSelections") is not None:
        import capo_cloudwatch.types.resource_metric_selection_list

        out["metric_selections"] = (
            capo_cloudwatch.types.resource_metric_selection_list.deserialize_aws_json_1_0(
                data["MetricSelections"]
            )
        )
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: UpdateResourceMetricsConfigurationInput,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "resource_arn" in value:
        pairs.append((f"{key_prefix}ResourceArn", str(value["resource_arn"])))
    if "metric_selections" in value:
        import capo_cloudwatch.types.resource_metric_selection_list

        capo_cloudwatch.types.resource_metric_selection_list.serialize_query(
            value["metric_selections"], pairs, f"{key_prefix}MetricSelections"
        )


def deserialize_query(el: Element) -> UpdateResourceMetricsConfigurationInput:
    out: UpdateResourceMetricsConfigurationInput = {}  # type: ignore[typeddict-item]
    child_resource_arn = el.find("ResourceArn")
    if child_resource_arn is not None:
        out["resource_arn"] = str(child_resource_arn.text or "")
    child_metric_selections = el.find("MetricSelections")
    if child_metric_selections is not None:
        import capo_cloudwatch.types.resource_metric_selection_list

        out["metric_selections"] = (
            capo_cloudwatch.types.resource_metric_selection_list.deserialize_query(
                child_metric_selections
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateResourceMetricsConfigurationInput) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "metric_selections" in value:
        import capo_cloudwatch.types.resource_metric_selection_list

        out["MetricSelections"] = (
            capo_cloudwatch.types.resource_metric_selection_list.serialize_cbor(
                value["metric_selections"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> UpdateResourceMetricsConfigurationInput:
    out: UpdateResourceMetricsConfigurationInput = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    if data.get("MetricSelections") is not None:
        import capo_cloudwatch.types.resource_metric_selection_list

        out["metric_selections"] = (
            capo_cloudwatch.types.resource_metric_selection_list.deserialize_cbor(
                data["MetricSelections"]
            )
        )
    return out
