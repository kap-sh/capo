"""Generated from Smithy shape ``com.amazonaws.athena#StartQueryExecutionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_athena.types.engine_configuration
    import capo_athena.types.execution_parameters
    import capo_athena.types.idempotency_token
    import capo_athena.types.query_execution_context
    import capo_athena.types.query_string
    import capo_athena.types.result_configuration
    import capo_athena.types.result_reuse_configuration
    import capo_athena.types.work_group_name


class StartQueryExecutionInput(TypedDict, closed=True):
    query_string: "capo_athena.types.query_string.QueryString"
    """<p>The SQL query statements to be executed.</p>"""
    client_request_token: NotRequired[
        "capo_athena.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A unique case-sensitive string used to ensure the request to create the query is idempotent (executes only once). If another <code>StartQueryExecution</code> request is received, the same response is returned and another query is not created. An error is returned if a parameter, such as <code>QueryString</code>, has changed. A call to <code>StartQueryExecution</code> that uses a previous client request token returns the same <code>QueryExecutionId</code> even if the requester doesn't have permission on the tables specified in <code>QueryString</code>.</p> <important> <p>This token is listed as not required because Amazon Web Services SDKs (for example the Amazon Web Services SDK for Java) auto-generate the token for users. If you are not using the Amazon Web Services SDK or the Amazon Web Services CLI, you must provide this token or the action will fail.</p> </important>"""
    query_execution_context: NotRequired[
        "capo_athena.types.query_execution_context.QueryExecutionContext"
    ]
    """<p>The database within which the query executes.</p>"""
    result_configuration: NotRequired[
        "capo_athena.types.result_configuration.ResultConfiguration"
    ]
    """<p>Specifies information about where and how to save the results of the query execution. If the query runs in a workgroup, then workgroup's settings may override query settings. This affects the query results location. The workgroup settings override is specified in EnforceWorkGroupConfiguration (true/false) in the WorkGroupConfiguration. See <a>WorkGroupConfiguration$EnforceWorkGroupConfiguration</a>.</p>"""
    work_group: NotRequired["capo_athena.types.work_group_name.WorkGroupName"]
    """<p>The name of the workgroup in which the query is being started.</p>"""
    execution_parameters: NotRequired[
        "capo_athena.types.execution_parameters.ExecutionParameters"
    ]
    """<p>A list of values for the parameters in a query. The values are applied sequentially to the parameters in the query in the order in which the parameters occur.</p>"""
    result_reuse_configuration: NotRequired[
        "capo_athena.types.result_reuse_configuration.ResultReuseConfiguration"
    ]
    """<p>Specifies the query result reuse behavior for the query.</p>"""
    engine_configuration: NotRequired[
        "capo_athena.types.engine_configuration.EngineConfiguration"
    ]
    """<p>The engine configuration for the workgroup, which includes the minimum/maximum number of Data Processing Units (DPU) that queries should use when running in provisioned capacity. If not specified, Athena uses default values (Default value for min is 4 and for max is Minimum of 124 and allocated DPUs).</p> <p>To specify minimum and maximum DPU values for Capacity Reservations queries, the workgroup containing <code>EngineConfiguration</code> should have the following values: The name of the <code>Classifications</code> should be <code>athena-query-engine-properties</code>, with the only allowed properties as <code>max-dpu-count</code> and <code>min-dpu-count</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartQueryExecutionInput) -> dict:
    out: dict = {}
    out["QueryString"] = value["query_string"]
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "query_execution_context" in value:
        import capo_athena.types.query_execution_context

        out["QueryExecutionContext"] = (
            capo_athena.types.query_execution_context.serialize_aws_json_1_1(
                value["query_execution_context"]
            )
        )
    if "result_configuration" in value:
        import capo_athena.types.result_configuration

        out["ResultConfiguration"] = (
            capo_athena.types.result_configuration.serialize_aws_json_1_1(
                value["result_configuration"]
            )
        )
    if "work_group" in value:
        out["WorkGroup"] = value["work_group"]
    if "execution_parameters" in value:
        import capo_athena.types.execution_parameters

        out["ExecutionParameters"] = (
            capo_athena.types.execution_parameters.serialize_aws_json_1_1(
                value["execution_parameters"]
            )
        )
    if "result_reuse_configuration" in value:
        import capo_athena.types.result_reuse_configuration

        out["ResultReuseConfiguration"] = (
            capo_athena.types.result_reuse_configuration.serialize_aws_json_1_1(
                value["result_reuse_configuration"]
            )
        )
    if "engine_configuration" in value:
        import capo_athena.types.engine_configuration

        out["EngineConfiguration"] = (
            capo_athena.types.engine_configuration.serialize_aws_json_1_1(
                value["engine_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartQueryExecutionInput:
    out: StartQueryExecutionInput = {}  # type: ignore[typeddict-item]
    if data.get("QueryString") is not None:
        out["query_string"] = data["QueryString"]
    else:
        out["query_string"] = ""
    if data.get("ClientRequestToken") is not None:
        out["client_request_token"] = data["ClientRequestToken"]
    if data.get("QueryExecutionContext") is not None:
        import capo_athena.types.query_execution_context

        out["query_execution_context"] = (
            capo_athena.types.query_execution_context.deserialize_aws_json_1_1(
                data["QueryExecutionContext"]
            )
        )
    if data.get("ResultConfiguration") is not None:
        import capo_athena.types.result_configuration

        out["result_configuration"] = (
            capo_athena.types.result_configuration.deserialize_aws_json_1_1(
                data["ResultConfiguration"]
            )
        )
    if data.get("WorkGroup") is not None:
        out["work_group"] = data["WorkGroup"]
    if data.get("ExecutionParameters") is not None:
        import capo_athena.types.execution_parameters

        out["execution_parameters"] = (
            capo_athena.types.execution_parameters.deserialize_aws_json_1_1(
                data["ExecutionParameters"]
            )
        )
    if data.get("ResultReuseConfiguration") is not None:
        import capo_athena.types.result_reuse_configuration

        out["result_reuse_configuration"] = (
            capo_athena.types.result_reuse_configuration.deserialize_aws_json_1_1(
                data["ResultReuseConfiguration"]
            )
        )
    if data.get("EngineConfiguration") is not None:
        import capo_athena.types.engine_configuration

        out["engine_configuration"] = (
            capo_athena.types.engine_configuration.deserialize_aws_json_1_1(
                data["EngineConfiguration"]
            )
        )
    return out
