"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#TestAction``."""

from typing_extensions import NotRequired, TypedDict


class TestAction(TypedDict, closed=True):
    action_id: "str"
    """<p>The identifier of the fault action.</p>"""
    description: NotRequired["str"]
    """<p>A description of the fault action.</p>"""
    resource_type: "str"
    """<p>The resource type that the action targets.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TestAction) -> dict:
    out: dict = {}
    out["actionId"] = value["action_id"]
    if "description" in value:
        out["description"] = value["description"]
    out["resourceType"] = value["resource_type"]
    return out


def deserialize_json(data: dict) -> TestAction:
    out: TestAction = {}  # type: ignore[typeddict-item]
    if data.get("actionId") is not None:
        out["action_id"] = data["actionId"]
    else:
        out["action_id"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("resourceType") is not None:
        out["resource_type"] = data["resourceType"]
    else:
        out["resource_type"] = ""
    return out
