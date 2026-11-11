"""Generated from Smithy shape ``com.amazonaws.glue#UpdateDataQualityEvaluationConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.data_quality_evaluation_config_additional_run_options
    import capo_glue.types.data_quality_evaluation_config_data_source
    import capo_glue.types.data_quality_evaluation_config_managed_ruleset
    import capo_glue.types.data_quality_evaluation_config_schedule_expression
    import capo_glue.types.data_quality_evaluation_config_triggers
    import capo_glue.types.data_source_map
    import capo_glue.types.name_string
    import capo_glue.types.nullable_boolean
    import capo_glue.types.nullable_integer
    import capo_glue.types.role_string
    import capo_glue.types.timeout
    import capo_glue.types.timestamp


class UpdateDataQualityEvaluationConfigRequest(TypedDict, closed=True):
    name: "capo_glue.types.name_string.NameString"
    """<p>The name of the data quality evaluation configuration to update.</p>"""
    data_source: NotRequired[
        "capo_glue.types.data_quality_evaluation_config_data_source.DataQualityEvaluationConfigDataSource"
    ]
    """<p>The database or table that the configuration applies to. Replaces the current data source.</p>"""
    ruleset_name: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The name of a Data Quality Definition Language (DQDL) ruleset, containing analyzers, rules, or both, to evaluate tables with. You create the ruleset using the <code>CreateDataQualityRuleset</code> API. Specify either <code>RulesetName</code> or <code>ManagedRulesetName</code>, not both.</p>"""
    managed_ruleset_name: NotRequired[
        "capo_glue.types.data_quality_evaluation_config_managed_ruleset.DataQualityEvaluationConfigManagedRuleset"
    ]
    """<p>A built-in ruleset, <code>SIMPLE</code> or <code>ADVANCED</code>, that profiles each table.</p>"""
    triggers: NotRequired[
        "capo_glue.types.data_quality_evaluation_config_triggers.DataQualityEvaluationConfigTriggers"
    ]
    """<p>When the configuration evaluates tables. Replaces the current triggers. Choose from the following triggers:</p> <dl> <dt>ONCE</dt> <dd> <p>Evaluates each table one time, including when tables are added to a database or catalog.</p> </dd> <dt>SCHEDULE</dt> <dd> <p>Evaluates each table on the cron or rate expression in <code>ScheduleExpression</code>, between the optional <code>StartAt</code> and <code>EndAt</code> times.</p> </dd> <dt>METADATA_CHANGE</dt> <dd> <p>Evaluates a table whenever its Glue Data Catalog metadata changes, such as a schema change or an Apache Iceberg commit.</p> </dd> </dl>"""
    schedule_expression: NotRequired[
        "capo_glue.types.data_quality_evaluation_config_schedule_expression.DataQualityEvaluationConfigScheduleExpression"
    ]
    """<p>A cron or rate expression, in UTC, for the <code>SCHEDULE</code> trigger, for example <code>cron(0 6 * * ? *)</code>. The schedule can run at most once an hour.</p>"""
    start_at: NotRequired["capo_glue.types.timestamp.Timestamp"]
    """<p>The time from which the schedule runs, inclusive.</p>"""
    end_at: NotRequired["capo_glue.types.timestamp.Timestamp"]
    """<p>The time at which the schedule stops running, exclusive.</p>"""
    pause_runs: NotRequired["capo_glue.types.nullable_boolean.NullableBoolean"]
    """<p>Specifies whether to pause the configuration. While paused, the configuration evaluates nothing, including tables added to the catalog or database.</p>"""
    role: NotRequired["capo_glue.types.role_string.RoleString"]
    """<p>The IAM role that evaluations assume. You can specify the role name or the role Amazon Resource Name (ARN). The role needs the trust policy and permissions described for <code>CreateDataQualityEvaluationConfig</code>.</p>"""
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
def serialize_aws_json_1_1(value: UpdateDataQualityEvaluationConfigRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
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


def deserialize_aws_json_1_1(data: dict) -> UpdateDataQualityEvaluationConfigRequest:
    out: UpdateDataQualityEvaluationConfigRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
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
