"""Generated from Smithy shape ``com.amazonaws.swf#ActivityType``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_swf.types.name
    import capo_swf.types.version


class ActivityType(TypedDict, closed=True):
    name: "capo_swf.types.name.Name"
    """<p>The name of this activity.</p> <note> <p>The combination of activity type name and version must be unique within a domain.</p> </note>"""
    version: "capo_swf.types.version.Version"
    """<p>The version of this activity.</p> <note> <p>The combination of activity type name and version must be unique with in a domain.</p> </note>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ActivityType) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["version"] = value["version"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ActivityType:
    out: ActivityType = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("version") is not None:
        out["version"] = data["version"]
    else:
        out["version"] = ""
    return out
