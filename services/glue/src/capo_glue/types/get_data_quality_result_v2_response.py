"""Generated from Smithy shape ``com.amazonaws.glue#GetDataQualityResultV2Response``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.data_quality_aggregated_metrics
    import capo_glue.types.data_quality_analyzer_results
    import capo_glue.types.data_quality_observations
    import capo_glue.types.data_quality_rule_results
    import capo_glue.types.data_source
    import capo_glue.types.generic_bounded_double
    import capo_glue.types.hash_string
    import capo_glue.types.name_string
    import capo_glue.types.publish_data_quality_result_descriptors
    import capo_glue.types.publish_data_quality_result_dimensions
    import capo_glue.types.publish_data_quality_result_tags
    import capo_glue.types.timestamp


class GetDataQualityResultV2Response(TypedDict, closed=True):
    result_id: NotRequired["capo_glue.types.hash_string.HashString"]
    """<p>A unique result ID for the data quality result.</p>"""
    data_source: NotRequired["capo_glue.types.data_source.DataSource"]
    """<p>The table associated with the data quality result, if any.</p>"""
    profile_id: NotRequired["capo_glue.types.hash_string.HashString"]
    """<p>The Profile ID for the data quality result.</p>"""
    dimensions: NotRequired[
        "capo_glue.types.publish_data_quality_result_dimensions.PublishDataQualityResultDimensions"
    ]
    """<p>A map of platform-specific identifiers, such as cluster, application, workgroup, or project IDs, that identify where the data quality evaluation ran.</p>"""
    tags: NotRequired[
        "capo_glue.types.publish_data_quality_result_tags.PublishDataQualityResultTags"
    ]
    """<p>A map of tags associated with the data quality result.</p>"""
    execution_started_on: NotRequired["capo_glue.types.timestamp.Timestamp"]
    """<p>The date and time when this data quality run started.</p>"""
    execution_completed_on: NotRequired["capo_glue.types.timestamp.Timestamp"]
    """<p>The date and time when this data quality run completed.</p>"""
    result_published_on: NotRequired["capo_glue.types.timestamp.Timestamp"]
    """<p>The date and time when this data quality result was published.</p>"""
    score: NotRequired["capo_glue.types.generic_bounded_double.GenericBoundedDouble"]
    """<p>An aggregate data quality score. Represents the ratio of rules that passed to the total number of rules.</p>"""
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
    evaluation_context: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The evaluation context for the data quality result. This value identifies a specific data quality result, or a series of related results, within a run.</p>"""
    descriptors: NotRequired[
        "capo_glue.types.publish_data_quality_result_descriptors.PublishDataQualityResultDescriptors"
    ]
    """<p>A map of user-provided descriptors that add contextual metadata and configuration to the data quality result, such as database name, table name, team, or environment.</p>"""
    aggregated_metrics: NotRequired[
        "capo_glue.types.data_quality_aggregated_metrics.DataQualityAggregatedMetrics"
    ]
    """<p>A summary of <code>DataQualityAggregatedMetrics</code> objects showing the total counts of processed rows and rules, including their pass/fail statistics based on row-level results.</p>"""
    ruleset_name: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The name of the ruleset associated with the data quality result.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDataQualityResultV2Response) -> dict:
    out: dict = {}
    if "result_id" in value:
        out["ResultId"] = value["result_id"]
    if "data_source" in value:
        import capo_glue.types.data_source

        out["DataSource"] = capo_glue.types.data_source.serialize_aws_json_1_1(
            value["data_source"]
        )
    if "profile_id" in value:
        out["ProfileId"] = value["profile_id"]
    if "dimensions" in value:
        import capo_glue.types.publish_data_quality_result_dimensions

        out["Dimensions"] = (
            capo_glue.types.publish_data_quality_result_dimensions.serialize_aws_json_1_1(
                value["dimensions"]
            )
        )
    if "tags" in value:
        import capo_glue.types.publish_data_quality_result_tags

        out["Tags"] = (
            capo_glue.types.publish_data_quality_result_tags.serialize_aws_json_1_1(
                value["tags"]
            )
        )
    if "execution_started_on" in value:
        import capo_glue.types.timestamp

        out["ExecutionStartedOn"] = capo_glue.types.timestamp.serialize_aws_json_1_1(
            value["execution_started_on"]
        )
    if "execution_completed_on" in value:
        import capo_glue.types.timestamp

        out["ExecutionCompletedOn"] = capo_glue.types.timestamp.serialize_aws_json_1_1(
            value["execution_completed_on"]
        )
    if "result_published_on" in value:
        import capo_glue.types.timestamp

        out["ResultPublishedOn"] = capo_glue.types.timestamp.serialize_aws_json_1_1(
            value["result_published_on"]
        )
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
    if "evaluation_context" in value:
        out["EvaluationContext"] = value["evaluation_context"]
    if "descriptors" in value:
        import capo_glue.types.publish_data_quality_result_descriptors

        out["Descriptors"] = (
            capo_glue.types.publish_data_quality_result_descriptors.serialize_aws_json_1_1(
                value["descriptors"]
            )
        )
    if "aggregated_metrics" in value:
        import capo_glue.types.data_quality_aggregated_metrics

        out["AggregatedMetrics"] = (
            capo_glue.types.data_quality_aggregated_metrics.serialize_aws_json_1_1(
                value["aggregated_metrics"]
            )
        )
    if "ruleset_name" in value:
        out["RulesetName"] = value["ruleset_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDataQualityResultV2Response:
    out: GetDataQualityResultV2Response = {}  # type: ignore[typeddict-item]
    if data.get("ResultId") is not None:
        out["result_id"] = data["ResultId"]
    if data.get("DataSource") is not None:
        import capo_glue.types.data_source

        out["data_source"] = capo_glue.types.data_source.deserialize_aws_json_1_1(
            data["DataSource"]
        )
    if data.get("ProfileId") is not None:
        out["profile_id"] = data["ProfileId"]
    if data.get("Dimensions") is not None:
        import capo_glue.types.publish_data_quality_result_dimensions

        out["dimensions"] = (
            capo_glue.types.publish_data_quality_result_dimensions.deserialize_aws_json_1_1(
                data["Dimensions"]
            )
        )
    if data.get("Tags") is not None:
        import capo_glue.types.publish_data_quality_result_tags

        out["tags"] = (
            capo_glue.types.publish_data_quality_result_tags.deserialize_aws_json_1_1(
                data["Tags"]
            )
        )
    if data.get("ExecutionStartedOn") is not None:
        import capo_glue.types.timestamp

        out["execution_started_on"] = (
            capo_glue.types.timestamp.deserialize_aws_json_1_1(
                data["ExecutionStartedOn"]
            )
        )
    if data.get("ExecutionCompletedOn") is not None:
        import capo_glue.types.timestamp

        out["execution_completed_on"] = (
            capo_glue.types.timestamp.deserialize_aws_json_1_1(
                data["ExecutionCompletedOn"]
            )
        )
    if data.get("ResultPublishedOn") is not None:
        import capo_glue.types.timestamp

        out["result_published_on"] = capo_glue.types.timestamp.deserialize_aws_json_1_1(
            data["ResultPublishedOn"]
        )
    if data.get("Score") is not None:
        out["score"] = float(data["Score"])
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
    if data.get("EvaluationContext") is not None:
        out["evaluation_context"] = data["EvaluationContext"]
    if data.get("Descriptors") is not None:
        import capo_glue.types.publish_data_quality_result_descriptors

        out["descriptors"] = (
            capo_glue.types.publish_data_quality_result_descriptors.deserialize_aws_json_1_1(
                data["Descriptors"]
            )
        )
    if data.get("AggregatedMetrics") is not None:
        import capo_glue.types.data_quality_aggregated_metrics

        out["aggregated_metrics"] = (
            capo_glue.types.data_quality_aggregated_metrics.deserialize_aws_json_1_1(
                data["AggregatedMetrics"]
            )
        )
    if data.get("RulesetName") is not None:
        out["ruleset_name"] = data["RulesetName"]
    return out


def redact_sensitive(value: GetDataQualityResultV2Response) -> dict[str, Any]:
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
