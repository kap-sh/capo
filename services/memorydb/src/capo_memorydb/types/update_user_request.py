"""Generated from Smithy shape ``com.amazonaws.memorydb#UpdateUserRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.access_string
    import capo_memorydb.types.authentication_mode
    import capo_memorydb.types.user_name


class UpdateUserRequest(TypedDict, closed=True):
    user_name: "capo_memorydb.types.user_name.UserName"
    """<p>The name of the user</p>"""
    authentication_mode: NotRequired[
        "capo_memorydb.types.authentication_mode.AuthenticationMode"
    ]
    """<p>Denotes the user's authentication properties, such as whether it requires a password to authenticate.</p>"""
    access_string: NotRequired["capo_memorydb.types.access_string.AccessString"]
    """<p>Access permissions string used for this user.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateUserRequest) -> dict:
    out: dict = {}
    out["UserName"] = value["user_name"]
    if "authentication_mode" in value:
        import capo_memorydb.types.authentication_mode

        out["AuthenticationMode"] = (
            capo_memorydb.types.authentication_mode.serialize_aws_json_1_1(
                value["authentication_mode"]
            )
        )
    if "access_string" in value:
        out["AccessString"] = value["access_string"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateUserRequest:
    out: UpdateUserRequest = {}  # type: ignore[typeddict-item]
    if data.get("UserName") is not None:
        out["user_name"] = data["UserName"]
    else:
        out["user_name"] = ""
    if data.get("AuthenticationMode") is not None:
        import capo_memorydb.types.authentication_mode

        out["authentication_mode"] = (
            capo_memorydb.types.authentication_mode.deserialize_aws_json_1_1(
                data["AuthenticationMode"]
            )
        )
    if data.get("AccessString") is not None:
        out["access_string"] = data["AccessString"]
    return out
