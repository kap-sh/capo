"""Generated from Smithy shape ``com.amazonaws.cleanrooms#IdNamespaceAssociationInputReferenceProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.id_mapping_workflows_supported
    import capo_cleanrooms.types.id_namespace_type


class IdNamespaceAssociationInputReferenceProperties(TypedDict, closed=True):
    id_namespace_type: "capo_cleanrooms.types.id_namespace_type.IdNamespaceType"
    """<p>The ID namespace type for this ID namespace association.</p>"""
    id_mapping_workflows_supported: "capo_cleanrooms.types.id_mapping_workflows_supported.IdMappingWorkflowsSupported"
    """<p>Defines how ID mapping workflows are supported for this ID namespace association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IdNamespaceAssociationInputReferenceProperties) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.id_namespace_type

    out["idNamespaceType"] = capo_cleanrooms.types.id_namespace_type.serialize_json(
        value["id_namespace_type"]
    )
    import capo_cleanrooms.types.id_mapping_workflows_supported

    out["idMappingWorkflowsSupported"] = (
        capo_cleanrooms.types.id_mapping_workflows_supported.serialize_json(
            value["id_mapping_workflows_supported"]
        )
    )
    return out


def deserialize_json(data: dict) -> IdNamespaceAssociationInputReferenceProperties:
    out: IdNamespaceAssociationInputReferenceProperties = {}  # type: ignore[typeddict-item]
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
    if data.get("idMappingWorkflowsSupported") is not None:
        import capo_cleanrooms.types.id_mapping_workflows_supported

        out["id_mapping_workflows_supported"] = (
            capo_cleanrooms.types.id_mapping_workflows_supported.deserialize_json(
                data["idMappingWorkflowsSupported"]
            )
        )
    else:
        out["id_mapping_workflows_supported"] = []
    return out
