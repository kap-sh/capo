"""Generated from Smithy shape ``com.amazonaws.glue#UpdateDataQualityEvaluationConfigResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.data_quality_evaluation_config_additional_run_options
    import capo_glue.types.data_quality_evaluation_config_data_source
    import capo_glue.types.data_quality_evaluation_config_level
    import capo_glue.types.data_quality_evaluation_config_managed_ruleset
    import capo_glue.types.data_quality_evaluation_config_schedule_expression
    import capo_glue.types.data_quality_evaluation_config_triggers
    import capo_glue.types.data_quality_evaluation_run_mode
    import capo_glue.types.data_source_map
    import capo_glue.types.name_string
    import capo_glue.types.nullable_boolean
    import capo_glue.types.nullable_integer
    import capo_glue.types.role_string
    import capo_glue.types.timeout
    import capo_glue.types.timestamp


class UpdateDataQualityEvaluationConfigResponse(TypedDict, closed=True):
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
        "capo_glue.types.data_quality_evaluation_config_data_source.DataQualityEvaluationConfigDataSource"
    ]
    """<p>The catalog, database, or table that the configuration applies to.</p>"""
    ruleset_name: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The name of the data quality ruleset that tables are evaluated with.</p>"""
    managed_ruleset_name: NotRequired[
        "capo_glue.types.data_quality_evaluation_config_managed_ruleset.DataQualityEvaluationConfigManagedRuleset"
    ]
    """<p>The built-in ruleset that tables are evaluated with.</p>"""
    triggers: NotRequired[
        "capo_glue.types.data_quality_evaluation_config_triggers.DataQualityEvaluationConfigTriggers"
    ]
    """<p>When the configuration evaluates tables:</p> <dl> <dt>ONCE</dt> <dd> <p>Each table is evaluated one time, including when tables are added to a database or catalog.</p> </dd> <dt>SCHEDULE</dt> <dd> <p>Each table is evaluated on the cron or rate expression in <code>ScheduleExpression</code>.</p> </dd> <dt>METADATA_CHANGE</dt> <dd> <p>A table is evaluated whenever its Glue Data Catalog metadata changes.</p> </dd> </dl>"""
    schedule_expression: NotRequired[
        "capo_glue.types.data_quality_evaluation_config_schedule_expression.DataQualityEvaluationConfigScheduleExpression"
    ]
    """<p>The cron or rate expression, in UTC, for the <code>SCHEDULE</code> trigger.</p>"""
    start_at: NotRequired["capo_glue.types.timestamp.Timestamp"]
    """<p>The time from which the schedule runs, inclusive.</p>"""
    end_at: NotRequired["capo_glue.types.timestamp.Timestamp"]
    """<p>The time at which the schedule stops running, exclusive.</p>"""
    pause_runs: NotRequired["capo_glue.types.nullable_boolean.NullableBoolean"]
    """<p>Specifies whether evaluations are paused.</p>"""
    role: NotRequired["capo_glue.types.role_string.RoleString"]
    """<p>The Amazon Resource Name (ARN) of the IAM role that evaluation runs assume.</p>"""
    number_of_workers: NotRequired["capo_glue.types.nullable_integer.NullableInteger"]
    """<p>The number of <code>G.1X</code> workers to be used in the run. The default is 5.</p>"""
    timeout: NotRequired["capo_glue.types.timeout.Timeout"]
    """<p>The timeout for a run in minutes. This is the maximum time that a run can consume resources before it is terminated and enters <code>TIMEOUT</code> status. The default is 2,880 minutes (48 hours).</p>"""
    additional_run_options: NotRequired[
        "capo_glue.types.data_quality_evaluation_config_additional_run_options.DataQualityEvaluationConfigAdditionalRunOptions"
    ]
    """<p>Additional run options you can specify for an evaluation run.</p>"""
    additional_data_sources: NotRequired[
        "capo_glue.types.data_source_map.DataSourceMap"
    ]
    """<p>A map of reference strings to additional data sources you can specify for an evaluation run.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateDataQualityEvaluationConfigResponse) -> dict:
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
        import capo_glue.types.data_quality_evaluation_config_data_source

        out["DataSource"] = (
            capo_glue.types.data_quality_evaluation_config_data_source.serialize_aws_json_1_1(
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
    if "triggers" in value:
        import capo_glue.types.data_quality_evaluation_config_triggers

        out["Triggers"] = (
            capo_glue.types.data_quality_evaluation_config_triggers.serialize_aws_json_1_1(
                value["triggers"]
            )
        )
    if "schedule_expression" in value:
        out["ScheduleExpression"] = value["schedule_expression"]
    if "start_at" in value:
        import capo_glue.types.timestamp

        out["StartAt"] = capo_glue.types.timestamp.serialize_aws_json_1_1(
            value["start_at"]
        )
    if "end_at" in value:
        import capo_glue.types.timestamp

        out["EndAt"] = capo_glue.types.timestamp.serialize_aws_json_1_1(value["end_at"])
    if "pause_runs" in value:
        out["PauseRuns"] = value["pause_runs"]
    if "role" in value:
        out["Role"] = value["role"]
    if "number_of_workers" in value:
        out["NumberOfWorkers"] = value["number_of_workers"]
    if "timeout" in value:
        out["Timeout"] = value["timeout"]
    if "additional_run_options" in value:
        import capo_glue.types.data_quality_evaluation_config_additional_run_options

        out["AdditionalRunOptions"] = (
            capo_glue.types.data_quality_evaluation_config_additional_run_options.serialize_aws_json_1_1(
                value["additional_run_options"]
            )
        )
    if "additional_data_sources" in value:
        import capo_glue.types.data_source_map

        out["AdditionalDataSources"] = (
            capo_glue.types.data_source_map.serialize_aws_json_1_1(
                value["additional_data_sources"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateDataQualityEvaluationConfigResponse:
    out: UpdateDataQualityEvaluationConfigResponse = {}  # type: ignore[typeddict-item]
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
        import capo_glue.types.data_quality_evaluation_config_data_source

        out["data_source"] = (
            capo_glue.types.data_quality_evaluation_config_data_source.deserialize_aws_json_1_1(
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
    if data.get("Triggers") is not None:
        import capo_glue.types.data_quality_evaluation_config_triggers

        out["triggers"] = (
            capo_glue.types.data_quality_evaluation_config_triggers.deserialize_aws_json_1_1(
                data["Triggers"]
            )
        )
    if data.get("ScheduleExpression") is not None:
        out["schedule_expression"] = data["ScheduleExpression"]
    if data.get("StartAt") is not None:
        import capo_glue.types.timestamp

        out["start_at"] = capo_glue.types.timestamp.deserialize_aws_json_1_1(
            data["StartAt"]
        )
    if data.get("EndAt") is not None:
        import capo_glue.types.timestamp

        out["end_at"] = capo_glue.types.timestamp.deserialize_aws_json_1_1(
            data["EndAt"]
        )
    if data.get("PauseRuns") is not None:
        out["pause_runs"] = data["PauseRuns"]
    if data.get("Role") is not None:
        out["role"] = data["Role"]
    if data.get("NumberOfWorkers") is not None:
        out["number_of_workers"] = data["NumberOfWorkers"]
    if data.get("Timeout") is not None:
        out["timeout"] = data["Timeout"]
    if data.get("AdditionalRunOptions") is not None:
        import capo_glue.types.data_quality_evaluation_config_additional_run_options

        out["additional_run_options"] = (
            capo_glue.types.data_quality_evaluation_config_additional_run_options.deserialize_aws_json_1_1(
                data["AdditionalRunOptions"]
            )
        )
    if data.get("AdditionalDataSources") is not None:
        import capo_glue.types.data_source_map

        out["additional_data_sources"] = (
            capo_glue.types.data_source_map.deserialize_aws_json_1_1(
                data["AdditionalDataSources"]
            )
        )
    return out
