"""Generated from Smithy shape ``com.amazonaws.glue#DataQualityRuleResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.data_quality_rule_result_description
    import capo_glue.types.data_quality_rule_result_status
    import capo_glue.types.evaluated_metrics_map
    import capo_glue.types.labels
    import capo_glue.types.name_string
    import capo_glue.types.rule_metrics_map


class DataQualityRuleResult(TypedDict, closed=True):
    name: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The name of the data quality rule.</p>"""
    description: NotRequired[
        "capo_glue.types.data_quality_rule_result_description.DataQualityRuleResultDescription"
    ]
    """<p>A description of the data quality rule.</p>"""
    evaluation_message: NotRequired[
        "capo_glue.types.data_quality_rule_result_description.DataQualityRuleResultDescription"
    ]
    """<p>An evaluation message.</p>"""
    result: NotRequired[
        "capo_glue.types.data_quality_rule_result_status.DataQualityRuleResultStatus"
    ]
    """<p>A pass or fail status for the rule.</p>"""
    evaluated_metrics: NotRequired[
        "capo_glue.types.evaluated_metrics_map.EvaluatedMetricsMap"
    ]
    """<p>A map of metrics associated with the evaluation of the rule.</p>"""
    evaluated_rule: NotRequired[
        "capo_glue.types.data_quality_rule_result_description.DataQualityRuleResultDescription"
    ]
    """<p>The evaluated rule.</p>"""
    rule_metrics: NotRequired["capo_glue.types.rule_metrics_map.RuleMetricsMap"]
    """<p>A map containing metrics associated with the evaluation of the rule based on row-level results. </p>"""
    labels: NotRequired["capo_glue.types.labels.Labels"]
    """<p>A map containing labels assigned to the data quality rule. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataQualityRuleResult) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "evaluation_message" in value:
        out["EvaluationMessage"] = value["evaluation_message"]
    if "result" in value:
        import capo_glue.types.data_quality_rule_result_status

        out["Result"] = (
            capo_glue.types.data_quality_rule_result_status.serialize_aws_json_1_1(
                value["result"]
            )
        )
    if "evaluated_metrics" in value:
        import capo_glue.types.evaluated_metrics_map

        out["EvaluatedMetrics"] = (
            capo_glue.types.evaluated_metrics_map.serialize_aws_json_1_1(
                value["evaluated_metrics"]
            )
        )
    if "evaluated_rule" in value:
        out["EvaluatedRule"] = value["evaluated_rule"]
    if "rule_metrics" in value:
        import capo_glue.types.rule_metrics_map

        out["RuleMetrics"] = capo_glue.types.rule_metrics_map.serialize_aws_json_1_1(
            value["rule_metrics"]
        )
    if "labels" in value:
        import capo_glue.types.labels

        out["Labels"] = capo_glue.types.labels.serialize_aws_json_1_1(value["labels"])
    return out


def deserialize_aws_json_1_1(data: dict) -> DataQualityRuleResult:
    out: DataQualityRuleResult = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("EvaluationMessage") is not None:
        out["evaluation_message"] = data["EvaluationMessage"]
    if data.get("Result") is not None:
        import capo_glue.types.data_quality_rule_result_status

        out["result"] = (
            capo_glue.types.data_quality_rule_result_status.deserialize_aws_json_1_1(
                data["Result"]
            )
        )
    if data.get("EvaluatedMetrics") is not None:
        import capo_glue.types.evaluated_metrics_map

        out["evaluated_metrics"] = (
            capo_glue.types.evaluated_metrics_map.deserialize_aws_json_1_1(
                data["EvaluatedMetrics"]
            )
        )
    if data.get("EvaluatedRule") is not None:
        out["evaluated_rule"] = data["EvaluatedRule"]
    if data.get("RuleMetrics") is not None:
        import capo_glue.types.rule_metrics_map

        out["rule_metrics"] = capo_glue.types.rule_metrics_map.deserialize_aws_json_1_1(
            data["RuleMetrics"]
        )
    if data.get("Labels") is not None:
        import capo_glue.types.labels

        out["labels"] = capo_glue.types.labels.deserialize_aws_json_1_1(data["Labels"])
    return out


def redact_sensitive(value: DataQualityRuleResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    if "evaluation_message" in value:
        out["evaluation_message"] = "*** Sensitive Data Redacted ***"
    if "evaluated_metrics" in value:
        out["evaluated_metrics"] = "*** Sensitive Data Redacted ***"
    if "evaluated_rule" in value:
        out["evaluated_rule"] = "*** Sensitive Data Redacted ***"
    if "rule_metrics" in value:
        out["rule_metrics"] = "*** Sensitive Data Redacted ***"
    return out
