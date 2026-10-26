"""Generated from Smithy shape ``com.amazonaws.datazone#CreateFormTypeInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.description
    import capo_datazone.types.domain_id
    import capo_datazone.types.form_type_name
    import capo_datazone.types.form_type_status
    import capo_datazone.types.model
    import capo_datazone.types.project_id


class CreateFormTypeInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain in which this metadata form type is created.</p>"""
    name: "capo_datazone.types.form_type_name.FormTypeName"
    """<p>The name of this Amazon DataZone metadata form type.</p>"""
    model: "capo_datazone.types.model.Model"
    """<p>The model of this Amazon DataZone metadata form type.</p>"""
    owning_project_identifier: "capo_datazone.types.project_id.ProjectId"
    """<p>The ID of the Amazon DataZone project that owns this metadata form type.</p>"""
    status: NotRequired["capo_datazone.types.form_type_status.FormTypeStatus"]
    """<p>The status of this Amazon DataZone metadata form type.</p>"""
    description: NotRequired["capo_datazone.types.description.Description"]
    """<p>The description of this Amazon DataZone metadata form type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateFormTypeInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_datazone.types.model

    out["model"] = capo_datazone.types.model.serialize_json(value["model"])
    out["owningProjectIdentifier"] = value["owning_project_identifier"]
    if "status" in value:
        import capo_datazone.types.form_type_status

        out["status"] = capo_datazone.types.form_type_status.serialize_json(
            value["status"]
        )
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> CreateFormTypeInput:
    out: CreateFormTypeInput = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("model") is not None:
        import capo_datazone.types.model

        out["model"] = capo_datazone.types.model.deserialize_json(data["model"])
    else:
        out["model"] = {"$unknown": {"name": ""}}
    if data.get("owningProjectIdentifier") is not None:
        out["owning_project_identifier"] = data["owningProjectIdentifier"]
    else:
        out["owning_project_identifier"] = ""
    if data.get("status") is not None:
        import capo_datazone.types.form_type_status

        out["status"] = capo_datazone.types.form_type_status.deserialize_json(
            data["status"]
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    return out


def redact_sensitive(value: CreateFormTypeInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "model" in value:
        out["model"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
