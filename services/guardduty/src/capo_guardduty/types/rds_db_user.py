"""Generated from Smithy shape ``com.amazonaws.guardduty#RdsDbUser``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.string


class RdsDbUser(TypedDict, closed=True):
    user: NotRequired["capo_guardduty.types.string.String"]
    """<p>The user name that was used to log in.</p>"""
    application: NotRequired["capo_guardduty.types.string.String"]
    """<p>The name of the application that was used to log in.</p>"""
    database: NotRequired["capo_guardduty.types.string.String"]
    """<p>The name of the database that the user logged in to.</p>"""
    auth_method: NotRequired["capo_guardduty.types.string.String"]
    """<p>The authentication method that the user used.</p>"""
    ssl: NotRequired["capo_guardduty.types.string.String"]
    """<p>The version of Secure Sockets Layer (SSL) that the connection used.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RdsDbUser) -> dict:
    out: dict = {}
    if "user" in value:
        out["user"] = value["user"]
    if "application" in value:
        out["application"] = value["application"]
    if "database" in value:
        out["database"] = value["database"]
    if "auth_method" in value:
        out["authMethod"] = value["auth_method"]
    if "ssl" in value:
        out["ssl"] = value["ssl"]
    return out


def deserialize_json(data: dict) -> RdsDbUser:
    out: RdsDbUser = {}  # type: ignore[typeddict-item]
    if data.get("user") is not None:
        out["user"] = data["user"]
    if data.get("application") is not None:
        out["application"] = data["application"]
    if data.get("database") is not None:
        out["database"] = data["database"]
    if data.get("authMethod") is not None:
        out["auth_method"] = data["authMethod"]
    if data.get("ssl") is not None:
        out["ssl"] = data["ssl"]
    return out
