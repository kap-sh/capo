"""Generated from Smithy shape ``com.amazonaws.rdsdata#ExecuteStatementRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds_data.errors import DeserializationError

if TYPE_CHECKING:
    import capo_rds_data.types.arn
    import capo_rds_data.types.boolean
    import capo_rds_data.types.db_name
    import capo_rds_data.types.id
    import capo_rds_data.types.records_format_type
    import capo_rds_data.types.result_set_options
    import capo_rds_data.types.sql_parameters_list
    import capo_rds_data.types.sql_statement


class ExecuteStatementRequest(TypedDict, closed=True):
    resource_arn: "capo_rds_data.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the Aurora Serverless DB cluster.</p>"""
    secret_arn: "capo_rds_data.types.arn.Arn"
    r"""<p>The ARN of the secret that enables access to the DB cluster. Enter the database user name and password for the credentials in the secret.</p> <p>For information about creating the secret, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/create_database_secret.html">Create a database secret</a>.</p> <note> <p>When you use the CLI on Linux to reference a secret created in the RDS console, the ARN might include special characters like <code>rds!cluster</code>. If you enclose the ARN in double quotes, the <code>!</code> character might trigger a shell expansion error, such as <code>-bash: !cluster: event not found</code>. To avoid this, escape the exclamation mark (\!) in the ARN or enclose the entire ARN in single quotes (') instead of double quotes.</p> <p>Alternatively, disable shell history expansion by running <code>set +H</code> before you execute the command.</p> </note>"""
    sql: "capo_rds_data.types.sql_statement.SqlStatement"
    """<p>The SQL statement to run.</p>"""
    database: NotRequired["capo_rds_data.types.db_name.DbName"]
    """<p>The name of the database.</p>"""
    schema: NotRequired["capo_rds_data.types.db_name.DbName"]
    """<p>The name of the database schema.</p> <note> <p>Currently, the <code>schema</code> parameter isn't supported.</p> </note>"""
    parameters: NotRequired["capo_rds_data.types.sql_parameters_list.SqlParametersList"]
    """<p>The parameters for the SQL statement.</p> <note> <p>Array parameters are not supported.</p> </note>"""
    transaction_id: NotRequired["capo_rds_data.types.id.Id"]
    """<p>The identifier of a transaction that was started by using the <code>BeginTransaction</code> operation. Specify the transaction ID of the transaction that you want to include the SQL statement in.</p> <p>If the SQL statement is not part of a transaction, don't set this parameter.</p>"""
    include_result_metadata: "capo_rds_data.types.boolean.Boolean"
    """<p>A value that indicates whether to include metadata in the results.</p>"""
    continue_after_timeout: "capo_rds_data.types.boolean.Boolean"
    """<p>A value that indicates whether to continue running the statement after the call times out. By default, the statement stops running when the call times out.</p> <note> <p>For DDL statements, we recommend continuing to run the statement after the call times out. When a DDL statement terminates before it is finished running, it can result in errors and possibly corrupted data structures.</p> </note>"""
    result_set_options: NotRequired[
        "capo_rds_data.types.result_set_options.ResultSetOptions"
    ]
    """<p>Options that control how the result set is returned.</p>"""
    format_records_as: NotRequired[
        "capo_rds_data.types.records_format_type.RecordsFormatType"
    ]
    """<p>A value that indicates whether to format the result set as a single JSON string. This parameter only applies to <code>SELECT</code> statements and is ignored for other types of statements. Allowed values are <code>NONE</code> and <code>JSON</code>. The default value is <code>NONE</code>. The result is returned in the <code>formattedRecords</code> field.</p> <p>For usage information about the JSON format for result sets, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/data-api.html">Using the Data API</a> in the <i>Amazon Aurora User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExecuteStatementRequest) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    out["secretArn"] = value["secret_arn"]
    out["sql"] = value["sql"]
    if "database" in value:
        out["database"] = value["database"]
    if "schema" in value:
        out["schema"] = value["schema"]
    if "parameters" in value:
        import capo_rds_data.types.sql_parameters_list

        out["parameters"] = capo_rds_data.types.sql_parameters_list.serialize_json(
            value["parameters"]
        )
    if "transaction_id" in value:
        out["transactionId"] = value["transaction_id"]
    out["includeResultMetadata"] = value.get("include_result_metadata", False)
    out["continueAfterTimeout"] = value.get("continue_after_timeout", False)
    if "result_set_options" in value:
        import capo_rds_data.types.result_set_options

        out["resultSetOptions"] = capo_rds_data.types.result_set_options.serialize_json(
            value["result_set_options"]
        )
    if "format_records_as" in value:
        import capo_rds_data.types.records_format_type

        out["formatRecordsAs"] = capo_rds_data.types.records_format_type.serialize_json(
            value["format_records_as"]
        )
    return out


def deserialize_json(data: dict) -> ExecuteStatementRequest:
    out: ExecuteStatementRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError("ExecuteStatementRequest.resource_arn required")
    if data.get("secretArn") is not None:
        out["secret_arn"] = data["secretArn"]
    else:
        raise DeserializationError("ExecuteStatementRequest.secret_arn required")
    if data.get("sql") is not None:
        out["sql"] = data["sql"]
    else:
        raise DeserializationError("ExecuteStatementRequest.sql required")
    if data.get("database") is not None:
        out["database"] = data["database"]
    if data.get("schema") is not None:
        out["schema"] = data["schema"]
    if data.get("parameters") is not None:
        import capo_rds_data.types.sql_parameters_list

        out["parameters"] = capo_rds_data.types.sql_parameters_list.deserialize_json(
            data["parameters"]
        )
    if data.get("transactionId") is not None:
        out["transaction_id"] = data["transactionId"]
    if data.get("includeResultMetadata") is not None:
        out["include_result_metadata"] = data["includeResultMetadata"]
    else:
        out["include_result_metadata"] = False
    if data.get("continueAfterTimeout") is not None:
        out["continue_after_timeout"] = data["continueAfterTimeout"]
    else:
        out["continue_after_timeout"] = False
    if data.get("resultSetOptions") is not None:
        import capo_rds_data.types.result_set_options

        out["result_set_options"] = (
            capo_rds_data.types.result_set_options.deserialize_json(
                data["resultSetOptions"]
            )
        )
    if data.get("formatRecordsAs") is not None:
        import capo_rds_data.types.records_format_type

        out["format_records_as"] = (
            capo_rds_data.types.records_format_type.deserialize_json(
                data["formatRecordsAs"]
            )
        )
    return out
