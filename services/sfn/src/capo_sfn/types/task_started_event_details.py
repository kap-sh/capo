"""Generated from Smithy shape ``com.amazonaws.sfn#TaskStartedEventDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sfn.types.name


class TaskStartedEventDetails(TypedDict, closed=True):
    resource_type: "capo_sfn.types.name.Name"
    """<p>The service name of the resource in a task state.</p>"""
    resource: "capo_sfn.types.name.Name"
    """<p>The action of the resource called by a task state.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TaskStartedEventDetails) -> dict:
    out: dict = {}
    out["resourceType"] = value["resource_type"]
    out["resource"] = value["resource"]
    return out


def deserialize_aws_json_1_0(data: dict) -> TaskStartedEventDetails:
    out: TaskStartedEventDetails = {}  # type: ignore[typeddict-item]
    if data.get("resourceType") is not None:
        out["resource_type"] = data["resourceType"]
    else:
        out["resource_type"] = ""
    if data.get("resource") is not None:
        out["resource"] = data["resource"]
    else:
        out["resource"] = ""
    return out
