"""Generated from Smithy shape ``com.amazonaws.entityresolution#IdNamespaceSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_entityresolution.types.description
    import capo_entityresolution.types.entity_name
    import capo_entityresolution.types.id_namespace_arn
    import capo_entityresolution.types.id_namespace_id_mapping_workflow_metadata_list
    import capo_entityresolution.types.id_namespace_type


class IdNamespaceSummary(TypedDict, closed=True):
    id_namespace_name: "capo_entityresolution.types.entity_name.EntityName"
    """<p>The name of the ID namespace.</p>"""
    id_namespace_arn: "capo_entityresolution.types.id_namespace_arn.IdNamespaceArn"
    """<p>The Amazon Resource Name (ARN) of the ID namespace.</p>"""
    description: NotRequired["capo_entityresolution.types.description.Description"]
    """<p>The description of the ID namespace.</p>"""
    id_mapping_workflow_properties: NotRequired[
        "capo_entityresolution.types.id_namespace_id_mapping_workflow_metadata_list.IdNamespaceIdMappingWorkflowMetadataList"
    ]
    """<p>An object which defines any additional configurations required by the ID mapping workflow.</p>"""
    type: "capo_entityresolution.types.id_namespace_type.IdNamespaceType"
    """<p>The type of ID namespace. There are two types: <code>SOURCE</code> and <code>TARGET</code>.</p> <p>The <code>SOURCE</code> contains configurations for <code>sourceId</code> data that will be processed in an ID mapping workflow. </p> <p>The <code>TARGET</code> contains a configuration of <code>targetId</code> which all <code>sourceIds</code> will resolve to.</p>"""
    created_at: "datetime.datetime"
    """<p>The timestamp of when the ID namespace was created.</p>"""
    updated_at: "datetime.datetime"
    """<p>The timestamp of when the ID namespace was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IdNamespaceSummary) -> dict:
    out: dict = {}
    out["idNamespaceName"] = value["id_namespace_name"]
    out["idNamespaceArn"] = value["id_namespace_arn"]
    if "description" in value:
        out["description"] = value["description"]
    if "id_mapping_workflow_properties" in value:
        import capo_entityresolution.types.id_namespace_id_mapping_workflow_metadata_list

        out["idMappingWorkflowProperties"] = (
            capo_entityresolution.types.id_namespace_id_mapping_workflow_metadata_list.serialize_json(
                value["id_mapping_workflow_properties"]
            )
        )
    import capo_entityresolution.types.id_namespace_type

    out["type"] = capo_entityresolution.types.id_namespace_type.serialize_json(
        value["type"]
    )
    import capo_entityresolution.types._prelude.timestamp

    out["createdAt"] = capo_entityresolution.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    import capo_entityresolution.types._prelude.timestamp

    out["updatedAt"] = capo_entityresolution.types._prelude.timestamp.serialize_json(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> IdNamespaceSummary:
    out: IdNamespaceSummary = {}  # type: ignore[typeddict-item]
    if data.get("idNamespaceName") is not None:
        out["id_namespace_name"] = data["idNamespaceName"]
    else:
        out["id_namespace_name"] = ""
    if data.get("idNamespaceArn") is not None:
        out["id_namespace_arn"] = data["idNamespaceArn"]
    else:
        out["id_namespace_arn"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("idMappingWorkflowProperties") is not None:
        import capo_entityresolution.types.id_namespace_id_mapping_workflow_metadata_list

        out["id_mapping_workflow_properties"] = (
            capo_entityresolution.types.id_namespace_id_mapping_workflow_metadata_list.deserialize_json(
                data["idMappingWorkflowProperties"]
            )
        )
    if data.get("type") is not None:
        import capo_entityresolution.types.id_namespace_type

        out["type"] = capo_entityresolution.types.id_namespace_type.deserialize_json(
            data["type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_entityresolution.types.id_namespace_type.IdNamespaceType", ""
        )
    if data.get("createdAt") is not None:
        import capo_entityresolution.types._prelude.timestamp

        out["created_at"] = (
            capo_entityresolution.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("updatedAt") is not None:
        import capo_entityresolution.types._prelude.timestamp

        out["updated_at"] = (
            capo_entityresolution.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
