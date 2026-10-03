"""Generated from Smithy shape ``com.amazonaws.rdsdata#BatchExecuteStatementRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds_data.errors import DeserializationError

if TYPE_CHECKING:
    import capo_rds_data.types.arn
    import capo_rds_data.types.db_name
    import capo_rds_data.types.id
    import capo_rds_data.types.sql_parameter_sets
    import capo_rds_data.types.sql_statement


class BatchExecuteStatementRequest(TypedDict, closed=True):
    resource_arn: "capo_rds_data.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the Aurora Serverless DB cluster.</p>"""
    secret_arn: "capo_rds_data.types.arn.Arn"
    """<p>The ARN of the secret that enables access to the DB cluster. Enter the database user name and password for the credentials in the secret.</p> <p>For information about creating the secret, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/create_database_secret.html">Create a database secret</a>.</p>"""
    sql: "capo_rds_data.types.sql_statement.SqlStatement"
    """<p>The SQL statement to run. Don't include a semicolon (;) at the end of the SQL statement.</p>"""
    database: NotRequired["capo_rds_data.types.db_name.DbName"]
    """<p>The name of the database.</p>"""
    schema: NotRequired["capo_rds_data.types.db_name.DbName"]
    """<p>The name of the database schema.</p> <note> <p>Currently, the <code>schema</code> parameter isn't supported.</p> </note>"""
    parameter_sets: NotRequired[
        "capo_rds_data.types.sql_parameter_sets.SqlParameterSets"
    ]
    """<p>The parameter set for the batch operation.</p> <p>The SQL statement is executed as many times as the number of parameter sets provided. To execute a SQL statement with no parameters, use one of the following options:</p> <ul> <li> <p>Specify one or more empty parameter sets.</p> </li> <li> <p>Use the <code>ExecuteStatement</code> operation instead of the <code>BatchExecuteStatement</code> operation.</p> </li> </ul> <note> <p>Array parameters are not supported.</p> </note>"""
    transaction_id: NotRequired["capo_rds_data.types.id.Id"]
    """<p>The identifier of a transaction that was started by using the <code>BeginTransaction</code> operation. Specify the transaction ID of the transaction that you want to include the SQL statement in.</p> <p>If the SQL statement is not part of a transaction, don't set this parameter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchExecuteStatementRequest) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    out["secretArn"] = value["secret_arn"]
    out["sql"] = value["sql"]
    if "database" in value:
        out["database"] = value["database"]
    if "schema" in value:
        out["schema"] = value["schema"]
    if "parameter_sets" in value:
        import capo_rds_data.types.sql_parameter_sets

        out["parameterSets"] = capo_rds_data.types.sql_parameter_sets.serialize_json(
            value["parameter_sets"]
        )
    if "transaction_id" in value:
        out["transactionId"] = value["transaction_id"]
    return out


def deserialize_json(data: dict) -> BatchExecuteStatementRequest:
    out: BatchExecuteStatementRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError("BatchExecuteStatementRequest.resource_arn required")
    if data.get("secretArn") is not None:
        out["secret_arn"] = data["secretArn"]
    else:
        raise DeserializationError("BatchExecuteStatementRequest.secret_arn required")
    if data.get("sql") is not None:
        out["sql"] = data["sql"]
    else:
        raise DeserializationError("BatchExecuteStatementRequest.sql required")
    if data.get("database") is not None:
        out["database"] = data["database"]
    if data.get("schema") is not None:
        out["schema"] = data["schema"]
    if data.get("parameterSets") is not None:
        import capo_rds_data.types.sql_parameter_sets

        out["parameter_sets"] = capo_rds_data.types.sql_parameter_sets.deserialize_json(
            data["parameterSets"]
        )
    if data.get("transactionId") is not None:
        out["transaction_id"] = data["transactionId"]
    return out
