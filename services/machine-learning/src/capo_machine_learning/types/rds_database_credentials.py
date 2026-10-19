"""Generated from Smithy shape ``com.amazonaws.machinelearning#RDSDatabaseCredentials``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_machine_learning.types.rds_database_password
    import capo_machine_learning.types.rds_database_username


class RDSDatabaseCredentials(TypedDict, closed=True):
    username: "capo_machine_learning.types.rds_database_username.RDSDatabaseUsername"
    password: "capo_machine_learning.types.rds_database_password.RDSDatabasePassword"


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RDSDatabaseCredentials) -> dict:
    out: dict = {}
    out["Username"] = value["username"]
    out["Password"] = value["password"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RDSDatabaseCredentials:
    out: RDSDatabaseCredentials = {}  # type: ignore[typeddict-item]
    if data.get("Username") is not None:
        out["username"] = data["Username"]
    else:
        out["username"] = ""
    if data.get("Password") is not None:
        out["password"] = data["Password"]
    else:
        out["password"] = ""
    return out


def redact_sensitive(value: RDSDatabaseCredentials) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "password" in value:
        out["password"] = "*** Sensitive Data Redacted ***"
    return out
