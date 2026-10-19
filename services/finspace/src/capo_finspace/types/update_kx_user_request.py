"""Generated from Smithy shape ``com.amazonaws.finspace#UpdateKxUserRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_finspace.types.client_token
    import capo_finspace.types.id_type
    import capo_finspace.types.kx_user_name_string
    import capo_finspace.types.role_arn


class UpdateKxUserRequest(TypedDict, closed=True):
    environment_id: "capo_finspace.types.id_type.IdType"
    """<p>A unique identifier for the kdb environment.</p>"""
    user_name: "capo_finspace.types.kx_user_name_string.KxUserNameString"
    """<p>A unique identifier for the user.</p>"""
    iam_role: "capo_finspace.types.role_arn.RoleArn"
    """<p>The IAM role ARN that is associated with the user.</p>"""
    client_token: NotRequired["capo_finspace.types.client_token.ClientToken"]
    """<p>A token that ensures idempotency. This token expires in 10 minutes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateKxUserRequest) -> dict:
    out: dict = {}
    out["iamRole"] = value["iam_role"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdateKxUserRequest:
    out: UpdateKxUserRequest = {}  # type: ignore[typeddict-item]
    if data.get("iamRole") is not None:
        out["iam_role"] = data["iamRole"]
    else:
        out["iam_role"] = ""
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
