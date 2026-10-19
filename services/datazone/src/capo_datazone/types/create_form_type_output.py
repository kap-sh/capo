"""Generated from Smithy shape ``com.amazonaws.datazone#CreateFormTypeOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.description
    import capo_datazone.types.domain_id
    import capo_datazone.types.form_type_name
    import capo_datazone.types.project_id
    import capo_datazone.types.revision


class CreateFormTypeOutput(TypedDict, closed=True):
    domain_id: "capo_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain in which this metadata form type is created.</p>"""
    name: "capo_datazone.types.form_type_name.FormTypeName"
    """<p>The name of this Amazon DataZone metadata form type.</p>"""
    revision: "capo_datazone.types.revision.Revision"
    """<p>The revision of this Amazon DataZone metadata form type.</p>"""
    description: NotRequired["capo_datazone.types.description.Description"]
    """<p>The description of this Amazon DataZone metadata form type.</p>"""
    owning_project_id: NotRequired["capo_datazone.types.project_id.ProjectId"]
    """<p>The ID of the project that owns this Amazon DataZone metadata form type.</p>"""
    origin_domain_id: NotRequired["capo_datazone.types.domain_id.DomainId"]
    """<p>The ID of the Amazon DataZone domain in which this metadata form type was originally created.</p>"""
    origin_project_id: NotRequired["capo_datazone.types.project_id.ProjectId"]
    """<p>The ID of the project in which this Amazon DataZone metadata form type was originally created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateFormTypeOutput) -> dict:
    out: dict = {}
    out["domainId"] = value["domain_id"]
    out["name"] = value["name"]
    out["revision"] = value["revision"]
    if "description" in value:
        out["description"] = value["description"]
    if "owning_project_id" in value:
        out["owningProjectId"] = value["owning_project_id"]
    if "origin_domain_id" in value:
        out["originDomainId"] = value["origin_domain_id"]
    if "origin_project_id" in value:
        out["originProjectId"] = value["origin_project_id"]
    return out


def deserialize_json(data: dict) -> CreateFormTypeOutput:
    out: CreateFormTypeOutput = {}  # type: ignore[typeddict-item]
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
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("owningProjectId") is not None:
        out["owning_project_id"] = data["owningProjectId"]
    if data.get("originDomainId") is not None:
        out["origin_domain_id"] = data["originDomainId"]
    if data.get("originProjectId") is not None:
        out["origin_project_id"] = data["originProjectId"]
    return out


def redact_sensitive(value: CreateFormTypeOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
