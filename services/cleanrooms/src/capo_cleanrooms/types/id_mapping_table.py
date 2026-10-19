"""Generated from Smithy shape ``com.amazonaws.cleanrooms#IdMappingTable``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_cleanrooms.types.child_resource_list
    import capo_cleanrooms.types.collaboration_arn
    import capo_cleanrooms.types.id_mapping_table_arn
    import capo_cleanrooms.types.id_mapping_table_input_reference_config
    import capo_cleanrooms.types.id_mapping_table_input_reference_properties
    import capo_cleanrooms.types.kms_key_arn
    import capo_cleanrooms.types.membership_arn
    import capo_cleanrooms.types.resource_alias
    import capo_cleanrooms.types.resource_description
    import capo_cleanrooms.types.uuid


class IdMappingTable(TypedDict, closed=True):
    id: "capo_cleanrooms.types.uuid.UUID"
    """<p>The unique identifier of the ID mapping table.</p>"""
    arn: "capo_cleanrooms.types.id_mapping_table_arn.IdMappingTableArn"
    """<p>The Amazon Resource Name (ARN) of the ID mapping table.</p>"""
    input_reference_config: "capo_cleanrooms.types.id_mapping_table_input_reference_config.IdMappingTableInputReferenceConfig"
    """<p>The input reference configuration for the ID mapping table.</p>"""
    membership_id: "capo_cleanrooms.types.uuid.UUID"
    """<p>The unique identifier of the membership resource for the ID mapping table.</p>"""
    membership_arn: "capo_cleanrooms.types.membership_arn.MembershipArn"
    """<p>The Amazon Resource Name (ARN) of the membership resource for the ID mapping table.</p>"""
    collaboration_id: "capo_cleanrooms.types.uuid.UUID"
    """<p>The unique identifier of the collaboration that contains this ID mapping table.</p>"""
    collaboration_arn: "capo_cleanrooms.types.collaboration_arn.CollaborationArn"
    """<p>The Amazon Resource Name (ARN) of the collaboration that contains this ID mapping table.</p>"""
    description: NotRequired[
        "capo_cleanrooms.types.resource_description.ResourceDescription"
    ]
    """<p>The description of the ID mapping table.</p>"""
    name: "capo_cleanrooms.types.resource_alias.ResourceAlias"
    """<p>The name of the ID mapping table.</p>"""
    create_time: "datetime.datetime"
    """<p>The time at which the ID mapping table was created.</p>"""
    update_time: "datetime.datetime"
    """<p>The most recent time at which the ID mapping table was updated.</p>"""
    input_reference_properties: "capo_cleanrooms.types.id_mapping_table_input_reference_properties.IdMappingTableInputReferenceProperties"
    """<p>The input reference properties for the ID mapping table.</p>"""
    kms_key_arn: NotRequired["capo_cleanrooms.types.kms_key_arn.KMSKeyArn"]
    """<p>The Amazon Resource Name (ARN) of the Amazon Web Services KMS key.</p>"""
    child_resources: NotRequired[
        "capo_cleanrooms.types.child_resource_list.ChildResourceList"
    ]
    """<p>The child resources that depend on this ID mapping table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IdMappingTable) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    import capo_cleanrooms.types.id_mapping_table_input_reference_config

    out["inputReferenceConfig"] = (
        capo_cleanrooms.types.id_mapping_table_input_reference_config.serialize_json(
            value["input_reference_config"]
        )
    )
    out["membershipId"] = value["membership_id"]
    out["membershipArn"] = value["membership_arn"]
    out["collaborationId"] = value["collaboration_id"]
    out["collaborationArn"] = value["collaboration_arn"]
    if "description" in value:
        out["description"] = value["description"]
    out["name"] = value["name"]
    import capo_cleanrooms.types._prelude.timestamp

    out["createTime"] = capo_cleanrooms.types._prelude.timestamp.serialize_json(
        value["create_time"]
    )
    import capo_cleanrooms.types._prelude.timestamp

    out["updateTime"] = capo_cleanrooms.types._prelude.timestamp.serialize_json(
        value["update_time"]
    )
    import capo_cleanrooms.types.id_mapping_table_input_reference_properties

    out["inputReferenceProperties"] = (
        capo_cleanrooms.types.id_mapping_table_input_reference_properties.serialize_json(
            value["input_reference_properties"]
        )
    )
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    if "child_resources" in value:
        import capo_cleanrooms.types.child_resource_list

        out["childResources"] = (
            capo_cleanrooms.types.child_resource_list.serialize_json(
                value["child_resources"]
            )
        )
    return out


def deserialize_json(data: dict) -> IdMappingTable:
    out: IdMappingTable = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("inputReferenceConfig") is not None:
        import capo_cleanrooms.types.id_mapping_table_input_reference_config

        out["input_reference_config"] = (
            capo_cleanrooms.types.id_mapping_table_input_reference_config.deserialize_json(
                data["inputReferenceConfig"]
            )
        )
    else:
        raise DeserializationError("IdMappingTable.input_reference_config required")
    if data.get("membershipId") is not None:
        out["membership_id"] = data["membershipId"]
    else:
        out["membership_id"] = ""
    if data.get("membershipArn") is not None:
        out["membership_arn"] = data["membershipArn"]
    else:
        out["membership_arn"] = ""
    if data.get("collaborationId") is not None:
        out["collaboration_id"] = data["collaborationId"]
    else:
        out["collaboration_id"] = ""
    if data.get("collaborationArn") is not None:
        out["collaboration_arn"] = data["collaborationArn"]
    else:
        out["collaboration_arn"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("createTime") is not None:
        import capo_cleanrooms.types._prelude.timestamp

        out["create_time"] = capo_cleanrooms.types._prelude.timestamp.deserialize_json(
            data["createTime"]
        )
    else:
        import datetime

        out["create_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("updateTime") is not None:
        import capo_cleanrooms.types._prelude.timestamp

        out["update_time"] = capo_cleanrooms.types._prelude.timestamp.deserialize_json(
            data["updateTime"]
        )
    else:
        import datetime

        out["update_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("inputReferenceProperties") is not None:
        import capo_cleanrooms.types.id_mapping_table_input_reference_properties

        out["input_reference_properties"] = (
            capo_cleanrooms.types.id_mapping_table_input_reference_properties.deserialize_json(
                data["inputReferenceProperties"]
            )
        )
    else:
        raise DeserializationError("IdMappingTable.input_reference_properties required")
    if data.get("kmsKeyArn") is not None:
        out["kms_key_arn"] = data["kmsKeyArn"]
    if data.get("childResources") is not None:
        import capo_cleanrooms.types.child_resource_list

        out["child_resources"] = (
            capo_cleanrooms.types.child_resource_list.deserialize_json(
                data["childResources"]
            )
        )
    return out
