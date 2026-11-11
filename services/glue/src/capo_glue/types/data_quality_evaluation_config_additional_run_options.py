"""Generated from Smithy shape ``com.amazonaws.glue#DataQualityEvaluationConfigAdditionalRunOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.data_quality_rule_results_options
    import capo_glue.types.dq_composite_rule_evaluation_method
    import capo_glue.types.generic_string
    import capo_glue.types.nullable_boolean
    import capo_glue.types.observation_configuration
    import capo_glue.types.observation_mode
    import capo_glue.types.observation_results_options
    import capo_glue.types.profiling_results_options
    import capo_glue.types.row_level_results_options
    import capo_glue.types.uri_string


class DataQualityEvaluationConfigAdditionalRunOptions(TypedDict, closed=True):
    cloud_watch_metrics_enabled: NotRequired[
        "capo_glue.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Specifies whether to enable CloudWatch metrics.</p>"""
    results_s3_prefix: NotRequired["capo_glue.types.uri_string.UriString"]
    """<p>Prefix for Amazon S3 to store results.</p>"""
    composite_rule_evaluation_method: NotRequired[
        "capo_glue.types.dq_composite_rule_evaluation_method.DQCompositeRuleEvaluationMethod"
    ]
    """<p>Set the evaluation method for composite rules in the ruleset to ROW/COLUMN</p>"""
    row_level_results: NotRequired[
        "capo_glue.types.row_level_results_options.RowLevelResultsOptions"
    ]
    """<p>The configuration for writing row-level evaluation results to a Glue Data Catalog table.</p>"""
    profiling_results: NotRequired[
        "capo_glue.types.profiling_results_options.ProfilingResultsOptions"
    ]
    """<p>The configuration for writing profiling results to a Glue Data Catalog table.</p>"""
    observation_scope: NotRequired[
        "capo_glue.types.observation_configuration.ObservationConfiguration"
    ]
    """<p>The scope of the observation for the evaluation run. Specifies whether anomaly detection is enabled or disabled.</p>"""
    observation_mode: NotRequired["capo_glue.types.observation_mode.ObservationMode"]
    """<p>The observation mode for the evaluation run. Specifies how anomaly detection bounds are calculated.</p>"""
    data_quality_rule_results: NotRequired[
        "capo_glue.types.data_quality_rule_results_options.DataQualityRuleResultsOptions"
    ]
    """<p>The configuration for writing rule results to a Glue Data Catalog table.</p>"""
    observation_results: NotRequired[
        "capo_glue.types.observation_results_options.ObservationResultsOptions"
    ]
    """<p>The configuration for writing observation results to a Glue Data Catalog table.</p>"""
    custom_log_group_prefix: NotRequired["capo_glue.types.generic_string.GenericString"]
    """<p>A custom prefix for the CloudWatch log group names. When specified, evaluation run logs are written to <code><CustomLogGroupPrefix>/error</code> and <code><CustomLogGroupPrefix>/output</code> instead of the default <code>/aws-glue/data-quality/error</code> and <code>/aws-glue/data-quality/output</code> log groups.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DataQualityEvaluationConfigAdditionalRunOptions,
) -> dict:
    out: dict = {}
    if "cloud_watch_metrics_enabled" in value:
        out["CloudWatchMetricsEnabled"] = value["cloud_watch_metrics_enabled"]
    if "results_s3_prefix" in value:
        out["ResultsS3Prefix"] = value["results_s3_prefix"]
    if "composite_rule_evaluation_method" in value:
        import capo_glue.types.dq_composite_rule_evaluation_method

        out["CompositeRuleEvaluationMethod"] = (
            capo_glue.types.dq_composite_rule_evaluation_method.serialize_aws_json_1_1(
                value["composite_rule_evaluation_method"]
            )
        )
    if "row_level_results" in value:
        import capo_glue.types.row_level_results_options

        out["RowLevelResults"] = (
            capo_glue.types.row_level_results_options.serialize_aws_json_1_1(
                value["row_level_results"]
            )
        )
    if "profiling_results" in value:
        import capo_glue.types.profiling_results_options

        out["ProfilingResults"] = (
            capo_glue.types.profiling_results_options.serialize_aws_json_1_1(
                value["profiling_results"]
            )
        )
    if "observation_scope" in value:
        import capo_glue.types.observation_configuration

        out["ObservationScope"] = (
            capo_glue.types.observation_configuration.serialize_aws_json_1_1(
                value["observation_scope"]
            )
        )
    if "observation_mode" in value:
        import capo_glue.types.observation_mode

        out["ObservationMode"] = (
            capo_glue.types.observation_mode.serialize_aws_json_1_1(
                value["observation_mode"]
            )
        )
    if "data_quality_rule_results" in value:
        import capo_glue.types.data_quality_rule_results_options

        out["DataQualityRuleResults"] = (
            capo_glue.types.data_quality_rule_results_options.serialize_aws_json_1_1(
                value["data_quality_rule_results"]
            )
        )
    if "observation_results" in value:
        import capo_glue.types.observation_results_options

        out["ObservationResults"] = (
            capo_glue.types.observation_results_options.serialize_aws_json_1_1(
                value["observation_results"]
            )
        )
    if "custom_log_group_prefix" in value:
        out["CustomLogGroupPrefix"] = value["custom_log_group_prefix"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DataQualityEvaluationConfigAdditionalRunOptions:
    out: DataQualityEvaluationConfigAdditionalRunOptions = {}  # type: ignore[typeddict-item]
    if data.get("CloudWatchMetricsEnabled") is not None:
        out["cloud_watch_metrics_enabled"] = data["CloudWatchMetricsEnabled"]
    if data.get("ResultsS3Prefix") is not None:
        out["results_s3_prefix"] = data["ResultsS3Prefix"]
    if data.get("CompositeRuleEvaluationMethod") is not None:
        import capo_glue.types.dq_composite_rule_evaluation_method

        out["composite_rule_evaluation_method"] = (
            capo_glue.types.dq_composite_rule_evaluation_method.deserialize_aws_json_1_1(
                data["CompositeRuleEvaluationMethod"]
            )
        )
    if data.get("RowLevelResults") is not None:
        import capo_glue.types.row_level_results_options

        out["row_level_results"] = (
            capo_glue.types.row_level_results_options.deserialize_aws_json_1_1(
                data["RowLevelResults"]
            )
        )
    if data.get("ProfilingResults") is not None:
        import capo_glue.types.profiling_results_options

        out["profiling_results"] = (
            capo_glue.types.profiling_results_options.deserialize_aws_json_1_1(
                data["ProfilingResults"]
            )
        )
    if data.get("ObservationScope") is not None:
        import capo_glue.types.observation_configuration

        out["observation_scope"] = (
            capo_glue.types.observation_configuration.deserialize_aws_json_1_1(
                data["ObservationScope"]
            )
        )
    if data.get("ObservationMode") is not None:
        import capo_glue.types.observation_mode

        out["observation_mode"] = (
            capo_glue.types.observation_mode.deserialize_aws_json_1_1(
                data["ObservationMode"]
            )
        )
    if data.get("DataQualityRuleResults") is not None:
        import capo_glue.types.data_quality_rule_results_options

        out["data_quality_rule_results"] = (
            capo_glue.types.data_quality_rule_results_options.deserialize_aws_json_1_1(
                data["DataQualityRuleResults"]
            )
        )
    if data.get("ObservationResults") is not None:
        import capo_glue.types.observation_results_options

        out["observation_results"] = (
            capo_glue.types.observation_results_options.deserialize_aws_json_1_1(
                data["ObservationResults"]
            )
        )
    if data.get("CustomLogGroupPrefix") is not None:
        out["custom_log_group_prefix"] = data["CustomLogGroupPrefix"]
    return out
