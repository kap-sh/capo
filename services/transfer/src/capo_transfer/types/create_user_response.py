"""Generated from Smithy shape ``com.amazonaws.transfer#CreateUserResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_transfer.types.server_id
    import capo_transfer.types.user_name


class CreateUserResponse(TypedDict, closed=True):
    server_id: "capo_transfer.types.server_id.ServerId"
    """<p>The identifier of the server that the user is attached to.</p>"""
    user_name: "capo_transfer.types.user_name.UserName"
    """<p>A unique string that identifies a Transfer Family user.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateUserResponse) -> dict:
    out: dict = {}
    out["ServerId"] = value["server_id"]
    out["UserName"] = value["user_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateUserResponse:
    out: CreateUserResponse = {}  # type: ignore[typeddict-item]
    if data.get("ServerId") is not None:
        out["server_id"] = data["ServerId"]
    else:
        out["server_id"] = ""
    if data.get("UserName") is not None:
        out["user_name"] = data["UserName"]
    else:
        out["user_name"] = ""
    return out
