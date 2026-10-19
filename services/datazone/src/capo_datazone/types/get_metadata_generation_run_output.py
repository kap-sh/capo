"""Generated from Smithy shape ``com.amazonaws.datazone#GetMetadataGenerationRunOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.created_at
    import capo_datazone.types.created_by
    import capo_datazone.types.domain_id
    import capo_datazone.types.metadata_generation_run_identifier
    import capo_datazone.types.metadata_generation_run_status
    import capo_datazone.types.metadata_generation_run_target
    import capo_datazone.types.metadata_generation_run_type
    import capo_datazone.types.metadata_generation_run_type_stats
    import capo_datazone.types.metadata_generation_run_types
    import capo_datazone.types.project_id


class GetMetadataGenerationRunOutput(TypedDict, closed=True):
    domain_id: "capo_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain the metadata generation run of which you want to get.</p>"""
    id: "capo_datazone.types.metadata_generation_run_identifier.MetadataGenerationRunIdentifier"
    """<p>The ID of the metadata generation run.</p>"""
    target: NotRequired[
        "capo_datazone.types.metadata_generation_run_target.MetadataGenerationRunTarget"
    ]
    """<p>The asset for which you're generating metadata.</p>"""
    status: NotRequired[
        "capo_datazone.types.metadata_generation_run_status.MetadataGenerationRunStatus"
    ]
    """<p>The status of the metadata generation run.</p>"""
    type: NotRequired[
        "capo_datazone.types.metadata_generation_run_type.MetadataGenerationRunType"
    ]
    """<p>The type of metadata generation run.</p>"""
    types: NotRequired[
        "capo_datazone.types.metadata_generation_run_types.MetadataGenerationRunTypes"
    ]
    """<p>The types of the metadata generation run.</p>"""
    created_at: NotRequired["capo_datazone.types.created_at.CreatedAt"]
    """<p>The timestamp of when the metadata generation run was start.</p>"""
    created_by: NotRequired["capo_datazone.types.created_by.CreatedBy"]
    """<p>The Amazon DataZone user who started the metadata generation run.</p>"""
    owning_project_id: "capo_datazone.types.project_id.ProjectId"
    """<p>The ID of the project that owns the assets for which you're running metadata generation.</p>"""
    type_stats: NotRequired[
        "capo_datazone.types.metadata_generation_run_type_stats.MetadataGenerationRunTypeStats"
    ]
    """<p>The type stats included in the metadata generation run output details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMetadataGenerationRunOutput) -> dict:
    out: dict = {}
    out["domainId"] = value["domain_id"]
    out["id"] = value["id"]
    if "target" in value:
        import capo_datazone.types.metadata_generation_run_target

        out["target"] = (
            capo_datazone.types.metadata_generation_run_target.serialize_json(
                value["target"]
            )
        )
    if "status" in value:
        import capo_datazone.types.metadata_generation_run_status

        out["status"] = (
            capo_datazone.types.metadata_generation_run_status.serialize_json(
                value["status"]
            )
        )
    if "type" in value:
        import capo_datazone.types.metadata_generation_run_type

        out["type"] = capo_datazone.types.metadata_generation_run_type.serialize_json(
            value["type"]
        )
    if "types" in value:
        import capo_datazone.types.metadata_generation_run_types

        out["types"] = capo_datazone.types.metadata_generation_run_types.serialize_json(
            value["types"]
        )
    if "created_at" in value:
        import capo_datazone.types.created_at

        out["createdAt"] = capo_datazone.types.created_at.serialize_json(
            value["created_at"]
        )
    if "created_by" in value:
        out["createdBy"] = value["created_by"]
    out["owningProjectId"] = value["owning_project_id"]
    if "type_stats" in value:
        import capo_datazone.types.metadata_generation_run_type_stats

        out["typeStats"] = (
            capo_datazone.types.metadata_generation_run_type_stats.serialize_json(
                value["type_stats"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetMetadataGenerationRunOutput:
    out: GetMetadataGenerationRunOutput = {}  # type: ignore[typeddict-item]
    if data.get("domainId") is not None:
        out["domain_id"] = data["domainId"]
    else:
        out["domain_id"] = ""
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("target") is not None:
        import capo_datazone.types.metadata_generation_run_target

        out["target"] = (
            capo_datazone.types.metadata_generation_run_target.deserialize_json(
                data["target"]
            )
        )
    if data.get("status") is not None:
        import capo_datazone.types.metadata_generation_run_status

        out["status"] = (
            capo_datazone.types.metadata_generation_run_status.deserialize_json(
                data["status"]
            )
        )
    if data.get("type") is not None:
        import capo_datazone.types.metadata_generation_run_type

        out["type"] = capo_datazone.types.metadata_generation_run_type.deserialize_json(
            data["type"]
        )
    if data.get("types") is not None:
        import capo_datazone.types.metadata_generation_run_types

        out["types"] = (
            capo_datazone.types.metadata_generation_run_types.deserialize_json(
                data["types"]
            )
        )
    if data.get("createdAt") is not None:
        import capo_datazone.types.created_at

        out["created_at"] = capo_datazone.types.created_at.deserialize_json(
            data["createdAt"]
        )
    if data.get("createdBy") is not None:
        out["created_by"] = data["createdBy"]
    if data.get("owningProjectId") is not None:
        out["owning_project_id"] = data["owningProjectId"]
    else:
        out["owning_project_id"] = ""
    if data.get("typeStats") is not None:
        import capo_datazone.types.metadata_generation_run_type_stats

        out["type_stats"] = (
            capo_datazone.types.metadata_generation_run_type_stats.deserialize_json(
                data["typeStats"]
            )
        )
    return out
