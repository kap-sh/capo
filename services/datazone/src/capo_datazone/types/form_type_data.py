"""Generated from Smithy shape ``com.amazonaws.datazone#FormTypeData``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.created_at
    import capo_datazone.types.created_by
    import capo_datazone.types.description
    import capo_datazone.types.domain_id
    import capo_datazone.types.form_type_name
    import capo_datazone.types.form_type_status
    import capo_datazone.types.import_list
    import capo_datazone.types.model
    import capo_datazone.types.project_id
    import capo_datazone.types.revision


class FormTypeData(TypedDict, closed=True):
    domain_id: "capo_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon DataZone domain in which the form type exists.</p>"""
    name: "capo_datazone.types.form_type_name.FormTypeName"
    """<p>The name of the form type.</p>"""
    revision: "capo_datazone.types.revision.Revision"
    """<p>The revision of the form type.</p>"""
    model: NotRequired["capo_datazone.types.model.Model"]
    """<p>The model of the form type.</p>"""
    status: NotRequired["capo_datazone.types.form_type_status.FormTypeStatus"]
    """<p>The status of the form type.</p>"""
    owning_project_id: NotRequired["capo_datazone.types.project_id.ProjectId"]
    """<p>The identifier of the project that owns the form type.</p>"""
    origin_domain_id: NotRequired["capo_datazone.types.domain_id.DomainId"]
    """<p>The identifier of the Amazon DataZone domain in which the form type was originally created.</p>"""
    origin_project_id: NotRequired["capo_datazone.types.project_id.ProjectId"]
    """<p>The identifier of the project in which the form type was originally created.</p>"""
    created_at: NotRequired["capo_datazone.types.created_at.CreatedAt"]
    """<p>The timestamp of when the metadata form type was created.</p>"""
    created_by: NotRequired["capo_datazone.types.created_by.CreatedBy"]
    """<p>The Amazon DataZone user who created teh metadata form type.</p>"""
    description: NotRequired["capo_datazone.types.description.Description"]
    """<p>The description of the metadata form type.</p>"""
    imports: NotRequired["capo_datazone.types.import_list.ImportList"]
    """<p>The imports specified in the form type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FormTypeData) -> dict:
    out: dict = {}
    out["domainId"] = value["domain_id"]
    out["name"] = value["name"]
    out["revision"] = value["revision"]
    if "model" in value:
        import capo_datazone.types.model

        out["model"] = capo_datazone.types.model.serialize_json(value["model"])
    if "status" in value:
        import capo_datazone.types.form_type_status

        out["status"] = capo_datazone.types.form_type_status.serialize_json(
            value["status"]
        )
    if "owning_project_id" in value:
        out["owningProjectId"] = value["owning_project_id"]
    if "origin_domain_id" in value:
        out["originDomainId"] = value["origin_domain_id"]
    if "origin_project_id" in value:
        out["originProjectId"] = value["origin_project_id"]
    if "created_at" in value:
        import capo_datazone.types.created_at

        out["createdAt"] = capo_datazone.types.created_at.serialize_json(
            value["created_at"]
        )
    if "created_by" in value:
        out["createdBy"] = value["created_by"]
    if "description" in value:
        out["description"] = value["description"]
    if "imports" in value:
        import capo_datazone.types.import_list

        out["imports"] = capo_datazone.types.import_list.serialize_json(
            value["imports"]
        )
    return out


def deserialize_json(data: dict) -> FormTypeData:
    out: FormTypeData = {}  # type: ignore[typeddict-item]
    if data.get("domainId") is not None:
        out["domain_id"] = data["domainId"]
    else:
        out["domain_id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("revision") is not None:
        out["revision"] = data["revision"]
    else:
        out["revision"] = ""
    if data.get("model") is not None:
        import capo_datazone.types.model

        out["model"] = capo_datazone.types.model.deserialize_json(data["model"])
    if data.get("status") is not None:
        import capo_datazone.types.form_type_status

        out["status"] = capo_datazone.types.form_type_status.deserialize_json(
            data["status"]
        )
    if data.get("owningProjectId") is not None:
        out["owning_project_id"] = data["owningProjectId"]
    if data.get("originDomainId") is not None:
        out["origin_domain_id"] = data["originDomainId"]
    if data.get("originProjectId") is not None:
        out["origin_project_id"] = data["originProjectId"]
    if data.get("createdAt") is not None:
        import capo_datazone.types.created_at

        out["created_at"] = capo_datazone.types.created_at.deserialize_json(
            data["createdAt"]
        )
    if data.get("createdBy") is not None:
        out["created_by"] = data["createdBy"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("imports") is not None:
        import capo_datazone.types.import_list

        out["imports"] = capo_datazone.types.import_list.deserialize_json(
            data["imports"]
        )
    return out


def redact_sensitive(value: FormTypeData) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "model" in value:
        out["model"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    if "imports" in value:
        import capo_datazone.types.import_list

        out["imports"] = capo_datazone.types.import_list.redact_sensitive(
            value["imports"]
        )
    return out
