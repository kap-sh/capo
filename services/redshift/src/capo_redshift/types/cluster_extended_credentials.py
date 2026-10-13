"""Generated from Smithy shape ``com.amazonaws.redshift#ClusterExtendedCredentials``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.sensitive_string
    import capo_redshift.types.string
    import capo_redshift.types.t_stamp


class ClusterExtendedCredentials(TypedDict, closed=True):
    db_user: NotRequired["capo_redshift.types.string.String"]
    """<p>A database user name that you provide when you connect to a database. The database user is mapped 1:1 to the source IAM identity. </p>"""
    db_password: NotRequired["capo_redshift.types.sensitive_string.SensitiveString"]
    """<p>A temporary password that you provide when you connect to a database.</p>"""
    expiration: NotRequired["capo_redshift.types.t_stamp.TStamp"]
    """<p>The time (UTC) when the temporary password expires. After this timestamp, a log in with the temporary password fails.</p>"""
    next_refresh_time: NotRequired["capo_redshift.types.t_stamp.TStamp"]
    """<p>Reserved for future use.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ClusterExtendedCredentials, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "db_user" in value:
        pairs.append((f"{key_prefix}DbUser", str(value["db_user"])))
    if "db_password" in value:
        pairs.append((f"{key_prefix}DbPassword", str(value["db_password"])))
    if "expiration" in value:
        import capo_redshift.types.t_stamp

        capo_redshift.types.t_stamp.serialize_query(
            value["expiration"], pairs, f"{key_prefix}Expiration"
        )
    if "next_refresh_time" in value:
        import capo_redshift.types.t_stamp

        capo_redshift.types.t_stamp.serialize_query(
            value["next_refresh_time"], pairs, f"{key_prefix}NextRefreshTime"
        )


def deserialize_query(el: Element) -> ClusterExtendedCredentials:
    out: ClusterExtendedCredentials = {}  # type: ignore[typeddict-item]
    child_db_user = el.find("DbUser")
    if child_db_user is not None:
        out["db_user"] = str(child_db_user.text or "")
    child_db_password = el.find("DbPassword")
    if child_db_password is not None:
        out["db_password"] = str(child_db_password.text or "")
    child_expiration = el.find("Expiration")
    if child_expiration is not None:
        import capo_redshift.types.t_stamp

        out["expiration"] = capo_redshift.types.t_stamp.deserialize_query(
            child_expiration
        )
    child_next_refresh_time = el.find("NextRefreshTime")
    if child_next_refresh_time is not None:
        import capo_redshift.types.t_stamp

        out["next_refresh_time"] = capo_redshift.types.t_stamp.deserialize_query(
            child_next_refresh_time
        )
    return out


def redact_sensitive(value: ClusterExtendedCredentials) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "db_password" in value:
        out["db_password"] = "*** Sensitive Data Redacted ***"
    return out
