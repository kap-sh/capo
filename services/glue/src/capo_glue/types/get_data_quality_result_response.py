"""Generated from Smithy shape ``com.amazonaws.glue#GetDataQualityResultResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.data_quality_aggregated_metrics
    import capo_glue.types.data_quality_analyzer_results
    import capo_glue.types.data_quality_observations
    import capo_glue.types.data_quality_rule_results
    import capo_glue.types.data_source
    import capo_glue.types.generic_bounded_double
    import capo_glue.types.generic_string
    import capo_glue.types.hash_string
    import capo_glue.types.name_string
    import capo_glue.types.timestamp


class GetDataQualityResultResponse(TypedDict, closed=True):
    result_id: NotRequired["capo_glue.types.hash_string.HashString"]
    """<p>A unique result ID for the data quality result.</p>"""
    profile_id: NotRequired["capo_glue.types.hash_string.HashString"]
    """<p>The Profile ID for the data quality result.</p>"""
    score: NotRequired["capo_glue.types.generic_bounded_double.GenericBoundedDouble"]
    """<p>An aggregate data quality score. Represents the ratio of rules that passed to the total number of rules.</p>"""
    data_source: NotRequired["capo_glue.types.data_source.DataSource"]
    """<p>The table associated with the data quality result, if any.</p>"""
    ruleset_name: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The name of the ruleset associated with the data quality result.</p>"""
    evaluation_context: NotRequired["capo_glue.types.generic_string.GenericString"]
    """<p>In the context of a job in Glue Studio, each node in the canvas is typically assigned some sort of name and data quality nodes will have names. In the case of multiple nodes, the <code>evaluationContext</code> can differentiate the nodes.</p>"""
    started_on: NotRequired["capo_glue.types.timestamp.Timestamp"]
    """<p>The date and time when the run for this data quality result started.</p>"""
    completed_on: NotRequired["capo_glue.types.timestamp.Timestamp"]
    """<p>The date and time when the run for this data quality result was completed.</p>"""
    job_name: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The job name associated with the data quality result, if any.</p>"""
    job_run_id: NotRequired["capo_glue.types.hash_string.HashString"]
    """<p>The job run ID associated with the data quality result, if any.</p>"""
    ruleset_evaluation_run_id: NotRequired["capo_glue.types.hash_string.HashString"]
    """<p>The unique run ID associated with the ruleset evaluation.</p>"""
    rule_results: NotRequired[
        "capo_glue.types.data_quality_rule_results.DataQualityRuleResults"
    ]
    """<p>A list of <code>DataQualityRuleResult</code> objects representing the results for each rule.</p>"""
    analyzer_results: NotRequired[
        "capo_glue.types.data_quality_analyzer_results.DataQualityAnalyzerResults"
    ]
    """<p>A list of <code>DataQualityAnalyzerResult</code> objects representing the results for each analyzer.</p>"""
    observations: NotRequired[
        "capo_glue.types.data_quality_observations.DataQualityObservations"
    ]
    """<p>A list of <code>DataQualityObservation</code> objects representing the anomaly detection observations generated after evaluating the rules and analyzers.</p>"""
    aggregated_metrics: NotRequired[
        "capo_glue.types.data_quality_aggregated_metrics.DataQualityAggregatedMetrics"
    ]
    """<p> A summary of <code>DataQualityAggregatedMetrics</code> objects showing the total counts of processed rows and rules, including their pass/fail statistics based on row-level results. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDataQualityResultResponse) -> dict:
    out: dict = {}
    if "result_id" in value:
        out["ResultId"] = value["result_id"]
    if "profile_id" in value:
        out["ProfileId"] = value["profile_id"]
    if "score" in value:
        out["Score"] = (
            "NaN"
            if value["score"] != value["score"]
            else "Infinity"
            if value["score"] == float("inf")
            else "-Infinity"
            if value["score"] == float("-inf")
            else value["score"]
        )
    if "data_source" in value:
        import capo_glue.types.data_source

        out["DataSource"] = capo_glue.types.data_source.serialize_aws_json_1_1(
            value["data_source"]
        )
    if "ruleset_name" in value:
        out["RulesetName"] = value["ruleset_name"]
    if "evaluation_context" in value:
        out["EvaluationContext"] = value["evaluation_context"]
    if "started_on" in value:
        import capo_glue.types.timestamp

        out["StartedOn"] = capo_glue.types.timestamp.serialize_aws_json_1_1(
            value["started_on"]
        )
    if "completed_on" in value:
        import capo_glue.types.timestamp

        out["CompletedOn"] = capo_glue.types.timestamp.serialize_aws_json_1_1(
            value["completed_on"]
        )
    if "job_name" in value:
        out["JobName"] = value["job_name"]
    if "job_run_id" in value:
        out["JobRunId"] = value["job_run_id"]
    if "ruleset_evaluation_run_id" in value:
        out["RulesetEvaluationRunId"] = value["ruleset_evaluation_run_id"]
    if "rule_results" in value:
        import capo_glue.types.data_quality_rule_results

        out["RuleResults"] = (
            capo_glue.types.data_quality_rule_results.serialize_aws_json_1_1(
                value["rule_results"]
            )
        )
    if "analyzer_results" in value:
        import capo_glue.types.data_quality_analyzer_results

        out["AnalyzerResults"] = (
            capo_glue.types.data_quality_analyzer_results.serialize_aws_json_1_1(
                value["analyzer_results"]
            )
        )
    if "observations" in value:
        import capo_glue.types.data_quality_observations

        out["Observations"] = (
            capo_glue.types.data_quality_observations.serialize_aws_json_1_1(
                value["observations"]
            )
        )
    if "aggregated_metrics" in value:
        import capo_glue.types.data_quality_aggregated_metrics

        out["AggregatedMetrics"] = (
            capo_glue.types.data_quality_aggregated_metrics.serialize_aws_json_1_1(
                value["aggregated_metrics"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDataQualityResultResponse:
    out: GetDataQualityResultResponse = {}  # type: ignore[typeddict-item]
    if data.get("ResultId") is not None:
        out["result_id"] = data["ResultId"]
    if data.get("ProfileId") is not None:
        out["profile_id"] = data["ProfileId"]
    if data.get("Score") is not None:
        out["score"] = float(data["Score"])
    if data.get("DataSource") is not None:
        import capo_glue.types.data_source

        out["data_source"] = capo_glue.types.data_source.deserialize_aws_json_1_1(
            data["DataSource"]
        )
    if data.get("RulesetName") is not None:
        out["ruleset_name"] = data["RulesetName"]
    if data.get("EvaluationContext") is not None:
        out["evaluation_context"] = data["EvaluationContext"]
    if data.get("StartedOn") is not None:
        import capo_glue.types.timestamp

        out["started_on"] = capo_glue.types.timestamp.deserialize_aws_json_1_1(
            data["StartedOn"]
        )
    if data.get("CompletedOn") is not None:
        import capo_glue.types.timestamp

        out["completed_on"] = capo_glue.types.timestamp.deserialize_aws_json_1_1(
            data["CompletedOn"]
        )
    if data.get("JobName") is not None:
        out["job_name"] = data["JobName"]
    if data.get("JobRunId") is not None:
        out["job_run_id"] = data["JobRunId"]
    if data.get("RulesetEvaluationRunId") is not None:
        out["ruleset_evaluation_run_id"] = data["RulesetEvaluationRunId"]
    if data.get("RuleResults") is not None:
        import capo_glue.types.data_quality_rule_results

        out["rule_results"] = (
            capo_glue.types.data_quality_rule_results.deserialize_aws_json_1_1(
                data["RuleResults"]
            )
        )
    if data.get("AnalyzerResults") is not None:
        import capo_glue.types.data_quality_analyzer_results

        out["analyzer_results"] = (
            capo_glue.types.data_quality_analyzer_results.deserialize_aws_json_1_1(
                data["AnalyzerResults"]
            )
        )
    if data.get("Observations") is not None:
        import capo_glue.types.data_quality_observations

        out["observations"] = (
            capo_glue.types.data_quality_observations.deserialize_aws_json_1_1(
                data["Observations"]
            )
        )
    if data.get("AggregatedMetrics") is not None:
        import capo_glue.types.data_quality_aggregated_metrics

        out["aggregated_metrics"] = (
            capo_glue.types.data_quality_aggregated_metrics.deserialize_aws_json_1_1(
                data["AggregatedMetrics"]
            )
        )
    return out


def redact_sensitive(value: GetDataQualityResultResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "rule_results" in value:
        import capo_glue.types.data_quality_rule_results

        out["rule_results"] = (
            capo_glue.types.data_quality_rule_results.redact_sensitive(
                value["rule_results"]
            )
        )
    if "analyzer_results" in value:
        import capo_glue.types.data_quality_analyzer_results

        out["analyzer_results"] = (
            capo_glue.types.data_quality_analyzer_results.redact_sensitive(
                value["analyzer_results"]
            )
        )
    if "observations" in value:
        import capo_glue.types.data_quality_observations

        out["observations"] = (
            capo_glue.types.data_quality_observations.redact_sensitive(
                value["observations"]
            )
        )
    return out
