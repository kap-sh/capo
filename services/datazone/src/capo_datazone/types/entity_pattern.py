"""Generated from Smithy shape ``com.amazonaws.datazone#EntityPattern``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.filter_clause
    import capo_datazone.types.graph_entity_type


class EntityPattern(TypedDict, closed=True):
    entity_type: "capo_datazone.types.graph_entity_type.GraphEntityType"
    """<p>The type of entity to be matched during the graph query.</p>"""
    identifier: "str"
    """<p>The identifier of the root entity to start traversal from during the graph query.</p>"""
    filters: NotRequired["capo_datazone.types.filter_clause.FilterClause"]


# --- restJson1 ser/de ---
def serialize_json(value: EntityPattern) -> dict:
    out: dict = {}
    import capo_datazone.types.graph_entity_type

    out["entityType"] = capo_datazone.types.graph_entity_type.serialize_json(
        value["entity_type"]
    )
    out["identifier"] = value["identifier"]
    if "filters" in value:
        import capo_datazone.types.filter_clause

        out["filters"] = capo_datazone.types.filter_clause.serialize_json(
            value["filters"]
        )
    return out


def deserialize_json(data: dict) -> EntityPattern:
    out: EntityPattern = {}  # type: ignore[typeddict-item]
    if data.get("entityType") is not None:
        import capo_datazone.types.graph_entity_type

        out["entity_type"] = capo_datazone.types.graph_entity_type.deserialize_json(
            data["entityType"]
        )
    else:
        import typing

        out["entity_type"] = typing.cast(
            "capo_datazone.types.graph_entity_type.GraphEntityType", ""
        )
    if data.get("identifier") is not None:
        out["identifier"] = data["identifier"]
    else:
        out["identifier"] = ""
    if data.get("filters") is not None:
        import capo_datazone.types.filter_clause

        out["filters"] = capo_datazone.types.filter_clause.deserialize_json(
            data["filters"]
        )
    return out
