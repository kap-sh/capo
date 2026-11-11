"""Generated from Smithy shape ``com.amazonaws.lightsail#PendingModifiedRelationalDatabaseValues``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.boolean
    import capo_lightsail.types.sensitive_string
    import capo_lightsail.types.string


class PendingModifiedRelationalDatabaseValues(TypedDict, closed=True):
    master_user_password: NotRequired[
        "capo_lightsail.types.sensitive_string.SensitiveString"
    ]
    """<p>The password for the master user of the database.</p>"""
    engine_version: NotRequired["capo_lightsail.types.string.string"]
    """<p>The database engine version.</p>"""
    backup_retention_enabled: NotRequired["capo_lightsail.types.boolean.boolean"]
    """<p>A Boolean value indicating whether automated backup retention is enabled.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PendingModifiedRelationalDatabaseValues) -> dict:
    out: dict = {}
    if "master_user_password" in value:
        out["masterUserPassword"] = value["master_user_password"]
    if "engine_version" in value:
        out["engineVersion"] = value["engine_version"]
    if "backup_retention_enabled" in value:
        out["backupRetentionEnabled"] = value["backup_retention_enabled"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PendingModifiedRelationalDatabaseValues:
    out: PendingModifiedRelationalDatabaseValues = {}  # type: ignore[typeddict-item]
    if data.get("masterUserPassword") is not None:
        out["master_user_password"] = data["masterUserPassword"]
    if data.get("engineVersion") is not None:
        out["engine_version"] = data["engineVersion"]
    if data.get("backupRetentionEnabled") is not None:
        out["backup_retention_enabled"] = data["backupRetentionEnabled"]
    return out


def redact_sensitive(value: PendingModifiedRelationalDatabaseValues) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "master_user_password" in value:
        out["master_user_password"] = "*** Sensitive Data Redacted ***"
    return out
