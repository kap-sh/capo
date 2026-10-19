"""Generated from Smithy shape ``com.amazonaws.cloud9#UpdateEnvironmentMembershipRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloud9.types.environment_id
    import capo_cloud9.types.member_permissions
    import capo_cloud9.types.user_arn


class UpdateEnvironmentMembershipRequest(TypedDict, closed=True):
    environment_id: "capo_cloud9.types.environment_id.EnvironmentId"
    """<p>The ID of the environment for the environment member whose settings you want to change.</p>"""
    user_arn: "capo_cloud9.types.user_arn.UserArn"
    """<p>The Amazon Resource Name (ARN) of the environment member whose settings you want to change.</p>"""
    permissions: "capo_cloud9.types.member_permissions.MemberPermissions"
    """<p>The replacement type of environment member permissions you want to associate with this environment member. Available values include:</p> <ul> <li> <p> <code>read-only</code>: Has read-only access to the environment.</p> </li> <li> <p> <code>read-write</code>: Has read-write access to the environment.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateEnvironmentMembershipRequest) -> dict:
    out: dict = {}
    out["environmentId"] = value["environment_id"]
    out["userArn"] = value["user_arn"]
    import capo_cloud9.types.member_permissions

    out["permissions"] = capo_cloud9.types.member_permissions.serialize_aws_json_1_1(
        value["permissions"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateEnvironmentMembershipRequest:
    out: UpdateEnvironmentMembershipRequest = {}  # type: ignore[typeddict-item]
    if data.get("environmentId") is not None:
        out["environment_id"] = data["environmentId"]
    else:
        out["environment_id"] = ""
    if data.get("userArn") is not None:
        out["user_arn"] = data["userArn"]
    else:
        out["user_arn"] = ""
    if data.get("permissions") is not None:
        import capo_cloud9.types.member_permissions

        out["permissions"] = (
            capo_cloud9.types.member_permissions.deserialize_aws_json_1_1(
                data["permissions"]
            )
        )
    else:
        import typing

        out["permissions"] = typing.cast(
            "capo_cloud9.types.member_permissions.MemberPermissions", ""
        )
    return out
