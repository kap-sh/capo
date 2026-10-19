"""Generated from Smithy shape ``com.amazonaws.datazone#ProjectSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_datazone.types.created_by
    import capo_datazone.types.description
    import capo_datazone.types.domain_id
    import capo_datazone.types.domain_unit_id
    import capo_datazone.types.failure_reasons
    import capo_datazone.types.project_id
    import capo_datazone.types.project_name
    import capo_datazone.types.project_status


class ProjectSummary(TypedDict, closed=True):
    domain_id: "capo_datazone.types.domain_id.DomainId"
    """<p>The identifier of a Amazon DataZone domain where the project exists.</p>"""
    id: "capo_datazone.types.project_id.ProjectId"
    """<p>The identifier of a project.</p>"""
    name: "capo_datazone.types.project_name.ProjectName"
    """<p>The name of a project.</p>"""
    description: NotRequired["capo_datazone.types.description.Description"]
    """<p>The description of a project.</p>"""
    project_status: NotRequired["capo_datazone.types.project_status.ProjectStatus"]
    """<p>The status of the project.</p>"""
    failure_reasons: NotRequired["capo_datazone.types.failure_reasons.FailureReasons"]
    """<p>Specifies the error message that is returned if the operation cannot be successfully completed.</p>"""
    created_by: "capo_datazone.types.created_by.CreatedBy"
    """<p>The Amazon DataZone user who created the project.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The timestamp of when a project was created.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the project was updated.</p>"""
    domain_unit_id: NotRequired["capo_datazone.types.domain_unit_id.DomainUnitId"]
    """<p>The ID of the domain unit.</p>"""
    project_category: NotRequired["str"]
    """<p>The category of the project.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProjectSummary) -> dict:
    out: dict = {}
    out["domainId"] = value["domain_id"]
    out["id"] = value["id"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "project_status" in value:
        import capo_datazone.types.project_status

        out["projectStatus"] = capo_datazone.types.project_status.serialize_json(
            value["project_status"]
        )
    if "failure_reasons" in value:
        import capo_datazone.types.failure_reasons

        out["failureReasons"] = capo_datazone.types.failure_reasons.serialize_json(
            value["failure_reasons"]
        )
    out["createdBy"] = value["created_by"]
    if "created_at" in value:
        import capo_datazone._protocol.serialize

        out["createdAt"] = capo_datazone._protocol.serialize.fmt_date_time(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_datazone._protocol.serialize

        out["updatedAt"] = capo_datazone._protocol.serialize.fmt_date_time(
            value["updated_at"]
        )
    if "domain_unit_id" in value:
        out["domainUnitId"] = value["domain_unit_id"]
    if "project_category" in value:
        out["projectCategory"] = value["project_category"]
    return out


def deserialize_json(data: dict) -> ProjectSummary:
    out: ProjectSummary = {}  # type: ignore[typeddict-item]
    if data.get("domainId") is not None:
        out["domain_id"] = data["domainId"]
    else:
        out["domain_id"] = ""
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("projectStatus") is not None:
        import capo_datazone.types.project_status

        out["project_status"] = capo_datazone.types.project_status.deserialize_json(
            data["projectStatus"]
        )
    if data.get("failureReasons") is not None:
        import capo_datazone.types.failure_reasons

        out["failure_reasons"] = capo_datazone.types.failure_reasons.deserialize_json(
            data["failureReasons"]
        )
    if data.get("createdBy") is not None:
        out["created_by"] = data["createdBy"]
    else:
        out["created_by"] = ""
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    if data.get("updatedAt") is not None:
        import datetime

        out["updated_at"] = datetime.datetime.fromisoformat(
            data["updatedAt"].replace("Z", "+00:00")
        )
    if data.get("domainUnitId") is not None:
        out["domain_unit_id"] = data["domainUnitId"]
    if data.get("projectCategory") is not None:
        out["project_category"] = data["projectCategory"]
    return out


def redact_sensitive(value: ProjectSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
