"""Generated from Smithy shape ``com.amazonaws.entityresolution#IdNamespaceIdMappingWorkflowMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_entityresolution.types.id_mapping_type


class IdNamespaceIdMappingWorkflowMetadata(TypedDict, closed=True):
    id_mapping_type: "capo_entityresolution.types.id_mapping_type.IdMappingType"
    """<p>The type of ID mapping.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IdNamespaceIdMappingWorkflowMetadata) -> dict:
    out: dict = {}
    import capo_entityresolution.types.id_mapping_type

    out["idMappingType"] = capo_entityresolution.types.id_mapping_type.serialize_json(
        value["id_mapping_type"]
    )
    return out


def deserialize_json(data: dict) -> IdNamespaceIdMappingWorkflowMetadata:
    out: IdNamespaceIdMappingWorkflowMetadata = {}  # type: ignore[typeddict-item]
    if data.get("idMappingType") is not None:
        import capo_entityresolution.types.id_mapping_type

        out["id_mapping_type"] = (
            capo_entityresolution.types.id_mapping_type.deserialize_json(
                data["idMappingType"]
            )
        )
    else:
        import typing

        out["id_mapping_type"] = typing.cast(
            "capo_entityresolution.types.id_mapping_type.IdMappingType", ""
        )
    return out
