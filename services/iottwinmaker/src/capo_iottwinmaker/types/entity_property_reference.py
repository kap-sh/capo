"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#EntityPropertyReference``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iottwinmaker.types.component_path
    import capo_iottwinmaker.types.entity_id
    import capo_iottwinmaker.types.external_id_property
    import capo_iottwinmaker.types.name


class EntityPropertyReference(TypedDict, closed=True):
    component_name: NotRequired["capo_iottwinmaker.types.name.Name"]
    """<p>The name of the component.</p>"""
    component_path: NotRequired["capo_iottwinmaker.types.component_path.ComponentPath"]
    """<p>This string specifies the path to the composite component, starting from the top-level component.</p>"""
    external_id_property: NotRequired[
        "capo_iottwinmaker.types.external_id_property.ExternalIdProperty"
    ]
    """<p>A mapping of external IDs to property names. External IDs uniquely identify properties from external data stores.</p>"""
    entity_id: NotRequired["capo_iottwinmaker.types.entity_id.EntityId"]
    """<p>The ID of the entity.</p>"""
    property_name: "capo_iottwinmaker.types.name.Name"
    """<p>The name of the property.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EntityPropertyReference) -> dict:
    out: dict = {}
    if "component_name" in value:
        out["componentName"] = value["component_name"]
    if "component_path" in value:
        out["componentPath"] = value["component_path"]
    if "external_id_property" in value:
        import capo_iottwinmaker.types.external_id_property

        out["externalIdProperty"] = (
            capo_iottwinmaker.types.external_id_property.serialize_json(
                value["external_id_property"]
            )
        )
    if "entity_id" in value:
        out["entityId"] = value["entity_id"]
    out["propertyName"] = value["property_name"]
    return out


def deserialize_json(data: dict) -> EntityPropertyReference:
    out: EntityPropertyReference = {}  # type: ignore[typeddict-item]
    if data.get("componentName") is not None:
        out["component_name"] = data["componentName"]
    if data.get("componentPath") is not None:
        out["component_path"] = data["componentPath"]
    if data.get("externalIdProperty") is not None:
        import capo_iottwinmaker.types.external_id_property

        out["external_id_property"] = (
            capo_iottwinmaker.types.external_id_property.deserialize_json(
                data["externalIdProperty"]
            )
        )
    if data.get("entityId") is not None:
        out["entity_id"] = data["entityId"]
    if data.get("propertyName") is not None:
        out["property_name"] = data["propertyName"]
    else:
        out["property_name"] = ""
    return out
