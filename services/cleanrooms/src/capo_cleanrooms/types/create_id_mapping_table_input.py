"""Generated from Smithy shape ``com.amazonaws.cleanrooms#CreateIdMappingTableInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanrooms.types.id_mapping_table_input_reference_config
    import capo_cleanrooms.types.kms_key_arn
    import capo_cleanrooms.types.membership_identifier
    import capo_cleanrooms.types.resource_alias
    import capo_cleanrooms.types.resource_description
    import capo_cleanrooms.types.tag_map


class CreateIdMappingTableInput(TypedDict, closed=True):
    membership_identifier: (
        "capo_cleanrooms.types.membership_identifier.MembershipIdentifier"
    )
    """<p>The unique identifier of the membership that contains the ID mapping table.</p>"""
    name: "capo_cleanrooms.types.resource_alias.ResourceAlias"
    """<p>A name for the ID mapping table.</p>"""
    description: NotRequired[
        "capo_cleanrooms.types.resource_description.ResourceDescription"
    ]
    """<p>A description of the ID mapping table.</p>"""
    input_reference_config: "capo_cleanrooms.types.id_mapping_table_input_reference_config.IdMappingTableInputReferenceConfig"
    """<p>The input reference configuration needed to create the ID mapping table.</p>"""
    tags: NotRequired["capo_cleanrooms.types.tag_map.TagMap"]
    """<p>An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.</p>"""
    kms_key_arn: NotRequired["capo_cleanrooms.types.kms_key_arn.KMSKeyArn"]
    """<p>The Amazon Resource Name (ARN) of the Amazon Web Services KMS key. This value is used to encrypt the mapping table data that is stored by Clean Rooms.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateIdMappingTableInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_cleanrooms.types.id_mapping_table_input_reference_config

    out["inputReferenceConfig"] = (
        capo_cleanrooms.types.id_mapping_table_input_reference_config.serialize_json(
            value["input_reference_config"]
        )
    )
    if "tags" in value:
        import capo_cleanrooms.types.tag_map

        out["tags"] = capo_cleanrooms.types.tag_map.serialize_json(value["tags"])
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_json(data: dict) -> CreateIdMappingTableInput:
    out: CreateIdMappingTableInput = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("inputReferenceConfig") is not None:
        import capo_cleanrooms.types.id_mapping_table_input_reference_config

        out["input_reference_config"] = (
            capo_cleanrooms.types.id_mapping_table_input_reference_config.deserialize_json(
                data["inputReferenceConfig"]
            )
        )
    else:
        raise DeserializationError(
            "CreateIdMappingTableInput.input_reference_config required"
        )
    if data.get("tags") is not None:
        import capo_cleanrooms.types.tag_map

        out["tags"] = capo_cleanrooms.types.tag_map.deserialize_json(data["tags"])
    if data.get("kmsKeyArn") is not None:
        out["kms_key_arn"] = data["kmsKeyArn"]
    return out
