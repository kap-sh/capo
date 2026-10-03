"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#MetricFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.apply_on_transformed_logs
    import capo_cloudwatch_logs.types.emit_system_fields
    import capo_cloudwatch_logs.types.field_selection_criteria
    import capo_cloudwatch_logs.types.filter_name
    import capo_cloudwatch_logs.types.filter_pattern
    import capo_cloudwatch_logs.types.log_group_name
    import capo_cloudwatch_logs.types.metric_transformations
    import capo_cloudwatch_logs.types.timestamp


class MetricFilter(TypedDict, closed=True):
    filter_name: NotRequired["capo_cloudwatch_logs.types.filter_name.FilterName"]
    """<p>The name of the metric filter.</p>"""
    filter_pattern: NotRequired[
        "capo_cloudwatch_logs.types.filter_pattern.FilterPattern"
    ]
    metric_transformations: NotRequired[
        "capo_cloudwatch_logs.types.metric_transformations.MetricTransformations"
    ]
    """<p>The metric transformations.</p>"""
    creation_time: NotRequired["capo_cloudwatch_logs.types.timestamp.Timestamp"]
    """<p>The creation time of the metric filter, expressed as the number of milliseconds after <code>Jan 1, 1970 00:00:00 UTC</code>.</p>"""
    log_group_name: NotRequired[
        "capo_cloudwatch_logs.types.log_group_name.LogGroupName"
    ]
    """<p>The name of the log group.</p>"""
    apply_on_transformed_logs: (
        "capo_cloudwatch_logs.types.apply_on_transformed_logs.ApplyOnTransformedLogs"
    )
    """<p>This parameter is valid only for log groups that have an active log transformer. For more information about log transformers, see <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutTransformer.html">PutTransformer</a>.</p> <p>If this value is <code>true</code>, the metric filter is applied on the transformed version of the log events instead of the original ingested log events.</p>"""
    field_selection_criteria: NotRequired[
        "capo_cloudwatch_logs.types.field_selection_criteria.FieldSelectionCriteria"
    ]
    """<p>The filter expression that specifies which log events are processed by this metric filter based on system fields. Returns the <code>fieldSelectionCriteria</code> value if it was specified when the metric filter was created.</p>"""
    emit_system_field_dimensions: NotRequired[
        "capo_cloudwatch_logs.types.emit_system_fields.EmitSystemFields"
    ]
    """<p>The list of system fields that are emitted as additional dimensions in the generated metrics. Returns the <code>emitSystemFieldDimensions</code> value if it was specified when the metric filter was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetricFilter) -> dict:
    out: dict = {}
    if "filter_name" in value:
        out["filterName"] = value["filter_name"]
    if "filter_pattern" in value:
        out["filterPattern"] = value["filter_pattern"]
    if "metric_transformations" in value:
        import capo_cloudwatch_logs.types.metric_transformations

        out["metricTransformations"] = (
            capo_cloudwatch_logs.types.metric_transformations.serialize_aws_json_1_1(
                value["metric_transformations"]
            )
        )
    if "creation_time" in value:
        out["creationTime"] = value["creation_time"]
    if "log_group_name" in value:
        out["logGroupName"] = value["log_group_name"]
    out["applyOnTransformedLogs"] = value.get("apply_on_transformed_logs", False)
    if "field_selection_criteria" in value:
        out["fieldSelectionCriteria"] = value["field_selection_criteria"]
    if "emit_system_field_dimensions" in value:
        import capo_cloudwatch_logs.types.emit_system_fields

        out["emitSystemFieldDimensions"] = (
            capo_cloudwatch_logs.types.emit_system_fields.serialize_aws_json_1_1(
                value["emit_system_field_dimensions"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> MetricFilter:
    out: MetricFilter = {}  # type: ignore[typeddict-item]
    if data.get("filterName") is not None:
        out["filter_name"] = data["filterName"]
    if data.get("filterPattern") is not None:
        out["filter_pattern"] = data["filterPattern"]
    if data.get("metricTransformations") is not None:
        import capo_cloudwatch_logs.types.metric_transformations

        out["metric_transformations"] = (
            capo_cloudwatch_logs.types.metric_transformations.deserialize_aws_json_1_1(
                data["metricTransformations"]
            )
        )
    if data.get("creationTime") is not None:
        out["creation_time"] = data["creationTime"]
    if data.get("logGroupName") is not None:
        out["log_group_name"] = data["logGroupName"]
    if data.get("applyOnTransformedLogs") is not None:
        out["apply_on_transformed_logs"] = data["applyOnTransformedLogs"]
    else:
        out["apply_on_transformed_logs"] = False
    if data.get("fieldSelectionCriteria") is not None:
        out["field_selection_criteria"] = data["fieldSelectionCriteria"]
    if data.get("emitSystemFieldDimensions") is not None:
        import capo_cloudwatch_logs.types.emit_system_fields

        out["emit_system_field_dimensions"] = (
            capo_cloudwatch_logs.types.emit_system_fields.deserialize_aws_json_1_1(
                data["emitSystemFieldDimensions"]
            )
        )
    return out
