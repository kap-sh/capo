"""Generated from Smithy shape ``com.amazonaws.datazone#RelationPattern``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.relation_direction
    import capo_datazone.types.relation_type


class RelationPattern(TypedDict, closed=True):
    relation_type: "capo_datazone.types.relation_type.RelationType"
    """<p>The type of relation to query.</p>"""
    relation_direction: "capo_datazone.types.relation_direction.RelationDirection"
    """<p>The direction to query.</p>"""
    max_path_length: NotRequired["int"]
    """<p>The number of hops to query.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RelationPattern) -> dict:
    out: dict = {}
    import capo_datazone.types.relation_type

    out["relationType"] = capo_datazone.types.relation_type.serialize_json(
        value["relation_type"]
    )
    import capo_datazone.types.relation_direction

    out["relationDirection"] = capo_datazone.types.relation_direction.serialize_json(
        value["relation_direction"]
    )
    if "max_path_length" in value:
        out["maxPathLength"] = value["max_path_length"]
    return out


def deserialize_json(data: dict) -> RelationPattern:
    out: RelationPattern = {}  # type: ignore[typeddict-item]
    if data.get("relationType") is not None:
        import capo_datazone.types.relation_type

        out["relation_type"] = capo_datazone.types.relation_type.deserialize_json(
            data["relationType"]
        )
    else:
        import typing

        out["relation_type"] = typing.cast(
            "capo_datazone.types.relation_type.RelationType", ""
        )
    if data.get("relationDirection") is not None:
        import capo_datazone.types.relation_direction

        out["relation_direction"] = (
            capo_datazone.types.relation_direction.deserialize_json(
                data["relationDirection"]
            )
        )
    else:
        import typing

        out["relation_direction"] = typing.cast(
            "capo_datazone.types.relation_direction.RelationDirection", ""
        )
    if data.get("maxPathLength") is not None:
        out["max_path_length"] = data["maxPathLength"]
    return out
