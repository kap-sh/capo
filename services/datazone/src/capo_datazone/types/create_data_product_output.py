"""Generated from Smithy shape ``com.amazonaws.datazone#CreateDataProductOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datazone.types.created_at
    import capo_datazone.types.created_by
    import capo_datazone.types.data_product_description
    import capo_datazone.types.data_product_id
    import capo_datazone.types.data_product_items
    import capo_datazone.types.data_product_name
    import capo_datazone.types.data_product_status
    import capo_datazone.types.domain_id
    import capo_datazone.types.form_output_list
    import capo_datazone.types.glossary_terms
    import capo_datazone.types.project_id
    import capo_datazone.types.revision


class CreateDataProductOutput(TypedDict, closed=True):
    domain_id: "capo_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain where the data product lives.</p>"""
    id: "capo_datazone.types.data_product_id.DataProductId"
    """<p>The ID of the data product.</p>"""
    revision: "capo_datazone.types.revision.Revision"
    """<p>The revision of the data product.</p>"""
    owning_project_id: "capo_datazone.types.project_id.ProjectId"
    """<p>The ID of the owning project of the data product.</p>"""
    name: "capo_datazone.types.data_product_name.DataProductName"
    """<p>The name of the data product.</p>"""
    status: "capo_datazone.types.data_product_status.DataProductStatus"
    """<p>The status of the data product.</p>"""
    description: NotRequired[
        "capo_datazone.types.data_product_description.DataProductDescription"
    ]
    """<p>The description of the data product.</p>"""
    glossary_terms: NotRequired["capo_datazone.types.glossary_terms.GlossaryTerms"]
    """<p>The glossary terms of the data product.</p>"""
    items: NotRequired["capo_datazone.types.data_product_items.DataProductItems"]
    """<p>The data assets of the data product.</p>"""
    forms_output: NotRequired["capo_datazone.types.form_output_list.FormOutputList"]
    """<p>The metadata forms of the data product.</p>"""
    created_at: NotRequired["capo_datazone.types.created_at.CreatedAt"]
    """<p>The timestamp at which the data product was created.</p>"""
    created_by: NotRequired["capo_datazone.types.created_by.CreatedBy"]
    """<p>The user who created the data product.</p>"""
    first_revision_created_at: NotRequired["capo_datazone.types.created_at.CreatedAt"]
    """<p>The timestamp at which the first revision of the data product was created.</p>"""
    first_revision_created_by: NotRequired["capo_datazone.types.created_by.CreatedBy"]
    """<p>The user who created the first revision of the data product.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDataProductOutput) -> dict:
    out: dict = {}
    out["domainId"] = value["domain_id"]
    out["id"] = value["id"]
    out["revision"] = value["revision"]
    out["owningProjectId"] = value["owning_project_id"]
    out["name"] = value["name"]
    import capo_datazone.types.data_product_status

    out["status"] = capo_datazone.types.data_product_status.serialize_json(
        value.get("status", "CREATED")
    )
    if "description" in value:
        out["description"] = value["description"]
    if "glossary_terms" in value:
        import capo_datazone.types.glossary_terms

        out["glossaryTerms"] = capo_datazone.types.glossary_terms.serialize_json(
            value["glossary_terms"]
        )
    if "items" in value:
        import capo_datazone.types.data_product_items

        out["items"] = capo_datazone.types.data_product_items.serialize_json(
            value["items"]
        )
    if "forms_output" in value:
        import capo_datazone.types.form_output_list

        out["formsOutput"] = capo_datazone.types.form_output_list.serialize_json(
            value["forms_output"]
        )
    if "created_at" in value:
        import capo_datazone.types.created_at

        out["createdAt"] = capo_datazone.types.created_at.serialize_json(
            value["created_at"]
        )
    if "created_by" in value:
        out["createdBy"] = value["created_by"]
    if "first_revision_created_at" in value:
        import capo_datazone.types.created_at

        out["firstRevisionCreatedAt"] = capo_datazone.types.created_at.serialize_json(
            value["first_revision_created_at"]
        )
    if "first_revision_created_by" in value:
        out["firstRevisionCreatedBy"] = value["first_revision_created_by"]
    return out


def deserialize_json(data: dict) -> CreateDataProductOutput:
    out: CreateDataProductOutput = {}  # type: ignore[typeddict-item]
    if data.get("domainId") is not None:
        out["domain_id"] = data["domainId"]
    else:
        raise DeserializationError("CreateDataProductOutput.domain_id required")
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        raise DeserializationError("CreateDataProductOutput.id required")
    if data.get("revision") is not None:
        out["revision"] = data["revision"]
    else:
        raise DeserializationError("CreateDataProductOutput.revision required")
    if data.get("owningProjectId") is not None:
        out["owning_project_id"] = data["owningProjectId"]
    else:
        raise DeserializationError("CreateDataProductOutput.owning_project_id required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateDataProductOutput.name required")
    if data.get("status") is not None:
        import capo_datazone.types.data_product_status

        out["status"] = capo_datazone.types.data_product_status.deserialize_json(
            data["status"]
        )
    else:
        out["status"] = "CREATED"
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("glossaryTerms") is not None:
        import capo_datazone.types.glossary_terms

        out["glossary_terms"] = capo_datazone.types.glossary_terms.deserialize_json(
            data["glossaryTerms"]
        )
    if data.get("items") is not None:
        import capo_datazone.types.data_product_items

        out["items"] = capo_datazone.types.data_product_items.deserialize_json(
            data["items"]
        )
    if data.get("formsOutput") is not None:
        import capo_datazone.types.form_output_list

        out["forms_output"] = capo_datazone.types.form_output_list.deserialize_json(
            data["formsOutput"]
        )
    if data.get("createdAt") is not None:
        import capo_datazone.types.created_at

        out["created_at"] = capo_datazone.types.created_at.deserialize_json(
            data["createdAt"]
        )
    if data.get("createdBy") is not None:
        out["created_by"] = data["createdBy"]
    if data.get("firstRevisionCreatedAt") is not None:
        import capo_datazone.types.created_at

        out["first_revision_created_at"] = (
            capo_datazone.types.created_at.deserialize_json(
                data["firstRevisionCreatedAt"]
            )
        )
    if data.get("firstRevisionCreatedBy") is not None:
        out["first_revision_created_by"] = data["firstRevisionCreatedBy"]
    return out


def redact_sensitive(value: CreateDataProductOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    if "forms_output" in value:
        import capo_datazone.types.form_output_list

        out["forms_output"] = capo_datazone.types.form_output_list.redact_sensitive(
            value["forms_output"]
        )
    return out
