"""Generated from Smithy shape ``com.amazonaws.datazone#DataProductResultItem``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.created_at
    import capo_datazone.types.created_by
    import capo_datazone.types.data_product_description
    import capo_datazone.types.data_product_id
    import capo_datazone.types.data_product_item_additional_attributes
    import capo_datazone.types.data_product_name
    import capo_datazone.types.domain_id
    import capo_datazone.types.glossary_terms
    import capo_datazone.types.project_id


class DataProductResultItem(TypedDict, closed=True):
    domain_id: "capo_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain where the data product lives.</p>"""
    id: "capo_datazone.types.data_product_id.DataProductId"
    """<p>The ID of the data product.</p>"""
    name: "capo_datazone.types.data_product_name.DataProductName"
    """<p>The name of the data product.</p>"""
    owning_project_id: "capo_datazone.types.project_id.ProjectId"
    """<p>The ID of the owning project of the data product.</p>"""
    description: NotRequired[
        "capo_datazone.types.data_product_description.DataProductDescription"
    ]
    """<p>The description of the data product.</p>"""
    glossary_terms: NotRequired["capo_datazone.types.glossary_terms.GlossaryTerms"]
    """<p>The glossary terms of the data product.</p>"""
    created_at: NotRequired["capo_datazone.types.created_at.CreatedAt"]
    """<p>The timestamp at which the data product was created.</p>"""
    created_by: NotRequired["capo_datazone.types.created_by.CreatedBy"]
    """<p>The user who created the data product.</p>"""
    first_revision_created_at: NotRequired["capo_datazone.types.created_at.CreatedAt"]
    """<p>The timestamp at which first revision of the data product was created.</p>"""
    first_revision_created_by: NotRequired["capo_datazone.types.created_by.CreatedBy"]
    """<p>The user who created the first revision of the data product.</p>"""
    additional_attributes: NotRequired[
        "capo_datazone.types.data_product_item_additional_attributes.DataProductItemAdditionalAttributes"
    ]
    """<p>The additional attributes of an Amazon DataZone data product.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataProductResultItem) -> dict:
    out: dict = {}
    out["domainId"] = value["domain_id"]
    out["id"] = value["id"]
    out["name"] = value["name"]
    out["owningProjectId"] = value["owning_project_id"]
    if "description" in value:
        out["description"] = value["description"]
    if "glossary_terms" in value:
        import capo_datazone.types.glossary_terms

        out["glossaryTerms"] = capo_datazone.types.glossary_terms.serialize_json(
            value["glossary_terms"]
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
    if "additional_attributes" in value:
        import capo_datazone.types.data_product_item_additional_attributes

        out["additionalAttributes"] = (
            capo_datazone.types.data_product_item_additional_attributes.serialize_json(
                value["additional_attributes"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataProductResultItem:
    out: DataProductResultItem = {}  # type: ignore[typeddict-item]
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
    if data.get("owningProjectId") is not None:
        out["owning_project_id"] = data["owningProjectId"]
    else:
        out["owning_project_id"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("glossaryTerms") is not None:
        import capo_datazone.types.glossary_terms

        out["glossary_terms"] = capo_datazone.types.glossary_terms.deserialize_json(
            data["glossaryTerms"]
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
    if data.get("additionalAttributes") is not None:
        import capo_datazone.types.data_product_item_additional_attributes

        out["additional_attributes"] = (
            capo_datazone.types.data_product_item_additional_attributes.deserialize_json(
                data["additionalAttributes"]
            )
        )
    return out


def redact_sensitive(value: DataProductResultItem) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
