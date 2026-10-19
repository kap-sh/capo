"""Generated from Smithy shape ``com.amazonaws.workspaces#RootStorage``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.non_empty_string


class RootStorage(TypedDict, closed=True):
    capacity: "capo_workspaces.types.non_empty_string.NonEmptyString"
    """<p>The size of the root volume.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RootStorage) -> dict:
    out: dict = {}
    out["Capacity"] = value["capacity"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RootStorage:
    out: RootStorage = {}  # type: ignore[typeddict-item]
    if data.get("Capacity") is not None:
        out["capacity"] = data["Capacity"]
    else:
        out["capacity"] = ""
    return out
