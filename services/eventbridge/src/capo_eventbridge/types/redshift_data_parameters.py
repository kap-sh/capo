"""Generated from Smithy shape ``com.amazonaws.eventbridge#RedshiftDataParameters``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_eventbridge.errors import DeserializationError

if TYPE_CHECKING:
    import capo_eventbridge.types.boolean
    import capo_eventbridge.types.database
    import capo_eventbridge.types.db_user
    import capo_eventbridge.types.redshift_secret_manager_arn
    import capo_eventbridge.types.sql
    import capo_eventbridge.types.sqls
    import capo_eventbridge.types.statement_name


class RedshiftDataParameters(TypedDict, closed=True):
    secret_manager_arn: NotRequired[
        "capo_eventbridge.types.redshift_secret_manager_arn.RedshiftSecretManagerArn"
    ]
    """<p>The name or ARN of the secret that enables access to the database. Required when authenticating using Amazon Web Services Secrets Manager.</p>"""
    database: "capo_eventbridge.types.database.Database"
    """<p>The name of the database. Required when authenticating using temporary credentials.</p>"""
    db_user: NotRequired["capo_eventbridge.types.db_user.DbUser"]
    """<p>The database user name. Required when authenticating using temporary credentials.</p>"""
    sql: NotRequired["capo_eventbridge.types.sql.Sql"]
    """<p>The SQL statement text to run.</p>"""
    statement_name: NotRequired["capo_eventbridge.types.statement_name.StatementName"]
    """<p>The name of the SQL statement. You can name the SQL statement when you create it to identify the query.</p>"""
    with_event: "capo_eventbridge.types.boolean.Boolean"
    """<p>Indicates whether to send an event back to EventBridge after the SQL statement runs.</p>"""
    sqls: NotRequired["capo_eventbridge.types.sqls.Sqls"]
    """<p>One or more SQL statements to run. The SQL statements are run as a single transaction. They run serially in the order of the array. Subsequent SQL statements don't start until the previous statement in the array completes. If any SQL statement fails, then because they are run as one transaction, all work is rolled back.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RedshiftDataParameters) -> dict:
    out: dict = {}
    if "secret_manager_arn" in value:
        out["SecretManagerArn"] = value["secret_manager_arn"]
    out["Database"] = value["database"]
    if "db_user" in value:
        out["DbUser"] = value["db_user"]
    if "sql" in value:
        out["Sql"] = value["sql"]
    if "statement_name" in value:
        out["StatementName"] = value["statement_name"]
    out["WithEvent"] = value.get("with_event", False)
    if "sqls" in value:
        import capo_eventbridge.types.sqls

        out["Sqls"] = capo_eventbridge.types.sqls.serialize_aws_json_1_1(value["sqls"])
    return out


def deserialize_aws_json_1_1(data: dict) -> RedshiftDataParameters:
    out: RedshiftDataParameters = {}  # type: ignore[typeddict-item]
    if data.get("SecretManagerArn") is not None:
        out["secret_manager_arn"] = data["SecretManagerArn"]
    if data.get("Database") is not None:
        out["database"] = data["Database"]
    else:
        raise DeserializationError("RedshiftDataParameters.database required")
    if data.get("DbUser") is not None:
        out["db_user"] = data["DbUser"]
    if data.get("Sql") is not None:
        out["sql"] = data["Sql"]
    if data.get("StatementName") is not None:
        out["statement_name"] = data["StatementName"]
    if data.get("WithEvent") is not None:
        out["with_event"] = data["WithEvent"]
    else:
        out["with_event"] = False
    if data.get("Sqls") is not None:
        import capo_eventbridge.types.sqls

        out["sqls"] = capo_eventbridge.types.sqls.deserialize_aws_json_1_1(data["Sqls"])
    return out


def redact_sensitive(value: RedshiftDataParameters) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "sql" in value:
        out["sql"] = "*** Sensitive Data Redacted ***"
    if "sqls" in value:
        out["sqls"] = "*** Sensitive Data Redacted ***"
    return out
