"""Generated from Smithy shape ``com.amazonaws.cleanrooms#IdNamespaceAssociationInputReferencePropertiesSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.id_namespace_type


class IdNamespaceAssociationInputReferencePropertiesSummary(TypedDict, closed=True):
    id_namespace_type: "capo_cleanrooms.types.id_namespace_type.IdNamespaceType"
    """<p>The ID namespace type for this ID namespace association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: IdNamespaceAssociationInputReferencePropertiesSummary,
) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.id_namespace_type

    out["idNamespaceType"] = capo_cleanrooms.types.id_namespace_type.serialize_json(
        value["id_namespace_type"]
    )
    return out


def deserialize_json(
    data: dict,
) -> IdNamespaceAssociationInputReferencePropertiesSummary:
    out: IdNamespaceAssociationInputReferencePropertiesSummary = {}  # type: ignore[typeddict-item]
    if data.get("idNamespaceType") is not None:
        import capo_cleanrooms.types.id_namespace_type

        out["id_namespace_type"] = (
            capo_cleanrooms.types.id_namespace_type.deserialize_json(
                data["idNamespaceType"]
            )
        )
    else:
        import typing

        out["id_namespace_type"] = typing.cast(
            "capo_cleanrooms.types.id_namespace_type.IdNamespaceType", ""
        )
    return out
