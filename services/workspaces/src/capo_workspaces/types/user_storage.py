"""Generated from Smithy shape ``com.amazonaws.workspaces#UserStorage``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.non_empty_string


class UserStorage(TypedDict, closed=True):
    capacity: "capo_workspaces.types.non_empty_string.NonEmptyString"
    """<p>The size of the user volume.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserStorage) -> dict:
    out: dict = {}
    out["Capacity"] = value["capacity"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UserStorage:
    out: UserStorage = {}  # type: ignore[typeddict-item]
    if data.get("Capacity") is not None:
        out["capacity"] = data["Capacity"]
    else:
        out["capacity"] = ""
    return out
