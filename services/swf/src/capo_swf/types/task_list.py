"""Generated from Smithy shape ``com.amazonaws.swf#TaskList``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_swf.types.name


class TaskList(TypedDict, closed=True):
    name: "capo_swf.types.name.Name"
    """<p>The name of the task list.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TaskList) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> TaskList:
    out: TaskList = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    return out
