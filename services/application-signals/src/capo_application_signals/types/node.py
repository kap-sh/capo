"""Generated from Smithy shape ``com.amazonaws.applicationsignals#Node``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_application_signals.types.attributes


class Node(TypedDict, closed=True):
    key_attributes: "capo_application_signals.types.attributes.Attributes"
    """<p>The key attributes that identify this node, including Type, Name, and Environment information.</p>"""
    name: "str"
    """<p>The name of the entity represented by this node.</p>"""
    node_id: "str"
    """<p>A unique identifier for this node within the dependency graph.</p>"""
    operation: NotRequired["str"]
    """<p>The operation associated with this node, if applicable.</p>"""
    type: NotRequired["str"]
    """<p>The type of entity represented by this node, such as <code>Service</code> or <code>Resource</code>.</p>"""
    duration: NotRequired["float"]
    """<p>The duration or processing time associated with this node, if applicable.</p>"""
    status: NotRequired["str"]
    """<p>The status of the entity represented by this node.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Node) -> dict:
    out: dict = {}
    import capo_application_signals.types.attributes

    out["KeyAttributes"] = capo_application_signals.types.attributes.serialize_json(
        value["key_attributes"]
    )
    out["Name"] = value["name"]
    out["NodeId"] = value["node_id"]
    if "operation" in value:
        out["Operation"] = value["operation"]
    if "type" in value:
        out["Type"] = value["type"]
    if "duration" in value:
        out["Duration"] = (
            "NaN"
            if value["duration"] != value["duration"]
            else "Infinity"
            if value["duration"] == float("inf")
            else "-Infinity"
            if value["duration"] == float("-inf")
            else value["duration"]
        )
    if "status" in value:
        out["Status"] = value["status"]
    return out


def deserialize_json(data: dict) -> Node:
    out: Node = {}  # type: ignore[typeddict-item]
    if data.get("KeyAttributes") is not None:
        import capo_application_signals.types.attributes

        out["key_attributes"] = (
            capo_application_signals.types.attributes.deserialize_json(
                data["KeyAttributes"]
            )
        )
    else:
        out["key_attributes"] = {}
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("NodeId") is not None:
        out["node_id"] = data["NodeId"]
    else:
        out["node_id"] = ""
    if data.get("Operation") is not None:
        out["operation"] = data["Operation"]
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    if data.get("Duration") is not None:
        out["duration"] = float(data["Duration"])
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    return out
