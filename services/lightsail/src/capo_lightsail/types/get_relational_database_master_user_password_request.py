"""Generated from Smithy shape ``com.amazonaws.lightsail#GetRelationalDatabaseMasterUserPasswordRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.relational_database_password_version
    import capo_lightsail.types.resource_name


class GetRelationalDatabaseMasterUserPasswordRequest(TypedDict, closed=True):
    relational_database_name: "capo_lightsail.types.resource_name.ResourceName"
    """<p>The name of your database for which to get the master user password.</p>"""
    password_version: NotRequired[
        "capo_lightsail.types.relational_database_password_version.RelationalDatabasePasswordVersion"
    ]
    """<p>The password version to return.</p> <p>Specifying <code>CURRENT</code> or <code>PREVIOUS</code> returns the current or previous passwords respectively. Specifying <code>PENDING</code> returns the newest version of the password that will rotate to <code>CURRENT</code>. After the <code>PENDING</code> password rotates to <code>CURRENT</code>, the <code>PENDING</code> password is no longer available.</p> <p>Default: <code>CURRENT</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: GetRelationalDatabaseMasterUserPasswordRequest,
) -> dict:
    out: dict = {}
    out["relationalDatabaseName"] = value["relational_database_name"]
    if "password_version" in value:
        import capo_lightsail.types.relational_database_password_version

        out["passwordVersion"] = (
            capo_lightsail.types.relational_database_password_version.serialize_aws_json_1_1(
                value["password_version"]
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> GetRelationalDatabaseMasterUserPasswordRequest:
    out: GetRelationalDatabaseMasterUserPasswordRequest = {}  # type: ignore[typeddict-item]
    if data.get("relationalDatabaseName") is not None:
        out["relational_database_name"] = data["relationalDatabaseName"]
    else:
        out["relational_database_name"] = ""
    if data.get("passwordVersion") is not None:
        import capo_lightsail.types.relational_database_password_version

        out["password_version"] = (
            capo_lightsail.types.relational_database_password_version.deserialize_aws_json_1_1(
                data["passwordVersion"]
            )
        )
    return out
