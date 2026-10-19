"""Generated from Smithy shape ``com.amazonaws.cloud9#EnvironmentMember``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloud9.types.environment_id
    import capo_cloud9.types.permissions
    import capo_cloud9.types.string
    import capo_cloud9.types.timestamp
    import capo_cloud9.types.user_arn


class EnvironmentMember(TypedDict, closed=True):
    permissions: "capo_cloud9.types.permissions.Permissions"
    """<p>The type of environment member permissions associated with this environment member. Available values include:</p> <ul> <li> <p> <code>owner</code>: Owns the environment.</p> </li> <li> <p> <code>read-only</code>: Has read-only access to the environment.</p> </li> <li> <p> <code>read-write</code>: Has read-write access to the environment.</p> </li> </ul>"""
    user_id: "capo_cloud9.types.string.String"
    """<p>The user ID in Identity and Access Management (IAM) of the environment member.</p>"""
    user_arn: "capo_cloud9.types.user_arn.UserArn"
    """<p>The Amazon Resource Name (ARN) of the environment member.</p>"""
    environment_id: "capo_cloud9.types.environment_id.EnvironmentId"
    """<p>The ID of the environment for the environment member.</p>"""
    last_access: NotRequired["capo_cloud9.types.timestamp.Timestamp"]
    """<p>The time, expressed in epoch time format, when the environment member last opened the environment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnvironmentMember) -> dict:
    out: dict = {}
    import capo_cloud9.types.permissions

    out["permissions"] = capo_cloud9.types.permissions.serialize_aws_json_1_1(
        value["permissions"]
    )
    out["userId"] = value["user_id"]
    out["userArn"] = value["user_arn"]
    out["environmentId"] = value["environment_id"]
    if "last_access" in value:
        import capo_cloud9.types.timestamp

        out["lastAccess"] = capo_cloud9.types.timestamp.serialize_aws_json_1_1(
            value["last_access"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EnvironmentMember:
    out: EnvironmentMember = {}  # type: ignore[typeddict-item]
    if data.get("permissions") is not None:
        import capo_cloud9.types.permissions

        out["permissions"] = capo_cloud9.types.permissions.deserialize_aws_json_1_1(
            data["permissions"]
        )
    else:
        import typing

        out["permissions"] = typing.cast(
            "capo_cloud9.types.permissions.Permissions", ""
        )
    if data.get("userId") is not None:
        out["user_id"] = data["userId"]
    else:
        out["user_id"] = ""
    if data.get("userArn") is not None:
        out["user_arn"] = data["userArn"]
    else:
        out["user_arn"] = ""
    if data.get("environmentId") is not None:
        out["environment_id"] = data["environmentId"]
    else:
        out["environment_id"] = ""
    if data.get("lastAccess") is not None:
        import capo_cloud9.types.timestamp

        out["last_access"] = capo_cloud9.types.timestamp.deserialize_aws_json_1_1(
            data["lastAccess"]
        )
    return out
