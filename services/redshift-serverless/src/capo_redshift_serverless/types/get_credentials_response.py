"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#GetCredentialsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_redshift_serverless.types.db_password
    import capo_redshift_serverless.types.db_user


class GetCredentialsResponse(TypedDict, closed=True):
    db_user: NotRequired["capo_redshift_serverless.types.db_user.DbUser"]
    """<p>A database user name that is authorized to log on to the database <code>DbName</code> using the password <code>DbPassword</code>. If the specified <code>DbUser</code> exists in the database, the new user name has the same database privileges as the the user named in <code>DbUser</code>. By default, the user is added to PUBLIC.</p>"""
    db_password: NotRequired["capo_redshift_serverless.types.db_password.DbPassword"]
    """<p>A temporary password that authorizes the user name returned by <code>DbUser</code> to log on to the database <code>DbName</code>.</p>"""
    expiration: NotRequired["datetime.datetime"]
    """<p>The date and time the password in <code>DbPassword</code> expires.</p>"""
    next_refresh_time: NotRequired["datetime.datetime"]
    """<p>The date and time of when the <code>DbUser</code> and <code>DbPassword</code> authorization refreshes.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCredentialsResponse) -> dict:
    out: dict = {}
    if "db_user" in value:
        out["dbUser"] = value["db_user"]
    if "db_password" in value:
        out["dbPassword"] = value["db_password"]
    if "expiration" in value:
        import capo_redshift_serverless.types._prelude.timestamp

        out["expiration"] = (
            capo_redshift_serverless.types._prelude.timestamp.serialize_aws_json_1_1(
                value["expiration"]
            )
        )
    if "next_refresh_time" in value:
        import capo_redshift_serverless.types._prelude.timestamp

        out["nextRefreshTime"] = (
            capo_redshift_serverless.types._prelude.timestamp.serialize_aws_json_1_1(
                value["next_refresh_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCredentialsResponse:
    out: GetCredentialsResponse = {}  # type: ignore[typeddict-item]
    if data.get("dbUser") is not None:
        out["db_user"] = data["dbUser"]
    if data.get("dbPassword") is not None:
        out["db_password"] = data["dbPassword"]
    if data.get("expiration") is not None:
        import capo_redshift_serverless.types._prelude.timestamp

        out["expiration"] = (
            capo_redshift_serverless.types._prelude.timestamp.deserialize_aws_json_1_1(
                data["expiration"]
            )
        )
    if data.get("nextRefreshTime") is not None:
        import capo_redshift_serverless.types._prelude.timestamp

        out["next_refresh_time"] = (
            capo_redshift_serverless.types._prelude.timestamp.deserialize_aws_json_1_1(
                data["nextRefreshTime"]
            )
        )
    return out


def redact_sensitive(value: GetCredentialsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "db_user" in value:
        out["db_user"] = "*** Sensitive Data Redacted ***"
    if "db_password" in value:
        out["db_password"] = "*** Sensitive Data Redacted ***"
    return out
