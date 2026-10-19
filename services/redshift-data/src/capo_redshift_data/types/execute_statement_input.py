"""Generated from Smithy shape ``com.amazonaws.redshiftdata#ExecuteStatementInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_redshift_data.types.client_token
    import capo_redshift_data.types.cluster_identifier_string
    import capo_redshift_data.types.result_format_string
    import capo_redshift_data.types.secret_arn
    import capo_redshift_data.types.session_alive_seconds
    import capo_redshift_data.types.sql_parameters_list
    import capo_redshift_data.types.statement_name_string
    import capo_redshift_data.types.statement_string
    import capo_redshift_data.types.string
    import capo_redshift_data.types.uuid
    import capo_redshift_data.types.wait_time_seconds
    import capo_redshift_data.types.workgroup_name_string


class ExecuteStatementInput(TypedDict, closed=True):
    sql: "capo_redshift_data.types.statement_string.StatementString"
    """<p>The SQL statement text to run. </p>"""
    cluster_identifier: NotRequired[
        "capo_redshift_data.types.cluster_identifier_string.ClusterIdentifierString"
    ]
    """<p>The cluster identifier. This parameter is required when connecting to a cluster and authenticating using either Secrets Manager or temporary credentials. </p>"""
    secret_arn: NotRequired["capo_redshift_data.types.secret_arn.SecretArn"]
    """<p>The name or ARN of the secret that enables access to the database. This parameter is required when authenticating using Secrets Manager. </p>"""
    db_user: NotRequired["capo_redshift_data.types.string.String"]
    """<p>The database user name. This parameter is required when connecting to a cluster as a database user and authenticating using temporary credentials. </p>"""
    database: NotRequired["capo_redshift_data.types.string.String"]
    """<p>The name of the database. This parameter is required when authenticating using either Secrets Manager or temporary credentials. </p>"""
    with_event: NotRequired["bool"]
    """<p>A value that indicates whether to send an event to the Amazon EventBridge event bus after the SQL statement runs. </p>"""
    statement_name: NotRequired[
        "capo_redshift_data.types.statement_name_string.StatementNameString"
    ]
    """<p>The name of the SQL statement. You can name the SQL statement when you create it to identify the query. </p>"""
    parameters: NotRequired[
        "capo_redshift_data.types.sql_parameters_list.SqlParametersList"
    ]
    """<p>The parameters for the SQL statement.</p>"""
    workgroup_name: NotRequired[
        "capo_redshift_data.types.workgroup_name_string.WorkgroupNameString"
    ]
    """<p>The serverless workgroup name or Amazon Resource Name (ARN). This parameter is required when connecting to a serverless workgroup and authenticating using either Secrets Manager or temporary credentials.</p>"""
    client_token: NotRequired["capo_redshift_data.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""
    result_format: NotRequired[
        "capo_redshift_data.types.result_format_string.ResultFormatString"
    ]
    """<p>The data format of the result of the SQL statement. If no format is specified, the default is JSON.</p>"""
    session_keep_alive_seconds: NotRequired[
        "capo_redshift_data.types.session_alive_seconds.SessionAliveSeconds"
    ]
    """<p>The number of seconds to keep the session alive after the query finishes. The maximum time a session can keep alive is 24 hours. After 24 hours, the session is forced closed and the query is terminated.</p>"""
    session_id: NotRequired["capo_redshift_data.types.uuid.UUID"]
    """<p>The session identifier of the query.</p>"""
    wait_time_seconds: NotRequired[
        "capo_redshift_data.types.wait_time_seconds.WaitTimeSeconds"
    ]
    """<p>The number of seconds to wait for the SQL statement to complete execution before returning the response. If the SQL statement does not complete within the specified time, the response returns the current status. The maximum value is 30 seconds.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExecuteStatementInput) -> dict:
    out: dict = {}
    out["Sql"] = value["sql"]
    if "cluster_identifier" in value:
        out["ClusterIdentifier"] = value["cluster_identifier"]
    if "secret_arn" in value:
        out["SecretArn"] = value["secret_arn"]
    if "db_user" in value:
        out["DbUser"] = value["db_user"]
    if "database" in value:
        out["Database"] = value["database"]
    if "with_event" in value:
        out["WithEvent"] = value["with_event"]
    if "statement_name" in value:
        out["StatementName"] = value["statement_name"]
    if "parameters" in value:
        import capo_redshift_data.types.sql_parameters_list

        out["Parameters"] = (
            capo_redshift_data.types.sql_parameters_list.serialize_aws_json_1_1(
                value["parameters"]
            )
        )
    if "workgroup_name" in value:
        out["WorkgroupName"] = value["workgroup_name"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "result_format" in value:
        out["ResultFormat"] = value["result_format"]
    if "session_keep_alive_seconds" in value:
        out["SessionKeepAliveSeconds"] = value["session_keep_alive_seconds"]
    if "session_id" in value:
        out["SessionId"] = value["session_id"]
    if "wait_time_seconds" in value:
        out["WaitTimeSeconds"] = value["wait_time_seconds"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ExecuteStatementInput:
    out: ExecuteStatementInput = {}  # type: ignore[typeddict-item]
    if data.get("Sql") is not None:
        out["sql"] = data["Sql"]
    else:
        out["sql"] = ""
    if data.get("ClusterIdentifier") is not None:
        out["cluster_identifier"] = data["ClusterIdentifier"]
    if data.get("SecretArn") is not None:
        out["secret_arn"] = data["SecretArn"]
    if data.get("DbUser") is not None:
        out["db_user"] = data["DbUser"]
    if data.get("Database") is not None:
        out["database"] = data["Database"]
    if data.get("WithEvent") is not None:
        out["with_event"] = data["WithEvent"]
    if data.get("StatementName") is not None:
        out["statement_name"] = data["StatementName"]
    if data.get("Parameters") is not None:
        import capo_redshift_data.types.sql_parameters_list

        out["parameters"] = (
            capo_redshift_data.types.sql_parameters_list.deserialize_aws_json_1_1(
                data["Parameters"]
            )
        )
    if data.get("WorkgroupName") is not None:
        out["workgroup_name"] = data["WorkgroupName"]
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("ResultFormat") is not None:
        out["result_format"] = data["ResultFormat"]
    if data.get("SessionKeepAliveSeconds") is not None:
        out["session_keep_alive_seconds"] = data["SessionKeepAliveSeconds"]
    if data.get("SessionId") is not None:
        out["session_id"] = data["SessionId"]
    if data.get("WaitTimeSeconds") is not None:
        out["wait_time_seconds"] = data["WaitTimeSeconds"]
    return out
