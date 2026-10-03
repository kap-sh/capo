"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#PutMetricFilterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.apply_on_transformed_logs
    import capo_cloudwatch_logs.types.emit_system_fields
    import capo_cloudwatch_logs.types.field_selection_criteria
    import capo_cloudwatch_logs.types.filter_name
    import capo_cloudwatch_logs.types.filter_pattern
    import capo_cloudwatch_logs.types.log_group_name
    import capo_cloudwatch_logs.types.metric_transformations


class PutMetricFilterRequest(TypedDict, closed=True):
    log_group_name: "capo_cloudwatch_logs.types.log_group_name.LogGroupName"
    """<p>The name of the log group.</p>"""
    filter_name: "capo_cloudwatch_logs.types.filter_name.FilterName"
    """<p>A name for the metric filter.</p>"""
    filter_pattern: "capo_cloudwatch_logs.types.filter_pattern.FilterPattern"
    """<p>A filter pattern for extracting metric data out of ingested log events.</p>"""
    metric_transformations: (
        "capo_cloudwatch_logs.types.metric_transformations.MetricTransformations"
    )
    """<p>A collection of information that defines how metric data gets emitted.</p>"""
    apply_on_transformed_logs: (
        "capo_cloudwatch_logs.types.apply_on_transformed_logs.ApplyOnTransformedLogs"
    )
    """<p>This parameter is valid only for log groups that have an active log transformer. For more information about log transformers, see <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutTransformer.html">PutTransformer</a>.</p> <p>If the log group uses either a log-group level or account-level transformer, and you specify <code>true</code>, the metric filter will be applied on the transformed version of the log events instead of the original ingested log events.</p>"""
    field_selection_criteria: NotRequired[
        "capo_cloudwatch_logs.types.field_selection_criteria.FieldSelectionCriteria"
    ]
    """<p>A filter expression that specifies which log events should be processed by this metric filter based on system fields such as source account and source region. Uses selection criteria syntax with operators like <code>=</code>, <code>!=</code>, <code>AND</code>, <code>OR</code>, <code>IN</code>, <code>NOT IN</code>. Example: <code>@aws.region = "us-east-1"</code> or <code>@aws.account IN ["123456789012", "987654321098"]</code>. Maximum length: 2000 characters.</p>"""
    emit_system_field_dimensions: NotRequired[
        "capo_cloudwatch_logs.types.emit_system_fields.EmitSystemFields"
    ]
    """<p>A list of system fields to emit as additional dimensions in the generated metrics. Valid values are <code>@aws.account</code> and <code>@aws.region</code>. These dimensions help identify the source of centralized log data and count toward the total dimension limit for metric filters.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutMetricFilterRequest) -> dict:
    out: dict = {}
    out["logGroupName"] = value["log_group_name"]
    out["filterName"] = value["filter_name"]
    out["filterPattern"] = value["filter_pattern"]
    import capo_cloudwatch_logs.types.metric_transformations

    out["metricTransformations"] = (
        capo_cloudwatch_logs.types.metric_transformations.serialize_aws_json_1_1(
            value["metric_transformations"]
        )
    )
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


def deserialize_aws_json_1_1(data: dict) -> PutMetricFilterRequest:
    out: PutMetricFilterRequest = {}  # type: ignore[typeddict-item]
    if data.get("logGroupName") is not None:
        out["log_group_name"] = data["logGroupName"]
    else:
        raise DeserializationError("PutMetricFilterRequest.log_group_name required")
    if data.get("filterName") is not None:
        out["filter_name"] = data["filterName"]
    else:
        raise DeserializationError("PutMetricFilterRequest.filter_name required")
    if data.get("filterPattern") is not None:
        out["filter_pattern"] = data["filterPattern"]
    else:
        raise DeserializationError("PutMetricFilterRequest.filter_pattern required")
    if data.get("metricTransformations") is not None:
        import capo_cloudwatch_logs.types.metric_transformations

        out["metric_transformations"] = (
            capo_cloudwatch_logs.types.metric_transformations.deserialize_aws_json_1_1(
                data["metricTransformations"]
            )
        )
    else:
        raise DeserializationError(
            "PutMetricFilterRequest.metric_transformations required"
        )
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
