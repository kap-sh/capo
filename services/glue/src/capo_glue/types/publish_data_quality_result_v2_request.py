"""Generated from Smithy shape ``com.amazonaws.glue#PublishDataQualityResultV2Request``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.client_token_string
    import capo_glue.types.data_quality_aggregated_metrics
    import capo_glue.types.data_quality_analyzer_results
    import capo_glue.types.data_quality_configuration_v2
    import capo_glue.types.data_quality_observations
    import capo_glue.types.data_quality_rule_results
    import capo_glue.types.data_quality_telemetry
    import capo_glue.types.generic_bounded_double
    import capo_glue.types.hash_string
    import capo_glue.types.name_string
    import capo_glue.types.publish_data_quality_result_descriptors
    import capo_glue.types.publish_data_quality_result_dimensions
    import capo_glue.types.publish_data_quality_result_tags
    import capo_glue.types.statistic_summary_list
    import capo_glue.types.timestamp


class PublishDataQualityResultV2Request(TypedDict, closed=True):
    dimensions: "capo_glue.types.publish_data_quality_result_dimensions.PublishDataQualityResultDimensions"
    """<p>The dimensions for the result.</p>"""
    tags: NotRequired[
        "capo_glue.types.publish_data_quality_result_tags.PublishDataQualityResultTags"
    ]
    """<p>The tags for the result.</p>"""
    execution_started_on: NotRequired["capo_glue.types.timestamp.Timestamp"]
    """<p>The time execution started for the result.</p>"""
    execution_completed_on: NotRequired["capo_glue.types.timestamp.Timestamp"]
    """<p>The time execution completed for the result.</p>"""
    score: "capo_glue.types.generic_bounded_double.GenericBoundedDouble"
    """<p>The score for the result.</p>"""
    rule_results: "capo_glue.types.data_quality_rule_results.DataQualityRuleResults"
    """<p>The rule level results.</p>"""
    analyzer_results: NotRequired[
        "capo_glue.types.data_quality_analyzer_results.DataQualityAnalyzerResults"
    ]
    """<p>The analyzer level results.</p>"""
    observations: NotRequired[
        "capo_glue.types.data_quality_observations.DataQualityObservations"
    ]
    """<p>The observations for the result.</p>"""
    aggregated_metrics: NotRequired[
        "capo_glue.types.data_quality_aggregated_metrics.DataQualityAggregatedMetrics"
    ]
    """<p>The aggregated metrics for the result.</p>"""
    statistics: NotRequired[
        "capo_glue.types.statistic_summary_list.StatisticSummaryList"
    ]
    """<p>The statistics for the result.</p>"""
    run_configuration: NotRequired[
        "capo_glue.types.data_quality_configuration_v2.DataQualityConfigurationV2"
    ]
    """<p>The run configuration for the result.</p>"""
    client_token: NotRequired["capo_glue.types.client_token_string.ClientTokenString"]
    """<p>The client token for the request.</p>"""
    evaluation_context: "capo_glue.types.name_string.NameString"
    """<p>The evaluation context for the result.</p>"""
    descriptors: NotRequired[
        "capo_glue.types.publish_data_quality_result_descriptors.PublishDataQualityResultDescriptors"
    ]
    """<p>The descriptors for the result.</p>"""
    ruleset_name: NotRequired["capo_glue.types.hash_string.HashString"]
    """<p>The ruleset name for the result.</p>"""
    data_quality_security_configuration: NotRequired[
        "capo_glue.types.name_string.NameString"
    ]
    """<p>The security configuration for the result.</p>"""
    telemetry: NotRequired[
        "capo_glue.types.data_quality_telemetry.DataQualityTelemetry"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PublishDataQualityResultV2Request) -> dict:
    out: dict = {}
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
    out["Score"] = (
        "NaN"
        if value["score"] != value["score"]
        else "Infinity"
        if value["score"] == float("inf")
        else "-Infinity"
        if value["score"] == float("-inf")
        else value["score"]
    )
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
    if "statistics" in value:
        import capo_glue.types.statistic_summary_list

        out["Statistics"] = (
            capo_glue.types.statistic_summary_list.serialize_aws_json_1_1(
                value["statistics"]
            )
        )
    if "run_configuration" in value:
        import capo_glue.types.data_quality_configuration_v2

        out["RunConfiguration"] = (
            capo_glue.types.data_quality_configuration_v2.serialize_aws_json_1_1(
                value["run_configuration"]
            )
        )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    out["EvaluationContext"] = value["evaluation_context"]
    if "descriptors" in value:
        import capo_glue.types.publish_data_quality_result_descriptors

        out["Descriptors"] = (
            capo_glue.types.publish_data_quality_result_descriptors.serialize_aws_json_1_1(
                value["descriptors"]
            )
        )
    if "ruleset_name" in value:
        out["RulesetName"] = value["ruleset_name"]
    if "data_quality_security_configuration" in value:
        out["DataQualitySecurityConfiguration"] = value[
            "data_quality_security_configuration"
        ]
    if "telemetry" in value:
        import capo_glue.types.data_quality_telemetry

        out["Telemetry"] = (
            capo_glue.types.data_quality_telemetry.serialize_aws_json_1_1(
                value["telemetry"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PublishDataQualityResultV2Request:
    out: PublishDataQualityResultV2Request = {}  # type: ignore[typeddict-item]
    if data.get("Dimensions") is not None:
        import capo_glue.types.publish_data_quality_result_dimensions

        out["dimensions"] = (
            capo_glue.types.publish_data_quality_result_dimensions.deserialize_aws_json_1_1(
                data["Dimensions"]
            )
        )
    else:
        raise DeserializationError(
            "PublishDataQualityResultV2Request.dimensions required"
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
    if data.get("Score") is not None:
        out["score"] = float(data["Score"])
    else:
        raise DeserializationError("PublishDataQualityResultV2Request.score required")
    if data.get("RuleResults") is not None:
        import capo_glue.types.data_quality_rule_results

        out["rule_results"] = (
            capo_glue.types.data_quality_rule_results.deserialize_aws_json_1_1(
                data["RuleResults"]
            )
        )
    else:
        raise DeserializationError(
            "PublishDataQualityResultV2Request.rule_results required"
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
    if data.get("Statistics") is not None:
        import capo_glue.types.statistic_summary_list

        out["statistics"] = (
            capo_glue.types.statistic_summary_list.deserialize_aws_json_1_1(
                data["Statistics"]
            )
        )
    if data.get("RunConfiguration") is not None:
        import capo_glue.types.data_quality_configuration_v2

        out["run_configuration"] = (
            capo_glue.types.data_quality_configuration_v2.deserialize_aws_json_1_1(
                data["RunConfiguration"]
            )
        )
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("EvaluationContext") is not None:
        out["evaluation_context"] = data["EvaluationContext"]
    else:
        raise DeserializationError(
            "PublishDataQualityResultV2Request.evaluation_context required"
        )
    if data.get("Descriptors") is not None:
        import capo_glue.types.publish_data_quality_result_descriptors

        out["descriptors"] = (
            capo_glue.types.publish_data_quality_result_descriptors.deserialize_aws_json_1_1(
                data["Descriptors"]
            )
        )
    if data.get("RulesetName") is not None:
        out["ruleset_name"] = data["RulesetName"]
    if data.get("DataQualitySecurityConfiguration") is not None:
        out["data_quality_security_configuration"] = data[
            "DataQualitySecurityConfiguration"
        ]
    if data.get("Telemetry") is not None:
        import capo_glue.types.data_quality_telemetry

        out["telemetry"] = (
            capo_glue.types.data_quality_telemetry.deserialize_aws_json_1_1(
                data["Telemetry"]
            )
        )
    return out


def redact_sensitive(value: PublishDataQualityResultV2Request) -> dict[str, Any]:
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
    if "statistics" in value:
        import capo_glue.types.statistic_summary_list

        out["statistics"] = capo_glue.types.statistic_summary_list.redact_sensitive(
            value["statistics"]
        )
    return out
