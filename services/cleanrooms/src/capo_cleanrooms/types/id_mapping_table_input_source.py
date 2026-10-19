"""Generated from Smithy shape ``com.amazonaws.cleanrooms#IdMappingTableInputSource``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.id_namespace_type


class IdMappingTableInputSource(TypedDict, closed=True):
    id_namespace_association_id: "str"
    """<p>The unique identifier of the ID namespace association.</p>"""
    type: "capo_cleanrooms.types.id_namespace_type.IdNamespaceType"
    """<p>The type of the input source of the ID mapping table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IdMappingTableInputSource) -> dict:
    out: dict = {}
    out["idNamespaceAssociationId"] = value["id_namespace_association_id"]
    import capo_cleanrooms.types.id_namespace_type

    out["type"] = capo_cleanrooms.types.id_namespace_type.serialize_json(value["type"])
    return out


def deserialize_json(data: dict) -> IdMappingTableInputSource:
    out: IdMappingTableInputSource = {}  # type: ignore[typeddict-item]
    if data.get("idNamespaceAssociationId") is not None:
        out["id_namespace_association_id"] = data["idNamespaceAssociationId"]
    else:
        out["id_namespace_association_id"] = ""
    if data.get("type") is not None:
        import capo_cleanrooms.types.id_namespace_type

        out["type"] = capo_cleanrooms.types.id_namespace_type.deserialize_json(
            data["type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_cleanrooms.types.id_namespace_type.IdNamespaceType", ""
        )
    return out
