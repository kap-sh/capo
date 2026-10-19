"""Generated from Smithy shape ``com.amazonaws.devopsagent#UserReference``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.user_type


class UserReference(TypedDict, closed=True):
    user_id: "str"
    """<p>The unique identifier for the user</p>"""
    user_type: "capo_devops_agent.types.user_type.UserType"
    """<p>The type of user</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserReference) -> dict:
    out: dict = {}
    out["userId"] = value["user_id"]
    import capo_devops_agent.types.user_type

    out["userType"] = capo_devops_agent.types.user_type.serialize_json(
        value["user_type"]
    )
    return out


def deserialize_json(data: dict) -> UserReference:
    out: UserReference = {}  # type: ignore[typeddict-item]
    if data.get("userId") is not None:
        out["user_id"] = data["userId"]
    else:
        out["user_id"] = ""
    if data.get("userType") is not None:
        import capo_devops_agent.types.user_type

        out["user_type"] = capo_devops_agent.types.user_type.deserialize_json(
            data["userType"]
        )
    else:
        import typing

        out["user_type"] = typing.cast("capo_devops_agent.types.user_type.UserType", "")
    return out
