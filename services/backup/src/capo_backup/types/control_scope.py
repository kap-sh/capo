"""Generated from Smithy shape ``com.amazonaws.backup#ControlScope``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.compliance_resource_id_list
    import capo_backup.types.resource_type_list
    import capo_backup.types.string_map


class ControlScope(TypedDict, closed=True):
    compliance_resource_ids: NotRequired[
        "capo_backup.types.compliance_resource_id_list.ComplianceResourceIdList"
    ]
    """<p>The ID of the only Amazon Web Services resource that you want your control scope to contain.</p>"""
    compliance_resource_types: NotRequired[
        "capo_backup.types.resource_type_list.ResourceTypeList"
    ]
    """<p>Describes whether the control scope includes one or more types of resources, such as <code>EFS</code> or <code>RDS</code>.</p>"""
    tags: NotRequired["capo_backup.types.string_map.stringMap"]
    """<p>The tag key-value pair applied to those Amazon Web Services resources that you want to trigger an evaluation for a rule. A maximum of one key-value pair can be provided. The tag value is optional, but it cannot be an empty string if you are creating or editing a framework from the console (though the value can be an empty string when included in a CloudFormation template).</p> <p>The structure to assign a tag is: <code>[{"Key":"string","Value":"string"}]</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ControlScope) -> dict:
    out: dict = {}
    if "compliance_resource_ids" in value:
        import capo_backup.types.compliance_resource_id_list

        out["ComplianceResourceIds"] = (
            capo_backup.types.compliance_resource_id_list.serialize_json(
                value["compliance_resource_ids"]
            )
        )
    if "compliance_resource_types" in value:
        import capo_backup.types.resource_type_list

        out["ComplianceResourceTypes"] = (
            capo_backup.types.resource_type_list.serialize_json(
                value["compliance_resource_types"]
            )
        )
    if "tags" in value:
        import capo_backup.types.string_map

        out["Tags"] = capo_backup.types.string_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> ControlScope:
    out: ControlScope = {}  # type: ignore[typeddict-item]
    if data.get("ComplianceResourceIds") is not None:
        import capo_backup.types.compliance_resource_id_list

        out["compliance_resource_ids"] = (
            capo_backup.types.compliance_resource_id_list.deserialize_json(
                data["ComplianceResourceIds"]
            )
        )
    if data.get("ComplianceResourceTypes") is not None:
        import capo_backup.types.resource_type_list

        out["compliance_resource_types"] = (
            capo_backup.types.resource_type_list.deserialize_json(
                data["ComplianceResourceTypes"]
            )
        )
    if data.get("Tags") is not None:
        import capo_backup.types.string_map

        out["tags"] = capo_backup.types.string_map.deserialize_json(data["Tags"])
    return out
