"""Generated from Smithy shape ``com.amazonaws.memorydb#DeleteUserRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.user_name


class DeleteUserRequest(TypedDict, closed=True):
    user_name: "capo_memorydb.types.user_name.UserName"
    """<p>The name of the user to delete</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteUserRequest) -> dict:
    out: dict = {}
    out["UserName"] = value["user_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteUserRequest:
    out: DeleteUserRequest = {}  # type: ignore[typeddict-item]
    if data.get("UserName") is not None:
        out["user_name"] = data["UserName"]
    else:
        out["user_name"] = ""
    return out
