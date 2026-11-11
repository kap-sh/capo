"""Generated from Smithy shape ``com.amazonaws.glue#CreateDataQualityEvaluationConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.client_token_string
    import capo_glue.types.data_quality_evaluation_config_additional_run_options
    import capo_glue.types.data_quality_evaluation_config_data_source
    import capo_glue.types.data_quality_evaluation_config_level
    import capo_glue.types.data_quality_evaluation_config_managed_ruleset
    import capo_glue.types.data_quality_evaluation_config_schedule_expression
    import capo_glue.types.data_quality_evaluation_config_triggers
    import capo_glue.types.data_source_map
    import capo_glue.types.name_string
    import capo_glue.types.nullable_integer
    import capo_glue.types.role_string
    import capo_glue.types.tags_map
    import capo_glue.types.timeout
    import capo_glue.types.timestamp


class CreateDataQualityEvaluationConfigRequest(TypedDict, closed=True):
    name: "capo_glue.types.name_string.NameString"
    """<p>A name for the data quality evaluation configuration. The name must be unique within your account.</p>"""
    level: "capo_glue.types.data_quality_evaluation_config_level.DataQualityEvaluationConfigLevel"
    """<p>The Glue Data Catalog hierarchical level that the configuration applies to. Valid values are <code>CATALOG</code>, <code>DATABASE</code>, and <code>TABLE</code>.</p>"""
    data_source: "capo_glue.types.data_quality_evaluation_config_data_source.DataQualityEvaluationConfigDataSource"
    """<p>The catalog, database, or table that the configuration applies to, as specified by <code>Level</code>.</p>"""
    ruleset_name: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The name of a Data Quality Definition Language (DQDL) ruleset, containing analyzers, rules, or both, to evaluate tables with. You create the ruleset using the <code>CreateDataQualityRuleset</code> API. Specify either <code>RulesetName</code> or <code>ManagedRulesetName</code>, not both.</p>"""
    managed_ruleset_name: NotRequired[
        "capo_glue.types.data_quality_evaluation_config_managed_ruleset.DataQualityEvaluationConfigManagedRuleset"
    ]
    """<p>A built-in ruleset that profiles each table, used when <code>RulesetName</code> is not set. The default is <code>SIMPLE</code>. Choose from the following built-in rulesets:</p> <dl> <dt>SIMPLE</dt> <dd> <p>Row count and column count, completeness, minimum, and maximum for every column, mean, sum, and standard deviation for numeric columns, and column length for string columns.</p> </dd> <dt>ADVANCED</dt> <dd> <p>Every statistic in <code>SIMPLE</code>, plus distribution, uniqueness, and distinct values count.</p> </dd> </dl>"""
    triggers: NotRequired[
        "capo_glue.types.data_quality_evaluation_config_triggers.DataQualityEvaluationConfigTriggers"
    ]
    """<p>When the configuration evaluates tables. You can choose one or more triggers, and each table is evaluated at most once an hour. The default is <code>ONCE</code>. Choose from the following triggers:</p> <dl> <dt>ONCE</dt> <dd> <p>Evaluates each table one time, including when tables are added to a database or catalog.</p> </dd> <dt>SCHEDULE</dt> <dd> <p>Evaluates each table on the cron or rate expression in <code>ScheduleExpression</code>, between the optional <code>StartAt</code> and <code>EndAt</code> times.</p> </dd> <dt>METADATA_CHANGE</dt> <dd> <p>Evaluates a table whenever its Glue Data Catalog metadata changes, such as a schema change or an Apache Iceberg commit.</p> </dd> </dl>"""
    schedule_expression: NotRequired[
        "capo_glue.types.data_quality_evaluation_config_schedule_expression.DataQualityEvaluationConfigScheduleExpression"
    ]
    """<p>A cron or rate expression, in UTC, for the <code>SCHEDULE</code> trigger, for example <code>cron(0 6 * * ? *)</code>. The schedule can run at most once an hour.</p>"""
    start_at: NotRequired["capo_glue.types.timestamp.Timestamp"]
    """<p>The time from which the schedule runs, inclusive.</p>"""
    end_at: NotRequired["capo_glue.types.timestamp.Timestamp"]
    """<p>The time at which the schedule stops running, exclusive.</p>"""
    role: "capo_glue.types.role_string.RoleString"
    """<p>The IAM role that evaluations assume. You can specify the role name or the role Amazon Resource Name (ARN).</p> <p>The role must allow the <code>glue.amazonaws.com</code> service principal to assume it, and needs permissions to read the catalog (<code>glue:GetCatalog</code>, <code>glue:GetDatabase</code>, <code>glue:GetTable</code>, <code>glue:SearchTables</code>, and <code>glue:GetPartitions</code>), read and create rulesets (<code>glue:GetDataQualityRuleset</code> and <code>glue:CreateDataQualityRuleset</code>), start evaluations (<code>glue:StartDataQualityRulesetEvaluationRun</code>, <code>glue:PublishDataQuality</code>, and <code>iam:PassRole</code> on the role itself), read the tables' data in Amazon S3, and write logs to Amazon CloudWatch Logs. If a catalog-level or database-level configuration applies to an Amazon S3 Tables catalog, the role also needs <code>s3tables:ListTableBuckets</code> and <code>s3tables:ListTables</code>. If you use Lake Formation, the role needs the <code>DESCRIBE</code> permission on the tables.</p>"""
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
    tags: NotRequired["capo_glue.types.tags_map.TagsMap"]
    """<p>A list of tags applied to the data quality evaluation configuration.</p>"""
    client_token: NotRequired["capo_glue.types.client_token_string.ClientTokenString"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the operation completes no more than one time. If this token matches a previous request, the service ignores the request, but does not return an error.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDataQualityEvaluationConfigRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_glue.types.data_quality_evaluation_config_level

    out["Level"] = (
        capo_glue.types.data_quality_evaluation_config_level.serialize_aws_json_1_1(
            value["level"]
        )
    )
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
    if "tags" in value:
        import capo_glue.types.tags_map

        out["Tags"] = capo_glue.types.tags_map.serialize_aws_json_1_1(value["tags"])
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDataQualityEvaluationConfigRequest:
    out: CreateDataQualityEvaluationConfigRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Level") is not None:
        import capo_glue.types.data_quality_evaluation_config_level

        out["level"] = (
            capo_glue.types.data_quality_evaluation_config_level.deserialize_aws_json_1_1(
                data["Level"]
            )
        )
    else:
        import typing

        out["level"] = typing.cast(
            "capo_glue.types.data_quality_evaluation_config_level.DataQualityEvaluationConfigLevel",
            "",
        )
    if data.get("DataSource") is not None:
        import capo_glue.types.data_quality_evaluation_config_data_source

        out["data_source"] = (
            capo_glue.types.data_quality_evaluation_config_data_source.deserialize_aws_json_1_1(
                data["DataSource"]
            )
        )
    else:
        raise DeserializationError(
            "CreateDataQualityEvaluationConfigRequest.data_source required"
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
    if data.get("Role") is not None:
        out["role"] = data["Role"]
    else:
        out["role"] = ""
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
    if data.get("Tags") is not None:
        import capo_glue.types.tags_map

        out["tags"] = capo_glue.types.tags_map.deserialize_aws_json_1_1(data["Tags"])
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out
