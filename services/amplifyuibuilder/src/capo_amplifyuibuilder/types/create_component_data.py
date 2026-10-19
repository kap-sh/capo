"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#CreateComponentData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amplifyuibuilder.types.component_binding_properties
    import capo_amplifyuibuilder.types.component_child_list
    import capo_amplifyuibuilder.types.component_collection_properties
    import capo_amplifyuibuilder.types.component_events
    import capo_amplifyuibuilder.types.component_name
    import capo_amplifyuibuilder.types.component_overrides
    import capo_amplifyuibuilder.types.component_properties
    import capo_amplifyuibuilder.types.component_type
    import capo_amplifyuibuilder.types.component_variants
    import capo_amplifyuibuilder.types.tags


class CreateComponentData(TypedDict, closed=True):
    name: "capo_amplifyuibuilder.types.component_name.ComponentName"
    """<p>The name of the component</p>"""
    source_id: NotRequired["str"]
    """<p>The unique ID of the component in its original source system, such as Figma.</p>"""
    component_type: "capo_amplifyuibuilder.types.component_type.ComponentType"
    """<p>The component type. This can be an Amplify custom UI component or another custom component.</p>"""
    properties: "capo_amplifyuibuilder.types.component_properties.ComponentProperties"
    """<p>Describes the component's properties.</p>"""
    children: NotRequired[
        "capo_amplifyuibuilder.types.component_child_list.ComponentChildList"
    ]
    """<p>A list of child components that are instances of the main component.</p>"""
    variants: "capo_amplifyuibuilder.types.component_variants.ComponentVariants"
    """<p>A list of the unique variants of this component.</p>"""
    overrides: "capo_amplifyuibuilder.types.component_overrides.ComponentOverrides"
    """<p>Describes the component properties that can be overriden to customize an instance of the component.</p>"""
    binding_properties: "capo_amplifyuibuilder.types.component_binding_properties.ComponentBindingProperties"
    """<p>The data binding information for the component's properties.</p>"""
    collection_properties: NotRequired[
        "capo_amplifyuibuilder.types.component_collection_properties.ComponentCollectionProperties"
    ]
    """<p>The data binding configuration for customizing a component's properties. Use this for a collection component.</p>"""
    tags: NotRequired["capo_amplifyuibuilder.types.tags.Tags"]
    """<p>One or more key-value pairs to use when tagging the component data.</p>"""
    events: NotRequired["capo_amplifyuibuilder.types.component_events.ComponentEvents"]
    """<p>The event configuration for the component. Use for the workflow feature in Amplify Studio that allows you to bind events and actions to components.</p>"""
    schema_version: NotRequired["str"]
    """<p>The schema version of the component when it was imported.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateComponentData) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "source_id" in value:
        out["sourceId"] = value["source_id"]
    out["componentType"] = value["component_type"]
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
    import capo_amplifyuibuilder.types.component_variants

    out["variants"] = capo_amplifyuibuilder.types.component_variants.serialize_json(
        value["variants"]
    )
    import capo_amplifyuibuilder.types.component_overrides

    out["overrides"] = capo_amplifyuibuilder.types.component_overrides.serialize_json(
        value["overrides"]
    )
    import capo_amplifyuibuilder.types.component_binding_properties

    out["bindingProperties"] = (
        capo_amplifyuibuilder.types.component_binding_properties.serialize_json(
            value["binding_properties"]
        )
    )
    if "collection_properties" in value:
        import capo_amplifyuibuilder.types.component_collection_properties

        out["collectionProperties"] = (
            capo_amplifyuibuilder.types.component_collection_properties.serialize_json(
                value["collection_properties"]
            )
        )
    if "tags" in value:
        import capo_amplifyuibuilder.types.tags

        out["tags"] = capo_amplifyuibuilder.types.tags.serialize_json(value["tags"])
    if "events" in value:
        import capo_amplifyuibuilder.types.component_events

        out["events"] = capo_amplifyuibuilder.types.component_events.serialize_json(
            value["events"]
        )
    if "schema_version" in value:
        out["schemaVersion"] = value["schema_version"]
    return out


def deserialize_json(data: dict) -> CreateComponentData:
    out: CreateComponentData = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("sourceId") is not None:
        out["source_id"] = data["sourceId"]
    if data.get("componentType") is not None:
        out["component_type"] = data["componentType"]
    else:
        out["component_type"] = ""
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
    if data.get("variants") is not None:
        import capo_amplifyuibuilder.types.component_variants

        out["variants"] = (
            capo_amplifyuibuilder.types.component_variants.deserialize_json(
                data["variants"]
            )
        )
    else:
        out["variants"] = []
    if data.get("overrides") is not None:
        import capo_amplifyuibuilder.types.component_overrides

        out["overrides"] = (
            capo_amplifyuibuilder.types.component_overrides.deserialize_json(
                data["overrides"]
            )
        )
    else:
        out["overrides"] = {}
    if data.get("bindingProperties") is not None:
        import capo_amplifyuibuilder.types.component_binding_properties

        out["binding_properties"] = (
            capo_amplifyuibuilder.types.component_binding_properties.deserialize_json(
                data["bindingProperties"]
            )
        )
    else:
        out["binding_properties"] = {}
    if data.get("collectionProperties") is not None:
        import capo_amplifyuibuilder.types.component_collection_properties

        out["collection_properties"] = (
            capo_amplifyuibuilder.types.component_collection_properties.deserialize_json(
                data["collectionProperties"]
            )
        )
    if data.get("tags") is not None:
        import capo_amplifyuibuilder.types.tags

        out["tags"] = capo_amplifyuibuilder.types.tags.deserialize_json(data["tags"])
    if data.get("events") is not None:
        import capo_amplifyuibuilder.types.component_events

        out["events"] = capo_amplifyuibuilder.types.component_events.deserialize_json(
            data["events"]
        )
    if data.get("schemaVersion") is not None:
        out["schema_version"] = data["schemaVersion"]
    return out
