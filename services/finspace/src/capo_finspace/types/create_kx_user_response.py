"""Generated from Smithy shape ``com.amazonaws.finspace#CreateKxUserResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_finspace.types.id_type
    import capo_finspace.types.kx_user_arn
    import capo_finspace.types.kx_user_name_string
    import capo_finspace.types.role_arn


class CreateKxUserResponse(TypedDict, closed=True):
    user_name: NotRequired["capo_finspace.types.kx_user_name_string.KxUserNameString"]
    """<p>A unique identifier for the user.</p>"""
    user_arn: NotRequired["capo_finspace.types.kx_user_arn.KxUserArn"]
    """<p> The Amazon Resource Name (ARN) that identifies the user. For more information about ARNs and how to use ARNs in policies, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html">IAM Identifiers</a> in the <i>IAM User Guide</i>. </p>"""
    environment_id: NotRequired["capo_finspace.types.id_type.IdType"]
    """<p>A unique identifier for the kdb environment.</p>"""
    iam_role: NotRequired["capo_finspace.types.role_arn.RoleArn"]
    """<p>The IAM role ARN that will be associated with the user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateKxUserResponse) -> dict:
    out: dict = {}
    if "user_name" in value:
        out["userName"] = value["user_name"]
    if "user_arn" in value:
        out["userArn"] = value["user_arn"]
    if "environment_id" in value:
        out["environmentId"] = value["environment_id"]
    if "iam_role" in value:
        out["iamRole"] = value["iam_role"]
    return out


def deserialize_json(data: dict) -> CreateKxUserResponse:
    out: CreateKxUserResponse = {}  # type: ignore[typeddict-item]
    if data.get("userName") is not None:
        out["user_name"] = data["userName"]
    if data.get("userArn") is not None:
        out["user_arn"] = data["userArn"]
    if data.get("environmentId") is not None:
        out["environment_id"] = data["environmentId"]
    if data.get("iamRole") is not None:
        out["iam_role"] = data["iamRole"]
    return out
