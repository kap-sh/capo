"""Generated from Smithy shape ``com.amazonaws.pipes#PipeTargetRedshiftDataParameters``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pipes.types.boolean
    import capo_pipes.types.database
    import capo_pipes.types.db_user
    import capo_pipes.types.secret_manager_arn_or_json_path
    import capo_pipes.types.sqls
    import capo_pipes.types.statement_name


class PipeTargetRedshiftDataParameters(TypedDict, closed=True):
    secret_manager_arn: NotRequired[
        "capo_pipes.types.secret_manager_arn_or_json_path.SecretManagerArnOrJsonPath"
    ]
    """<p>The name or ARN of the secret that enables access to the database. Required when authenticating using Secrets Manager.</p>"""
    database: "capo_pipes.types.database.Database"
    """<p>The name of the database. Required when authenticating using temporary credentials.</p>"""
    db_user: NotRequired["capo_pipes.types.db_user.DbUser"]
    """<p>The database user name. Required when authenticating using temporary credentials.</p>"""
    statement_name: NotRequired["capo_pipes.types.statement_name.StatementName"]
    """<p>The name of the SQL statement. You can name the SQL statement when you create it to identify the query.</p>"""
    with_event: "capo_pipes.types.boolean.Boolean"
    """<p>Indicates whether to send an event back to EventBridge after the SQL statement runs.</p>"""
    sqls: "capo_pipes.types.sqls.Sqls"
    """<p>The SQL statement text to run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PipeTargetRedshiftDataParameters) -> dict:
    out: dict = {}
    if "secret_manager_arn" in value:
        out["SecretManagerArn"] = value["secret_manager_arn"]
    out["Database"] = value["database"]
    if "db_user" in value:
        out["DbUser"] = value["db_user"]
    if "statement_name" in value:
        out["StatementName"] = value["statement_name"]
    out["WithEvent"] = value.get("with_event", False)
    import capo_pipes.types.sqls

    out["Sqls"] = capo_pipes.types.sqls.serialize_json(value["sqls"])
    return out


def deserialize_json(data: dict) -> PipeTargetRedshiftDataParameters:
    out: PipeTargetRedshiftDataParameters = {}  # type: ignore[typeddict-item]
    if data.get("SecretManagerArn") is not None:
        out["secret_manager_arn"] = data["SecretManagerArn"]
    if data.get("Database") is not None:
        out["database"] = data["Database"]
    else:
        out["database"] = ""
    if data.get("DbUser") is not None:
        out["db_user"] = data["DbUser"]
    if data.get("StatementName") is not None:
        out["statement_name"] = data["StatementName"]
    if data.get("WithEvent") is not None:
        out["with_event"] = data["WithEvent"]
    else:
        out["with_event"] = False
    if data.get("Sqls") is not None:
        import capo_pipes.types.sqls

        out["sqls"] = capo_pipes.types.sqls.deserialize_json(data["Sqls"])
    else:
        out["sqls"] = []
    return out


def redact_sensitive(value: PipeTargetRedshiftDataParameters) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "database" in value:
        out["database"] = "*** Sensitive Data Redacted ***"
    if "db_user" in value:
        out["db_user"] = "*** Sensitive Data Redacted ***"
    if "statement_name" in value:
        out["statement_name"] = "*** Sensitive Data Redacted ***"
    if "sqls" in value:
        import capo_pipes.types.sqls

        out["sqls"] = capo_pipes.types.sqls.redact_sensitive(value["sqls"])
    return out
