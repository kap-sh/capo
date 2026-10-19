"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#ComponentChild``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amplifyuibuilder.types.component_child_list
    import capo_amplifyuibuilder.types.component_events
    import capo_amplifyuibuilder.types.component_properties


class ComponentChild(TypedDict, closed=True):
    component_type: "str"
    """<p>The type of the child component. </p>"""
    name: "str"
    """<p>The name of the child component.</p>"""
    properties: "capo_amplifyuibuilder.types.component_properties.ComponentProperties"
    """<p>Describes the properties of the child component. You can't specify <code>tags</code> as a valid property for <code>properties</code>.</p>"""
    children: NotRequired[
        "capo_amplifyuibuilder.types.component_child_list.ComponentChildList"
    ]
    """<p>The list of <code>ComponentChild</code> instances for this component.</p>"""
    events: NotRequired["capo_amplifyuibuilder.types.component_events.ComponentEvents"]
    """<p>Describes the events that can be raised on the child component. Use for the workflow feature in Amplify Studio that allows you to bind events and actions to components.</p>"""
    source_id: NotRequired["str"]
    """<p>The unique ID of the child component in its original source system, such as Figma.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComponentChild) -> dict:
    out: dict = {}
    out["componentType"] = value["component_type"]
    out["name"] = value["name"]
    import capo_amplifyuibuilder.types.component_properties

    out["properties"] = capo_amplifyuibuilder.types.component_properties.serialize_json(
        value["properties"]
    )
    if "children" in value:
        import capo_amplifyuibuilder.types.component_child_list

        out["children"] = (
            capo_amplifyuibuilder.types.component_child_list.serialize_json(
                value["children"]
            )
        )
    if "events" in value:
        import capo_amplifyuibuilder.types.component_events

        out["events"] = capo_amplifyuibuilder.types.component_events.serialize_json(
            value["events"]
        )
    if "source_id" in value:
        out["sourceId"] = value["source_id"]
    return out


def deserialize_json(data: dict) -> ComponentChild:
    out: ComponentChild = {}  # type: ignore[typeddict-item]
    if data.get("componentType") is not None:
        out["component_type"] = data["componentType"]
    else:
        out["component_type"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("properties") is not None:
        import capo_amplifyuibuilder.types.component_properties

        out["properties"] = (
            capo_amplifyuibuilder.types.component_properties.deserialize_json(
                data["properties"]
            )
        )
    else:
        out["properties"] = {}
    if data.get("children") is not None:
        import capo_amplifyuibuilder.types.component_child_list

        out["children"] = (
            capo_amplifyuibuilder.types.component_child_list.deserialize_json(
                data["children"]
            )
        )
    if data.get("events") is not None:
        import capo_amplifyuibuilder.types.component_events

        out["events"] = capo_amplifyuibuilder.types.component_events.deserialize_json(
            data["events"]
        )
    if data.get("sourceId") is not None:
        out["source_id"] = data["sourceId"]
    return out
