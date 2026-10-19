"""Generated from Smithy shape ``com.amazonaws.cleanrooms#CreateIdNamespaceAssociationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanrooms.types.generic_resource_name
    import capo_cleanrooms.types.id_mapping_config
    import capo_cleanrooms.types.id_namespace_association_input_reference_config
    import capo_cleanrooms.types.membership_identifier
    import capo_cleanrooms.types.resource_description
    import capo_cleanrooms.types.tag_map


class CreateIdNamespaceAssociationInput(TypedDict, closed=True):
    membership_identifier: (
        "capo_cleanrooms.types.membership_identifier.MembershipIdentifier"
    )
    """<p>The unique identifier of the membership that contains the ID namespace association.</p>"""
    input_reference_config: "capo_cleanrooms.types.id_namespace_association_input_reference_config.IdNamespaceAssociationInputReferenceConfig"
    """<p>The input reference configuration needed to create the ID namespace association.</p>"""
    tags: NotRequired["capo_cleanrooms.types.tag_map.TagMap"]
    """<p>An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.</p>"""
    name: "capo_cleanrooms.types.generic_resource_name.GenericResourceName"
    """<p>The name for the ID namespace association.</p>"""
    description: NotRequired[
        "capo_cleanrooms.types.resource_description.ResourceDescription"
    ]
    """<p>The description of the ID namespace association.</p>"""
    id_mapping_config: NotRequired[
        "capo_cleanrooms.types.id_mapping_config.IdMappingConfig"
    ]
    """<p>The configuration settings for the ID mapping table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateIdNamespaceAssociationInput) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.id_namespace_association_input_reference_config

    out["inputReferenceConfig"] = (
        capo_cleanrooms.types.id_namespace_association_input_reference_config.serialize_json(
            value["input_reference_config"]
        )
    )
    if "tags" in value:
        import capo_cleanrooms.types.tag_map

        out["tags"] = capo_cleanrooms.types.tag_map.serialize_json(value["tags"])
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "id_mapping_config" in value:
        import capo_cleanrooms.types.id_mapping_config

        out["idMappingConfig"] = capo_cleanrooms.types.id_mapping_config.serialize_json(
            value["id_mapping_config"]
        )
    return out


def deserialize_json(data: dict) -> CreateIdNamespaceAssociationInput:
    out: CreateIdNamespaceAssociationInput = {}  # type: ignore[typeddict-item]
    if data.get("inputReferenceConfig") is not None:
        import capo_cleanrooms.types.id_namespace_association_input_reference_config

        out["input_reference_config"] = (
            capo_cleanrooms.types.id_namespace_association_input_reference_config.deserialize_json(
                data["inputReferenceConfig"]
            )
        )
    else:
        raise DeserializationError(
            "CreateIdNamespaceAssociationInput.input_reference_config required"
        )
    if data.get("tags") is not None:
        import capo_cleanrooms.types.tag_map

        out["tags"] = capo_cleanrooms.types.tag_map.deserialize_json(data["tags"])
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("idMappingConfig") is not None:
        import capo_cleanrooms.types.id_mapping_config

        out["id_mapping_config"] = (
            capo_cleanrooms.types.id_mapping_config.deserialize_json(
                data["idMappingConfig"]
            )
        )
    return out
