"""Generated from Smithy shape ``com.amazonaws.machinelearning#RedshiftDatabaseCredentials``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_machine_learning.errors import DeserializationError

if TYPE_CHECKING:
    import capo_machine_learning.types.redshift_database_password
    import capo_machine_learning.types.redshift_database_username


class RedshiftDatabaseCredentials(TypedDict, closed=True):
    username: "capo_machine_learning.types.redshift_database_username.RedshiftDatabaseUsername"
    password: "capo_machine_learning.types.redshift_database_password.RedshiftDatabasePassword"


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RedshiftDatabaseCredentials) -> dict:
    out: dict = {}
    out["Username"] = value["username"]
    out["Password"] = value["password"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RedshiftDatabaseCredentials:
    out: RedshiftDatabaseCredentials = {}  # type: ignore[typeddict-item]
    if data.get("Username") is not None:
        out["username"] = data["Username"]
    else:
        raise DeserializationError("RedshiftDatabaseCredentials.username required")
    if data.get("Password") is not None:
        out["password"] = data["Password"]
    else:
        raise DeserializationError("RedshiftDatabaseCredentials.password required")
    return out


def redact_sensitive(value: RedshiftDatabaseCredentials) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "password" in value:
        out["password"] = "*** Sensitive Data Redacted ***"
    return out
