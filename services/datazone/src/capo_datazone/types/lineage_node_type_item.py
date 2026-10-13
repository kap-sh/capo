"""Generated from Smithy shape ``com.amazonaws.datazone#LineageNodeTypeItem``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datazone.types.created_at
    import capo_datazone.types.created_by
    import capo_datazone.types.domain_id
    import capo_datazone.types.forms_output_map
    import capo_datazone.types.revision
    import capo_datazone.types.updated_at
    import capo_datazone.types.updated_by


class LineageNodeTypeItem(TypedDict, closed=True):
    domain_id: "capo_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain where the data lineage node type lives.</p>"""
    name: NotRequired["str"]
    """<p>The name of the data lineage node type.</p>"""
    description: NotRequired["str"]
    """<p>The description of the data lineage node type.</p>"""
    created_at: NotRequired["capo_datazone.types.created_at.CreatedAt"]
    """<p>The timestamp at which the data lineage node type was created.</p>"""
    created_by: NotRequired["capo_datazone.types.created_by.CreatedBy"]
    """<p>The user who created the data lineage node type.</p>"""
    updated_at: NotRequired["capo_datazone.types.updated_at.UpdatedAt"]
    """<p>The timestamp at which the data lineage node type was updated.</p>"""
    updated_by: NotRequired["capo_datazone.types.updated_by.UpdatedBy"]
    """<p>The user who updated the data lineage node type.</p>"""
    revision: "capo_datazone.types.revision.Revision"
    """<p>The revision of the data lineage node type.</p>"""
    forms_output: "capo_datazone.types.forms_output_map.FormsOutputMap"
    """<p>The forms output of the data lineage node type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LineageNodeTypeItem) -> dict:
    out: dict = {}
    out["domainId"] = value["domain_id"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "created_at" in value:
        import capo_datazone.types.created_at

        out["createdAt"] = capo_datazone.types.created_at.serialize_json(
            value["created_at"]
        )
    if "created_by" in value:
        out["createdBy"] = value["created_by"]
    if "updated_at" in value:
        import capo_datazone.types.updated_at

        out["updatedAt"] = capo_datazone.types.updated_at.serialize_json(
            value["updated_at"]
        )
    if "updated_by" in value:
        out["updatedBy"] = value["updated_by"]
    out["revision"] = value["revision"]
    import capo_datazone.types.forms_output_map

    out["formsOutput"] = capo_datazone.types.forms_output_map.serialize_json(
        value["forms_output"]
    )
    return out


def deserialize_json(data: dict) -> LineageNodeTypeItem:
    out: LineageNodeTypeItem = {}  # type: ignore[typeddict-item]
    if data.get("domainId") is not None:
        out["domain_id"] = data["domainId"]
    else:
        raise DeserializationError("LineageNodeTypeItem.domain_id required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("createdAt") is not None:
        import capo_datazone.types.created_at

        out["created_at"] = capo_datazone.types.created_at.deserialize_json(
            data["createdAt"]
        )
    if data.get("createdBy") is not None:
        out["created_by"] = data["createdBy"]
    if data.get("updatedAt") is not None:
        import capo_datazone.types.updated_at

        out["updated_at"] = capo_datazone.types.updated_at.deserialize_json(
            data["updatedAt"]
        )
    if data.get("updatedBy") is not None:
        out["updated_by"] = data["updatedBy"]
    if data.get("revision") is not None:
        out["revision"] = data["revision"]
    else:
        raise DeserializationError("LineageNodeTypeItem.revision required")
    if data.get("formsOutput") is not None:
        import capo_datazone.types.forms_output_map

        out["forms_output"] = capo_datazone.types.forms_output_map.deserialize_json(
            data["formsOutput"]
        )
    else:
        raise DeserializationError("LineageNodeTypeItem.forms_output required")
    return out


def redact_sensitive(value: LineageNodeTypeItem) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "forms_output" in value:
        import capo_datazone.types.forms_output_map

        out["forms_output"] = capo_datazone.types.forms_output_map.redact_sensitive(
            value["forms_output"]
        )
    return out
