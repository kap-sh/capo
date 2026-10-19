"""Generated from Smithy shape ``com.amazonaws.datazone#LineageNodeSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_datazone.types.created_at
    import capo_datazone.types.created_by
    import capo_datazone.types.domain_id
    import capo_datazone.types.lineage_node_id
    import capo_datazone.types.revision
    import capo_datazone.types.updated_at
    import capo_datazone.types.updated_by


class LineageNodeSummary(TypedDict, closed=True):
    domain_id: "capo_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain of the data lineage node.</p>"""
    name: NotRequired["str"]
    """<p>The name of the data lineage node.</p>"""
    description: NotRequired["str"]
    """<p>The description of the data lineage node.</p>"""
    created_at: NotRequired["capo_datazone.types.created_at.CreatedAt"]
    """<p>The timestamp at which the data lineage node was created.</p>"""
    created_by: NotRequired["capo_datazone.types.created_by.CreatedBy"]
    """<p>The user who created the data lineage node.</p>"""
    updated_at: NotRequired["capo_datazone.types.updated_at.UpdatedAt"]
    """<p>The timestamp at which the data lineage node was updated.</p>"""
    updated_by: NotRequired["capo_datazone.types.updated_by.UpdatedBy"]
    """<p>The user who updated the data lineage node.</p>"""
    id: "capo_datazone.types.lineage_node_id.LineageNodeId"
    """<p>The ID of the data lineage node.</p>"""
    type_name: "str"
    """<p>The name of the type of the data lineage node.</p>"""
    type_revision: NotRequired["capo_datazone.types.revision.Revision"]
    """<p>The type of the revision of the data lineage node.</p>"""
    source_identifier: NotRequired["str"]
    """<p>The alternate ID of the data lineage node.</p>"""
    event_timestamp: NotRequired["datetime.datetime"]
    """<p>The event timestamp of the data lineage node.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LineageNodeSummary) -> dict:
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
    out["id"] = value["id"]
    out["typeName"] = value["type_name"]
    if "type_revision" in value:
        out["typeRevision"] = value["type_revision"]
    if "source_identifier" in value:
        out["sourceIdentifier"] = value["source_identifier"]
    if "event_timestamp" in value:
        import capo_datazone.types._prelude.timestamp

        out["eventTimestamp"] = capo_datazone.types._prelude.timestamp.serialize_json(
            value["event_timestamp"]
        )
    return out


def deserialize_json(data: dict) -> LineageNodeSummary:
    out: LineageNodeSummary = {}  # type: ignore[typeddict-item]
    if data.get("domainId") is not None:
        out["domain_id"] = data["domainId"]
    else:
        out["domain_id"] = ""
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
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("typeName") is not None:
        out["type_name"] = data["typeName"]
    else:
        out["type_name"] = ""
    if data.get("typeRevision") is not None:
        out["type_revision"] = data["typeRevision"]
    if data.get("sourceIdentifier") is not None:
        out["source_identifier"] = data["sourceIdentifier"]
    if data.get("eventTimestamp") is not None:
        import capo_datazone.types._prelude.timestamp

        out["event_timestamp"] = (
            capo_datazone.types._prelude.timestamp.deserialize_json(
                data["eventTimestamp"]
            )
        )
    return out
