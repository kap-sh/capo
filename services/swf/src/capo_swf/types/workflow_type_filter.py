"""Generated from Smithy shape ``com.amazonaws.swf#WorkflowTypeFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_swf.types.name
    import capo_swf.types.version_optional


class WorkflowTypeFilter(TypedDict, closed=True):
    name: "capo_swf.types.name.Name"
    """<p> Name of the workflow type.</p>"""
    version: NotRequired["capo_swf.types.version_optional.VersionOptional"]
    """<p>Version of the workflow type.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WorkflowTypeFilter) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "version" in value:
        out["version"] = value["version"]
    return out


def deserialize_aws_json_1_0(data: dict) -> WorkflowTypeFilter:
    out: WorkflowTypeFilter = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("version") is not None:
        out["version"] = data["version"]
    return out
