"""Generated from Smithy shape ``com.amazonaws.finspace#CreateKxUserRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_finspace.types.client_token
    import capo_finspace.types.id_type
    import capo_finspace.types.kx_user_name_string
    import capo_finspace.types.role_arn
    import capo_finspace.types.tag_map


class CreateKxUserRequest(TypedDict, closed=True):
    environment_id: "capo_finspace.types.id_type.IdType"
    """<p>A unique identifier for the kdb environment where you want to create a user.</p>"""
    user_name: "capo_finspace.types.kx_user_name_string.KxUserNameString"
    """<p>A unique identifier for the user.</p>"""
    iam_role: "capo_finspace.types.role_arn.RoleArn"
    """<p>The IAM role ARN that will be associated with the user.</p>"""
    tags: NotRequired["capo_finspace.types.tag_map.TagMap"]
    """<p>A list of key-value pairs to label the user. You can add up to 50 tags to a user.</p>"""
    client_token: NotRequired["capo_finspace.types.client_token.ClientToken"]
    """<p>A token that ensures idempotency. This token expires in 10 minutes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateKxUserRequest) -> dict:
    out: dict = {}
    out["userName"] = value["user_name"]
    out["iamRole"] = value["iam_role"]
    if "tags" in value:
        import capo_finspace.types.tag_map

        out["tags"] = capo_finspace.types.tag_map.serialize_json(value["tags"])
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateKxUserRequest:
    out: CreateKxUserRequest = {}  # type: ignore[typeddict-item]
    if data.get("userName") is not None:
        out["user_name"] = data["userName"]
    else:
        out["user_name"] = ""
    if data.get("iamRole") is not None:
        out["iam_role"] = data["iamRole"]
    else:
        out["iam_role"] = ""
    if data.get("tags") is not None:
        import capo_finspace.types.tag_map

        out["tags"] = capo_finspace.types.tag_map.deserialize_json(data["tags"])
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
