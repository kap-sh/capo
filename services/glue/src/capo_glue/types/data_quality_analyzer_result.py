"""Generated from Smithy shape ``com.amazonaws.glue#DataQualityAnalyzerResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.data_quality_rule_result_description
    import capo_glue.types.evaluated_distributions_map
    import capo_glue.types.evaluated_metrics_map
    import capo_glue.types.name_string


class DataQualityAnalyzerResult(TypedDict, closed=True):
    name: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The name of the data quality analyzer.</p>"""
    description: NotRequired[
        "capo_glue.types.data_quality_rule_result_description.DataQualityRuleResultDescription"
    ]
    """<p>A description of the data quality analyzer.</p>"""
    evaluation_message: NotRequired[
        "capo_glue.types.data_quality_rule_result_description.DataQualityRuleResultDescription"
    ]
    """<p>An evaluation message.</p>"""
    evaluated_metrics: NotRequired[
        "capo_glue.types.evaluated_metrics_map.EvaluatedMetricsMap"
    ]
    """<p>A map of metrics associated with the evaluation of the analyzer.</p>"""
    evaluated_distributions: NotRequired[
        "capo_glue.types.evaluated_distributions_map.EvaluatedDistributionsMap"
    ]
    """<p>A map of distribution metrics associated with the evaluation of the analyzer.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataQualityAnalyzerResult) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "evaluation_message" in value:
        out["EvaluationMessage"] = value["evaluation_message"]
    if "evaluated_metrics" in value:
        import capo_glue.types.evaluated_metrics_map

        out["EvaluatedMetrics"] = (
            capo_glue.types.evaluated_metrics_map.serialize_aws_json_1_1(
                value["evaluated_metrics"]
            )
        )
    if "evaluated_distributions" in value:
        import capo_glue.types.evaluated_distributions_map

        out["EvaluatedDistributions"] = (
            capo_glue.types.evaluated_distributions_map.serialize_aws_json_1_1(
                value["evaluated_distributions"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DataQualityAnalyzerResult:
    out: DataQualityAnalyzerResult = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("EvaluationMessage") is not None:
        out["evaluation_message"] = data["EvaluationMessage"]
    if data.get("EvaluatedMetrics") is not None:
        import capo_glue.types.evaluated_metrics_map

        out["evaluated_metrics"] = (
            capo_glue.types.evaluated_metrics_map.deserialize_aws_json_1_1(
                data["EvaluatedMetrics"]
            )
        )
    if data.get("EvaluatedDistributions") is not None:
        import capo_glue.types.evaluated_distributions_map

        out["evaluated_distributions"] = (
            capo_glue.types.evaluated_distributions_map.deserialize_aws_json_1_1(
                data["EvaluatedDistributions"]
            )
        )
    return out


def redact_sensitive(value: DataQualityAnalyzerResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    if "evaluation_message" in value:
        out["evaluation_message"] = "*** Sensitive Data Redacted ***"
    if "evaluated_metrics" in value:
        out["evaluated_metrics"] = "*** Sensitive Data Redacted ***"
    if "evaluated_distributions" in value:
        out["evaluated_distributions"] = "*** Sensitive Data Redacted ***"
    return out
