"""Generated from Smithy shape ``com.amazonaws.cloud9#DeleteEnvironmentMembershipRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloud9.types.environment_id
    import capo_cloud9.types.user_arn


class DeleteEnvironmentMembershipRequest(TypedDict, closed=True):
    environment_id: "capo_cloud9.types.environment_id.EnvironmentId"
    """<p>The ID of the environment to delete the environment member from.</p>"""
    user_arn: "capo_cloud9.types.user_arn.UserArn"
    """<p>The Amazon Resource Name (ARN) of the environment member to delete from the environment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteEnvironmentMembershipRequest) -> dict:
    out: dict = {}
    out["environmentId"] = value["environment_id"]
    out["userArn"] = value["user_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteEnvironmentMembershipRequest:
    out: DeleteEnvironmentMembershipRequest = {}  # type: ignore[typeddict-item]
    if data.get("environmentId") is not None:
        out["environment_id"] = data["environmentId"]
    else:
        out["environment_id"] = ""
    if data.get("userArn") is not None:
        out["user_arn"] = data["userArn"]
    else:
        out["user_arn"] = ""
    return out
