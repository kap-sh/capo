"""Generated from Smithy shape ``com.amazonaws.datazone#ProjectProfileSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_datazone.types.created_by
    import capo_datazone.types.description
    import capo_datazone.types.domain_id
    import capo_datazone.types.domain_unit_id
    import capo_datazone.types.project_profile_id
    import capo_datazone.types.project_profile_name
    import capo_datazone.types.status


class ProjectProfileSummary(TypedDict, closed=True):
    domain_id: "capo_datazone.types.domain_id.DomainId"
    """<p>The domain ID of the project profile.</p>"""
    id: "capo_datazone.types.project_profile_id.ProjectProfileId"
    """<p>The ID of the project profile.</p>"""
    name: "capo_datazone.types.project_profile_name.ProjectProfileName"
    """<p>The name of a project profile.</p>"""
    description: NotRequired["capo_datazone.types.description.Description"]
    """<p>The description of the project profile.</p>"""
    status: NotRequired["capo_datazone.types.status.Status"]
    """<p>The status of a project profile.</p>"""
    created_by: "capo_datazone.types.created_by.CreatedBy"
    """<p>The user who created the project profile.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the project profile was created.</p>"""
    last_updated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp at which a project profile was last updated.</p>"""
    domain_unit_id: NotRequired["capo_datazone.types.domain_unit_id.DomainUnitId"]
    """<p>The domain unit ID of the project profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProjectProfileSummary) -> dict:
    out: dict = {}
    out["domainId"] = value["domain_id"]
    out["id"] = value["id"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "status" in value:
        import capo_datazone.types.status

        out["status"] = capo_datazone.types.status.serialize_json(value["status"])
    out["createdBy"] = value["created_by"]
    if "created_at" in value:
        import capo_datazone._protocol.serialize

        out["createdAt"] = capo_datazone._protocol.serialize.fmt_date_time(
            value["created_at"]
        )
    if "last_updated_at" in value:
        import capo_datazone._protocol.serialize

        out["lastUpdatedAt"] = capo_datazone._protocol.serialize.fmt_date_time(
            value["last_updated_at"]
        )
    if "domain_unit_id" in value:
        out["domainUnitId"] = value["domain_unit_id"]
    return out


def deserialize_json(data: dict) -> ProjectProfileSummary:
    out: ProjectProfileSummary = {}  # type: ignore[typeddict-item]
    if data.get("domainId") is not None:
        out["domain_id"] = data["domainId"]
    else:
        raise DeserializationError("ProjectProfileSummary.domain_id required")
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        raise DeserializationError("ProjectProfileSummary.id required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ProjectProfileSummary.name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("status") is not None:
        import capo_datazone.types.status

        out["status"] = capo_datazone.types.status.deserialize_json(data["status"])
    if data.get("createdBy") is not None:
        out["created_by"] = data["createdBy"]
    else:
        raise DeserializationError("ProjectProfileSummary.created_by required")
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    if data.get("lastUpdatedAt") is not None:
        import datetime

        out["last_updated_at"] = datetime.datetime.fromisoformat(
            data["lastUpdatedAt"].replace("Z", "+00:00")
        )
    if data.get("domainUnitId") is not None:
        out["domain_unit_id"] = data["domainUnitId"]
    return out


def redact_sensitive(value: ProjectProfileSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
