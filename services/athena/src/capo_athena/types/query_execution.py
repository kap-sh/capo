"""Generated from Smithy shape ``com.amazonaws.athena#QueryExecution``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_athena.types.engine_version
    import capo_athena.types.execution_parameters
    import capo_athena.types.managed_query_results_configuration
    import capo_athena.types.query_execution_context
    import capo_athena.types.query_execution_id
    import capo_athena.types.query_execution_statistics
    import capo_athena.types.query_execution_status
    import capo_athena.types.query_results_s3_access_grants_configuration
    import capo_athena.types.query_string
    import capo_athena.types.result_configuration
    import capo_athena.types.result_reuse_configuration
    import capo_athena.types.statement_type
    import capo_athena.types.string
    import capo_athena.types.work_group_name


class QueryExecution(TypedDict, closed=True):
    query_execution_id: NotRequired[
        "capo_athena.types.query_execution_id.QueryExecutionId"
    ]
    """<p>The unique identifier for each query execution.</p>"""
    query: NotRequired["capo_athena.types.query_string.QueryString"]
    """<p>The SQL query statements which the query execution ran.</p>"""
    statement_type: NotRequired["capo_athena.types.statement_type.StatementType"]
    """<p>The type of query statement that was run. <code>DDL</code> indicates DDL query statements. <code>DML</code> indicates DML (Data Manipulation Language) query statements, such as <code>CREATE TABLE AS SELECT</code>. <code>UTILITY</code> indicates query statements other than DDL and DML, such as <code>SHOW CREATE TABLE</code>, <code>EXPLAIN</code>, <code>DESCRIBE</code>, or <code>SHOW TABLES</code>.</p>"""
    managed_query_results_configuration: NotRequired[
        "capo_athena.types.managed_query_results_configuration.ManagedQueryResultsConfiguration"
    ]
    """<p> The configuration for storing results in Athena owned storage, which includes whether this feature is enabled; whether encryption configuration, if any, is used for encrypting query results. </p>"""
    result_configuration: NotRequired[
        "capo_athena.types.result_configuration.ResultConfiguration"
    ]
    """<p>The location in Amazon S3 where query and calculation results are stored and the encryption option, if any, used for query results. These are known as "client-side settings". If workgroup settings override client-side settings, then the query uses the location for the query results and the encryption configuration that are specified for the workgroup.</p>"""
    result_reuse_configuration: NotRequired[
        "capo_athena.types.result_reuse_configuration.ResultReuseConfiguration"
    ]
    """<p>Specifies the query result reuse behavior that was used for the query.</p>"""
    query_execution_context: NotRequired[
        "capo_athena.types.query_execution_context.QueryExecutionContext"
    ]
    """<p>The database in which the query execution occurred.</p>"""
    status: NotRequired["capo_athena.types.query_execution_status.QueryExecutionStatus"]
    """<p>The completion date, current state, submission time, and state change reason (if applicable) for the query execution.</p>"""
    statistics: NotRequired[
        "capo_athena.types.query_execution_statistics.QueryExecutionStatistics"
    ]
    """<p>Query execution statistics, such as the amount of data scanned, the amount of time that the query took to process, and the type of statement that was run.</p>"""
    work_group: NotRequired["capo_athena.types.work_group_name.WorkGroupName"]
    """<p>The name of the workgroup in which the query ran.</p>"""
    engine_version: NotRequired["capo_athena.types.engine_version.EngineVersion"]
    """<p>The engine version that executed the query.</p>"""
    execution_parameters: NotRequired[
        "capo_athena.types.execution_parameters.ExecutionParameters"
    ]
    """<p>A list of values for the parameters in a query. The values are applied sequentially to the parameters in the query in the order in which the parameters occur. The list of parameters is not returned in the response.</p>"""
    substatement_type: NotRequired["capo_athena.types.string.String"]
    """<p>The kind of query statement that was run.</p>"""
    query_results_s3_access_grants_configuration: NotRequired[
        "capo_athena.types.query_results_s3_access_grants_configuration.QueryResultsS3AccessGrantsConfiguration"
    ]
    """<p>Specifies whether Amazon S3 access grants are enabled for query results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QueryExecution) -> dict:
    out: dict = {}
    if "query_execution_id" in value:
        out["QueryExecutionId"] = value["query_execution_id"]
    if "query" in value:
        out["Query"] = value["query"]
    if "statement_type" in value:
        import capo_athena.types.statement_type

        out["StatementType"] = capo_athena.types.statement_type.serialize_aws_json_1_1(
            value["statement_type"]
        )
    if "managed_query_results_configuration" in value:
        import capo_athena.types.managed_query_results_configuration

        out["ManagedQueryResultsConfiguration"] = (
            capo_athena.types.managed_query_results_configuration.serialize_aws_json_1_1(
                value["managed_query_results_configuration"]
            )
        )
    if "result_configuration" in value:
        import capo_athena.types.result_configuration

        out["ResultConfiguration"] = (
            capo_athena.types.result_configuration.serialize_aws_json_1_1(
                value["result_configuration"]
            )
        )
    if "result_reuse_configuration" in value:
        import capo_athena.types.result_reuse_configuration

        out["ResultReuseConfiguration"] = (
            capo_athena.types.result_reuse_configuration.serialize_aws_json_1_1(
                value["result_reuse_configuration"]
            )
        )
    if "query_execution_context" in value:
        import capo_athena.types.query_execution_context

        out["QueryExecutionContext"] = (
            capo_athena.types.query_execution_context.serialize_aws_json_1_1(
                value["query_execution_context"]
            )
        )
    if "status" in value:
        import capo_athena.types.query_execution_status

        out["Status"] = capo_athena.types.query_execution_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "statistics" in value:
        import capo_athena.types.query_execution_statistics

        out["Statistics"] = (
            capo_athena.types.query_execution_statistics.serialize_aws_json_1_1(
                value["statistics"]
            )
        )
    if "work_group" in value:
        out["WorkGroup"] = value["work_group"]
    if "engine_version" in value:
        import capo_athena.types.engine_version

        out["EngineVersion"] = capo_athena.types.engine_version.serialize_aws_json_1_1(
            value["engine_version"]
        )
    if "execution_parameters" in value:
        import capo_athena.types.execution_parameters

        out["ExecutionParameters"] = (
            capo_athena.types.execution_parameters.serialize_aws_json_1_1(
                value["execution_parameters"]
            )
        )
    if "substatement_type" in value:
        out["SubstatementType"] = value["substatement_type"]
    if "query_results_s3_access_grants_configuration" in value:
        import capo_athena.types.query_results_s3_access_grants_configuration

        out["QueryResultsS3AccessGrantsConfiguration"] = (
            capo_athena.types.query_results_s3_access_grants_configuration.serialize_aws_json_1_1(
                value["query_results_s3_access_grants_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> QueryExecution:
    out: QueryExecution = {}  # type: ignore[typeddict-item]
    if data.get("QueryExecutionId") is not None:
        out["query_execution_id"] = data["QueryExecutionId"]
    if data.get("Query") is not None:
        out["query"] = data["Query"]
    if data.get("StatementType") is not None:
        import capo_athena.types.statement_type

        out["statement_type"] = (
            capo_athena.types.statement_type.deserialize_aws_json_1_1(
                data["StatementType"]
            )
        )
    if data.get("ManagedQueryResultsConfiguration") is not None:
        import capo_athena.types.managed_query_results_configuration

        out["managed_query_results_configuration"] = (
            capo_athena.types.managed_query_results_configuration.deserialize_aws_json_1_1(
                data["ManagedQueryResultsConfiguration"]
            )
        )
    if data.get("ResultConfiguration") is not None:
        import capo_athena.types.result_configuration

        out["result_configuration"] = (
            capo_athena.types.result_configuration.deserialize_aws_json_1_1(
                data["ResultConfiguration"]
            )
        )
    if data.get("ResultReuseConfiguration") is not None:
        import capo_athena.types.result_reuse_configuration

        out["result_reuse_configuration"] = (
            capo_athena.types.result_reuse_configuration.deserialize_aws_json_1_1(
                data["ResultReuseConfiguration"]
            )
        )
    if data.get("QueryExecutionContext") is not None:
        import capo_athena.types.query_execution_context

        out["query_execution_context"] = (
            capo_athena.types.query_execution_context.deserialize_aws_json_1_1(
                data["QueryExecutionContext"]
            )
        )
    if data.get("Status") is not None:
        import capo_athena.types.query_execution_status

        out["status"] = (
            capo_athena.types.query_execution_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if data.get("Statistics") is not None:
        import capo_athena.types.query_execution_statistics

        out["statistics"] = (
            capo_athena.types.query_execution_statistics.deserialize_aws_json_1_1(
                data["Statistics"]
            )
        )
    if data.get("WorkGroup") is not None:
        out["work_group"] = data["WorkGroup"]
    if data.get("EngineVersion") is not None:
        import capo_athena.types.engine_version

        out["engine_version"] = (
            capo_athena.types.engine_version.deserialize_aws_json_1_1(
                data["EngineVersion"]
            )
        )
    if data.get("ExecutionParameters") is not None:
        import capo_athena.types.execution_parameters

        out["execution_parameters"] = (
            capo_athena.types.execution_parameters.deserialize_aws_json_1_1(
                data["ExecutionParameters"]
            )
        )
    if data.get("SubstatementType") is not None:
        out["substatement_type"] = data["SubstatementType"]
    if data.get("QueryResultsS3AccessGrantsConfiguration") is not None:
        import capo_athena.types.query_results_s3_access_grants_configuration

        out["query_results_s3_access_grants_configuration"] = (
            capo_athena.types.query_results_s3_access_grants_configuration.deserialize_aws_json_1_1(
                data["QueryResultsS3AccessGrantsConfiguration"]
            )
        )
    return out
