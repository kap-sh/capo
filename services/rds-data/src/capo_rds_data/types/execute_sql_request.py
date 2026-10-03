"""Generated from Smithy shape ``com.amazonaws.rdsdata#ExecuteSqlRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds_data.errors import DeserializationError

if TYPE_CHECKING:
    import capo_rds_data.types.arn
    import capo_rds_data.types.db_name
    import capo_rds_data.types.sql_statement


class ExecuteSqlRequest(TypedDict, closed=True):
    db_cluster_or_instance_arn: "capo_rds_data.types.arn.Arn"
    """<p>The ARN of the Aurora Serverless DB cluster.</p>"""
    aws_secret_store_arn: "capo_rds_data.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the secret that enables access to the DB cluster. Enter the database user name and password for the credentials in the secret.</p> <p>For information about creating the secret, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/create_database_secret.html">Create a database secret</a>.</p>"""
    sql_statements: "capo_rds_data.types.sql_statement.SqlStatement"
    """<p>One or more SQL statements to run on the DB cluster.</p> <p>You can separate SQL statements from each other with a semicolon (;). Any valid SQL statement is permitted, including data definition, data manipulation, and commit statements. </p>"""
    database: NotRequired["capo_rds_data.types.db_name.DbName"]
    """<p>The name of the database.</p>"""
    schema: NotRequired["capo_rds_data.types.db_name.DbName"]
    """<p>The name of the database schema.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExecuteSqlRequest) -> dict:
    out: dict = {}
    out["dbClusterOrInstanceArn"] = value["db_cluster_or_instance_arn"]
    out["awsSecretStoreArn"] = value["aws_secret_store_arn"]
    out["sqlStatements"] = value["sql_statements"]
    if "database" in value:
        out["database"] = value["database"]
    if "schema" in value:
        out["schema"] = value["schema"]
    return out


def deserialize_json(data: dict) -> ExecuteSqlRequest:
    out: ExecuteSqlRequest = {}  # type: ignore[typeddict-item]
    if data.get("dbClusterOrInstanceArn") is not None:
        out["db_cluster_or_instance_arn"] = data["dbClusterOrInstanceArn"]
    else:
        raise DeserializationError(
            "ExecuteSqlRequest.db_cluster_or_instance_arn required"
        )
    if data.get("awsSecretStoreArn") is not None:
        out["aws_secret_store_arn"] = data["awsSecretStoreArn"]
    else:
        raise DeserializationError("ExecuteSqlRequest.aws_secret_store_arn required")
    if data.get("sqlStatements") is not None:
        out["sql_statements"] = data["sqlStatements"]
    else:
        raise DeserializationError("ExecuteSqlRequest.sql_statements required")
    if data.get("database") is not None:
        out["database"] = data["database"]
    if data.get("schema") is not None:
        out["schema"] = data["schema"]
    return out
