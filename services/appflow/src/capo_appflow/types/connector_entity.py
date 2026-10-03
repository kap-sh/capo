"""Generated from Smithy shape ``com.amazonaws.appflow#ConnectorEntity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_appflow.errors import DeserializationError

if TYPE_CHECKING:
    import capo_appflow.types.boolean
    import capo_appflow.types.label
    import capo_appflow.types.name


class ConnectorEntity(TypedDict, closed=True):
    name: "capo_appflow.types.name.Name"
    """<p> The name of the connector entity. </p>"""
    label: NotRequired["capo_appflow.types.label.Label"]
    """<p> The label applied to the connector entity. </p>"""
    has_nested_entities: "capo_appflow.types.boolean.Boolean"
    """<p> Specifies whether the connector entity is a parent or a category and has more entities nested underneath it. If another call is made with <code>entitiesPath = "the_current_entity_name_with_hasNestedEntities_true"</code>, then it returns the nested entities underneath it. This provides a way to retrieve all supported entities in a recursive fashion. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorEntity) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "label" in value:
        out["label"] = value["label"]
    out["hasNestedEntities"] = value.get("has_nested_entities", False)
    return out


def deserialize_json(data: dict) -> ConnectorEntity:
    out: ConnectorEntity = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ConnectorEntity.name required")
    if data.get("label") is not None:
        out["label"] = data["label"]
    if data.get("hasNestedEntities") is not None:
        out["has_nested_entities"] = data["hasNestedEntities"]
    else:
        out["has_nested_entities"] = False
    return out
