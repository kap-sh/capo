"""Generated from Smithy shape ``com.amazonaws.glue#DataQualityEvaluationConfigListDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.data_quality_evaluation_config_level
    import capo_glue.types.data_quality_evaluation_config_list_data_source
    import capo_glue.types.data_quality_evaluation_config_managed_ruleset
    import capo_glue.types.data_quality_evaluation_run_mode
    import capo_glue.types.name_string
    import capo_glue.types.nullable_boolean
    import capo_glue.types.timestamp


class DataQualityEvaluationConfigListDetails(TypedDict, closed=True):
    name: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The name of the data quality evaluation configuration.</p>"""
    evaluation_run_mode: NotRequired[
        "capo_glue.types.data_quality_evaluation_run_mode.DataQualityEvaluationRunMode"
    ]
    """<p>The evaluation run mode of the configuration's results, which is <code>EVALUATION_CONFIG</code>.</p>"""
    created_on: NotRequired["capo_glue.types.timestamp.Timestamp"]
    """<p>The time when the configuration was created.</p>"""
    last_modified_on: NotRequired["capo_glue.types.timestamp.Timestamp"]
    """<p>The time when the configuration was last modified.</p>"""
    level: NotRequired[
        "capo_glue.types.data_quality_evaluation_config_level.DataQualityEvaluationConfigLevel"
    ]
    """<p>The Glue Data Catalog hierarchical level that the configuration applies to.</p>"""
    data_source: NotRequired[
        "capo_glue.types.data_quality_evaluation_config_list_data_source.DataQualityEvaluationConfigListDataSource"
    ]
    """<p>The catalog, database, or table that the configuration applies to.</p>"""
    ruleset_name: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The name of the data quality ruleset that tables are evaluated with.</p>"""
    managed_ruleset_name: NotRequired[
        "capo_glue.types.data_quality_evaluation_config_managed_ruleset.DataQualityEvaluationConfigManagedRuleset"
    ]
    """<p>The built-in ruleset that tables are evaluated with.</p>"""
    pause_runs: NotRequired["capo_glue.types.nullable_boolean.NullableBoolean"]
    """<p>Specifies whether evaluations are paused.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataQualityEvaluationConfigListDetails) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "evaluation_run_mode" in value:
        import capo_glue.types.data_quality_evaluation_run_mode

        out["EvaluationRunMode"] = (
            capo_glue.types.data_quality_evaluation_run_mode.serialize_aws_json_1_1(
                value["evaluation_run_mode"]
            )
        )
    if "created_on" in value:
        import capo_glue.types.timestamp

        out["CreatedOn"] = capo_glue.types.timestamp.serialize_aws_json_1_1(
            value["created_on"]
        )
    if "last_modified_on" in value:
        import capo_glue.types.timestamp

        out["LastModifiedOn"] = capo_glue.types.timestamp.serialize_aws_json_1_1(
            value["last_modified_on"]
        )
    if "level" in value:
        import capo_glue.types.data_quality_evaluation_config_level

        out["Level"] = (
            capo_glue.types.data_quality_evaluation_config_level.serialize_aws_json_1_1(
                value["level"]
            )
        )
    if "data_source" in value:
        import capo_glue.types.data_quality_evaluation_config_list_data_source

        out["DataSource"] = (
            capo_glue.types.data_quality_evaluation_config_list_data_source.serialize_aws_json_1_1(
                value["data_source"]
            )
        )
    if "ruleset_name" in value:
        out["RulesetName"] = value["ruleset_name"]
    if "managed_ruleset_name" in value:
        import capo_glue.types.data_quality_evaluation_config_managed_ruleset

        out["ManagedRulesetName"] = (
            capo_glue.types.data_quality_evaluation_config_managed_ruleset.serialize_aws_json_1_1(
                value["managed_ruleset_name"]
            )
        )
    if "pause_runs" in value:
        out["PauseRuns"] = value["pause_runs"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DataQualityEvaluationConfigListDetails:
    out: DataQualityEvaluationConfigListDetails = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("EvaluationRunMode") is not None:
        import capo_glue.types.data_quality_evaluation_run_mode

        out["evaluation_run_mode"] = (
            capo_glue.types.data_quality_evaluation_run_mode.deserialize_aws_json_1_1(
                data["EvaluationRunMode"]
            )
        )
    if data.get("CreatedOn") is not None:
        import capo_glue.types.timestamp

        out["created_on"] = capo_glue.types.timestamp.deserialize_aws_json_1_1(
            data["CreatedOn"]
        )
    if data.get("LastModifiedOn") is not None:
        import capo_glue.types.timestamp

        out["last_modified_on"] = capo_glue.types.timestamp.deserialize_aws_json_1_1(
            data["LastModifiedOn"]
        )
    if data.get("Level") is not None:
        import capo_glue.types.data_quality_evaluation_config_level

        out["level"] = (
            capo_glue.types.data_quality_evaluation_config_level.deserialize_aws_json_1_1(
                data["Level"]
            )
        )
    if data.get("DataSource") is not None:
        import capo_glue.types.data_quality_evaluation_config_list_data_source

        out["data_source"] = (
            capo_glue.types.data_quality_evaluation_config_list_data_source.deserialize_aws_json_1_1(
                data["DataSource"]
            )
        )
    if data.get("RulesetName") is not None:
        out["ruleset_name"] = data["RulesetName"]
    if data.get("ManagedRulesetName") is not None:
        import capo_glue.types.data_quality_evaluation_config_managed_ruleset

        out["managed_ruleset_name"] = (
            capo_glue.types.data_quality_evaluation_config_managed_ruleset.deserialize_aws_json_1_1(
                data["ManagedRulesetName"]
            )
        )
    if data.get("PauseRuns") is not None:
        out["pause_runs"] = data["PauseRuns"]
    return out
